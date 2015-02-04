# https://projecteuler.net/problem=45

import math

def is_triangle(triangle):
	return ((-1 + math.sqrt(1 + 8 * triangle)) / 2.0).is_integer()

def is_pentagonal(pentagonal):
	return ((1 + math.sqrt(1 + 24 * pentagonal)) / 6.0).is_integer()

def hexagonal(h):
	return h * (2 * h - 1)

h = 144
while True:
	n = hexagonal(h)
	if is_triangle(n) and is_pentagonal(n):
		break
	h = h + 1
print n
