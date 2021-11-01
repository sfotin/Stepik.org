n, m = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = (i + j) % m + 1
        print(str(matrix[i][j]).ljust(3), end='')
    print()
