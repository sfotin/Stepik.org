# На вход программе подается строка текста. Напишите программу, которая выводит слова введенной строки в столбик.
s = input()
ls = s.split()
print(*ls, sep="\n")