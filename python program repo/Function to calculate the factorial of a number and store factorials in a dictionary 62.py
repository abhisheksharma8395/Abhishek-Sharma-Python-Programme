factorial_dict = {}

def factorial(n):
    if n in factorial_dict:
        return factorial_dict[n]
    elif n == 0 or n == 1:
        factorial_dict[n] = 1
        return 1
    else:
        result = n * factorial(n - 1)
        factorial_dict[n] = result
        return result

number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial:", result)
print("Factorial Dictionary:", factorial_dict)
