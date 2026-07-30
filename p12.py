# Write a Python program to copy the contents of a file to another file

with open("demo.txt", "r") as src, open("copy.txt", "w") as dst:
    dst.write(src.read())

print("File copied successfully.")