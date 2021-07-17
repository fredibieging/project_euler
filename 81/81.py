#!/usr/bin/python
# http://projecteuler.net/problem=81

matrix = []
with open('matrix.txt') as the_file:
    for line in the_file:
        matrix.append([int(x) for x in line.split(",")])

rows = len(matrix)
for i in range(rows):
    for j in range(rows):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            matrix[i][j] = matrix[i][j] + matrix[i][j-1]
        elif j == 0:
            matrix[i][j] = matrix[i][j] + matrix[i-1][j]
        else:
            matrix[i][j] = min(matrix[i-1][j] + matrix[i][j], matrix[i][j-1] + matrix[i][j])

print(matrix[rows - 1][rows - 1])
