#http://projecteuler.net/problem=16

a_big_number = 2 ** 1000
result = 0
while a_big_number:
	result += a_big_number % 10
	a_big_number /= 10
print result
