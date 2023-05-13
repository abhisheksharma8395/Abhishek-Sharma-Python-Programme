def sumOfSquares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

n = int(input("Enter the value of n: "))
result = sumOfSquares(n)
print(f"The sum of squares of first {n} natural numbers is: {result}")