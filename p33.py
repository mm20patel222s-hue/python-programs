# Write the function for the Input number is Palindrome or not.

def is_palindrome(num):
    temp = str(num)

    if temp == temp[::-1]:
        print(num, "is a Palindrome.")
    else:
        print(num, "is not a Palindrome.")

num = input("Enter a number: ")
is_palindrome(num)

