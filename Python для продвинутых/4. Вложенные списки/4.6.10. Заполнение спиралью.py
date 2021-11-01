n, m = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]

num = 1  # заполнитель ячеек
left, right, top, bottom = 0, m - 1, 0, n - 1  # границы витка спирали
stop = (n + 1) // 2  # последний виток спирали

for start in range(stop):  # стартуем до последнего витка
    for to_right in range(left, right + 1):  # идём вправо
        matrix[start][to_right] = num
        num += 1
    for to_down in range(top + 1, bottom + 1):  # идём вниз
        matrix[to_down][right] = num
        num += 1
    if top == bottom or right == left:  # если спираль делает не полный оборот
        break
    for to_left in range(right - 1, left - 1, -1):  # идём влево
        matrix[bottom][to_left] = num
        num += 1
    for to_up in range(bottom - 1, top, -1):  # идём вверх
        matrix[to_up][left] = num
        num += 1
    left += 1
    right -= 1
    top += 1
    bottom -= 1
    if left > right or top > bottom:  # если одной петли достаточно
        break

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
