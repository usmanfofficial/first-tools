import storage

def mark_done(task_id):
    tasks = storage.load_tasks()
    for t in tasks:
        if t.id == task_id:
            t.done = True
    storage.save_tasks(tasks)

