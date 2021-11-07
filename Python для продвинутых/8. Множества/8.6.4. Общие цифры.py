digits = [set(input()) for _ in range(int(input()))]
set1 = set(digits[0])
for s in range(1, len(digits)):
    set1.intersection_update(digits[s])

print(*sorted(set1))
