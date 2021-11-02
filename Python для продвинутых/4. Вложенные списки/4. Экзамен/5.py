n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n-j-1][n-i-1]:
            flag = False

print('YES' if flag else 'NO')
