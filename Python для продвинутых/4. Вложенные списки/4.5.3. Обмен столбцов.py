n, m = int(input()), int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
ij = [int(x) for x in input().split()]

for row in matrix:
    row[ij[0]], row[ij[1]] = row[ij[1]], row[ij[0]]

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
