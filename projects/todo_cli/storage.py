# projects/todo_cli/storage.py
import json
from .model import Task

def save_tasks(tasks, filename="tasks.json"):
    data = [t.__dict__ for t in tasks]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Task(**d) for d in data]
    except FileNotFoundError:
        return []
