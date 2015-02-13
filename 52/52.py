# https://projecteuler.net/problem=52

def same_digits(numbers):
	return len(set(["".join(sorted(n)) for n in numbers])) == 1

x = 1
while True:
	if same_digits([str(n * x) for n in xrange(1,7)]):
		break
	x += 1

print x
