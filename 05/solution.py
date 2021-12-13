diagram = [[0 for _ in range(1000)] for __ in range(1000)]
overlaps = 0
with open('input') as input:
  for line in input:
    pos1, pos2 = sorted([tuple(int(x) for x in point.split(",")) for point in line.split(" -> ")])
    if pos1[0] == pos2[0]:
      for i in range(pos1[1], pos2[1]+1):
        if diagram[pos1[0]][i] == 1:
          overlaps += 1;
        diagram[pos1[0]][i] += 1

    elif pos1[1] == pos2[1]:
      for i in range(pos1[0], pos2[0]+1):
        if diagram[i][pos1[1]] == 1:
          overlaps += 1
        diagram[i][pos1[1]] += 1

    elif abs(pos2[0]-pos1[0]) == abs(pos2[1]-pos1[1]):
      sign = -1 if pos1[1] > pos2[1] else 1
      for i in range(pos2[0]-pos1[0]+1):
        if diagram[pos1[0]+i][pos1[1]+sign*i] == 1:
          overlaps += 1
        diagram[pos1[0]+i][pos1[1]+sign*i] += 1

print(overlaps)


  
