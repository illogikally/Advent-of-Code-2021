input = open('input').read().splitlines()

matrix = [[int(x) for x in line] for line in input]

def flash(pos):
  i, j = pos
  adjs = [(i+ii, j+jj) for jj in (-1, 0, 1) for ii in (-1, 0, 1)]
  adjs = set([(i, j) for (i, j) in adjs if i in range(0, 10) and j in range(0, 10)])
  flashed.add(pos)
  for adj in adjs:
    i, j = adj
    matrix[i][j] += 1
    if matrix[i][j] > 9 and (i, j) not in flashed:
      flashed.add(adj)
      flash((i, j))

def step():
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      matrix[i][j] += 1
      if matrix[i][j] > 9 and (i, j) not in flashed:
        flash((i, j))

  flash_count = len(flashed)

  while flashed:
    i, j = flashed.pop()
    matrix[i][j] = 0
  
  return flash_count
  
  
flashed = set()
flash_count = 0
all_flashed = 0
while True:
  all_flashed += 1
  if step() == 100:
    print(all_flashed)
    break