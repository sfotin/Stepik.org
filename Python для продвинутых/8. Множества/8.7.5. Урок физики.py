sets = [set(input().split()) for _ in range(3)]

print(*sorted(sets[2] - (sets[0] | sets[1]), key=int, reverse=True))
