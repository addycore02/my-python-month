
####    FILE BASED TO-DO MANAGER    ####

print("      FILE BASED TO-DO MANAGER      ")

FILE_NAME = "tasks.txt"

def add_task():
    task = input(" Enter Task : ")

    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")

    print(" Task Added Successfully!")


def view_tasks():
    try:

        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if len(tasks) == 0:
            print(" No Tasks Found.")

        else:
            print("\n Stored Tasks :")

            for i, task in enumerate(tasks, start=1):
                print(i, "]", task.strip())

    except FileNotFoundError:
        print(" No Tasks Found.")

def remove_task():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if len(tasks) == 0:
            print(" No Tasks Available.")

        else:
            print("\n Stored Tasks :")

            for i, task in enumerate(tasks, start=1):
                print(i, "]", task.strip())

            number = int(input(" Enter Task Number to Remove : "))

            if number >= 1 and number <= len(tasks):

                tasks.pop(number - 1)

                with open(FILE_NAME, "w") as file:
                    file.writelines(tasks)

                print(" Task Removed Successfully!")

            else:
                print(" Invalid Task Number.")

    except FileNotFoundError:
        print(" No Tasks Found.")

def complete_task():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if len(tasks) == 0:
            print(" No Tasks Available.")

        else:
            print("\n Stored Tasks :")

            for i, task in enumerate(tasks, start=1):
                print(i, "]", task.strip())

            number = int(input(" Enter Task Number to Complete : "))

            if number >= 1 and number <= len(tasks):

                task = tasks[number - 1].strip()

                if not task.startswith("[DONE]"):
                    tasks[number - 1] = "[DONE] " + task + "\n"

                    with open(FILE_NAME, "w") as file:
                        file.writelines(tasks)

                    print(" Task Marked as Completed!")

                else:
                    print(" Task is Already Completed.")

            else:
                print(" Invalid Task Number.")

    except FileNotFoundError:
        print(" No Tasks Found.")

while True:
    print(" 1] Add Task")
    print(" 2] View Tasks")
    print(" 3] Complete Task")
    print(" 4] Remove Task")
    print(" 5] Exit")

    choice = input(" Enter Your Choice : ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        remove_task()

    elif choice == "5":
        print(" Exiting To-Do Manager")
        break

    else:
        print(" Invalid Choice! Please Try Again.")