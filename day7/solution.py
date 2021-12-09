import math

input = sorted([int(x) for x in open("input").read().split(",")])

maxX = max(input)
cost = [0] * (maxX+1)
for i in range(1, maxX+1):
  cost[i] = cost[i-1]+i

smol = (0, math.inf)
for i in range(min(input), maxX+1):
  fuel_cost = 0
  for j in input:
    fuel_cost += cost[abs(j-i)]
  smol = (i, fuel_cost) if fuel_cost < smol[1] else smol

print(smol)

