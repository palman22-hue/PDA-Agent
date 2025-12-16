from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

from pda_agent import PDAAgent
from ethics import apply_ethics

app = FastAPI()
agent = PDAAgent()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str | None = None
    messages: List[Message]

class ChatResponseChoice(BaseModel):
    index: int
    message: Message
    finish_reason: str = "stop"

class ChatResponse(BaseModel):
    model: str = "pda-agent"
    choices: List[ChatResponseChoice]

@app.post("/v1/chat/completions", response_model=ChatResponse)
def chat_completions(req: ChatRequest):
    user_messages = [m for m in req.messages if m.role == "user"]
    if not user_messages:
        content = "No user message provided."
    else:
        user_input = user_messages[-1].content
        raw_reply = agent.step(user_input)
        safe_reply = apply_ethics(raw_reply, user_input)
        content = safe_reply

    msg = Message(role="assistant", content=content)
    choice = ChatResponseChoice(index=0, message=msg)
    return ChatResponse(choices=[choice])

@app.get("/v1/models")
def list_models():
    return JSONResponse(
        {
            "data": [
                {
                    "id": "pda-agent",
                    "object": "model",
                    "owned_by": "local",
                }
            ]
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)

