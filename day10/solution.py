input = open('input').read().splitlines()

pair     = {'(': ')', '[': ']', '{': '}', '<': '>'}
error    = {')': 3, ']': 57, '}': 1197, '>': 25137}
complete = {'(': 1, '[': 2, '{': 3, '<': 4}
close    = {')', '}', '>', ']'}

q = []

def solve(line):
  error_score = 0
  complete_score = 0
  for c in line:
    if c in close:
      if q:
        if pair[q.pop()] != c:
          error_score += error[c]
          break
      else:
        error_score += error[c]
        break
    else:
      q.append(c)
  
  while q:
    complete_score = complete_score * 5 + complete[q.pop()]
  return (complete_score, error_score)

complete_scores = []
total_error_score = 0
for line in input:
  c, e = solve(line.strip())
  if c and not e:
    complete_scores.append(c)
  if e:
    total_error_score += e

print(sorted(complete_scores)[len(complete_scores)//2])
print(total_error_score)