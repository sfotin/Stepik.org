n, k1 = [int(x) for x in input().split()]
matrix1 = [[int(x) for x in input().split()] for _ in range(n)]
input()
k2, m = [int(x) for x in input().split()]
matrix2 = [[int(x) for x in input().split()] for _ in range(k2)]

matrix_result = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        for k in range(k1):
            matrix_result[i][j] += matrix1[i][k] * matrix2[k][j]

for row in matrix_result:
    print(*row)
