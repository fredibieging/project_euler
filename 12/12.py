#http://projecteuler.net/problem=12

import math

def number_of_factors(n):
  i = 2;
  count = 2;
  limit = math.sqrt(n)
  while i < limit:
    if n % i == 0:
      count += 2
    i += 1;
  if i * i == n:
    count += 1 
  return count

step = 2
triangle = 1
while number_of_factors(triangle) < 500:
  triangle += step
  step += 1

print triangle
