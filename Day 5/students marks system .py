#### STUDENTS MARKS SYSTEM ####

print(" ---- STUDENTS MARKS SYSTEM ---- ")

print(" ENTER STUDENTS DETAILS ")
stu_name = input(" Enter Your Name : ")
roll_no = int(input(" Enter Your Roll Number : "))

subjects = ["English","Maths","Science","History","Geography","Hindi","Marathi"]

number = int(input(" Enter number of Subjects : "))

selected_subjects = subjects[:number]

print(selected_subjects)

marks_list = []

for subject in selected_subjects:
    marks = int(input(f"Enter marks for {subject}: "))
    marks_list.append(marks)


# Calculate Total Marks
total_marks = sum(marks_list)

# Calculate Percentage
percentage = total_marks / number

print(f" Total Marks : {total_marks}")
print(f" Percentage : {percentage}%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print(f" Grade : {grade}")

#### OUTPUT ####

 ---- STUDENTS MARKS SYSTEM ----
 ENTER STUDENTS DETAILS
 Enter Your Name : Addy
 Enter Your Roll Number : 01
 Enter number of Subjects : 5
['English', 'Maths', 'Science', 'History', 'Geography']
Enter marks for English: 75
Enter marks for Maths: 90
Enter marks for Science: 80
Enter marks for History: 70
Enter marks for Geography: 60
 Total Marks : 375
 Percentage : 75.0%
 Grade : B