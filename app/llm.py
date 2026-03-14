from typing import List


def generate_reply(message: str, memories: List[str]) -> str:

    if memories:
        memory_text = " | ".join(memories)
        return f"You said: {message}\nI also remember: {memory_text}"

    return f"You said: {message}\nI do not have relevant memory yet."
