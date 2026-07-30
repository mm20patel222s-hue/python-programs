# Write a function that takes a character (i.e. a string of length 1) and returns True if it
# is a vowel, False otherwise.

def is_vowel(char):
    return char.lower() in "aeiou"

ch = input("Enter a character: ")

print(is_vowel(ch))