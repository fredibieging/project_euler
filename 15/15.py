# http://projecteuler.net/problem=15
from operator import mul

print reduce(mul, range(21, 41)) / reduce(mul, range(1, 21))
