import re

arr = [ [ (c,int(x)) for c,x in [line.split()] ]
        for line in open('input').read().splitlines() ]

print(arr)
x = 0
y = 0
aim = 0
with open('aoc2.input') as input:
  for line in input:
    amount = int(line.split()[1])
    command = line.split()[0]
    if command == 'forward':
      x += amount;
      y += aim * amount
    elif command == 'up':
      aim -= amount
    else:
      aim += amount



print(x)
print(y)
print(x*y)

