a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print("Before swapping: a =", a, "and b =", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping: a =", a, "and b =", b)