from collections import defaultdict

input = open('input').read()
template, rules = input.split('\n\n')
rules = {k: v for line in rules.split('\n') for k, v in [line.split(' -> ')]}

char_count = defaultdict(int)
for c in template:
  char_count[c] += 1

pair_count = defaultdict(int)
for i in range(len(template)):
  p = template[i:i+2]
  if len(p) == 2: pair_count[p] += 1

for _ in range(40):
  for k, v in list(pair_count.items()):
    p = rules[k]
    char_count[p] += v
    pair_count[k] -= v
    pair_count[k[0]+p] += v
    pair_count[p+k[1]] += v

l = sorted(list(map(lambda x: x[1], char_count.items())))
print(l[-1] - l[0])