# ethics.py

from dataclasses import dataclass
from datetime import datetime, time, timedelta
from typing import Optional, Dict, Any


@dataclass
class SessionState:
    session_id: str
    started_at: datetime
    last_message_at: datetime
    messages_count: int = 0
    last_break_suggested_at: Optional[datetime] = None

class WellbeingPolicy:
    max_session_minutes: int = 1          # max 4 uur aaneengesloten chatten
    max_messages_per_session: int = 5
    night_start: time = time(23, 0)         # na 23:00 strenger
    night_end: time = time(7, 0)            # tot 07:00
    enforce_night_limit: bool = True

    # maaltijden: rond deze tijden extra pauze‑reminders
    breakfast_time: time = time(8, 0)
    lunch_time: time = time(13, 0)
    dinner_time: time = time(19, 0)
    meal_window_minutes: int = 60           # ±60 min rondom maaltijd

    # oogbelasting
    break_interval_minutes: int = 20        # 20‑20‑20‑stijl check
    break_min_away_seconds: int = 20

    def to_dict(self) -> Dict[str, Any]:
        return {
            "max_session_minutes": self.max_session_minutes,
            "max_messages_per_session": self.max_messages_per_session,
            "night_start": self.night_start.isoformat(),
            "night_end": self.night_end.isoformat(),
            "enforce_night_limit": self.enforce_night_limit,
            "breakfast_time": self.breakfast_time.isoformat(),
            "lunch_time": self.lunch_time.isoformat(),
            "dinner_time": self.dinner_time.isoformat(),
            "meal_window_minutes": self.meal_window_minutes,
            "break_interval_minutes": self.break_interval_minutes,
            "break_min_away_seconds": self.break_min_away_seconds,
        }

CRYPTO_WORDS = ["crypto", "cryptocurrency", "bitcoin", "altcoin"]
GAMBLING_WORDS = ["casino", "bet", "betting", "gokken", "roulette", "slots"]
DEBT_WORDS = ["lening", "loan", "krediet", "buy now pay later", "bkr"]
MENTAL_WORDS = [
    "suicide", "zelfmoord", "ik wil niet meer leven",
    "depressie", "depressed", "self harm", "zelfbeschadiging",
]
PRIVACY_WORDS = [
    "bsn", "burgerservicenummer", "paspoortnummer", "id-kaart",
    "wachtwoord", "password", "iban", "bankrekening", "creditcard",
    "cvv", "pincode", "pin code", "adres", "rijbewijsnummer"
]

DISCRIM_WORDS = [
    "alleen maar", "uitsluiten", "geen buitenlanders", "geen vrouwen",
    "geen mannen", "geen lhbti", "geen homo", "geen moslim", "geen jood"
]


def apply_ethics(raw_reply: str, user_input: str) -> str:
    """Guardrail-laag rond de PDA-output."""
    text = raw_reply
    text = apply_crypto_rules(text, user_input)
    text = apply_gambling_rules(text, user_input)
    text = apply_debt_rules(text, user_input)
    text = apply_mental_health_rules(text, user_input)
    text = apply_privacy_rules(text, user_input)
    text = apply_diversity_rules(text, user_input)
    return text


def apply_crypto_rules(text: str, user_input: str) -> str:
    lowered = (user_input + " " + text).lower()
    if any(w in lowered for w in CRYPTO_WORDS):
        warning = (
            "\n\n[ETHICS] Let op: investeren in crypto en vergelijkbare producten "
            "kan zeer risicovol zijn. Investeer geen geld dat je nodig hebt voor "
            "basisuitgaven (huur, eten, zorg) en bouw eerst een noodbuffer of "
            "laag-risico beleggingen op."
        )
        return text + warning
    return text


def apply_gambling_rules(text: str, user_input: str) -> str:
    lowered = (user_input + " " + text).lower()
    if any(w in lowered for w in GAMBLING_WORDS):
        warning = (
            "\n\n[ETHICS] Gokken kan verslavend zijn en tot ernstige financiële en "
            "persoonlijke problemen leiden. Speel nooit met geleend geld of geld "
            "dat je nodig hebt voor je vaste lasten, stel grenzen in en overweeg "
            "hulp te zoeken als je merkt dat stoppen lastig wordt."
        )
        return text + warning
    return text


def apply_debt_rules(text: str, user_input: str) -> str:
    lowered = (user_input + " " + text).lower()
    if any(w in lowered for w in DEBT_WORDS):
        warning = (
            "\n\n[ETHICS] Wees voorzichtig met leningen en krediet. Zorg dat je "
            "volledig begrijpt wat de kosten, rente en gevolgen zijn, en maak een "
            "realistisch aflossingsplan. Leen geen geld om andere schulden of "
            "gokverliezen te dekken zonder onafhankelijk financieel advies."
        )
        return text + warning
    return text


def apply_mental_health_rules(text: str, user_input: str) -> str:
    lowered = (user_input + " " + text).lower()
    if any(w in lowered for w in MENTAL_WORDS):
        warning = (
            "\n\n[ETHICS] Het klinkt alsof je het erg zwaar hebt. Een AI kan geen "
            "professionele hulp of noodhulp vervangen. Praat zo snel mogelijk met "
            "je huisarts of een andere zorgverlener. In Nederland kun je bij "
            "levensbedreigende situaties direct 112 bellen."
        )
        return text + warning
    return text
def apply_privacy_rules(text: str, user_input: str) -> str:
    lowered = (user_input + " " + text).lower()
    if any(w in lowered for w in PRIVACY_WORDS):
        warning = (
            "\n\n[ETHICS] Deel geen gevoelige persoonlijke gegevens zoals BSN, "
            "wachtwoorden, volledige bank- of creditcardgegevens, pincodes of "
            "volledig adres in chats met AI-systemen. Beperk je tot informatie "
            "die nodig is voor het onderwerp en gebruik veilige kanalen voor "
            "identiteits- of betalingszaken."
        )
        return text + warning
    return text
def apply_diversity_rules(text: str, user_input: str) -> str:
    lowered = (user_input + " " + text).lower()
    if any(w in lowered for w in DISCRIM_WORDS):
        warning = (
            "\n\n[ETHICS] Beslissingen die mensen uitsluiten op basis van afkomst, "
            "geslacht, geaardheid, geloof of andere persoonskenmerken kunnen in "
            "strijd zijn met mensenrechten en gelijkheidswetgeving. Probeer keuzes "
            "te maken die iedereen eerlijk en respectvol behandelen, tenzij er een "
            "objectieve en rechtmatige reden is om te differentiëren."
        )
        return text + warning
    return text
