
def sieve(limit):
	sieve = [False] * 2 + [True] * (limit - 2)
	for n in xrange(2, limit):
	        if sieve[n]:
	                for i in xrange(n * n, limit, n):
	                        sieve[i] = False
	return sieve

def primes(limit):
	candidates = sieve(limit)
	return [prime for prime in xrange(limit) if candidates[prime]]

def is_prime(number):
	if number <= 3:
		return number > 1
	if number % 2 == 0 or number % 3 == 0:
		return False
	for i in range(5, int(number ** 0.5) + 1, 6):
		if number % i == 0 or number % (i + 2) == 0:
			return False
	return True
