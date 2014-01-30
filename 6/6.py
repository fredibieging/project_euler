# http://projecteuler.net/problem=6

numbers = range(1, 101)
print (sum(numbers) ** 2) - sum([n * n for n in numbers])
