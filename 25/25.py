# http://projecteuler.net/problem=25

term = 2
the_previous = the_next = 1

while len(str(the_next)) != 1000:
  the_next, the_previous = the_next + the_previous, the_next
  term += 1

print term
