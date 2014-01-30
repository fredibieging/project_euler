# http://projecteuler.net/problem=5

divisors = range(2, 21)

accumulator = 1
while len(divisors) > 0:
  divisor = divisors[0]
  for x in range(0, len(divisors)):
    if divisors[x] % divisor == 0:
      divisors[x] /= divisor
  accumulator *= divisor
  divisors = [d for d in divisors if d > 1]
print accumulator
