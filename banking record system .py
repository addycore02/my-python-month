#### BANKING RECORD SYSTEM ####

print("    BANKING RECORD SYSTEM    ")

accounts = []

while True:

    print("\n 1] Create Account")
    print(" 2] View Accounts")
    print(" 3] Update Account")
    print(" 4] Delete Account")
    print(" 5] Exit")

    choice = input(" Enter Your Choice : ")

    if choice == "1":

        name = input(" Enter Account Holder Name : ")
        account_type = input(" Enter Account Type : ")
        account_number = int(input(" Enter Account Number : "))
        balance = int(input(" Enter Saving Amount : "))

        account = {
            "name": name,
            "type": account_type,
            "number": account_number,
            "balance": balance
        }

        accounts.append(account)

        print(" Account Created Successfully")

    elif choice == "2":

        if len(accounts) == 0:
            print(" No Accounts Found ")

        else:
            print("\n Stored Accounts :")

            for i, account in enumerate(accounts, start=1):
                print(
                    i, "]",
                    account["number"], "|",
                    account["name"], "|",
                    account["type"], "|",
                    account["balance"]
                )

    elif choice == "3":

        if len(accounts) == 0:
            print(" No Accounts Found ")

        else:
            account_number = int(input(" Enter Account Number to Update : "))

            found = False

            for account in accounts:

                if account["number"] == account_number:

                    print("\n Account Found ")

                    account["name"] = input(" Enter New Account Holder Name : ")
                    account["type"] = input(" Enter New Account Type : ")
                    account["balance"] = int(input(" Enter New Saving Amount : "))

                    print(" Account Updated Successfully ")

                    found = True
                    break

            if found == False:
                print(" Account Not Found ")

    elif choice == "4":

        if len(accounts) == 0:
            print(" No Accounts Found ")

        else:
            account_number = int(input(" Enter Account Number to Delete : "))

            found = False

            for account in accounts:

                if account["number"] == account_number:

                    accounts.remove(account)

                    print(" Account Deleted Successfully ")

                    found = True
                    break

            if found == False:
                print(" Account Not Found ")

    elif choice == "5":

        print(" Thank You for Using Banking Record System ")
        break

    else:
        print(" Invalid Choice ")
