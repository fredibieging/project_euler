# http://projecteuler.net/problem=23

is_abundant = list()

def sum_of_divisors(n):
  return sum([x for x in xrange(1, int(n / 2) + 1) if n % x == 0])

def cant_be_written(n):
  i = 1
  while i <= n / 2:
    if is_abundant[i] and is_abundant[n - i]:
      return False
    i += 1
  return True
        
the_sum = 0
for number in xrange(28124): 
  is_abundant.append(sum_of_divisors(number) > number)
  if cant_be_written(number):
    the_sum += number
print the_sum
