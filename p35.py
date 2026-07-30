# Define a function that computes the length of a given list or string.

def compute_length(item):
    return len(item)

text = input("Enter a string: ")
print("Length of string:", compute_length(text))

lst = input("Enter list elements separated by space: ").split()
print("Length of list:", compute_length(lst))