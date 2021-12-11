data = []
result = []
for _ in range(int(input())):
    class_data = []
    for _ in range(int(input())):
        surname, volume = input().split()
        d = [int(volume), surname]
        class_data.append(d)
    data.append(class_data)
    result.append(any(map(lambda x: x[0] == 5, class_data)))

print('YES' if all(result) else 'NO')


# n = int(input())
# students = []
# for _ in range(n):
#     m = int(input())
#     temp = []
#     for _ in range(m):
#         surname, mark = input().split()
#         temp.append((surname, int(mark)))
#     students.append(temp)
#
# result = all(map(lambda x: any(map(lambda y: y[1] == 5, x)), students))
# print('YES' if result else 'NO')
