n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

flag = True
mask = []

matrix_r = [[0] * n for i in range(n)]
for i in range(n):
    mask.append(i + 1)
    for j in range(n):
        matrix_r[i][j] = matrix[j][i]

for i in range(n):
    matrix[i].sort()
    matrix_r[i].sort()
    if matrix[i] != mask or matrix_r[i] != mask:
        flag = False

print('YES' if flag else 'NO')
