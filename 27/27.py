# https://projecteuler.net/problem=27

from prime import *

max_sequence = 0
for a in xrange(-999, 1000):
    for b in xrange(-1000, 1001):
        n = 0
        while is_prime(n ** 2 + a * n + b):
            n = n + 1
        if n > max_sequence:
            max_sequence, solution = n, a * b
print solution
