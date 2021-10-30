n = int(input())
matrix = []
total = 0

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    total += matrix[i][i]

print(total)
