num = list(input())
# ch = -3
# while -len(num) < ch:
#     num.insert(ch, ',')
#     ch -= 4
# print(*num, sep='')
#
for i in range(len(num) - 3, 0, -3):
    num.insert(i, ',')
print(*num, sep='')
