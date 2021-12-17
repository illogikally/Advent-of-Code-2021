input = open('input').read().strip()

xran, yran = [tuple(map(int, x.split('=')[1].split('..'))) \
              for x in input.split(': ')[1].strip().split(',')]

area = set([(i, j) for j in range(xran[0], xran[1]+1) for i in range(yran[0], yran[1]+1)])

i = 0
j = 0
hits = []
for yyy in range(-1000, 1000):
  for xxx in range(1000):
    highest = 0
    print(yyy, xxx)
    xx = xxx
    yy = yyy
    while j <= xran[1] and i >= yran[0]:
      i += yy
      j += xx
      if yy == 0:
        highest = i

      if (i, j) in area:
        hits.append(highest)
        i = 0
        j = 0
        break
      xx = xx-1 if xx-1 > 0 else 0
      yy -= 1
    i = 0
    j = 0

print(len(hits))
