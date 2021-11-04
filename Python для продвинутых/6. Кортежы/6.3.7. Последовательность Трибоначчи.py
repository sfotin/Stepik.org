# n = int(input())
# result = [1, 1, 1]
# for i in range(3, n):
#     *x, a, b, c = result
#     result.append(a + b + c)
# print(*result[:n])

n = int(input())
t1, t2, t3 = 1, 1, 1
for i in range(n):
    print(t1, end=' ')
    t1, t2, t3 = t2, t3, t1 + t2 + t3
