def findPrimeFactors(num):
    prime_factors = []
    while num % 2 == 0:
        prime_factors.append(2)
        num = num // 2
    for i in range(3, int(num**0.5) + 1, 2):
        while num % i == 0:
            prime_factors.append(i)
            num = num // i
    if num > 2:
        prime_factors.append(num)
    return prime_factors

num = int(input("Enter a number: "))
factors = findPrimeFactors(num)
print(f"The prime factors of {num} are: {factors}")
