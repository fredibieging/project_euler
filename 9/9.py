# http://projecteuler.net/problem=9

def find_pythagorean_triplet():
  for i in range(1, 1000):
    for j in range(i + 1, 1000):
      k = 1000 - i - j
      if i ** 2 + j ** 2 == k ** 2:
        return i * j * k
 
print find_pythagorean_triplet()      
