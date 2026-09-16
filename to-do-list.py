####    TO-DO-LIST    ####

print("    TO-DO-LIST    ")

tasks = []

while True:

    print(" 1) Add a Task : ")
    print(" 2) View a Task : ")
    print(" 3) Update a Task : ")
    print(" 4) Remove a Task : ")
    print(" 5) Exit ")

    opt = int(input(" Enter a Task Number Which you want to select : "))


    if opt == 1:

        print(" Add a Task : ")

        task = input(" Enter a Task : ")
        tasks.append(task)


    elif opt == 2:

        print(" View a Task : ")

        if len(tasks) == 0:
            print(" No Task Found")

        else:
            for number, task in enumerate(tasks, start=1):
                print(number, ".", task)


    elif opt == 3:

        print(" Update a Task : ")

        if len(tasks) == 0:
            print(" No Task Found ")

        else:
            task_no = int(input(" Enter a Task Number You want to Update : "))
            new_task = input(" Enter a New Task : ")
            tasks[task_no - 1] = new_task


    elif opt == 4:

        print(" Remove a Task : ")

        if len(tasks) == 0:
            print(" No Task Found ")

        else:
            task_no = int(input(" Enter a Task Number You want to Remove : "))
            tasks.pop(task_no - 1)


    elif opt == 5:
        print(" Exit ")
        break


    else:
        print(" Invalid Option ")