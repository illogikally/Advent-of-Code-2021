from collections import defaultdict
from copy import deepcopy

input = open('input').read().splitlines()

g = defaultdict(list)

for line in input:
  x, y = line.split('-')
  if x != 'end' and y != 'start':
    g[x].append(y)
  if y != 'end' and x != 'start':
    g[y].append(x)


ended = []
def traverse(path, vertex, duplicate):
  path.append(vertex)

  if vertex == 'end':
    ended.append(path)
    return;

  for neighbor in g[vertex]:
    if neighbor.islower() and neighbor in path:
      if duplicate:
        continue
      else:
        traverse(path.copy(), neighbor, True)
    else:
      traverse(path.copy(), neighbor, duplicate)


traverse([], 'start', False)
print(len(ended))
