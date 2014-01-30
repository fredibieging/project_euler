# http://projecteuler.net/problem=49

def remove_multiples(l):
  n = l[0]
  l2 = []
  for x in range(0, len(l)):
    if l[x] % n != 0:
      l2.append(l[x]);
  return l2;

def is_permutation(first, second, third):
  first = sorted(first)
  second = sorted(second)
  third = sorted(third)
  if first == second and first == third:
    return True
  return False

numbers = range(2, 10000)      
primes = []
while len(numbers) > 0:
  primes.append(numbers[0])
  numbers = remove_multiples(numbers)
numbers = [p for p in primes if p > 1000]

ignore_it = 1487
difference = 3330
for first in [n for n in numbers if n < (difference * 2)]:
  second = first + difference
  third = second + difference
  if second in numbers and third in numbers and first != ignore_it: 
    first = str(first)
    second = str(second)
    third = str(third)
    if is_permutation(first, second, third):
      print first + second + third
