n = int(input())
matrix = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j] = '*'
        elif i == n - j - 1:
            matrix[i][j] = '*'
        elif i == n // 2:
            matrix[i][j] = '*'
        elif j == n // 2:
            matrix[i][j] = '*'

for row in matrix:
    print(*row)
