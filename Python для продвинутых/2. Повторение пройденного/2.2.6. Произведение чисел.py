n = int(input())
num = [int(input()) for _ in range(n)]
product = int(input())
flag = False
print(n, num, product, sep='\n')
while len(num) > 0:
    temp = num[0]
    num.pop(0)
    if product / temp in num:
        flag = True
        break
print("ДА" if flag else "НЕТ")
