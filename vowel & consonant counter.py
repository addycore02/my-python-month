#### VOWEL & CONSONANT COUNTER ####

print(" VOWEL & CONSONANT COUNTER ")

text = input(" Enter a Word or Sentence : ")

text = text.lower()

vowels = 0
consonants = 0

for char in text:

    if char.isalpha():

        if char in "aeiou":
            vowels += 1

        else:
            consonants += 1

print(" Vowels     : " , vowels )
print(" Consonants : " , consonants )

# OUTPUT #

VOWEL & CONSONANT COUNTER
 Enter a Word or Sentence : Hello My Name is Addy
 Vowels     :  6
 Consonants :  11