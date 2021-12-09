import numpy as np

input = open('aoc3.input').read().splitlines()
data = np.array([list(map(lambda x: int(x), list(line))) for line in input])

def rating(mask, data=data):
  for i in range(len(data[0])):
    if len(data) == 1:
      break;
    data = data[mask(data[:,i], 0 + np.sum(data[:,i]) >= len(data)/2), :]
  return int("".join(str(x) for x in data.flatten()), 2)

print(rating(lambda x, y: x == y) * rating(lambda x, y: x != y))



