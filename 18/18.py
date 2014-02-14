# http://projecteuler.net/problem=18

triangle = [[int(number) for number in row.split()] for row in open("triangle").read().splitlines()]

for i in xrange(1, len(triangle)):
	for j in xrange(len(triangle[i])):
		if j == 0:
			triangle[i][j] += triangle[i - 1][j]
		elif j == len(triangle[i]) - 1:
			triangle[i][j] += triangle[i - 1][j - 1]
		else:
			triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])
print max(triangle[len(triangle) - 1])
print triangle[len(triangle) - 1]

