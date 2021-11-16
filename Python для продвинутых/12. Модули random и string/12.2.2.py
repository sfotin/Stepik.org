# Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква английского алфавита, Number – число от 00 до 9999 (включительно).

from random import randrange as r
from random import choice as chs
from string import ascii_uppercase as ul

def generate_index():
    return (f'{chs(ul)}{chs(ul)}{r(100)}_{r(100)}{chs(ul)}{chs(ul)}')


for _ in range(5):
    print(generate_index())
