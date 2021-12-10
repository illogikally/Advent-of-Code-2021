from collections import defaultdict
from functools import reduce
import sys

# Adding walls of 9 around input
# 999999
# 9....9
# 9....9
# 999999
M = 0
N = 0
matrix = []
with open('input') as input:
  for line in input:
    if not matrix:
      N = len(line.strip()) + 2
      matrix.append(['9']*N)
    n = [x for x in line.strip()]
    n.insert(0, '9')
    n.append('9')
    matrix.append(n)
    M += 1
  matrix.append(['9']*N)
  M += 2

positions = set([(i, j) for j in range(1, N-1) for i in range(1, M-1)])

def flood(pos):
  sum = 0
  children = [pos]
  i, j = pos
  matrix[i][j] = '9'
  while children:
    child = children.pop()
    i, j = child
    adjs = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
    sum += 1
    for adj in adjs:
      i, j = adj
      if matrix[i][j] != '9':
        children.append(adj)
        positions.remove(adj)
        matrix[i][j] = '9'
  return sum

b = [0]*3
while positions:
  i, j = positions.pop()
  if matrix[i][j] != '9':
    r = flood((i, j))
    for i in range(3):
      if b[i] < r:
        b.insert(i, r)
        break

print(b[0] * b[1] * b[2])

# Part 1
# def smolest(x, args):
#   (i, j) = pos
#   adjs = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
#   for arg in args:
#     if x >= arg:
#       return False
#   return True;

# sum = 0
#     adjs = [matrix[(i, j+1)], matrix[(i, j-1)], matrix[(i-1, j)], matrix[(i+1, j)]]
#     if smolest(matrix[(i,j)], adjs):
#       sum += matrix[(i,j)]+1