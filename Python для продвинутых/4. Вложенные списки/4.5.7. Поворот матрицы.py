n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
matrix_90 = []

for j in range(n):
    temp = []
    for i in range(n-1, -1, -1):
        temp.append(matrix[i][j])
    matrix_90.append(temp)

for row in matrix_90:
    print(*row)
