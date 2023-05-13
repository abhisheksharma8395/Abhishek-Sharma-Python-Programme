def isArmstrongNumber(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum

n = int(input("Enter a number: "))
armstrong_numbers = []
for num in range(1, n+1):
    if isArmstrongNumber(num):
        armstrong_numbers.append(num)
print(f"The Armstrong numbers between 1 and {n} are: {armstrong_numbers}")