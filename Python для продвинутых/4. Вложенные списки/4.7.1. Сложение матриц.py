n, m = [int(x) for x in input().split()]
matrix1 = [[int(x) for x in input().split()] for _ in range(n)]
input()
matrix2 = [[int(x) for x in input().split()] for _ in range(n)]
matrix_result = []

for i in range(n):
    temp = []
    for j in range(m):
        temp.append(matrix1[i][j] + matrix2[i][j])
    print(*temp)
    matrix_result.append(temp)
