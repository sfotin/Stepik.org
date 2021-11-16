# Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой

from random import choice, shuffle

def generate_password(length):
    up_let, lo_let, dig = 'ABCDEFGHJKLMNPQRSTUVWXYZ', 'abcdefghijkmnpqrstuvwxyz', '23456789'
    symbols = list(up_let + lo_let + dig)
    shuffle(symbols)
    return ''.join([choice(symbols) for _ in range(length)])

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n = int(input())  # количество
m = int(input())  # длина
print(*generate_passwords(n, m), sep='\n')
