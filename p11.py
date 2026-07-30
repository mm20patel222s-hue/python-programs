# Write a Python program to work with the read and write operations on a file.

file = open("demo.txt", "w")
file.write("Hello Python")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()