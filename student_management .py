#    STUDENT MANAGEMENT SYSTEM

import sqlite3
import csv

# DATABASE CONNECTION

def connect_database():
    # sqlite3.connect() creates the database file if it
    # does not already exist.
    return sqlite3.connect("students.db")

# CREATE TABLE

def create_table():

    connection = connect_database()
    cursor = connection.cursor()

    # CREATE TABLE IF NOT EXISTS prevents the table from
    # being created again if it already exists.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            maths REAL NOT NULL,
            python REAL NOT NULL,
            dbms REAL NOT NULL,
            total REAL NOT NULL,
            percentage REAL NOT NULL,
            grade TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

# STUDENT CLASS

class Student:

    def __init__(
        self,
        name,
        age,
        course,
        email,
        maths,
        python,
        dbms
    ):

        self.name = name
        self.age = age
        self.course = course
        self.email = email
        self.maths = maths
        self.python = python
        self.dbms = dbms

        # Calculate result automatically when Student object
        # is created.
        self.total = self.calculate_total()
        self.percentage = self.calculate_percentage()
        self.grade = self.calculate_grade()

    # CALCULATE TOTAL

    def calculate_total(self):

        return self.maths + self.python + self.dbms

    # CALCULATE PERCENTAGE

    def calculate_percentage(self):

        # There are 3 subjects, each carrying 100 marks.
        return (self.total / 300) * 100

    # CALCULATE GRADE

    def calculate_grade(self):

        if self.percentage >= 90:
            return "A+"

        elif self.percentage >= 80:
            return "A"

        elif self.percentage >= 70:
            return "B"

        elif self.percentage >= 60:
            return "C"

        elif self.percentage >= 50:
            return "D"

        elif self.percentage >= 40:
            return "E"

        else:
            return "F"

# VALIDATION FUNCTIONS

def get_name():

    while True:

        name = input("Enter Student Name : ").strip()

        if name == "":
            print("Name cannot be empty.")

        elif not name.replace(" ", "").isalpha():
            print("Name should contain only letters.")

        else:
            return name


# ------------------------------------------------------------

def get_age():

    while True:

        try:

            age = int(input("Enter Age : "))

            if age <= 0:
                print("Age must be greater than 0.")

            elif age > 100:
                print("Please enter a valid age.")

            else:
                return age

        except ValueError:

            print("Please enter a valid number.")


# ------------------------------------------------------------

def get_course():

    while True:

        course = input("Enter Course : ").strip()

        if course == "":
            print("Course cannot be empty.")

        else:
            return course


# ------------------------------------------------------------

def get_email():

    while True:

        email = input("Enter Email : ").strip()

        if email == "":
            print("Email cannot be empty.")

        elif "@" not in email or "." not in email:

            print("Please enter a valid email.")

        else:
            return email


# ------------------------------------------------------------

def get_marks(subject):

    while True:

        try:

            marks = float(
                input(f"Enter {subject} Marks (0-100) : ")
            )

            if marks < 0 or marks > 100:

                print("Marks must be between 0 and 100.")

            else:

                return marks

        except ValueError:

            print("Please enter a valid number.")

# ADD STUDENT

def add_student():

    print("\n========== ADD STUDENT ==========\n")

    name = get_name()
    age = get_age()
    course = get_course()
    email = get_email()

    maths = get_marks("Maths")
    python_marks = get_marks("Python")
    dbms = get_marks("DBMS")

    # Create Student object.
    student = Student(
        name,
        age,
        course,
        email,
        maths,
        python_marks,
        dbms
    )

    connection = connect_database()
    cursor = connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO students
            (
                name,
                age,
                course,
                email,
                maths,
                python,
                dbms,
                total,
                percentage,
                grade
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            student.name,
            student.age,
            student.course,
            student.email,
            student.maths,
            student.python,
            student.dbms,
            student.total,
            student.percentage,
            student.grade
        ))

        connection.commit()

        print("\nStudent added successfully.")
        print(f"Total      : {student.total}")
        print(f"Percentage : {student.percentage:.2f}%")
        print(f"Grade      : {student.grade}")

    except sqlite3.IntegrityError:

        print("\nError: This email already exists.")

    except sqlite3.Error as error:

        print(f"\nDatabase Error: {error}")

    finally:

        connection.close()

