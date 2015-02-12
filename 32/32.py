# https://projecteuler.net/problem=32

def is_pandigital(n):
	return len(set(sorted(n.replace('0', '')))) == 9	

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
