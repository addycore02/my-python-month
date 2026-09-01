#### SIMPLE CALCULATOR ####

num1 = float(input(" Enter The First Number : "))
num2 = float(input(" Enter The Second Number : "))

# Addition
print( num1 + num2 )

# Subtraction
print( num1 - num2 )

# Multiplication
print( num1 * num2 )

# Division
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")