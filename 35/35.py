# https://projecteuler.net/problem=35

from sieve import *

def rotate(number, n):
	return int(number[n:] + number[:n])

def all_rotations(n):
	rotations = []
	for i in xrange(1, len(str(n)) + 1):
		rotation = rotate(str(n), i)
		if len(str(rotation)) < len(str(n)):
                        continue
		rotations.append(rotation)
	return rotations

limit = 1000000
the_sieve = sieve(limit)

for p in xrange(2, limit):
	if the_sieve[p]:
		rotations = all_rotations(p)
		circular = True
		for rotation in rotations:
			if the_sieve[rotation] is not True:
				circular = False
				break
		if circular is False:
			for rotation in rotations:
				the_sieve[rotation] = False

print the_sieve.count(True)	
