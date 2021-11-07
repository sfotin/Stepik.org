set1 = set([int(x) for x in input().split()])
set2 = set([int(x) for x in input().split()])
set_sorted = sorted(set1 & set2)
print(*set_sorted)
