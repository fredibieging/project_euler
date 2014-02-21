#http://projecteuler.net/problem=22

def alphabetical_score(name):
  score = 0
  for character in list(name):
    score += ord(character) - 64
  return score

total = 0
names = sorted(open("names.txt").read().replace('"', '').split(','))
for position in xrange(len(names)):
  total += (position + 1) * alphabetical_score(names[position])

print total
