import sys
import core

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py [add <title>] [list]")
        return

    cmd = sys.argv[1]

    if cmd == "add":
        title = " ".join(sys.argv[2:])
        task = core.add_task(title)
        print(f"Added: {task.title} (id {task.id})")

    elif cmd == "list":
        tasks = core.list_tasks()
        for t in tasks:
            mark = "[x]" if t.done else "[ ]"
            print(f"{mark} {t.id}: {t.title}")
