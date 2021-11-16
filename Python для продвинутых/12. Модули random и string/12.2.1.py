# Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.
import random

def generate_ip():
    return '.'.join([str(random.randint(0, 255)) for _ in range(4)])

for _ in range(5):
    print(generate_ip())


# from random import randrange as r
#
# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'