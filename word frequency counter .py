#### WORD FREQUENCY COUNTER ####

print("    WORD FREQUENCY COUNTER    ")

string = input(" Enter a Word or Sentence : ")
# Tells the user to Enter the Text

string = string.lower()
# This converts the every text in the string into small words

words = string.split()
# We use because it seprates each word from the string

frequency = {}
# It is used to store words

for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

print(" Word Frequency : ")

for word, count in frequency.items():
    print(word, ":", count)

## OUTPUT ##
 Enter a Word or Sentence : Hey I'm Addy and I'm Learning Python
 Word Frequency :
hey : 1
i'm : 2
addy : 1
and : 1
learning : 1
python : 1

#### WORD FREQUENCY COUNTER ####

print("    WORD FREQUENCY COUNTER    ")

string = input(" Enter a Word or Sentence : ")
# Tells the user to Enter the Text

string = string.lower()
# This converts the every text in the string into small words

words = string.split()
# We use because it seprates each word from the string

frequency = {}
# It is used to store words

for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

print(" Word Frequency : ")

for word, count in frequency.items():
    print(word, ":", count)

## OUTPUT ##
 Enter a Word or Sentence : Hey I'm Addy and I'm Learning Python
 Word Frequency :
hey : 1
i'm : 2
addy : 1
and : 1
learning : 1
python : 1

