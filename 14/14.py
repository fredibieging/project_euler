# http://projecteuler.net/problem=14

chain = [0, 1]

def generate_sequence(n):
  if n < len(chain):
    return chain[n]
  if n % 2 == 0:
    n /= 2
  else:
    n = 3 * n + 1
  return 1 + generate_sequence(n);

for n in range(2, 1000000):
  chain.append(generate_sequence(n))

print chain.index(max(chain))
