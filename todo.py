def add_task():
    task=input("Enter a new task:")
    with open("todo.txt","a") as file:
        file.write(task,"\n")
        print("Task added successfully!")

def view_tasks():
    try:
        with open("todo.txt","r") as file:
            tasks = file.readlines() 
        if tasks:
            print("\nYour To-Do List:")
            for i,task in enumerate(tasks,1):
                print(f"{i}.{task.strip()}")
        else:
            print("To-Do list is empty.")
    except FileNotFoundError:
        print("No To-Do list found yet.") 

def delete_task():
    try:
        with open("todo.txt","r") as file:
            tasks = file.readlines()
        if tasks:
            print("\nSelect task number to delete:")
            for i,task in enumerate(tasks,1):
                print(f"{i}.{task.strip()}")
            choice = int(input("Enter task number to delete:"))
            if 1 <= choice <= len(tasks):
                removed = tasks.pop(choice -1)
                with open("todo.txt","w") as file:
                 file.writelines(tasks)
                print(f"Deleted:{removed.strip()}")
            else:
                print("Invalid task number.")
        else:
            print("No task to delete")
    except FileNotFoundError:
        print("To-Do list doesn't exist yet.")

while True:
    print("\n---To-Do List App ---")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    option= int(input("Choose an option:"))
    if option == "1":
        add_task()
    elif option == "2":
        view_tasks
    elif option =="3":
        delete_task
    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose a correct option.")


              
