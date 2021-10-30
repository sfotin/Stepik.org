n, m = int(input()), int(input())
matrix = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(input())
    matrix.append(temp)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
