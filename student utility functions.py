####    STUDENT UTILITY FUNCTIONS    ####

print("    SSTDENT UTILITYV FUNCTIONS    ")

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return ( total / 500 ) * 100

def calculate_average(marks):
    return sum(marks) / len(marks)

def check_result(percentage):
    if percentage > 40:
        return " PASS "
    else:
        return " FAIL "

def calculate_grade(marks):
    if percentage >= 90:
        return " A+ "
    elif percentage >= 85:
        return " A "
    elif percentage >= 80:
        return " B+ "
    elif percentage >= 70:
        return " B "
    elif percentage >= 60:
        return " C "
    elif percentage >= 50:
        return " D "
    elif percentage >= 40:
        return " E "
    else :
        return " F "

name = input(" Enter Student Name : ")
marks = []

print(" Enter Marks 5 Subject ")

for i in range (5) :
    marks = float(input(f" Enter Subject {i=1} "))
    marks.append(mark)

total = calculate_total(marks)
percentage = calculate_percentage(marks)
average = calculate_average(marks)
result = check_result((percentage) )
grade = calculate_grade(marks)

print("    STUDENT RESULT    ")

print(" Student Name :", name)
print(" Total Marks :", total, "/ 500")
print(" Percentage :", percentage, "%")
print(" Average :", average)
print(" Result :", result)
print(" Grade :", grade)