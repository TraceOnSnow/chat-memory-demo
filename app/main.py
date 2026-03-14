from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse, MemoryListResponse
from app.memory import search_memories, list_memories
from app.llm import generate_reply

app = FastAPI()


@app.post("/chat", response_model=ChatResponse)
def chat(chat_request: ChatRequest):
    memories = search_memories(chat_request.user_id, chat_request.message)
    reply = generate_reply(chat_request.message, memories)
    return ChatResponse(answer=reply, memories_used=memories)

@app.get("/memories", response_model=MemoryListResponse)
def get_memories(user_id: str):
    memories = list_memories(user_id)
    return MemoryListResponse(user_id=user_id, memories=memories)

@app.get("/", response_model=dict)
def root():
    return {"message": "Memory Demo Running"}
