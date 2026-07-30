# Write a function to check if the input value is Armstrong or not

def armstrong(num):
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10

    if num == total:
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")

num = int(input("Enter a number: "))
armstrong(num)