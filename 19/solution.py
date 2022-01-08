from itertools import combinations, permutations, product
from collections import defaultdict, deque
import sys
import pickle
report = open('exa.input').read().split('\n\n')

bacons = [[tuple(map(int, x.split(','))) for x in y.splitlines()[1:]] for y in report]

def sub(p, x):
  return (p[0] - x[0], p[1] - x[1], p[2] - x[2])

def add(p, x):
  return (p[0] + x[0], p[1] + x[1], p[2] + x[2])

def diff(a, b):
  return (
    abs(a[0] - b[0]),
    abs(a[1] - b[1]),
    abs(a[2] - b[2])
  )

ds = ( 
  lambda p: (p[0], p[1], p[2]),
  lambda p: (-p[0], -p[1], p[2]),
  lambda p: (p[1], -p[0], p[2]),
  lambda p: (-p[1], p[0], p[2]),
  lambda p: (p[2], p[1], -p[0]),
  lambda p: (-p[2], p[1], p[0]),
)

rs = (
  lambda p: (p[0], p[1], p[2]),
  lambda p: (p[0], -p[2], p[1]),
  lambda p: (p[0], -p[1], -p[2]),
  lambda p: (p[0], p[2], -p[1]),
)

def manhattan(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def dd():
  bd = []
  for b in bacons:
    distances = set() 
    for pair in combinations(b, 2):
      x, y = pair
      distances.add(diff(x, y))
    bd.append(distances)
  return bd

b_distances = dd()
print(len(b_distances))
print(len(b_distances[0]))
for pair in combinations(b_distances, 2):
  sa, sb = pair
  count = 0
  for p in sa:
    if (set.intersection(set(permutations(p)), sb)):
      count += 1
      if count >= 36:
        print('pog')
        break
        
  # if len(set.intersection(sa, sb)) >= 12:
  #   print('gto')
    
  

sys.exit()
N = len(bacons[0])
linked = set()
q = deque()
def solve(base_scanner, r_scanner):
  for d in ds:
    for r in rs:
      ss1 = [r(d(x)) for x in r_scanner]
      for big in ss1[:N-11]:
        for boy in base_scanner:
          s = (big, boy)
          scanner_pos = sub(s[1], s[0])
          matched = set()
          ss1_c = ss1.copy()
          matched.add(s[1])
          ss1_c.remove(s[0])
          # for p in ss1:
          while ss1_c:
            p = ss1_c.pop()
            if len(ss1_c) + len(matched) < 11:
              break

            for k in base_scanner:
              if k not in matched and sub(k, p) == scanner_pos:
                matched.add(k)
                if len(matched) == 12:
                  return ((r, d), scanner_pos)
                break

treer = defaultdict(list)
weet = defaultdict(tuple)
def get_0(i, rs):
  rs.append(i)
  if i == 0:
    return rs
    
  b = treer[i]
  for ve in b:
    if ve not in rs:
      r = get_0(ve, rs)
      if r[-1] == 0:
        rs = r
        break
  return rs



scanners = [(0,0,0)]*len(bacons)
linked = defaultdict(bool)
visited = set()
beacons = set()
sss = []
def bigg():
  q.append(0)
  beacons.update(bacons[0])
  while q:
    print(len(sss))
    index = q.popleft()
    for i in range(len(bacons)):
      if index == i or linked[(i, index)]:
        continue
      m = solve(bacons[index], bacons[i])
      if m:
        linked[(index, i)] = True
        (r, d), pos = m
        scanners[i] = pos
        transformed = [add(r(d(x)), pos) for x in bacons[i]]
        # mat.append(i)
        # beacons.update(transformed)
        bacons[i] = transformed
        if i not in visited:
          q.append(i)
          sss.append(i)
          visited.add(i)


  max_d = -float('inf')
  for i in range(len(scanners)):
    for j in range(i+1, len(scanners)):
      max_d = max(max_d, manhattan(scanners[i], scanners[j]))
  
  print(max_d)

      
  # print(len(beacons))


  with open('beacons', 'wb') as f:
    pickle.dump(scanners, f, protocol=pickle.HIGHEST_PROTOCOL)

  with open('records', 'wb') as f:
    pickle.dump(bacons, f, protocol=pickle.HIGHEST_PROTOCOL)
  print('saved output')

bigg()
sys.exit()
