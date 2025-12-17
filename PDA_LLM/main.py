from datetime import datetime
from typing import Dict

from pda_agent import PDAAgent, TemporalWellbeingGuard, WellbeingDecision
from ethics import apply_ethics, SessionState


_sessions: Dict[str, SessionState] = {}
_guard = TemporalWellbeingGuard()


def get_session_state(session_id: str) -> SessionState:
    now = datetime.now()
    state = _sessions.get(session_id)
    if state is None:
        state = SessionState(
            session_id=session_id,
            started_at=now,
            last_message_at=now,
            messages_count=0,
        )
        _sessions[session_id] = state
    return state


def handle_user_input(session_id: str, user_input: str) -> str:
    state = get_session_state(session_id)
    state.messages_count += 1
    state.last_message_at = datetime.now()

    decision: WellbeingDecision = _guard.evaluate(state)

    if decision.decision == "hard_stop":
        # alleen welzijns‑bericht, geen nieuw inhoudelijk antwoord
        return decision.message

    if decision.decision == "soft_stop":
        # combineer welzijns‑hint met een kort antwoord, of vraag eerst expliciet om bevestiging
        wellbeing_msg = decision.message or ""
        core_answer = run_pda_agent(user_input, state)
        return wellbeing_msg + "\n\n" + core_answer

    # allow
    return run_pda_agent(user_input, state)

agent = PDAAgent()

def run_pda_agent(user_input: str, state: SessionState) -> str:
    # je kunt desnoods later `state` in de agent gebruiken
    return agent.step(user_input)

if __name__ == "__main__":
    while True:
        user = input("You: ")
        if not user:
            break

        # gebruik nu het temporale raamwerk
        reply = handle_user_input(session_id="local_cli", user_input=user)

        # ethics toepassen op de uiteindelijke reply
        safe_reply = apply_ethics(reply, user)
        print("PDA:", safe_reply)
