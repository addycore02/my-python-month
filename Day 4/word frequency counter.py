#### WORD FREQUENCY COUNTER ####

print(" WORD FREQUENCY COUNTER ")

text = input("Enter a sentence: ")

words = text.lower().split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1


print("\n     WORD FREQUENCY    ")

for word in frequency:
    print(word, ":", frequency[word])

#### Output ####

     WORD FREQUENCY
hey : 1
, : 1
i'm : 1
doing : 1
my-python-month : 1
for : 1
30 : 1
days : 1
and : 1
today : 1
is : 1
my : 1
day : 1
4 : 1