tasks =[]

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for x in tasks:
            print(f" - {x}")

def remove_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' removed successfully!")

def complete_task():
    if not tasks:
        print("No task Found")
    else:
        task = input("Enter the completed task: ")
        if task in tasks:
            index = tasks.index(task)  
            tasks[index] = task + " ✅"
            print(f"Task '{task}' is marked as complete!")
        else:
            print("Task not found in the list.")

while True:
    print("\n1. Add Task 2. View Tasks  3. Remove Task 4. Complete Task  5. Exit")
    choice = input("Choose an Option (From 1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice =="3":
        remove_tasks()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")