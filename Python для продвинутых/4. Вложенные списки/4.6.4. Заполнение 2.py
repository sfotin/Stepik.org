n, m = [int(x) for x in input().split()]
matrix = [['.' for _ in range(m)] for _ in range(n)]
count = 0

for j in range(m):
    for i in range(n):
        count += 1
        matrix[i][j] = count

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
