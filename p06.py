# Write Python programs to work with the following:
# i) input( )
# ii) print( )
# iii) ‘sep’ attribute
# iv) ‘end’ attribute
# v) replacement Operator ({ })

name = input("Enter your name: ")

print("Welcome", name)

print("Python", "is", "fun", sep="-")

print("Hello", end=" ")
print(name)

age = 20
print("{} is {} years old.".format(name, age))