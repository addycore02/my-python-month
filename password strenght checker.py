#### PASSWORD STRENGTH CHECKER ####

print(" PASSWORD STRENGTH CHECKER ")

password = input(" Enter Your Password : ")

# we assume that password does not contain these things
has_uppercase = False
has_lowercase = False
has_number = False
has_special = False

# Checking every character in password

for char in password :

    if char.isupper():
        has_uppercase = True

    elif char.islower():
        has_lowercase = True

    elif char.isdigit():
        has_digit = True

    else:
        has_special = True

# Counting Password Requirements

score = 0

if len(password) >= 8:
        score += 1

if has_uppercase :
        score += 1

if has_lowercase :
        score += 1

if has_digit :
        score += 1

if has_special :
        score += 1

# Checking Strength Of Password

if score <= 2 :
    strength = " Weak "

elif score <= 4 :
    strength = " Easy "

elif score <= 6 :
    strength = " Hard "

else :
    strength = " Strong "


print(f"Your Password Strength is {strength}")