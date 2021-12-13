from collections import defaultdict
import sys

input = open('input').read().splitlines()
# Part 1
# output = [x for line in input  for x in line.split(" | ")[1].split(" ")]
# print(functools.reduce(lambda a, b: a + int(len(b) in (2,3,7,4)), output, 0))

# Part 2
toNumber = {x[1]: x[0] for x in enumerate(['abcefg',
                                            'cf', 
                                            'acdeg', 
                                            'acdfg', 
                                            'bcdf', 
                                            'abdfg', 
                                            'abdefg',  
                                            'acf', 
                                            'abcdefg', 
                                            'abcdfg'])}

total = 0
for line in input:
  outputs = [x for x in line.split(" | ")[1].split(" ")]

  length = defaultdict(list)
  for signal in [x for x in line.split(" | ")[0].split(" ")]:
    length[len(signal)].append(signal)

  two_three_five = length[5]
  zero_six_nine  = length[6]
  one            = length[2][0]
  four           = length[4][0]
  seven          = length[3][0]
  eight          = length[7][0]


  def differ(*args):
    args = list(args)
    r = set(args.pop(0))
    for arg in args:
      r -= set(arg)
    return r

  seg = {}
  seg['a'] = differ(seven, one)
  seg['g'] = {len(x): x for x in [differ(s, seven, four) for s in zero_six_nine]}[1]
  seg['d'] = {len(x): x for x in [differ(s, seven, seg['g']) for s in two_three_five]}[1]
  seg['b'] = differ(four, one, seg['d'])
  seg['f'] = {len(x): x for x in [differ(s, seg['a'], seg['b'], seg['d'], seg['g']) for s in two_three_five]}[1]
  seg['c'] = differ(one, seg['f'])
  seg['e'] = differ(eight, seg['a'], seg['g'], seg['d'], seg['b'], seg['f'], seg['c'])

  rev_seg = {x[1].pop(): x[0] for x in seg.items()}

  def mapper(output):
    return toNumber["".join(sorted(rev_seg[c] for c in output))]

  total += int("".join([str(mapper(output)) for output in outputs]))

print(total)


