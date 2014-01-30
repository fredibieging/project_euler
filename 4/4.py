# http://projecteuler.net/problem=4

def is_palindrome(w):
  return w == w[::-1]

biggest = 0
for i in range(100, 999):
  for j in range(i, 999):
    product = i * j
    if is_palindrome(str(product)) and product > biggest:
      biggest = product
print biggest
