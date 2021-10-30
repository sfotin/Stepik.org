n, m = [int(i) for i in input().split()]
matrix = [['.' for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            matrix[i][j] = '*'

for row in matrix:
    print(*row)
