# На вход программе подается строка текста. 
# Напишите программу, которая выводит на экран символ, который появляется наиболее часто.

s = input()
max_ch = ""
max_count = 0
for i in s:
    c = s.count(i)
    if c >= max_count:
        max_count = c
        max_ch = i
print(max_ch)