sets = [set([int(x) for x in input().split()]) for _ in range(3)]
print(*sorted(sets[0] & sets[1] - sets[2], reverse=True))
