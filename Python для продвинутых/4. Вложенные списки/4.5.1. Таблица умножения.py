n, m = int(input()), int(input())
matrix = [[i * j for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
