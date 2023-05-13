def computeLCM(a, b):
    hcf = computeHCF(a, b)
    lcm = (a * b) // hcf
    return lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
lcm = computeLCM(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm}")
