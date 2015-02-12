
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

