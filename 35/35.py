# https://projecteuler.net/problem=35

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
sieve = [False] * 2 + [True] * (limit - 2)
for p in xrange(2, limit):
	if sieve[p]:
		for i in xrange(p * p, limit, p):
			sieve[i] = False

for p in xrange(2, limit):
	if sieve[p]:
		rotations = all_rotations(p)
		circular = True
		for rotation in rotations:
			if sieve[rotation] is not True:
				circular = False
				break
		if circular is False:
			for rotation in rotations:
				sieve[rotation] = False

print sieve.count(True)	
