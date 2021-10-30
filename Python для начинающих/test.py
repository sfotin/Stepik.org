# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов
# три целых числа a, b, c – коэффициенты квадратного уравнения ax^2+bx+c = 0
# и возвращает его корни в порядке возрастания.
from typing import Union, Any


def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
    x1 = (- b - d**0.5) / (2 * a)
    x2 = (- b + d**0.5) / (2 * a)
    print(x1, x2)

    return min(x1, x2), max(x1, x2)

print(solve(1, -4, -5))
print(solve(-2, 7, -5))
print(solve(1, 2, 1))
