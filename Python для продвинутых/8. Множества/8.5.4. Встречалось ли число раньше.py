s = set()
for t in input().split():
    i = int(t)
    if i not in s:
        print('NO')
        s.add(i)
    else:
        print('YES')
