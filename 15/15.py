# http://projecteuler.net/problem=15

pascal = [1]
for _ in xrange(0, 40):
	pascal = [1] + [pascal[i] + pascal[i+1] for i in range(0, len(pascal) - 1)] + [1]
print pascal[len(pascal) / 2]
