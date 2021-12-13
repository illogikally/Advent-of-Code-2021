with open('exa.input', 'r') as f:
    input = [int(i) for i in f.read().strip().split(',')]
    lowest = 100000000000000000000000
    for i in range(max(input)):
        total = 0
        for crab in input:
            distance = abs(i - crab)
            total += distance * (distance + 1) / 2
        if lowest > total:
            lowest = total
        else:
            break
    print(lowest)
