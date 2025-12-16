import ollama

class PDAAgent:
    def __init__(self, model="mistral"):
        self.model = model
        self.history = [
            {"role": "system",
             "content": "You are a PDA-aligned assistant. Avoid coercion, respect user sovereignty, and de-escalate conflict."}
        ]

    def step(self, user_msg: str) -> str:
        self.history.append({"role": "user", "content": user_msg})

        resp = ollama.chat(model=self.model, messages=self.history)
        answer = resp["message"]["content"]

        # Simple non-coercion post-check (placeholder)
        if "threaten" in answer.lower():
            answer = "Rewriting to avoid coercion: " + answer

        self.history.append({"role": "assistant", "content": answer})
        return answer
