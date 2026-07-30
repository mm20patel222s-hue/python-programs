# Write a Python program to work with the following Operators in Python with
# suitable examples.
# i) Arithmetic Operators
# ii) Relational Operators
# iii) Assignment Operator
# iv) Logical Operators
# v) Bit wise Operators
# vi) Ternary Operator

a = 10
b = 3

print("Addition:", a + b)
print("Is a > b?", a > b)

a += 5
print("After += :", a)

print("Logical AND:", True and False)

print("Bitwise AND:", a & b)

max_value = a if a > b else b
print("Max value:", max_value)
