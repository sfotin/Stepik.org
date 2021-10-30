n = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i>=j and i <= n-j-1 or i<=j and i >= n-j-1) and matrix[i][j] > largest:
            largest = matrix[i][j]

print(largest)
