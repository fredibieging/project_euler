#http://projecteuler.net/problem=12

import math

def factors(n):
  i = 2;
  count = 2;
  while i < math.sqrt(n):
    if n % i == 0:
      count += 2
    i += 1;
  if i * i == n:
    count += 1 
  return count

step = 2
triangle = 1
while factors(triangle) < 500:
  triangle += step
  step += 1
print triangle
