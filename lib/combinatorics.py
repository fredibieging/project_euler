def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n + 1))

def combinatorics(n, r):
    return reduce(lambda x, y: x*y, range(n, r, -1)) / factorial(n - r)
