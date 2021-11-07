list1 = list(input())
list1.sort()
list2 = sorted(set(list1))

print('YES' if list1 == list2 else 'NO')
