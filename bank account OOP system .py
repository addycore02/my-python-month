#### BANK ACCOUNT OOP SYSTEM ####

print("    BANK ACCOUNT OOP SYSTEM    ")



class BankAccount:

    def __init__(self, name, account_number, account_type, balance):

        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance


    def view_account(self):

        print("\n---------- ACCOUNT DETAILS ----------")

        print("Account Holder :", self.name)
        print("Account Number :", self.account_number)
        print("Account Type   :", self.account_type)
        print("Balance        :", self.balance)

        print("-------------------------------------")


    def deposit(self, amount):

        if amount <= 0:

            print("Invalid deposit amount.")

        else:

            self.balance = self.balance + amount

            print("Amount deposited successfully.")
            print("New Balance :", self.balance)


    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid withdrawal amount.")

        elif amount > self.balance:

            print("Insufficient balance.")

        else:

            self.balance = self.balance - amount

            print("Amount withdrawn successfully.")
            print("Remaining Balance :", self.balance)


    def check_balance(self):

        print("\nCurrent Balance :", self.balance)


print("\nCreate Your Bank Account")

name = input("Enter Account Holder Name : ")

account_number = input("Enter Account Number : ")

account_type = input("Enter Account Type : ")

balance = float(input("Enter Initial Balance : "))


account = BankAccount(
    name,
    account_number,
    account_type,
    balance
)


while True:

    print("    BANK ACCOUNT MENU    ")

    print("1] View Account")
    print("2] Deposit Money")
    print("3] Withdraw Money")
    print("4] Check Balance")
    print("5] Exit")

    choice = input("Enter Your Choice : ")


    if choice == "1":

        account.view_account()


    elif choice == "2":

        amount = float(input("Enter Amount to Deposit : "))

        account.deposit(amount)


    elif choice == "3":

        amount = float(input("Enter Amount to Withdraw : "))

        account.withdraw(amount)


    elif choice == "4":

        account.check_balance()


    elif choice == "5":

        print("\nThank you for using Bank Account System.")

        break


    else:

        print("Invalid choice. Please try again.")