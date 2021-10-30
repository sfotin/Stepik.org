num = [int(i) for i in input().split()]
for i in range(1, len(num), 2):
       num[i], num[i - 1] = num[i - 1], num[i]
print(*num)
