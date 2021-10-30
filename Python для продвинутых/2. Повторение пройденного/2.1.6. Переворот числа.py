num = input()
# if len(num) == 6:
#     num6 = int(num[0]) * 100_000
#     num5 = int(num[1:][::-1])
#     num = num6 + num5
# else:
#     num = int(num[::-1])
reversed_num = int(num[:-5] + num[-5:][::-1])
print(reversed_num)
