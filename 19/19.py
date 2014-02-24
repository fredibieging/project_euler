# http://projecteuler.net/problem=19

def is_leap_year(y):
  return y % 4 == 0 and (not y % 100 is 0 or y % 400 is 0)

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sundays_felt_on_first_of_the_month = 0
dow = 2

for year in xrange(1900, 2001):
  months[1] = 28
  if is_leap_year(year): 
    months[1] = 29
  for month in months:
    for day in xrange(1, month + 1):
      if day == 1 and dow == 1 and year > 1900:
        sundays_felt_on_first_of_the_month += 1
      dow = (dow + 1) % 7

print sundays_felt_on_first_of_the_month
