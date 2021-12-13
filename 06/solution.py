initial_states = [int(x) for x in open("input").read().split(",")]
fish_tracker = [0] * 9
for state in initial_states:
  fish_tracker[state] += 1

for day in range(256):
  zeros = fish_tracker[0]

  for i in range(8):
    fish_tracker[i] = fish_tracker[i+1]
  fish_tracker[8] = zeros
  fish_tracker[6] += zeros

print(sum(fish_tracker))



