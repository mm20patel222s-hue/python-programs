# Write a Python program to compute the number of characters, words and lines in a
# file.

with open("demo.txt", "r") as file:
    text = file.read()

chars = len(text)
words = len(text.split())
lines = len(text.splitlines())

print("Characters:", chars)
print("Words:", words)
print("Lines:", lines)