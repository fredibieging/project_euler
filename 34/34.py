# http://projecteuler.net/problem=34

import math

result = 0
factorial = [math.factorial(x) for x in xrange(0,10)]

for number in xrange(3, 10000000):
	factorial_sum = sum([factorial[int(x)] for x in str(number)])
	if (number == factorial_sum):
		result = result + number

print result
