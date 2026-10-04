#### SQLITE STUDENT DATABASE ####

import sqlite3

# If the file exists, it connects to that database.
conn = sqlite3.connect("student.db")

# A cursor executes SQL commands and retrieves database results.
cursor = conn.cursor()

# CREATE TABLE creates a table to store student records.
# IF NOT EXISTS prevents an error if the table already exists.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT,
        percentage REAL
    )
""")

# Commit() saves database changes permanently.
conn.commit()

print("\n===== SQLITE STUDENT DATABASE =====")

while True:

    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # ADD STUDENT
    if choice == "1":

        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        percentage = float(input("Enter Percentage: "))

        try:
            cursor.execute("""
                INSERT INTO students
                (roll_no, name, age, course, percentage)
                VALUES (?, ?, ?, ?, ?)
            """, (roll_no, name, age, course, percentage))

            conn.commit()

            print("\nStudent added successfully!")

        except sqlite3.IntegrityError:
            print("\nError: Roll Number already exists!")

    # VIEW ALL STUDENTS
    elif choice == "2":

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        if len(students) == 0:
            print("\nNo student records found.")

        else:
            print("\n----- STUDENT RECORDS -----")

            for student in students:
                print(f"""
Roll Number : {student[0]}
Name        : {student[1]}
Age         : {student[2]}
Course      : {student[3]}
Percentage  : {student[4]}%
""")

    # SEARCH STUDENT
    elif choice == "3":

        roll_no = int(input("Enter Roll Number to Search: "))

        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        # It returns None if no matching record exists.
        student = cursor.fetchone()

        if student:
            print("\n----- STUDENT FOUND -----")
            print("Roll Number :", student[0])
            print("Name        :", student[1])
            print("Age         :", student[2])
            print("Course      :", student[3])
            print("Percentage  :", student[4], "%")

        else:
            print("\nStudent not found!")

    # UPDATE STUDENT
    elif choice == "4":

        roll_no = int(input("Enter Roll Number to Update: "))

        # Check whether the student exists before updating.
        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        student = cursor.fetchone()

        if student:

            print("\nEnter New Student Details")

            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            course = input("Enter New Course: ")
            percentage = float(input("Enter New Percentage: "))

            cursor.execute("""
                UPDATE students
                SET name = ?, age = ?, course = ?, percentage = ?
                WHERE roll_no = ?
            """, (name, age, course, percentage, roll_no))

            conn.commit()

            print("\nStudent updated successfully!")

        else:
            print("\nStudent not found!")

    elif choice == "5":

        roll_no = int(input("Enter Roll Number to Delete: "))

        cursor.execute(
            "SELECT * FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        student = cursor.fetchone()

        if student:

            cursor.execute(
                "DELETE FROM students WHERE roll_no = ?",
                (roll_no,)
            )

            conn.commit()

            print("\nStudent deleted successfully!")

        else:
            print("\nStudent not found!")


    # EXIT
    elif choice == "6":

        print("\nExiting Student Database...")
        break


    else:
        print("\nInvalid choice! Please try again.")

conn.close()

print("Database connection closed.")