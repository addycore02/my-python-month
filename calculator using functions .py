#### CALCULATOR USING FUNCTIONS ####

print("    CALCULATOR USING FUNCTIONS    ")


def addition(a, b):
    result = a + b
    return result


# SUBTRACTION FUNCTION
def subtraction(a, b):
    result = a - b
    return result


# MULTIPLICATION FUNCTION
def multiplication(a, b):
    result = a * b
    return result


# DIVISION FUNCTION
def division(a, b):
    result = a / b
    return result


while True:

    print("\n 1] - Addition ")
    print(" 2] - Subtraction ")
    print(" 3] - Multiplication ")
    print(" 4] - Division ")
    print(" 5] - Exit ")

    choice = int(input(" Enter Your Choice Number : "))


    if choice == 1:
        a = float(input(" Enter First Number : "))
        b = float(input(" Enter Second Number : "))

        result = addition(a, b)

        print(f" Answer : {result} ")


    elif choice == 2:
        a = float(input(" Enter First Number : "))
        b = float(input(" Enter Second Number : "))

        result = subtraction(a, b)

        print(f" Answer : {result} ")


    elif choice == 3:
        a = float(input(" Enter First Number : "))
        b = float(input(" Enter Second Number : "))

        result = multiplication(a, b)

        print(f" Answer : {result} ")


    elif choice == 4:
        a = float(input(" Enter First Number : "))
        b = float(input(" Enter Second Number : "))

        if b == 0:
            print(" Number Cannot be Divided by 0 ")

        else:
            result = division(a, b)
            print(f" Answer : {result} ")


    elif choice == 5:
        print(" Calculator Closed ")
        break


    else:
        print(" Invalid Choice ")