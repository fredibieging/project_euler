# http://projecteuler.net/problem=17

units = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
thousand = 11
_and = 3

def calculate(number):
  if number < 10:
    return units[number]
  elif number < 20:
    return teens[number - 10]
  elif number < 100:
    return tens[((int) (number / 10)) - 2] + calculate(number % 10)
  elif number < 1000:
    partial = units[(int) (number / 100)] + hundred 
    if number % 100 == 0:
      return partial
    return partial + _and + calculate(number % 100)
  return thousand

total = 0
for n in xrange(1, 1001):
  total += calculate(n)
print total

def number_size(number):
  return len(number.replace(" ", ""))

assert(calculate(1) == number_size("one"))
assert(calculate(9) == number_size("nine"))
assert(calculate(11) == number_size("eleven"))
assert(calculate(19) == number_size("nineteen"))
assert(calculate(21) == number_size("twenty one"))
assert(calculate(99) == number_size("ninety nine"))
assert(calculate(100) == number_size("one hundred"))
assert(calculate(101) == number_size("one hundred and one"))
assert(calculate(199) == number_size("one hundred and ninety nine"))
assert(calculate(200) == number_size("two hundred"))
assert(calculate(210) == number_size("two hundred and ten"))
assert(calculate(401) == number_size("four hundred and one"))
assert(calculate(1000) == number_size("one thousand"))
