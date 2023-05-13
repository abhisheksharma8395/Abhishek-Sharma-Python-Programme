n = int(input("Enter a number: "))
prime_sum = 0
for num in range(2, n+1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += num
print(f"The sum of prime numbers between 1 and {n} is: {prime_sum}")