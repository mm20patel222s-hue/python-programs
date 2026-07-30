# Write a Python program to return multiple values at a time using a return statement.

def student_details():
    name = "student"
    age = 22
    course = "BCA"
    return name, age, course

n, a, c = student_details()

print("Name:", n)
print("Age:", a)
print("Course:", c)