#### SQUARE & CUBE GENERATOR ####

print(" SQUARE & CUBE GENERATOR ")

print(" 1] Square of Given Number ")
print(" 2] Cube of Given Number ")

choice = int(input(" Enter Your Choice : "))

num = int(input(" Enter Number : "))

if choice == 1 :
    square = num ** 2
    print(f" Square of The Given Number : {square}")

elif choice == 2 :
    cube = num ** 3
    print(f" Cube  of The Given Number : {cube}")

else :
    print(" Invalid Choice ")

