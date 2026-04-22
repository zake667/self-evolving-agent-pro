import json
import os

FILE = "memory/state.json"

def load_memory():
    if not os.path.exists(FILE):
        return {"history": []}
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"history": []}

def save_memory(mem):
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(mem, f, indent=2)
