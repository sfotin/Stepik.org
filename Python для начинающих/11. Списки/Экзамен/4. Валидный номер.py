# На вход программе подается строка текста. Напишите программу, которая определяет является ли введенная
# строка корректным телефонным номером. Строка текста является корректным телефонным номером если она имеет формат:
#
# abc-def-hijk или
# 7-abc-def-hijk
# где a, b, c, d, e, f, h, ch, j, k – цифры от 0 до 9.

phone = input().split('-')
if phone[0] == '7': del phone[0]  # нормализуем к abc-def-hijk
mask = [len(i) for i in phone]
print('YES' if mask == [3, 3, 4] and "".join(phone).isdigit() else 'NO')