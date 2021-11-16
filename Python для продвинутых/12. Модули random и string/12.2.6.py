# Для игры в бинго требуется карточка размером 5 \times 55×5, содержащая различные (уникальные) целые числа от 11 до 7575 (включительно), при этом центральная клетка является пустой (она заполняется числом 00).

from random import randint as r
from random import shuffle as sh
my_set = set()
result = [[0] * 5 for _ in range(5)]
while len(my_set) < 25:
    my_set.add(r(1, 75))
my_list = list(my_set)
sh(my_list)
k = -1
for i in range(5):
    for j in range(5):
        k += 1
        result[i][j] = my_list[k]
result[2][2] = 0
for i in range(5):
    for j in range(5):
        print(str(result[i][j]).ljust(3), end='')
    print()
