list1, n = [], int(input())
for _ in range(n):
    elem = [int(i + 1) for i in range(n)]
    list1.append(elem)
print(*list1, sep='\n')

# n = int(input())
# result = []
# for _ in range(n):
#     result.append(list(range(1, n + 1)))
# print(*result, sep='\n')
