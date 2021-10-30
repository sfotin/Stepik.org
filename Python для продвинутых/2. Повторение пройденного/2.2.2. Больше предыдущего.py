num = [int(i) for i in input().split()]
count = 0
for i in range(1, len(num)):
    if num[i] > num[i - 1]:
        count += 1
print(count)
