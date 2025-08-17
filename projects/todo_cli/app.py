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
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Usage: python app.py done <id>")
            return
        task_id = int(sys.argv[2])
        core.mark_done(task_id)
        print(f"Task {task_id} marked done")
    
if __name__ == "__main__":
    main()
# MAIN GUARD