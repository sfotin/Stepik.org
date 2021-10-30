# На вход программе подается натуральное число nn, затем nn строк, затем еще одна строка — поисковый запрос.
# Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
n, data = int(input()), []
for _ in range(n): data.append(input())
google = input()
for i in range(n):
    if google.lower() in data[i].lower(): print(data[i])