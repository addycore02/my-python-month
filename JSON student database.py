#### JSON STUDENT DATABASE ####

import json

print(" JSON Student Database ")

print(" 1] Add Student ")
print(" 2] View Student ")
print(" 3] Update Student ")
print(" 4] Delete Student ")
print(" 5] Exit ")

try:
    with open("students.json", "r") as file:
        students = json.load(file)

except FileNotFoundError:
    students = {}

while True:

    choice = input("\nEnter Your Choice : ")

    if choice == "1":

        student_id = input("Enter Student ID : ")

        if student_id in students:
            print("Student ID already exists!")

        else:

            name = input("Enter Student Name : ")
            course = input("Enter Course : ")
            percentage = float(input("Enter Percentage : "))

            students[student_id] = {
                "name": name,
                "course": course,
                "percentage": percentage
            }

            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

            print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found!")

        else:

            for student_id, student in students.items():

                print("\nStudent ID :", student_id)
                print("Name       :", student["name"])
                print("Course     :", student["course"])
                print("Percentage :", student["percentage"])

    elif choice == "3":

        student_id = input("Enter Student ID to Update : ")

        if student_id in students:

            name = input("Enter New Name : ")
            course = input("Enter New Course : ")
            percentage = float(input("Enter New Percentage : "))

            students[student_id]["name"] = name
            students[student_id]["course"] = course
            students[student_id]["percentage"] = percentage

            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

            print("Student Updated Successfully!")

        else:
            print("Student ID Not Found!")

    elif choice == "4":

        student_id = input("Enter Student ID to Delete : ")

        if student_id in students:

            del students[student_id]

            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

            print("Student Deleted Successfully!")

        else:
            print("Student ID Not Found!")

    elif choice == "5":

        print("Exiting JSON Student Database...")
        break

    else:

        print("Invalid Choice! Please Enter 1 to 5.")