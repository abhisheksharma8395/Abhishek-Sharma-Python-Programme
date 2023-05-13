n = int(input("Enter a number: "))
prime_numbers = []
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)
print(f"The prime numbers between 1 and {n} are: {prime_numbers}")