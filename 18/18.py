# http://projecteuler.net/problem=18

triangle = [[0] + [int(number) for number in row.split()] + [0] for row in open("triangle").read().splitlines()]

for i in xrange(1, len(triangle)):
	for j in xrange(1, len(triangle[i]) - 1):
		triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])
print max(triangle[len(triangle) - 1])
print triangle[len(triangle) - 1]
