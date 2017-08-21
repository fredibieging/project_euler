# https://projecteuler.net/problem=50

from prime import *

longest = 0
awswer = 0
the_primes = primes(1000000)
for x in xrange(0, len(the_primes) - 1):
    for y in xrange(x + 1, len(the_primes)):
        if y - x > longest:
            primes_sum = sum(the_primes[x:y])
            if primes_sum > 1000000:
                break
            if is_prime(primes_sum):
                longest = y - x
                answer = primes_sum
print answer
