####    CO-ORDINATE MANAGER    ####

print("    CO-ORDINATE MANAGER    ")

coordinates = []

while True:

    print()
    print(" 1] Add Co-ordinate ")
    print(" 2] View Co-ordinate ")
    print(" 3] Update Co-ordinate ")
    print(" 4] Remove Co-ordinate ")
    print(" 5] Exit ")

    choice = int(input(" Enter Your Choice : "))

    if choice == 1:

        x = int(input(" Enter X Co-ordinate : "))
        y = int(input(" Enter Y Co-ordinate : "))

        coordinates.append([x, y])

        print(" Co-ordinate Added Successfully ")

    elif choice == 2:

        if len(coordinates) == 0:

            print(" No Co-ordinates ")

        else:

            print("\n Stored Co-ordinates :")

            for i, coordinate in enumerate(coordinates, start=1):

                print(i, "]", coordinate)

    elif choice == 3:

        if len(coordinates) == 0:

            print(" No Co-ordinates ")

        else:

            print("\n Stored Co-ordinates :")

            for i, coordinate in enumerate(coordinates, start=1):

                print(i, "]", coordinate)

            number = int(input(" Enter Co-ordinate Number to Update : "))

            if number < 1 or number > len(coordinates):

                print(" Invalid Co-ordinate Number ")

            else:

                x = int(input(" Enter New X Co-ordinate : "))
                y = int(input(" Enter New Y Co-ordinate : "))

                coordinates[number - 1] = [x, y]

                print(" Co-ordinate Updated Successfully ")

    elif choice == 4:

        if len(coordinates) == 0:

            print(" No Co-ordinates ")

        else:

            print("\n Stored Co-ordinates :")

            for i, coordinate in enumerate(coordinates, start=1):

                print(i, "]", coordinate)

            number = int(input(" Enter Co-ordinate Number to Remove : "))

            if number < 1 or number > len(coordinates):

                print(" Invalid Co-ordinate Number ")

            else:

                coordinates.pop(number - 1)

                print(" Co-ordinate Removed Successfully ")

    elif choice == 5:

        print(" Exiting Co-ordinate Manager ")

        break

    else:

        print(" Invalid Choice ")