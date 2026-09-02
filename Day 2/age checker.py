#### AGE CHECKER ####

print(" AGE CHECKER ")

name = input(" Enter Your Name : ")
age = int(input("Enter Your Age : "))

if age <= 12:
    category = "Child"

elif age <= 17:
    category = "Teenager"

elif age <= 45:
    category = "Adult"

elif age <= 59:
    category = "Senior"

else :
    category = "Senior Citizen"

print(f"Name : {name} and Age : {age} is under {category}")

