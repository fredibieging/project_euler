#http://projecteuler.net/problem=13

def read_numbers():
  numbers = open("50-digit-numbers").read().splitlines()
  return [int(n) for n in numbers]

print str(sum(read_numbers()))[0:10]

