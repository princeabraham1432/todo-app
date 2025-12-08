import json
import sys
import os

FILE = "tasks.json"


# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


# Add a task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Added: {task}")


# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return

    for i, t in enumerate(tasks, 1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. {t['task']}  [{status}]")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python todo.py add \"task name\"")
        print("  python todo.py list")
        return

    command = sys.argv[1]

    if command == "add":
        task_name = " ".join(sys.argv[2:])
        add_task(task_name)

    elif command == "list":
        list_tasks()

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
