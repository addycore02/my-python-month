#### REUSABLE UTILITY LIBRARY ####

print("===== REUSABLE UTILITY LIBRARY =====")


# Add Two Numbers

def add_numbers(a, b):
    return a + b


# Check Even or Odd

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"

    else:
        return "Odd"

# Find Maximum Number

def find_maximum(a, b):

    if a > b:
        return a

    else:
        return b

# Check Positive or Negative

def check_positive_negative(num):

    if num > 0:
        return "Positive"

    elif num < 0:
        return "Negative"

    else:
        return "Zero"


# Calculate Square

def calculate_square(num):
    return num * num

# Reverse String

def reverse_string(text):
    return text[::-1]


# Count Characters

def count_characters(text):
    return len(text)


# Calculate Factorial

def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

# Main Menu

while True:

    print()
    print("===== MENU =====")
    print("1. Add Two Numbers")
    print("2. Check Even or Odd")
    print("3. Find Maximum Number")
    print("4. Check Positive or Negative")
    print("5. Calculate Square")
    print("6. Reverse String")
    print("7. Count Characters")
    print("8. Calculate Factorial")
    print("9. Exit")

    choice = input("Enter Your Choice : ")


    # Add Two Numbers

    if choice == "1":

        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number : "))

        result = add_numbers(num1, num2)

        print("Result :", result)

    # Check Even or Odd

    elif choice == "2":
        num = int(input("Enter Number : "))
        result = check_even_odd(num)
        print("Number is", result)


    # Find Maximum Number

    elif choice == "3":

        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second Number : "))
        result = find_maximum(num1, num2)
        print("Maximum Number :", result)


    # Check Positive or Negative

    elif choice == "4":
        num = float(input("Enter Number : "))
        result = check_positive_negative(num)
        print("Number is", result)


    # Calculate Square

    elif choice == "5":
        num = float(input("Enter Number : "))
        result = calculate_square(num)
        print("Square :", result)

    # Reverse String

    elif choice == "6":
        text = input("Enter A String : ")
        result = reverse_string(text)
        print("Reversed String :", result)


    # Count Characters

    elif choice == "7":
        text = input("Enter A String : ")
        result = count_characters(text)
        print("Number Of Characters :", result)


    # Calculate Factorial

    elif choice == "8":
        num = int(input("Enter Number : "))
        if num < 0:
            print("Factorial is not possible for negative numbers")

        else:
            result = calculate_factorial(num)
            print("Factorial :", result)


    # Exit

    elif choice == "9":
        print("Thank You For Using Utility Library")
        break


    # Invalid Choice

    else:
        print("Invalid Choice")