# http://projecteuler.net/problem=3

number = 600851475143
primes = [2]
while primes[-1] < number:
  while number % primes[-1] == 0:
    number = number / primes[-1]
  candidate = primes[-1] + 1
  while len([n for n in primes if candidate % n == 0]) > 0:
    candidate += 1
  primes.append(candidate)
print number
