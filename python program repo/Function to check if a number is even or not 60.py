def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if check_even(number):
    print("The number is even.")
else:
    print("The number is not even.")