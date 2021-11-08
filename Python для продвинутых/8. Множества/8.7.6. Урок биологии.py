a, b, c = [set([int(x) for x in input().split()]) for _ in range(3)]
d = set(range(11))
print(*sorted(d - (a | b | c), key=int))