# VIEW ALL STUDENTS

def view_students():

    print("\n========== ALL STUDENTS ==========\n")

    connection = connect_database()
    cursor = connection.cursor()

    try:

        cursor.execute("""
            SELECT
                id,
                name,
                age,
                course,
                email,
                maths,
                python,
                dbms,
                total,
                percentage,
                grade
            FROM students
        """)

        students = cursor.fetchall()

        if len(students) == 0:

            print("No students found.")

        else:

            for student in students:

                print("----------------------------------------")

                print(f"ID         : {student[0]}")
                print(f"Name       : {student[1]}")
                print(f"Age        : {student[2]}")
                print(f"Course     : {student[3]}")
                print(f"Email      : {student[4]}")
                print(f"Maths      : {student[5]}")
                print(f"Python     : {student[6]}")
                print(f"DBMS       : {student[7]}")
                print(f"Total      : {student[8]}")
                print(f"Percentage : {student[9]:.2f}%")
                print(f"Grade      : {student[10]}")

            print("----------------------------------------")

    except sqlite3.Error as error:

        print(f"Database Error: {error}")

    finally:

        connection.close()

# SEARCH STUDENT

def search_student():

    print("\n========== SEARCH STUDENT ==========\n")

    print("1. Search by ID")
    print("2. Search by Name")
    print("3. Search by Course")

    choice = input("Enter Choice : ").strip()

    connection = connect_database()
    cursor = connection.cursor()

    try:

        if choice == "1":

            try:

                student_id = int(
                    input("Enter Student ID : ")
                )

            except ValueError:

                print("Invalid ID.")
                return

            cursor.execute(
                "SELECT * FROM students WHERE id = ?",
                (student_id,)
            )

        elif choice == "2":

            name = input("Enter Student Name : ").strip()

            cursor.execute(
                "SELECT * FROM students WHERE name LIKE ?",
                (f"%{name}%",)
            )

        elif choice == "3":

            course = input("Enter Course : ").strip()

            cursor.execute(
                "SELECT * FROM students WHERE course LIKE ?",
                (f"%{course}%",)
            )

        else:

            print("Invalid choice.")
            return

        students = cursor.fetchall()

        if len(students) == 0:

            print("\nNo student found.")

        else:

            for student in students:

                print("\n----------------------------------------")

                print(f"ID         : {student[0]}")
                print(f"Name       : {student[1]}")
                print(f"Age        : {student[2]}")
                print(f"Course     : {student[3]}")
                print(f"Email      : {student[4]}")
                print(f"Maths      : {student[5]}")
                print(f"Python     : {student[6]}")
                print(f"DBMS       : {student[7]}")
                print(f"Total      : {student[8]}")
                print(f"Percentage : {student[9]:.2f}%")
                print(f"Grade      : {student[10]}")

            print("----------------------------------------")

    except sqlite3.Error as error:

        print(f"Database Error: {error}")

    finally:

        connection.close()

# UPDATE STUDENT

