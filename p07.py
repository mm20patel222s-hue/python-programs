# Write a Python program to work with the Conditional statements in Python with
# suitable examples. 
# i) if statement 
# ii) if else statement 
# iii) if – elif – else statement


num = int(input("Enter a number: "))

if num > 0:
    print("Positive")

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")