#### RANDOM PASSWORD GENERATOR ####

import random
import string

string.ascii_lowercase
string.ascii_uppercase
string.digits
string.punctuation

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

length = int(input(" Enter The Length Of The Password : "))

password = ""

for i in range(length) :
    password = password + random.choice(characters)

print(f" Random Genrerated Password : {password} ")