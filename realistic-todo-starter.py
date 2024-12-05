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
    print("Welcome to Todo3.0!!")
    print("commands : uses")
    print("ts \"todo\" :  to add a task")
    print("exit : to get out from window")
    print("dl \"todo_id\" : for delete task")
    print("cp \"todo_id\" : for marking task as complete")
    print("view : to view todo")
    tasks = TodoList()
    while True:
        command = input("user $>> ")
        if command == "exit":
            print("Thank you")
            break
        elif command[0:2] == "ts":
            tasks.add_task(command[3:])
            print("item added successfully")
        elif command[0:2] == "dl":
            tasks.delete_task(int(command[3:]) - 1)
            print("item deleted successfully")
        elif command[0:2] == "cp":
            tasks.complete_task(int(command[3:]) - 1)
            print("status updated")
        elif command == "view":
            cnt = 1
            print("todo_id-----------------------------task-------------------------------status")
            print("_____________________________________________________________________________")
            for i in tasks.view_tasks():
                print(str(cnt) + "---------|--------" + i[0] + "---------|---------" + str(i[1]))
                cnt += 1
            print("_____________________________________________________________________________")
        else:
            print("command is not recognizable - 404")








if __name__ == "__main__":
    main()
