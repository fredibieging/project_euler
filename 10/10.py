#http://projecteuler.net/problem=10

limit = 2000000
primes = []
sieve = [True] * limit
for p in range(2, limit):
  if sieve[p]:
    primes.append(p)
    for i in range(p * p, limit, p):
      sieve[i] = False
print sum(primes)
