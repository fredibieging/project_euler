# https://projecteuler.net/problem=32

from pandigital import *

limit = 10000
products = set()
for a in xrange(1, limit):
	for b in xrange(a + 1, limit):
		product = a * b
		number = str(product) + str(a) + str(b)
		if len(number) > 9:
			break
		if is_pandigital(number):
			products.add(product)
print sum(products)
