#http://projecteuler.net/problem=2

def fibonacci():
  fib = [1, 2]
  while True:
    the_next = fib[-2] + fib[-1]
    if the_next > 4000000:
      break
    fib.append(the_next)
  return fib

print sum(n for n in fibonacci() if n % 2 == 0)
