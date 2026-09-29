#### CSV EXPENSE ANALYZER ####

import csv
import os

FILE_NAME = "expenses.csv"


# CREATE CSV FILE IF IT DOES NOT EXIST
def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["Date", "Category", "Description", "Amount"])


# ADD EXPENSE
def add_expense():

    date = input("Enter Date : ")
    category = input("Enter Category : ")
    description = input("Enter Description : ")
    amount = float(input("Enter Amount : "))

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([date, category, description, amount])

    print("\nExpense Added Successfully!")


# VIEW EXPENSES
def view_expenses():

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        expenses = list(reader)

    if len(expenses) == 0:

        print("\nNo Expenses Found.")

    else:

        print("\n----------- ALL EXPENSES -----------")

        for i, expense in enumerate(expenses, start=1):

            print(
                i, "]",
                expense["Date"], "|",
                expense["Category"], "|",
                expense["Description"], "| ₹",
                expense["Amount"]
            )


# CALCULATE TOTAL EXPENSE
def total_expense():

    total = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for expense in reader:

            total += float(expense["Amount"])

    print("\nTotal Expense : ₹", total)


# FIND HIGHEST EXPENSE
def highest_expense():

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        expenses = list(reader)

    if len(expenses) == 0:

        print("\nNo Expenses Found.")

    else:

        highest = max(
            expenses,
            key=lambda expense: float(expense["Amount"])
        )

        print("\n----------- HIGHEST EXPENSE -----------")

        print("Date        :", highest["Date"])
        print("Category    :", highest["Category"])
        print("Description :", highest["Description"])
        print("Amount      : ₹", highest["Amount"])


# CATEGORY ANALYZER
def category_analysis():

    category_total = {}

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for expense in reader:

            category = expense["Category"]
            amount = float(expense["Amount"])

            if category in category_total:

                category_total[category] += amount

            else:

                category_total[category] = amount

    if len(category_total) == 0:

        print("\nNo Expenses Found.")

    else:

        print("\n----------- CATEGORY ANALYSIS -----------")

        for category, amount in category_total.items():

            print(category, ":", "₹", amount)


# MAIN PROGRAM

create_file()

while True:

    print("\n================================")
    print("       CSV EXPENSE ANALYZER")
    print("================================")

    print("1] Add Expense")
    print("2] View Expenses")
    print("3] Total Expense")
    print("4] Highest Expense")
    print("5] Category Analysis")
    print("6] Exit")

    choice = input("\nEnter Your Choice : ")

    if choice == "1":

        add_expense()

    elif choice == "2":

        view_expenses()

    elif choice == "3":

        total_expense()

    elif choice == "4":

        highest_expense()

    elif choice == "5":

        category_analysis()

    elif choice == "6":

        print("\nThank You for Using CSV Expense Analyzer!")
        break

    else:

        print("\nInvalid Choice. Please Try Again.")