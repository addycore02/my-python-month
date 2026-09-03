#### ROCK PAPER SCISSOR GAME ####

import random
print(" Welcome To Rock Paper Scissor Game ")

user_option = input(" Enter Your Option : " )

option = [ "rock" , "paper" , "scissor"]

computer_option = random.choice(option)

print(f"Your choice is {user_option} and Computer Choice is {computer_option}")

if user_option == computer_option :
    print(" Draw ")

elif (user_option == "rock" and computer_option == "scissor"):
    print(" You Win ")

elif (user_option == "paper" and computer_option == "rock"):
    print(" You Win ")

elif (user_option == "scissor" and computer_option == "paper"):
    print(" You Win ")

else :
    print("You Lose")

