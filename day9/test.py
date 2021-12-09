def xx(x, y):
  if y > 2:
    return 0
  print('yo')
  for i in range(5):
    x += xx(1, y+1)
  return x

f = 0
print(xx(f, 0))