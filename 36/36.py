# http://projecteuler.net/problem=36

def is_palindrome(string):
  return string == string[::-1]

sum = int()
for number in range(1, 1000000, 2):
  decimal = str(number)
  if is_palindrome(decimal):
    binary = str(bin(number)[2:])
    if is_palindrome(binary):
      sum += number
print sum
