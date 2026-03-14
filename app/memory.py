from typing import Dict, List

# mock in-memory storage
_MEMORY_DB: Dict[str, List[str]] = {
    "demo_user": [
        "User prefers concise answers.",
        "User is building an AI memory demo."
    ]
}


def list_memories(user_id: str) -> List[str]:
    return _MEMORY_DB.get(user_id, [])


def search_memories(user_id: str, query: str) -> List[str]:
    memories = _MEMORY_DB.get(user_id, [])

    query_lower = query.lower()

    results = []

    for memory in memories:
        for word in query_lower.split():
            if word in memory.lower():
                results.append(memory)
                break

    return results
