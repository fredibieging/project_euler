# https://projecteuler.net/problem=53

from combinatorics import *

solution = 0
for n in xrange(23, 101):
    for r in xrange(1, n):
        if combinatorics(n, r) > 1000000:
            solution = solution + 1
print solution
