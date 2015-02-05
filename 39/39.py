# https://projecteuler.net/problem=39

max_perimeter = 1000
perimeter = [0] * max_perimeter

for p in xrange(1, len(perimeter)):
	for a in xrange(1, p):
		for b in xrange(a + 1, p - a):
			c = p - a - b
			if c * c == (a * a + b * b):
				perimeter[p] += 1
print perimeter.index(max(perimeter))
