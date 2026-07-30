# Write a Python program to print each line of a file in reverse order

with open("demo.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())