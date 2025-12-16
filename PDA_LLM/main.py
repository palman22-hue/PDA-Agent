from pda_agent import PDAAgent
from ethics import apply_ethics   # nieuwe module

agent = PDAAgent()

while True:
    user = input("You: ")
    if not user:
        break
    raw_reply = agent.step(user)
    safe_reply = apply_ethics(raw_reply, user)  # filter / verrijking
    print("PDA:", safe_reply)
