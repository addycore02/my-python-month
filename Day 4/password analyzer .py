#### PASSWORD ANALYZER ####

print(" PASSWORD ANALYZER ")

password = input("Enter Your Password: ")

# Checking variables
has_uppercase = False
has_lowercase = False
has_number = False
has_special = False

# Checking Every Character
for character in password:

    if character.isupper():
        has_uppercase = True

    elif character.islower():
        has_lowercase = True

    elif character.isdigit():
        has_number = True

    else:
        has_special = True


# Password Score
score = 0

if len(password) >= 8:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_number:
    score += 1

if has_special:
    score += 1


# Display Analysis
print("\n----- PASSWORD ANALYSIS -----")

print("Password Length:", len(password))
print("Contains Uppercase:", has_uppercase)
print("Contains Lowercase:", has_lowercase)
print("Contains Number:", has_number)
print("Contains Special Character:", has_special)
print("Password Score:", score, "/ 5")


# Final Strength
if score <= 2:
    print("Password Strength: WEAK")

elif score <= 4:
    print("Password Strength: MEDIUM")

else:
    print("Password Strength: STRONG")


#### Output ####

 ----- PASSWORD ANALYSIS -----
Password Length: 9
Contains Uppercase: True
Contains Lowercase: True
Contains Number: True
Contains Special Character: True
Password Score: 5 / 5
Password Strength: STRONG