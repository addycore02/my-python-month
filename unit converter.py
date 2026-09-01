#### UNIT CONVERTER ####

print(" 1) Celsius to Farenheit ")
print(" 2) Kilometers to Miles ")
print(" 3) Kilograms to Pounds ")

choice = input(" Enter Your Choice [ 1, 2, 3 ]: " )

if choice == "1":
    celsius = float(input("Enter The Celsius : "))
    farenheit = (celsius * 9 / 5 ) + 32
    print(f"{celsius} C : {farenheit:.2f} F")

elif choice == "2":
    kilometers = float(input(" Enter The Kilometers : "))
    miles = ( kilometers * 0.6213 )
    print(f"{kilometers} km  : {miles:.2f} miles ")

elif choice == "3":
    kg = float(input("Enter The Kilograms : "))
    pounds = ( kg * 2.2026 )
    print(f"{kg} kg : {pounds:.2f} pounds ")

else :
    print( " Choice Not Found ")


