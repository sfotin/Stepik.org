# На вход программе подается натуральное число nn и nn строк, а затем число kk.
# Напишите программу, которая выводит kk-ую букву из введенных строк на одной строке без пробелов.

n = int(input())
ls = []
for _ in range(n):
    ls.append(input())
k = int(input())
for i in range(n):
    s = ls[i]
    if len(s) >= k:
        s = s[k - 1]
    else:
        s = ''
    print(s, end="")