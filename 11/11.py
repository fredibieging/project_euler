# http://projecteuler.net/problem=11

def read_grid():
  grid = []
  lines = open("grid").read().splitlines()
  for line in lines:
    grid.append([int(n) for n in line.split()]) 
  return grid

def horizontal(x, y, size, grid):
  return brute_force(x, y, 0, 1, size, grid)

def vertical(x, y, size, grid):
  return brute_force(x, y, 1, 0, size, grid)

def left_diagonal(x, y, size, grid):
  return brute_force(x, y, 1, -1, size, grid)

def right_diagonal(x, y, size, grid):
  return brute_force(x, y, 1, 1, size, grid)

def brute_force(x, y, factor_x, factor_y, size, grid):
  if x + 4 * factor_x < size and y + 4 * factor_y < size and y + 4 * factor_y >= 0:
    result = grid[x][y]
    for i in range(1, 4):
      result *= grid[x + factor_x * i][y + factor_y * i]
    return result
  return 0

grid = read_grid()
size = len(grid)
greatest = 0
for x in range(0, size):
  for y in range(0, size):
    greatest = max(vertical(x, y, size, grid), greatest)
    greatest = max(horizontal(x, y, size, grid), greatest)
    greatest = max(left_diagonal(x, y, size, grid), greatest)
    greatest = max(right_diagonal(x, y, size, grid), greatest)
print greatest
