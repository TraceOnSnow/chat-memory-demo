from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
    user_id: str
    message: str


class ChatResponse(BaseModel):
    answer: str
    memories_used: List[str]


class MemoryListResponse(BaseModel):
    user_id: str
    memories: List[str]
