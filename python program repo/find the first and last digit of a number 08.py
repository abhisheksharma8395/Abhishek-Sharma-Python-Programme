num = int(input("Enter a number: "))
first_digit = num % 10
while num >= 10:
    num = num // 10
last_digit = num
print(f"The first digit is: {first_digit}")
print(f"The last digit is: {last_digit}")