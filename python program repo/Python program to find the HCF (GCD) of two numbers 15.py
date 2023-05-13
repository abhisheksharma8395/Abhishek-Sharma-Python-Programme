def computeHCF(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
hcf = computeHCF(num1, num2)
print(f"The HCF of {num1} and {num2} is: {hcf}")