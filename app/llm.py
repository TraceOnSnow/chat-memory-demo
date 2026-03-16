# from typing import List


# def generate_reply(message: str, memories: List[str]) -> str:

#     if memories:
#         memory_text = " | ".join(memories)
#         return f"You said: {message}\nI also remember: {memory_text}"

#     return f"You said: {message}\nI do not have relevant memory yet."
import os
from typing import List
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3-flash-preview")


def generate_reply(message: str, memories: List[str]) -> str:
    memory_block = "\n".join(f"- {m}" for m in memories) if memories else "None"

    prompt = f"""
You are a helpful assistant.

Relevant user memories:
{memory_block}

User message:
{message}

Reply naturally and use the memories if helpful.
""".strip()

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text