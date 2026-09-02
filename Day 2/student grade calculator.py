#### STUDENT PERCENTAGE AND GRADE CALCULATOR ####

print(" PERCENTAGE AND GRADE CALCULATOR ")

name = input(" Enter Your Name : ")
Class = input(" Enter Your Class : ")

print(" Enter Your Subject Grades ")

eng = int(input(" Enter Marks for English : "))
maths = int(input(" Enter Marks for Maths : "))
sci = int(input(" Enter Marks for Science : "))
his = int(input(" Enter Marks for Political Science : "))
geo = int(input(" Enter Marks for Geography : "))

percentage = (( eng + maths + sci + his + geo ) / 500) * 100

if percentage >= 90:
    grade = "A+"
    print(" You Passed : A+ GRADE ")

elif percentage >= 85:
    grade = 'A"'
    print(" You Passed : A GRADE ")

elif percentage >= 75:
    grade = "B"
    print(" You Passed : B GRADE ")

elif percentage >= 60:
    grade = "C"
    print(" You Passed : C GRADE ")

elif percentage >= 50:
    grade = "D"
    print(" You Passed : D GRADE ")

else:
    print(" You Failed ")

print(f" Total Percentage {percentage} % for {name} from Class {Class} - Grade:{grade}  ")

