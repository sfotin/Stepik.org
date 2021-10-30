list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1
for ls1 in list1:
    if max(ls1) > maximum:
        maximum = max(ls1)
print(maximum)
