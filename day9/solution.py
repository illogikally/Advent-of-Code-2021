from collections import defaultdict
from functools import reduce
import sys

matrix = defaultdict(lambda: float('inf'))
with open('bb.input') as input:
  i = 0
  for line in input:
    for j in range(len(line.strip())):
      matrix[(i,j)] = int(line[j])
    i += 1

def flood(pos, positions, matrix=matrix):
  sum = 0
  children = [pos]
  matrix[pos] = 9
  while children:
    child = children.pop()
    (i, j) = child
    adjs = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
    sum += 1
    for adj in adjs:
      if matrix[adj] not in (9, float('inf')):
        children.append(adj)
        positions.remove(adj)
        matrix[adj] = 9
  return sum


basins = []
positions = set(matrix.keys())
while positions:
  pos = positions.pop()
  if matrix[pos] != 9:
    basins.append(flood(pos, positions))

print(reduce(lambda x, y: x*y, sorted(basins)[-3:]))

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