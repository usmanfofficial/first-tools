# projects/todo_cli/core.py
from .model import Task
from . import storage

def add_task(title, note=None, filename="tasks.json"):
    tasks = storage.load_tasks(filename)
    new_id = (max([t.id for t in tasks], default=0) + 1)
    task = Task(id=new_id, title=title, note=note)
    tasks.append(task)
    storage.save_tasks(tasks, filename)
    return task

def list_tasks(filename="tasks.json"):
    return storage.load_tasks(filename)

def mark_done(task_id, filename="tasks.json"):
    tasks = storage.load_tasks(filename)
    for t in tasks:
        if t.id == task_id:
            t.done = True
    storage.save_tasks(tasks, filename)
