#### PASSWORD CHECKING SYSTEM ####

print(" PASSWORD CHECKING SYSTEM ")

correct_password = "Python0102"
# It stores the correct password

max_attempts = 5
# Maximum Attempts that user will get

attempts = 0
# Initial attempt count is 0

sucess = False
# It means that logic is not successful yet

while attempts < max_attempts :
# Runs the loop while user has attempts left

    password = input(" Enter Your Password : ")
    # Ask the user to enter password

    if password == "":
        print(" Password Cannot be Empty ")
        # Display this above message if user entered nothing

        continue
        # Pause the loop and ask user to enter password again

    attempts += 1
    # Count by 1 because valid password is entered

    if password == correct_password :
        print(" You Entered Correct Password ")
        # Display this above message when user entered Correct Password

        sucess = True
        # False to True because logic changes

        break
        # Stops loop instantly because user entered Correct Password

    else:

        print(" Entered Incorrect Password ")
        # Appears when user entered incorrect password


        remaining = max_attempts - attempts
        # Calculation of how many attempts are available


        print(" Attempts Remaining : ", remaining )
        # Shows no of remaining password

if not success :


    print(" All attempts used . Account Locked ")
    # Runs when all attempts are used without success