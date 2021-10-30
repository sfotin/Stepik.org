# На вход программе подается строка текста. Напишите программу, 
# которая подсчитывает количество цифр в данной строке.

s = input()
digits = "0123456789"
count = 0
for i in range(len(s)):
    if digits.count(s[i]) > 0: count += 1
print(count)