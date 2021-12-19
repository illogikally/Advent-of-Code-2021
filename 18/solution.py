from functools import reduce
from copy import deepcopy
from copy import copy
homework = open('input').read().splitlines()


def pp(pair):
  p = pair
  while p.parent:
    p = p.parent
  print(p.to_string())
  print()

class Pair:
  def __init__(self, number='', depth=0, parent=None, position=None):
    self.values = [-1, -1]
    self.pairs = [None, None]
    self.depth = depth
    self.parent = parent
    self.position = position

    if not number:
      return
    l, r = self._parse(number)
    if l[0] != '[':
      self.values[0] = int(l)
    else:
      self.pairs[0] = Pair(l, self.depth+1, self, 0)

    if r[0] != '[':
      self.values[1] = int(r)
    else:
      self.pairs[1] = Pair(r, self.depth+1, self, 1)

  @staticmethod
  def add(a, b):
    pair = Pair()
    pair.depth = -1
    aa = deepcopy(a)
    bb = deepcopy(b)
    aa.position = 0
    bb.position = 1
    aa.parent = pair
    bb.parent = pair
    pair.pairs = [aa, bb]
    pair.increase_depth()
    while pair.not_reduced():
      pair.reduce()
    return pair
  
  def increase_depth(self):
    self.depth += 1
    for pair in self.pairs:
      if pair:
        pair.increase_depth()
        Pair.explode(pair)

  def reduce(self):
    for i in (0, 1):
      if self.pairs[i]:
        if self.pairs[i].reduce():
          return True
        if Pair.explode(self.pairs[i]):
          return True
      else:
        if Pair.split(self, i):
          return True

    return False

  def not_reduced(self):
    for i in (0, 1):
      if self.pairs[i]:
        if self.pairs[i].not_reduced():
          return True
      else:
        if self.values[i] >= 10:
          return True
    return False
    
  @staticmethod
  def split(pair, p):
    expl = False
    if pair.values[p] >= 10:
      v = pair.values[p]
      number = '[{},{}]'.format(v//2, (v+1)//2)
      # print(number)
      pair.pairs[p] = Pair(number, pair.depth+1, pair, p)
      pair.values[p] = -1
      # pp(pair)
      expl = Pair.explode(pair.pairs[p])
      expl = True
    return expl


  @staticmethod
  def explode(pair):
    if pair.depth >= 4:
      p = copy(pair)
      p.parent.values[p.position] = 0
      p.parent.pairs[p.position] = None
      if p.position == 0:
        parent = p.parent
        while parent.parent and parent.parent.pairs[0] == parent:
          parent = parent.parent
        
        if parent.parent:
          parent = parent.parent
          if parent.pairs[0]:
            n = parent.pairs[0]
            while n.pairs[1]:
              n = n.pairs[1]
            n.values[1] += p.values[0]
          else:
            parent.values[0] += p.values[0]
        
        parent = p.parent
        if parent.pairs[1]:
          n = parent.pairs[1]
          while n.pairs[0]:
            n = n.pairs[0]
          n.values[0] += p.values[1]
        else:
          parent.values[1] += p.values[1]
      else:
        parent = p.parent
        if parent.pairs[0]:
          n = parent.pairs[0]
          while n.pairs[1]:
            n = n.pairs[1]
          n.values[1] += p.values[0]
        else:
          parent.values[0] += p.values[0]
        
        parent = p.parent
        while parent.parent and parent.parent.pairs[1] == parent:
          parent = parent.parent
        
        if parent.parent:
          parent = parent.parent
          if parent.pairs[1]:
            n = parent.pairs[1]
            while n.pairs[0]:
              n = n.pairs[0]
            n.values[0] += p.values[1]
          else:
            parent.values[1] += p.values[1]
      # pp(p)
      return True
    return False
    
  def mag(self):
    mag = 0
    if self.pairs[0]:
      mag += 3*self.pairs[0].mag()
    else:
      mag += 3*self.values[0]

    if self.pairs[1]:
      mag += 2*self.pairs[1].mag()
    else:
      mag += 2*self.values[1]
    return mag

  def to_string(self):
    s = '['
    if self.pairs[0]:
      s += self.pairs[0].to_string()
    else:
      s += str(self.values[0])
    s += ','  

    if self.pairs[1]:
      s += self.pairs[1].to_string()
    else:
      s += str(self.values[1])
    s += ']'
    return s
      
  def _parse(self, number):
    i = 1
    o = 0
    while number[i] != ',' or o != 0:
      if number[i] == '[':
        o += 1
      if number[i] == ']':
        o -= 1
      i += 1
    return (number[1:i], number[i+1:-1])



# print(x.to_string())
# x.increase_depth()
# print(x.to_string())
# y = Pair('[1,1]')
# print(Pair.addition(x, y).to_string())


homework = [Pair(x) for x in homework]
# z = reduce(Pair.add, homework)
# # print(Pair.add(z, homework[4]).to_string())
# print(z.mag())


bigest = 0
h = homework
for i in range(len(homework)):
  print(i)
  for j in range(len(homework)):
    if j == i:
      continue
    r = Pair.add(h[i], h[j]).mag()
    bigest = max(r, bigest)

print(bigest)
# print(homework[8])
# print(homework[0])
# print(Pair.add(homework[8], homework[0]).mag())
# a = Pair('[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]')
# b = Pair('[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]')
# a = Pair('[[[[4,3],4],4],[7,[[8,4],9]]]')
# b = Pair('[1,1]')

# z = reduce(Pair.add, [a,b])
# print(z.to_string())
# print(z.mag())

# x = Pair('[[6,[5,[4,[3,2]]]],1]')
# print(x.to_string())
# x.increase_depth()
# print(x.to_string())
