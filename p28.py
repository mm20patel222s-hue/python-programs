# Write a program that asks the user to enter their name and their age. Print out a
# message addressed to them that tells them the year that they will turn 60 years old.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

year = 2025 + (60 - age)

print(f"Hello {name}, you will turn 60 in the year {year}.")