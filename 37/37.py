# https://projecteuler.net/problem=37

from sieve import *

def partitions(n):
	n = str(n)
	partitions = set()
	for i in xrange(1, len(n)):
		partitions.add(int(n[:i]))	
		partitions.add(int(n[i:]))	
	return list(partitions)

limit = 800000
the_sieve = sieve(limit)

for n in xrange(10, limit):
	if the_sieve[n]:
		if any(character in '0 4 6 8' for character in list(str(n))):
			the_sieve[n] = False

the_sum = 0
for number in [n for n in xrange(8, limit) if the_sieve[n] == True]:
	truncatable = True
	for partition in partitions(number):
		if the_sieve[partition] == False:
			truncatable = False
			break
	if truncatable:
		the_sum += number
print the_sum
