# Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы (двумерного списка).

from random import *

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

for row in matrix:
    shuffle(row)


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
