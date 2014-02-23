# http://projecteuler.net/problem=21

import math

def calculate_divisors(n):
  return [x for x in xrange(1, int(n / 2) + 1) if n % x == 0]

limit = 10000
divisors_sum = [sum(calculate_divisors(i)) for i in xrange(limit)]
amicable = [n for n, ds in enumerate(divisors_sum) if ds < limit and n == divisors_sum[ds] and ds != n]

print sum(amicable)
