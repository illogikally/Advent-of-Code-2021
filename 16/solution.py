from functools import reduce

hexa = open('input').read().strip()
transmission = bin(int('1'+hexa, 16))[3:]

def literal(i):
  value = ''
  while s := transmission[i]:
    value += transmission[i+1:i+5]
    i += 5
    if s == '0':
      break
  return (int(value, 2), i)

def operator(i):
  label = transmission[i]
  sub_versions = 0
  values = []
  if label == '0':
    l = int(transmission[i+1:i+16], 2)
    i += 16
    co = i
    while i - co != l:
      version, i, value = packet(i)
      sub_versions += version
      values.append(value)
  else:
    n = int(transmission[i+1:i+12], 2)
    i += 12
    for _ in range(n):
      version, i, value = packet(i)
      sub_versions += version
      values.append(value)

  return (sub_versions, i, values)

def product(values):
  return reduce(lambda x, y: x*y, values)

switch = {
  0: sum,
  1: product,
  2: min,
  3: max,
  5: lambda v: int(v[0] >  v[1]),
  6: lambda v: int(v[0] <  v[1]),
  7: lambda v: int(v[0] == v[1])
}

def packet(i):
  version = int(transmission[i:i+3], 2)
  tid = int(transmission[i+3:i+6], 2)
  value = 0

  if tid == 4:
    value, i = literal(i+6)
    return (version, i, value)

  sub_versions, i, values = operator(i+6)
  version += sub_versions
  value = switch[tid](values)
  return (version, i, value)

print(packet(0))