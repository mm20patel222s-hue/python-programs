# Write Python programs to print the following Patterns:
# 1
# 22
# 333
# 4444
# 55555
# A
# A B
# A B C
# A B C D
# A B C D E
# *****
# ****
# ***
# **
# *

for i in range(1, 6):
    print(str(i) * i)

print()

for i in range(1, 6):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()

print()

for i in range(5, 0, -1):
    print("*" * i)