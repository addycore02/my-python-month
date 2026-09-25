#### ROBUST ATM ####

print("        ROBUST ATM        ")

pin = "1234"
balance = 5000
transactions = []

def verify_pin():
    attempts = 0

    while attempts < 3:
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            print("PIN verified successfully!")
            return True

        attempts += 1
        print("Incorrect PIN.")

        if attempts < 3:
            print("Attempts remaining:", 3 - attempts)

    print("Too many incorrect attempts.")
    return False

def check_balance():
    print("\nCurrent Balance:", balance)

def deposit_money():
    global balance

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Amount must be greater than 0.")

        else:
            balance += amount
            transactions.append("Deposited ₹" + str(amount))
            print("Money deposited successfully.")
            print("Updated Balance:", balance)

    except ValueError:
        print("Invalid amount. Please enter a number.")

def withdraw_money():
    global balance

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Amount must be greater than 0.")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance -= amount
            transactions.append("Withdrawn ₹" + str(amount))
            print("Please collect your cash.")
            print("Remaining Balance:", balance)

    except ValueError:
        print("Invalid amount. Please enter a number.")

def change_pin():
    global pin

    old_pin = input("Enter your current PIN: ")

    if old_pin != pin:
        print("Incorrect current PIN.")
        return

    new_pin = input("Enter your new 4-digit PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    confirm_pin = input("Confirm your new PIN: ")

    if new_pin != confirm_pin:
        print("PINs do not match.")
        return

    pin = new_pin
    print("PIN changed successfully.")

def show_transactions():

    if len(transactions) == 0:
        print("\nNo transactions available.")

    else:
        print("\nTransaction History:")

        for i, transaction in enumerate(transactions, start=1):
            print(i, "]", transaction)

if verify_pin():

    while True:

        print("\n----------------------------")
        print("        ATM MENU")
        print("----------------------------")
        print("1] Check Balance")
        print("2] Deposit Money")
        print("3] Withdraw Money")
        print("4] Change PIN")
        print("5] Transaction History")
        print("6] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit_money()

        elif choice == "3":
            withdraw_money()

        elif choice == "4":
            change_pin()

        elif choice == "5":
            show_transactions()

        elif choice == "6":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")

else:
    print("ATM locked. Please try again later.")