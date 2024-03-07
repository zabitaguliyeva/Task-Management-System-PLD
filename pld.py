import json
import os
import uuid


class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
    def mark_as_completed(self):
        self.completed = True

class TaskManager:
    file = "file.json"
    def __init__(self):
        self.tasks = {
        }
        if not os.path.exists(self.file):
            return
        with open(self.file, "r") as f:
            tasks = json.load(f)
        for task in tasks.values():
            self.tasks[task["id"]] = Task(id=task["id"], 
                                       title=task["title"],
                                       description=task["description"],
                                       completed=task["completed"])
            
    def add_task(self, title, description):
        task_id = int(uuid.uuid4())
        new_task = Task(task_id, title, description)
        self.tasks[task_id] = new_task
        with open(self.file, 'w') as f:
            json.dump(self.tasks, f, default=vars)
        

    def remove_task(self, id):
        if id in self.tasks:
            del self.tasks[id]
        with open(self.file, 'w') as f:
            json.dump(self.tasks, f,default=vars)
    def mark_task_completed(self, id):
        task = self.find_task(id)
        if task:
            task.mark_as_completed()
        with open(self.file, 'w') as f:
            json.dump(self.tasks, f,default=vars)

    def list_tasks(self):
        for task_id, task in self.tasks.items():
            print(f"Task ID: {task_id}, Title: {task.title}, Completed: {task.completed}")

    def find_task(self, id):
        if not self.tasks.get(id):
            raise ValueError("Id not correct or not found")
        return self.tasks.get(id)

    
import argparse
def main():
    parser = argparse.ArgumentParser(description="Task Management System")
    parser.add_argument("command", choices=["add", "remove", "complete", "list"])
    parser.add_argument("-id", type=int, help="Task ID")
    parser.add_argument("-title", help="Task Title")
    parser.add_argument("-description", help="Task Description")
    args = parser.parse_args()
    task_manager = TaskManager()
    if args.command == "add":
        task_manager.add_task(args.title, args.description)
    elif args.command == "remove":
        task_manager.remove_task(args.id)
    elif args.command == "complete":
        task_manager.mark_task_completed(args.id)
    elif args.command == "list":
        task_manager.list_tasks()
if __name__ == "__main__":
    main()