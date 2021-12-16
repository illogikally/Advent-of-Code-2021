from collections import defaultdict

input = open('input').read().splitlines()

matrix = [[int(x) for x in line] for line in input]
M = len(matrix)*5
N = len(matrix[0])*5
unvisited = set([(i, j) for j in range(N) for i in range(M)])

distances = defaultdict(lambda: float('inf'))
distances[(0, 0)] = 0
ds = [(0, (0, 0))]
prev_vertex = {}

def get_shortest():
  while s := ds.pop()[1]:
    if s in unvisited: return s

def update(dist):
  ll = len(ds)
  low = 0
  high = ll-1
  mid = low + (high - low) // 2
  while True:
    if low == high or ll == 0:
      break

    left = ds[mid-1][0] if mid-1 >= 0 else float('inf')
    right = ds[mid+1][0] if mid+1 <= ll-1 else -float('inf')

    if ds[mid][0] <= dist[0]:
      if left >= dist[0]:
        break
    else:
      if right <= dist[0]:
        mid += 1
        break

    if ds[mid] >= dist: 
      low = mid+1
    else: 
      high = mid-1 

    mid = low + (high-low) // 2
  ds.insert(mid, dist)

def value(pos):
  w = len(matrix[0])
  h = len(matrix)
  i, j = pos
  r = (i//h + j//w) + matrix[i%h][j%w]
  return r if r < 10 else r%10 + 1

while unvisited:
  vertex = get_shortest()
  i, j = vertex
  adjs = ((i+1, j), (i, j+1), (i-1, j), (i, j-1))

  for adj in adjs:
    if adj not in unvisited: 
      continue
    current_distance = distances[vertex] + value(adj)
    if distances[adj] > current_distance:
      distances[adj] = current_distance
      update((current_distance, adj))
      prev_vertex[adj] = vertex
  unvisited.remove(vertex)

print(distances[(M-1, N-1)])