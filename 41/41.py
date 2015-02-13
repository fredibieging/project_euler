# https://projecteuler.net/problem=41

import itertools
from prime import *

ndigital = "1"
all_ndigitals = []

for i in xrange(2, 10):
	all_ndigitals = all_ndigitals + [n for n in list(map("".join, itertools.permutations(ndigital))) if is_prime(int(n))]
	ndigital = ndigital + str(i)

print max(all_ndigitals)
