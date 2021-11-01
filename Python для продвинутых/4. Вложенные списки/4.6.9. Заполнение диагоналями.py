n, m = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]
count = 0

for z in range(1, n + m):  # размер "окна"
    # заполняем побочную диагональ "окна" как для z-размерной матрицы
    for i in range(n):
        for j in range(m):
            if i == z - j - 1:
                count += 1
                matrix[i][j] = count

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
