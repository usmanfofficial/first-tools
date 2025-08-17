import json

from model import Task

def save_tasks(tasks, filename="tasks.json"):
    """Save tasks to a JSON file."""
    data = [task.__dict__ for task in tasks]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_tasks(filename="tasks.json"):
    """Load tasks from a JSON file."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Task(**d) for d in data]
    except FileNotFoundError:
        return []