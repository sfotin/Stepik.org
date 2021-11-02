list1 = input().split()
k = int(input())
result = []
for i in range(k):
    temp = []
    for j in range(i, len(list1), k):
        temp.append(list1[j])
    result.append(temp)

print(result)
