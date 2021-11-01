n, m = [int(x) for x in input().split()]
matrix = []
count = 0
for i in range(n):
    temp = []
    for j in range(m):
        count += 1
        temp.append(count)
    if i % 2 != 0:
        temp.reverse()
    matrix.append(temp)

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
