n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
flag = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
            break
print("YES" if flag else "NO")