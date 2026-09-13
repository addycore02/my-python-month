#### PALINDROME CHECKER ####

print("    PALINDROME CHECKER    ")

word = input(" Enter a word : ")
# Tell user to Enter a Word


word = word.lower()
# It converts the words into lower case

reverse_word = word[::-1]
# It reverses the given word or string


if word == reverse_word:
# It checks whether the word is equal to the reversed word

    print(" It is a Palindrome ")
    # If the above condition is true , it prints it


else:

    print(" It is Not a Palindrome ")
    # If condition is false then , it prints it

## OUTPUT ##

    PALINDROME CHECKER
 Enter a word : madam
 It is Not a Palindrome

    PALINDROME CHECKER
 Enter a word : Addy
 It is Not a Palindrome