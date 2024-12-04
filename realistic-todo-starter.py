"""
Todo List Application

Requirements:
- Implement a command line todo list manager
- Support adding, viewing, completing, and deleting tasks
- Include basic error handling
- Follow PEP 8 style guidelines

See README.md for full requirements
"""

class TodoList:
    def __init__(self):
        # Initialize your task storage here
        self.task = []


    def add_task(self, description: str) -> bool:
        """Add a new task"""
        self.task.append([description,False])
        return True
        

    def view_tasks(self) -> list:
        """Return all tasks"""
        return self.task

    def complete_task(self, task_id: int) -> bool:
        """Mark a task as complete"""
        self.task[task_id][1] = True
        return True
        
        

    def delete_task(self, task_id: int) -> bool:
        """Delete a task"""
        self.task.remove(self.task[task_id])
        return True


def main():
    # Implement your command line interface here
    todo = TodoList()
    todo.add_task("Play football")
    todo.add_task("Study law")
    todo.add_task("Hear music")

    todo.delete_task(2)
    todo.complete_task(0)
    print(todo.view_tasks())



if __name__ == "__main__":
    main()
