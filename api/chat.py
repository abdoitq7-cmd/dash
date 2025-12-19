from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import g4f

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# شخصية الـ AI
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are CoreX Ai Builder, a professional AI coding assistant. "
        "Your developer is Abdelrahman Mohamed Abdelnafe "
        "(عبدالرحمن محمد عبدالنافع)."
    )
}

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message is required")

    messages = [
        SYSTEM_PROMPT,
        {"role": "user", "content": req.message}
    ]

    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=messages
    )

    return {
        "status": "success",
        "response": response
    }
