# http://projecteuler.net/problem=28

step = 2
the_sum = 1
while step < 1001:
  the_sum += 2 * (2 * (step + 1) ** 2 - 3 * step)
  step += 2

print the_sum
