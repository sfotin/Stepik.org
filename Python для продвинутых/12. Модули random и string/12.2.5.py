# Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.

from random import shuffle as shu
word = list(input())
shu(word)
print(''.join(word))
