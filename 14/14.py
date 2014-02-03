# http://projecteuler.net/problem=14

chain = {1: 1}

def generate_sequence(n):
  if n in chain:
    return chain[n]
  if n % 2 == 0:
    n /= 2
  else:
    n = 3 * n + 1
  return 1 + generate_sequence(n);

for n in range(1, 1000000):
  chain[n] = generate_sequence(n)

print max(chain.keys(), key=lambda x: chain[x])
