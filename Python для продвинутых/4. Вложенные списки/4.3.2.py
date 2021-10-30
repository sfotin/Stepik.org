# n = int(input())
# list1 = []
# for row in range(1, n + 1):
#     list1.append(list(range(1, row + 1)))
# print(*list1, sep='\n')

print(*[[k for k in range(1, i + 1)] for i in range(1, int(input()) + 1)], sep='\n')


