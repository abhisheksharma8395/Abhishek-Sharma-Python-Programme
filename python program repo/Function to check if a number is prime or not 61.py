def check_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if check_prime(number):
    print("The number is prime.")
else:
    print("The number is not prime.")