#### QUIZ APPLICATION ####

print(" WELCOMR TO QUIZ ")

## 1 ##
print(" What is The Capital Of India ? ")
print(" A : Mumbai ")
print(" B : Indore ")
print(" C : Delhi ")
print(" D : Kolkata ")

option = input(" Enter Your Option : ")

score = 0

question = " What is the Capital Of India ? "

options = ["Mumbai" , "Indore", "Delhi" , "Kolkata"]

correct_option = "C"

if option.upper() == "C":
    print(" Correct Option ")
    score += 1

else :
    print(" Incorrect Option ")

## 2 ##
print(" What is The Financial Capital Of India ? ")
print(" A : Mumbai ")
print(" B : Indore ")
print(" C : Delhi ")
print(" D : Kolkata ")

option = input(" Enter Your Option : ")

question = " What is the Financial Capital Of India ? "

options = ["Mumbai" , "Indore", "Delhi" , "Kolkata"]

correct_option = "A"

if option.upper() == "A":
    print(" Correct Option ")
    score += 1
else :
    print(" Incorrect Option ")

## 3 ##
print(" Pink City Of India ? ")
print(" A : Mumbai ")
print(" B : Jaipur ")
print(" C : Delhi ")
print(" D : Jharkhand ")

option = input(" Enter Your Option : ")

question = " What is the Financial Capital Of India ? "

options = ["Mumbai" , "Jaipur" , "Delhi" , "Jharkhand"]

correct_option = "B"

if option.upper() == "B":
    print(" Correct Option ")
    score += 1
else :
    print(" Incorrect Option ")

## 4 ##
print(" Cleanest City Of India ? ")
print(" A : Mumbai ")
print(" B : Jaipur ")
print(" C : Delhi ")
print(" D : Indore ")

option = input(" Enter Your Option : ")

question = " Cleanest Of India ? "

options = ["Mumbai" , "Jaipur" , "Delhi" , "Indore"]

correct_option = "D"

if option.upper() == "D":
    print(" Correct Option ")
    score += 1
else :
    print(" Incorrect Option ")

## 5 ##
print(" Largest State Of India ? ")
print(" A : Maharashtra ")
print(" B : Rajasthan ")
print(" C : Uttar Pradesh ")
print(" D : Kerala ")

option = input(" Enter Your Option : ")

question = " Largest State Of India ? "

options = ["Maharashtra" , "Rajasthan" , "Uttar Pradesh" , "Kerala"]

correct_option = "B"

if option.upper() == "B":
    print(" Correct Option ")
    score += 1
else :
    print(" Incorrect Option ")

print(f" Your Score : {score} ")