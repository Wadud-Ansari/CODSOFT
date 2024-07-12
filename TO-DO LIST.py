import os

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo_list = ToDoList()

    while True:
        clear_screen()
        print("To-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task = input("Enter task: ").strip()
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
            input("Press Enter to continue...")
        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter task number to mark as completed: ").strip())
                todo_list.mark_task_completed(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")
        elif choice == "4":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter task number to delete: ").strip())
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
