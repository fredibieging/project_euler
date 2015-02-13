# https://projecteuler.net/problem=41

import itertools
from prime import *

ndigital = ""
all_ndigitals = []

for i in xrange(1, 10):
	ndigital = ndigital + str(i)
	all_ndigitals = all_ndigitals + [n for n in list(map("".join, itertools.permutations(ndigital))) if is_prime(int(n))]

print max(all_ndigitals)
