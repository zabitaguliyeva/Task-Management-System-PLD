import uuid
import cmd, sys
class Task:
    is_completed = False
    def __init__(self, title, description, completed ):    
        self.id=int(uuid.uuid4())
        self.title=title
        self.description= description

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self) -> str:
        print(self.__dict__)

class TaskManager(cmd.Cmd):
    tasks = {}
    def do_add_task(self,title, description):
        new_task = Task(title, description)
        
        self.tasks[new_task.id] = new_task
    def do_remove_task(self, id):
        if (self.tasks.get(id)):
            del self.tasks[id]

    def do_mark_task_completed(self, id):
        if not self.tasks.get(id):
            raise ValueError("Id not correct")
        self.tasks[id].mark_as_completed()
    
    def do_list_tasks(self):
        print(self.tasks)
    
    def do_find_task(self, id):
        if not self.tasks.get(id):
            raise ValueError("Id not correct or not found")

        print(self.tasks[id])
    



