#### PATTERN GENERATOR ####


print("    PATTERN GENERATOR    ")


rows = int(input("Enter Number of Rows : "))

print(" Choose a Pattern : ")
print(" 1. Increasing Triangle ")
print(" 2. Decreasing Triangle ")
print(" 3. Number Triangle ")
print(" 4. Pyramid ")

choice = input("Enter Your Choice : ")

print(" ----- OUTPUT ----- ")

# Increasing Triangle
if choice == "1" :

    for i in range(1, rows + 1):
        print("*" * i)


# Decreasing Triangle
elif choice == "2" :

    for i in range(rows, 0, -1):
        print("*" * i)


# Number Triangle
elif choice == "3" :

    for i in range(1, rows + 1) :
        for j in range(1, i + 1) :
            print(j, end=" ")
        print()


# Pyramid
elif choice == "4" :

    for i in range(1, rows + 1) :
        spaces = rows - i
        stars = (2 * i) - 1

        print(" " * spaces + "*" * stars)


else :
    print("Invalid Choice!")

print("    PROGRAM COMPLETED    ")