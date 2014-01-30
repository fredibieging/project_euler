#http://projecteuler.net/problem=7

primes = [2, 3]
candidate = primes[-1] + 2
length = 2
while length < 10001:
  for index, prime in enumerate(primes):
    if candidate % prime == 0:
      break
    if index == (length - 1):
      primes.append(candidate)
      length += 1
  candidate += 2
print primes[-1]
