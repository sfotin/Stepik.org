n = int(input())
m = [[int(x) for x in input().split()] for _ in range(n)]
temp = []
flag, count_c = True, 0
sum1, sum2, sum_row, sum_col = 0, 0, sum(m[0]), 0

for j in range(n):
    for i in range(n):
        if sum(m[i]) != sum_row:
            flag = False
            break

        temp.append(m[i][j])

        count_c += m[i][j]

    if sum_col != count_c and sum_col != 0:
        flag = False
        break
    else:
        sum_col = count_c
        count_c = 0

    sum1 += m[j][j]
    sum2 += m[j][n - j - 1]

temp.sort()
for k in range(len(temp)):
    if temp[k] != k + 1:
        flag = False
        break

print("YES" if sum1 == sum2 == sum_col == sum_row and flag else "NO")
