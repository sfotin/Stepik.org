# Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов
# два натуральных числа n и k и возвращает значение биномиального коэффициента,
# равного n!/k!(n−k)!
# Примечание 1. Факториалом натурального числа nn, называется произведение всех натуральных чисел от 11 до nn, то есть
# n! = 1⋅2⋅3⋅…⋅n
# Примечание 2. Реализуйте вспомогательную функцию factorial(n), вычисляющую
# факториал числа или воспользуйтесь уже готовой функцией из модуля math.
from math import factorial


def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


print(compute_binom(1, 1))
print(compute_binom(2, 1))
print(compute_binom(10, 1))
print(compute_binom(10, 2))
print(compute_binom(15, 2))
print(compute_binom(100, 3))
print(compute_binom(64, 7))
