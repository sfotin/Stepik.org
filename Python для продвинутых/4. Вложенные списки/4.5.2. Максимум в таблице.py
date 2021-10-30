n, m = int(input()), int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
max, max_ij = matrix[0][0], [0, 0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] > max:
            max = matrix[i][j]
            max_ij = [i, j]

print(*max_ij)
