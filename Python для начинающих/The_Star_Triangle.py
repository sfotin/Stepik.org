n = int(input())
n += 1
for j in range (1, n):
    if j <= n // 2:
        for _ in range (j):
            print("*", end="")
    else:
        for _ in range(j, n):
            print("*", end="")
    print()