#http://projecteuler.net/problem=20

def fat(n):
  if n == 1:
    return 1
  return n * fat(n - 1)

print sum([int(x) for x in str(fat(100))])
