n, sum = int(input()), [0, 0, 0, 0]
matrix = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i < j and i < n-j-1:
            sum[0] += matrix[i][j]
        elif i < j and i > n-j-1:
            sum[1] += matrix[i][j]
        elif i > j and i > n-j-1:
            sum[2] += matrix[i][j]
        elif i > j and i < n-j-1:
            sum[3] += matrix[i][j]

print("Верхняя четверть: {}\nПравая четверть: {}\n"
      "Нижняя четверть: {}\nЛевая четверть: {}\n".format(*sum))
