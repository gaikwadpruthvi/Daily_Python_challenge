#Implement a to-do list with tuple-based priorities.

import heapq

class ToDoList:
    def __init__(self):
        self.tasks = []  # Stores (priority, task_name) tuples

    def add_task(self):
        """Takes user input to add a task with priority."""
        task = input("Enter task name: ")
        while True:
            try:
                priority = int(input("Enter priority (lower number = higher priority): "))
                break
            except ValueError:
                print(" Invalid input! Please enter an integer for priority.")
        
        heapq.heappush(self.tasks, (priority, task))
        print(f" Task '{task}' added with priority {priority}.")

    def view_tasks(self):
        """Displays all tasks sorted by priority."""
        if not self.tasks:
            print(" To-Do List is empty!")
            return
        print("\n To-Do List (Sorted by Priority):")
        for priority, task in sorted(self.tasks):
            print(f"  {task} (Priority: {priority})")

    def remove_task(self):
        """Takes user input and removes a task by name."""
        if not self.tasks:
            print(" No tasks to remove!")
            return
        task_name = input("Enter the task name to remove: ")
        for i, (priority, task) in enumerate(self.tasks):
            if task == task_name:
                del self.tasks[i]
                heapq.heapify(self.tasks)  # Rebuild heap after deletion
                print(f" Task '{task_name}' removed.")
                return
        print(f" Task '{task_name}' not found!")

    def get_highest_priority_task(self):
        """Displays the highest-priority task without removing it."""
        if not self.tasks:
            print(" No tasks available!")
        else:
            print(f" Next task: '{self.tasks[0][1]}' (Priority: {self.tasks[0][0]})")

    def run(self):
        """Interactive menu for the to-do list."""
        while True:
            print("\n To-Do List Menu ")
            print("1 Add Task")
            print("2 View Tasks")
            print("3 Remove Task")
            print("4 Get Highest-Priority Task")
            print("5 Exit")

            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.remove_task()
            elif choice == "4":
                self.get_highest_priority_task()
            elif choice == "5":
                print(" Exiting... Have a productive day!")
                break
            else:
                print(" Invalid choice! Please enter a number between 1 and 5.")

#  Run the interactive To-Do List
todo = ToDoList()
todo.run()
