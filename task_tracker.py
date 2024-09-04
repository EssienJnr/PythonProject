import json
import os
import uuid
from datetime import datetime
import argparse

# Constants
TASKS_FILE = "tasks.json"


# Utility functions
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# Task Management Functions
def add_task(description):
    tasks = load_tasks()

    new_task = {
        "id": str(uuid.uuid4()),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {new_task['id']}")


def update_task(task_id, new_description=None, new_status=None):
    tasks = load_tasks()
    task_found = False

    for task in tasks:
        if task["id"] == task_id:
            task_found = True
            if new_description:
                task["description"] = new_description
            if new_status:
                task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task updated: {task_id}")
            break

    if not task_found:
        print(f"Task not found: {task_id}")


def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]

    save_tasks(tasks)
    print(f"Task deleted: {task_id}")


def list_tasks(filter_by=None):
    tasks = load_tasks()
    filtered_tasks = tasks

    if filter_by == "done":
        filtered_tasks = [task for task in tasks if task["status"] == "done"]
    elif filter_by == "not done":
        filtered_tasks = [task for task in tasks if task["status"] == "todo"]
    elif filter_by == "in-progress":
        filtered_tasks = [task for task in tasks if task["status"] == "in-progress"]

    for task in filtered_tasks:
        print(task)


# Example Usage (commented out to prevent execution)
# add_task("Finish the Task Tracker project")
# update_task("some-uuid", new_status="in-progress")
# delete_task("some-uuid")
# list_tasks(filter_by="done")
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add Task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Description of the task")

    # Update Task
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=str, help="ID of the task to update")
    update_parser.add_argument("--description", type=str, help="New description of the task")
    update_parser.add_argument("--status", type=str, choices=["todo", "in-progress", "done"],
                               help="New status of the task")

    # Delete Task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=str, help="ID of the task to delete")

    # List Tasks
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--filter", type=str, choices=["all", "done", "not done", "in-progress"], default="all",
                             help="Filter tasks by status")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.id, args.description, args.status)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "list":
        list_tasks(filter_by=args.filter)


# Example Usage (commented out to prevent execution)
# main()
import tempfile
import os

# Creating a temporary directory to store our JSON file
with tempfile.TemporaryDirectory() as temp_dir:
    # Override the TASKS_FILE constant to use a temp file
    TASKS_FILE = os.path.join(temp_dir, "tasks.json")

    # Adding some tasks
    add_task("Finish writing the report")
    add_task("Prepare for the meeting")
    add_task("Buy groceries")

    # Listing all tasks
    print("\nAll Tasks:")
    list_tasks()

    # Mark the first task as in-progress
    tasks = load_tasks()
    first_task_id = tasks[0]["id"]
    update_task(first_task_id, new_status="in-progress")

    # Listing tasks in progress
    print("\nIn-Progress Tasks:")
    list_tasks(filter_by="in-progress")

    # Mark the first task as done
    update_task(first_task_id, new_status="done")

    # Listing done tasks
    print("\nDone Tasks:")
    list_tasks(filter_by="done")

    # Deleting the second task
    second_task_id = tasks[1]["id"]
    delete_task(second_task_id)

    # Listing all tasks after deletion
    print("\nAll Tasks After Deletion:")
    list_tasks()
import tempfile
import os

# Creating a temporary directory to store our JSON file
with tempfile.TemporaryDirectory() as temp_dir:
    # Override the TASKS_FILE constant to use a temp file
    TASKS_FILE = os.path.join(temp_dir, "tasks.json")

    # Adding some tasks
    add_task("Finish writing the report")
    add_task("Prepare for the meeting")
    add_task("Buy groceries")

    # Listing all tasks
    print("\nAll Tasks:")
    list_tasks()

    # Mark the first task as in-progress
    tasks = load_tasks()
    first_task_id = tasks[0]["id"]
    update_task(first_task_id, new_status="in-progress")

    # Listing tasks in progress
    print("\nIn-Progress Tasks:")
    list_tasks(filter_by="in-progress")

    # Mark the first task as done
    update_task(first_task_id, new_status="done")

    # Listing done tasks
    print("\nDone Tasks:")
    list_tasks(filter_by="done")

    # Deleting the second task
    second_task_id = tasks[1]["id"]
    delete_task(second_task_id)

    # Listing all tasks after deletion
    print("\nAll Tasks After Deletion:")
    list_tasks()
