# Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой
from string import *
from random import shuffle, choice as ch

def generate_password(length):
    dig = [i for i in digits if i not in '01']
    ll = [i for i in ascii_lowercase if i not in 'lo']
    ul = [i for i in ascii_uppercase if i not in 'IO']
    result = [ch(dig)] + [ch(ll)] + [ch(ul)] + [ch(dig + ul + ll) for _ in range(4, length + 1)]
    shuffle(result)
    return ''.join(result)

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')
