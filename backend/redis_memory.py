import redis
from typing import Dict, Any

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def set_working_memory(key: str, value: str):
    redis_client.set(key, value)

def get_working_memory(key: str) -> Any:
    return redis_client.get(key)

class Agent:
    def __init__(self, name, func):
        self.name = name
        self.func = func

def chat_agent(text):
    return f"[ChatAgent] You said: {text}"

def search_agent(query):
    return f"[SearchAgent] Pretend results for: {query}"

registry: Dict[str, Agent] = {
    "chat": Agent("chat", chat_agent),
    "search": Agent("search", search_agent)
}

def run_workflow(task: str):
    if "search" in task:
        result = registry["search"].func(task)
        set_working_memory("last_search", result)
    else:
        result = registry["chat"].func(task)
    return result

if __name__ == "__main__":
    print(run_workflow("search AI chips"))
    print("Working memory:", get_working_memory("last_search"))
