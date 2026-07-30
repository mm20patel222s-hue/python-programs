# Write a function that reverses the user defined value using python.

def reverse_string(s):
    return s[::-1]

text = input("Enter a string: ")

print("Reversed:", reverse_string(text))