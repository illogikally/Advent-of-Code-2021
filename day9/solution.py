from collections import defaultdict
import functools

input = open('exa.input').read().splitlines()

matrix = defaultdict(lambda: float('inf'))
parsed = [[int(x) for x in line] for line in input]
positions = [tuple((x[0], j[0])) for x in enumerate(input) for j in enumerate(x[1])]

for pos in positions:
  matrix[pos] = parsed[pos[0]][pos[1]]

flooded = defaultdict(bool)

def flood(pos):
  flooded[pos] = True
  (i, j) = pos
  adjs = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))

  sum = 1
  for adj in adjs:
    if matrix[adj] != 9 and not flooded[adj] and matrix[adj] != float('inf'):
      sum += flood(adj)
  return sum

basins = []
for pos in positions:
  if matrix[pos] != 9 and not flooded[pos]:
    basins.append(flood(pos))

print(functools.reduce(lambda x, y: x*y, sorted(basins)[-3:]))

# def smolest(x, args):
#   for arg in args:
#     if x >= arg:
#       return False
#   return True;

# sum = 0
#     adjs = [matrix[(i, j+1)], matrix[(i, j-1)], matrix[(i-1, j)], matrix[(i+1, j)]]
#     if smolest(matrix[(i,j)], adjs):
#       sum += matrix[(i,j)]+1