import json
import sys
import os

FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Added: {task}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return

    for i, t in enumerate(tasks, 1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. {t['task']}  [{status}]")


def mark_done(task_index):
    tasks = load_tasks()
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task number!")
        return

    tasks[task_index - 1]["done"] = True
    save_tasks(tasks)
    print(f"Marked task #{task_index} as done ✔️")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  py todo.py add \"task name\"")
        print("  py todo.py list")
        print("  py todo.py done <task_number>")
        return

    command = sys.argv[1]

    if command == "add":
        task_name = " ".join(sys.argv[2:])
        add_task(task_name)

    elif command == "list":
        list_tasks()

    elif command == "done":
        if len(sys.argv) < 3:
            print("Please give the task number. Example: py todo.py done 1")
            return
        index = int(sys.argv[2])
        mark_done(index)

    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
