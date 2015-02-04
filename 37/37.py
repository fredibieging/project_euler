# https://projecteuler.net/problem=37

def partitions(n):
	n = str(n)
	partitions = set()
	for i in xrange(1, len(n)):
		partitions.add(int(n[:i]))	
		partitions.add(int(n[i:]))	
	return list(partitions)

limit = 800000
sieve = [False] * 2 + [True] * limit
for n in xrange(2, limit + 1):
        if sieve[n]:
                for i in xrange(n * n, limit + 1, n):
                        sieve[i] = False

for n in xrange(10, limit + 1):
	if sieve[n]:
		if any(character in '0 4 6 8' for character in list(str(n))):
			sieve[n] = False

the_sum = 0
for number in [n for n in xrange(8, limit + 1) if sieve[n] == True]:
	truncable = True
	for partition in partitions(number):
		if sieve[partition] == False:
			truncable = False
			break
	if truncable:
		the_sum += number
print the_sum
