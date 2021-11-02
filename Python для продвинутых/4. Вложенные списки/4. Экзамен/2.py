n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
result = matrix[n - 1][n - 1]

for i in range(n):
    for j in range(n):
        if i >= n - j - 1 and result < matrix[i][j]:
            result = matrix[i][j]

print(result)
