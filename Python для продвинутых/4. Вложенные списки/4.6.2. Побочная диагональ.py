n = int(input())
matrix = [[0 for _ in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == n-j-1:
            matrix[i][j] = 1
        elif i > n-j-1:
            matrix[i][j] = 2

for row in matrix:
    print(*row)
