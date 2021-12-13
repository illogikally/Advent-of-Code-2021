input = open('input').read().splitlines()

b = 0
M = 0
N = 0
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

def print_paper(M, N, dot_count):
  print()
  print(M, N, dot_count)
  for i in range(M+1):
    for j in range(N+1):
      x = '#' if (i, j) in dots else '.'
      print(x, end='')
    print()

def fold(M, N, intruction, dot_count):
  axis, line = intruction.split(' ')[-1].split('=')
  line = int(line)

  for (i, j) in dots.copy():
    dots.remove((i, j))
    if axis == 'y' and i > line:
      i = line*2 - i
    elif axis == 'x' and j > line:
      j = line*2 - j
    if (i, j) in dots:
      dot_count -= 1

    dots.add((i, j))
  
  M, N = (M, N//2-1) if axis == 'x' else (M//2-1, N) 
  return (M, N, dot_count)

for intruction in intructions:
  M, N, dot_count = fold(M, N, intruction, dot_count)
print_paper(M, N, dot_count)
