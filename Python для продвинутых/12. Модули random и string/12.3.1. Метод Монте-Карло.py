# Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы неравенств

from random import uniform

n = 10**6       # количество испытаний
k = 0
s0 = 16

for _ in range(n):
    x = uniform(-2, 2)
    y = uniform(-2, 2)
    if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
        k += 1

s = (k/n) * s0
print(s)
