n, m = [int(x) for x in input().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        count += 1
        matrix[i][j] = count
        print(str(matrix[i][j]).ljust(3), end='')
    print()
