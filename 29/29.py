# http://projecteuler.net/problem=29

numbers = set()
for x in xrange(2, 101):
  for y in xrange(2, 101):
    numbers.add(x ** y)
print len(numbers)
