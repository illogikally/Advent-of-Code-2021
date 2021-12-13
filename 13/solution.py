from collections import defaultdict

input = open('input').read().splitlines()

b = 0
M = 0
m = 0
N = 0
n = 0
dots = 0
paper = defaultdict(bool)
for line in input:
  b += 1
  if not line:
    break
  j, i = [int(x) for x in line.split(',')]
  M = max(i, M)
  N = max(j, N)
  dots += 1
  paper[(i, j)] = True
  
intructions = input[b:]

def print_paper(m, M, n, N, dots):
  print()
  print("({}, {}), ({}, {}), {}".format(m, M, n, N, dots))
  for i in range(m, M+1):
    for j in range(n, N+1):
      x = '#' if paper[(i, j)] else '.'
      print(x, end='')
    print()

def fold(dims, intruction, dots):
  axis, line = intruction.split(' ')[-1].split('=')
  line = int(line)
  m, M, n, N = dims
  if axis == 'x':
    n, N, m, M = dims
  d = -1 if line > M//2 else 1
  i = 1
  while line-i in range(m, M+1) and line+i in range(m, M+1):
    for j in range(n, N+1):
      pos = ()
      if axis == 'x':
        pos = (j, line-(i*d))
        op_pos = (j, line+(i*d))
      else:
        pos = (line-(i*d), j)
        op_pos = (line+(i*d), j)

      if paper[pos] & paper[op_pos]:
        dots -= 1
      paper[pos] |= paper[op_pos]
    i += 1

  if line < M//2:
    m = line+1
  else:
    M = line-1
  
  return (m, M, n, N, dots) if axis == 'y' else (n, N, m, M, dots)

for intruction in intructions:
  m, M, n, N, dots = fold((m, M, n, N), intruction, dots);
    
print_paper(m, M, n, N, dots)
