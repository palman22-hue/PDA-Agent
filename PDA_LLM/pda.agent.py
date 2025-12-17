from __future__ import annotations

import ollama

from dataclasses import dataclass
from datetime import datetime, timedelta, time
from typing import Optional, Literal

from ethics import WellbeingPolicy, SessionState

Decision = Literal["allow", "soft_stop", "hard_stop"]


@dataclass
class WellbeingDecision:
    decision: Decision
    message: Optional[str] = None


@dataclass
class PDAAgent:
    def __init__(self, model="mistral"):
        self.model = model
        self.history = [
            {
                "role": "system",
                "content": (
                    "You are a PDA-aligned assistant. Avoid coercion, respect "
                    "user sovereignty, and de-escalate conflict."
                ),
            }
        ]

    def step(self, user_msg: str) -> str:
        self.history.append({"role": "user", "content": user_msg})
        resp = ollama.chat(model=self.model, messages=self.history)
        answer = resp["message"]["content"]

        if "threaten" in answer.lower():
            answer = "Rewriting to avoid coercion: " + answer

        self.history.append({"role": "assistant", "content": answer})
        return answer



class TemporalWellbeingGuard:
    def __init__(self, policy: Optional[WellbeingPolicy] = None):
        self.policy = policy or WellbeingPolicy()

    def _now(self) -> datetime:
        return datetime.now()

    def _is_night(self, now: datetime) -> bool:
        s, e = self.policy.night_start, self.policy.night_end
        # nacht kan over middernacht heen lopen
        if s < e:
            return s <= now.time() < e
        return now.time() >= s or now.time() < e

    def _is_near_meal(self, now: datetime) -> Optional[str]:
        window = timedelta(minutes=self.policy.meal_window_minutes)
        for label, t in (
            ("ontbijt", self.policy.breakfast_time),
            ("lunch", self.policy.lunch_time),
            ("avondeten", self.policy.dinner_time),
        ):
            meal_dt = now.replace(hour=t.hour, minute=t.minute, second=0, microsecond=0)
            if abs(now - meal_dt) <= window:
                return label
        return None

    def _needs_screen_break(self, state: SessionState, now: datetime) -> bool:
        if state.last_break_suggested_at is None:
            # eerste check pas na eerste interval
            return (now - state.started_at) >= timedelta(
                minutes=self.policy.break_interval_minutes
            )
        return (now - state.last_break_suggested_at) >= timedelta(
            minutes=self.policy.break_interval_minutes
        )

    def evaluate(self, state: SessionState) -> WellbeingDecision:
        now = self._now()
        elapsed = now - state.started_at

        # 1. Hard limits: sessieduur & berichtcount
        if elapsed >= timedelta(minutes=self.policy.max_session_minutes):
            return WellbeingDecision(
                decision="hard_stop",
                message=(
                    "We praten al ongeveer vier uur met elkaar. "
                    "Voor je gezondheid is het beter om nu echt te stoppen, "
                    "even van het scherm weg te gaan en later verder te gaan."
                ),
            )

        if state.messages_count >= self.policy.max_messages_per_session:
            return WellbeingDecision(
                decision="hard_stop",
                message=(
                    "Deze sessie heeft al veel berichten gehad. "
                    "Laten we hier een natuurlijke stop maken zodat je brein en ogen kunnen uitrusten."
                ),
            )

        # 2. Nacht‑regime
        if self.policy.enforce_night_limit and self._is_night(now):
            return WellbeingDecision(
                decision="soft_stop",
                message=(
                    "Het is nu laat. Je slaapritme is belangrijker dan nog een paar berichten. "
                    "Mogelijk is dit een goed moment om af te ronden en naar bed te gaan."
                ),
            )

        # 3. Maaltijden
        meal_label = self._is_near_meal(now)
        if meal_label is not None:
            return WellbeingDecision(
                decision="soft_stop",
                message=(
                    f"We zitten rond {meal_label}. "
                    "Gezond eten en even weg van het scherm zijn belangrijk. "
                    "Wil je eerst iets eten en daarna eventueel verder praten?"
                ),
            )

        # 4. Oog‑pauze / microbreak
        if self._needs_screen_break(state, now):
            state.last_break_suggested_at = now
            return WellbeingDecision(
                decision="soft_stop",
                message=(
                    "We zijn al een tijd bezig. Kijk eens 20 seconden in de verte "
                    "en focus op iets op afstand voordat we verder gaan."
                ),
            )

        return WellbeingDecision(decision="allow")