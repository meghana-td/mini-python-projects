tasks=[]

while True:
    print("\n--- To-Do list ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        task=input("Enter a task: ")
        tasks.append(task)
        print("Task is added!")
    elif choice==2:
        if len(tasks) == 0:
            print("No tasks found")
        else:
            print("Tasks: ")
            for i, task in enumerate(tasks, start=1):
                print(i, task)
    elif choice==3:
        if len(tasks) ==0:
            print("No task found")
        else:
            print("Tasks: ")
            for i, task in enumerate(tasks, start=1):
                print(i, task)
            n=int(input("Enter task number to remove: "))
            tasks.pop(n-1)
            print("Task is removed")
    elif choice==4:
        print("...Exiting To-Do list...")
        break
    else:
        print("Invalid choice!!")
