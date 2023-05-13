num = int(input("Enter a number: "))
product_of_digits = 1
while num > 0:
    digit = num % 10
    product_of_digits *= digit
    num = num // 10
print(f"The product of digits is: {product_of_digits}")