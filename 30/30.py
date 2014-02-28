# http://projecteuler.net/problem=30

# Since: 
# 7 digits => 10^6 > 7 * 9^5
# 6 digits => 10^5 < 6 * 9^5
# certainly doesn't exist a number greater than 7 * 9^5 that can be written as the sum of fifth powers of their digits.

def digit_fifth_power(number):
  power_sum = 0
  while number > 0:
    power_sum += (number % 10) ** 5
    number /= 10
  return power_sum

result = 0
for number in xrange(10, 7 * (9 ** 5)): 
  if number == digit_fifth_power(number):
    result += number
print result
