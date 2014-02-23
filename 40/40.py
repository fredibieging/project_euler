# http://projecteuler.net/problem=40

from operator import mul

dn = int()
sequence = str()
while len(sequence) < 1000000:
  dn += 1
  sequence += str(dn)

print reduce(mul, [int(sequence[10 ** exp - 1]) for exp in range(7)])
