color = [int(x) for x in input().split()]
print(*map(lambda x: 255 - x, color))
