# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус
# окружности и возвращает два значения: длину окружности и площадь круга,
# ограниченного данной окружностью.
from math import pi

def get_circle(radius):
    return 2 * pi * radius, pi * radius**2

print(get_circle(1))
print(get_circle(1.5))