n = int(input())
matrix = []
max = -100

for _ in range(n):
    matrix.append([int(i) for i in input().split()])

for i in range(n):
    for j in range(n):
        if j <= i and matrix[i][j] > max:
            max = matrix[i][j]
print(max)
