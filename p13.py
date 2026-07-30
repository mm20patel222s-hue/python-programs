# Write a Python program to work with the count frequency of characters in a given
# file.

text = "banana"

freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)