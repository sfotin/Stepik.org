# num = [int(ch) for ch in input().split()]
# n = num[-1]
# for ch in range(len(num) - 1, -1, -1):
#     num[ch] = num[ch - 1]
# num[0] = n
# print(*num)

spisok = [int(i) for i in input().split()]
spisok = [spisok[len(spisok)-1]] + spisok[:len(spisok)-1]
print(spisok)