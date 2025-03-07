## 5. Task Tracker
tasks = {}
print("Task Tracker- your buddy\n")
while True:
    choice = input("1: Add Task, 2: Mark Complete, 3: Display, 4: Exit\n")
    if choice == "1":
        task = input("Enter task: ")
        tasks[task] = "Pending :|"
    elif choice == "2":
        task = input("Enter task to mark complete: ")
        if task in tasks:
            tasks[task] = "Task Completed Buddy :)"
    elif choice == "3":
        print(tasks)
    elif choice == "4":
        print("See you Soon Buddy :)!")
        break
    else:
        print("Invalid choice. :(")