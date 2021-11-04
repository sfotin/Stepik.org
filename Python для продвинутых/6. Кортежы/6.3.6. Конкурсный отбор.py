n = int(input())
pupils = [tuple([x for x in input().split()]) for _ in range(n)]
for row in pupils:
    print(*row)
print()
for row in pupils:
    if row[-1] > '3':
        print(*row)
