n = int(input())
matrix = []
for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for row in matrix:
    x = 0
    mid = sum(row) / len(row)
    for i in row:
        if i > mid:
            x += 1
    print(x)
