input = open('input').read().splitlines()

b = 0
M = 0
m = 0
N = 0
n = 0
dot_count = 0
dots = set() 
for line in input:
  b += 1
  if not line:
    break
  j, i = [int(x) for x in line.split(',')]
  M = max(i, M)
  N = max(j, N)
  dot_count += 1
  dots.add((i, j))

intructions = input[b:]

def print_paper(m, M, n, N, dot_count):
  print()
  print("({}, {}), ({}, {}), {}".format(m, M, n, N, dot_count))
  for i in range(m, M+1):
    for j in range(n, N+1):
      x = '#' if (i, j) in dots else ' '
      print(x, end='')
    print()

def fold(dims, intruction, dot_count):
  axis, line = intruction.split(' ')[-1].split('=')
  line = int(line)
  m, M, n, N = dims
  if axis == 'x':
    n, N, m, M = dims
  d = -1 if line > M//2 else 1
  i = 1
  while line-i in range(m, M+1) and line+i in range(m, M+1):
    for j in range(n, N+1):
      pos, inv_pos = ((j, line-i*d), (j, line+i*d)) if axis == 'x'  \
          else ((line-i*d, j), (line+i*d, j))
      if pos in dots and inv_pos in dots:
        dot_count -= 1
      elif pos in dots or inv_pos in dots:
        dots.add(pos)
    i += 1

  if line < M//2:
    m = line+1
  else:
    M = line-1
  
  return (m, M, n, N, dot_count) if axis == 'y' else (n, N, m, M, dot_count)

for intruction in intructions:
  m, M, n, N, dot_count = fold((m, M, n, N), intruction, dot_count);
    
print_paper(m, M, n, N, dot_count)
