# http://projecteuler.net/problem=24

def fat(n):
  if n == 1:
    return 1
  return n * fat(n-1)

result = str()
the_sum = atual = int()
the_list = range(10)

digits = len(the_list) - 1
while digits > 0:
  factorial = fat(digits)
  for i in xrange(len(the_list)):
    if factorial * (i + 1) + the_sum >= 1000000:
      the_sum += factorial * i
      result += str(the_list[i])
      digits -= 1
      del the_list[i]
      break
result += str(the_list[0])

print result
