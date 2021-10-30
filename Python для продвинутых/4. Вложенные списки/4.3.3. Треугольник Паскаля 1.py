def pascal(n):
    list1 = []
    for row in range(n + 1):
        elem_list = []
        for elem in range(row + 1):
            if elem == 0 or elem == row:
                elem_list.append(1)
            else:
                elem_list.append(list1[row - 1][elem] + list1[row - 1][elem - 1])
        list1.append(elem_list)
    return list1[n]

print(pascal(int(input())))
