def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def isStrongNumber(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += factorial(digit)
        temp //= 10
    return num == sum

num = int(input("Enter a number: "))
if isStrongNumber(num):
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")