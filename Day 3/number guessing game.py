#### NUMBEER GUESSSING GAME ####

print(" NUMBER GUESSING GAME ")
print(" Enter Number Between 1 and 100")

import random

computer_num = random.randint(1,100)
attempts = 0

while True:

    num = int(input(" Enter The Number : "))
    attempts += 1

    if num == computer_num:
        print(" You Guessed Correct Number ")
        print(" Attempts:", attempts)
        break

    elif num > computer_num:
        print(" You Guessed Too High ")

    else :
        print(" You Guessed Too Low ")

print(" Hope You Enjoyed Game ")
