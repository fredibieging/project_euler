def factorial(n):
    if n <= 1 and n >= 0:
        return 1
    return n * factorial(n - 1)

def combinatorics(n, r):
    x = 1
    for i in range(n, r, -1):
        x = x * i
    return x / factorial(n - r)