def update_student():

    print("\n========== UPDATE STUDENT ==========\n")

    try:

        student_id = int(
            input("Enter Student ID to Update : ")
        )

    except ValueError:

        print("Invalid Student ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    try:

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        existing_student = cursor.fetchone()

        if existing_student is None:

            print("Student not found.")
            return

        print("\nEnter new details:\n")

        name = get_name()
        age = get_age()
        course = get_course()
        email = get_email()

        maths = get_marks("Maths")
        python_marks = get_marks("Python")
        dbms = get_marks("DBMS")

        student = Student(
            name,
            age,
            course,
            email,
            maths,
            python_marks,
            dbms
        )

        cursor.execute("""
            UPDATE students
            SET
                name = ?,
                age = ?,
                course = ?,
                email = ?,
                maths = ?,
                python = ?,
                dbms = ?,
                total = ?,
                percentage = ?,
                grade = ?
            WHERE id = ?
        """, (
            student.name,
            student.age,
            student.course,
            student.email,
            student.maths,
            student.python,
            student.dbms,
            student.total,
            student.percentage,
            student.grade,
            student_id
        ))

        connection.commit()

        print("\nStudent updated successfully.")

    except sqlite3.IntegrityError:

        print("Error: This email is already being used.")

    except sqlite3.Error as error:

        print(f"Database Error: {error}")

    finally:

        connection.close()

# DELETE STUDENT

def delete_student():

    print("\n========== DELETE STUDENT ==========\n")

    try:

        student_id = int(
            input("Enter Student ID to Delete : ")
        )

    except ValueError:

        print("Invalid Student ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    try:

        cursor.execute(
            "SELECT name FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if student is None:

            print("Student not found.")
            return

        print(f"Student Name: {student[0]}")

        confirmation = input(
            "Are you sure you want to delete? (yes/no) : "
        ).lower().strip()

        if confirmation == "yes":

            cursor.execute(
                "DELETE FROM students WHERE id = ?",
                (student_id,)
            )

            connection.commit()

            print("Student deleted successfully.")

        else:

            print("Delete operation cancelled.")

    except sqlite3.Error as error:

        print(f"Database Error: {error}")

    finally:

        connection.close()

# CALCULATE RESULT

def calculate_result():

    print("\n========== CALCULATE RESULT ==========\n")

    try:

        student_id = int(
            input("Enter Student ID : ")
        )

    except ValueError:

        print("Invalid Student ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    try:

        cursor.execute("""
            SELECT
                name,
                maths,
                python,
                dbms
            FROM students
            WHERE id = ?
        """, (student_id,))

        student = cursor.fetchone()

        if student is None:

            print("Student not found.")
            return

        name = student[0]
        maths = student[1]
        python_marks = student[2]
        dbms = student[3]

        # Create Student object again to calculate result.
        result = Student(
            name,
            0,
            "",
            "",
            maths,
            python_marks,
            dbms
        )

        print("----------------------------------------")
        print(f"Student    : {name}")
        print(f"Maths      : {maths}")
        print(f"Python     : {python_marks}")
        print(f"DBMS       : {dbms}")
        print(f"Total      : {result.total}")
        print(f"Percentage : {result.percentage:.2f}%")
        print(f"Grade      : {result.grade}")
        print("----------------------------------------")

    except sqlite3.Error as error:

        print(f"Database Error: {error}")

    finally:

        connection.close()

# EXPORT DATA TO CSV

def export_data():

    print("\n========== EXPORT DATA ==========\n")

    connection = connect_database()
    cursor = connection.cursor()

    try:

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        if len(students) == 0:

            print("No student data available to export.")
            return

        # Create CSV file.
        with open(
            "students_export.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            # Column headings.
            writer.writerow([
                "ID",
                "Name",
                "Age",
                "Course",
                "Email",
                "Maths",
                "Python",
                "DBMS",
                "Total",
                "Percentage",
                "Grade"
            ])

            # Write student records.
            writer.writerows(students)

        print(
            "\nStudent data exported to "
            "'students_export.csv' successfully."
        )

    except sqlite3.Error as error:

        print(f"Database Error: {error}")

    except OSError as error:

        print(f"File Error: {error}")

    finally:

        connection.close()

# MAIN PROGRAM

def main():

    # Create database table before starting the application.
    create_table()

    while True:

        print("\n")
        print("=" * 45)
        print("       STUDENT MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Result")
        print("7. Export Data")
        print("8. Exit")

        print("=" * 45)

        choice = input("Enter Your Choice : ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            calculate_result()

        elif choice == "7":

            export_data()

        elif choice == "8":

            print("\nThank you for using Student Management System.")
            break

        else:

            print("\nInvalid choice. Please select 1-8.")

# PROGRAM START

if __name__ == "__main__":
    main()