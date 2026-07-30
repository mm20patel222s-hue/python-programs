# Write a Python program to work with the control transfer statements in Python with
# suitable examples. 
# i) break 
# ii) continue 
# iii) pass

print("Break")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("Continue")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("Pass")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)