n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
m = int(input())
matrix_result = matrix.copy()

for r in range(m - 1):
    temp_result = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp_sum = 0
            for k in range(n):
                temp_sum += matrix_result[i][k] * matrix[k][j]
            temp.append(temp_sum)
        temp_result.append(temp)
    matrix_result = temp_result.copy()

for row in matrix_result:
    print(*row)
