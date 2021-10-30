# константы
ru_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя' \
              'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz' \
              'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '.,!?-" 0123456789'

# Шифр Цезаря (text, n, lg, ende)
# text (string) - текст, который нужно закодировать или раскодировать
# n (int) - сдвиг шифра
# lg (string) - язык. принимает ru или en (русский или английский)
# ende (string) - принимает + или - (шифровать или расшифровывать)
def caesar_cryp(text, n, lg, ende):
    crypt_text = ''
    alphabet = en_alphabet
    if lg == 'ru':
        alphabet = ru_alphabet
    for i in text:
        if i in alphabet and ende == '+':
            crypt_text += alphabet[alphabet.find(i) + n]
        elif i in alphabet and ende == '-':
            crypt_text += alphabet[alphabet.rfind(i) - n]
        elif i in symbols:
            crypt_text += i
    return crypt_text

# main
# en_or_de = input('Шифруем / дешифруем? (+/-) - ')
# language = input('Выберите язык (по-умолчанию en/ru) - ')
# original_text = input('Введите текст: ')
# shift = int(input('Величина сдвига - '))

# en_or_de = '+'
# language = 'ru'
# original_text = 'Блажен, кто верует, тепло ему на свете!'
# shift = 10
# print(caesar_cryp(original_text, shift, language, en_or_de))
#
# en_or_de = '+'
# language = 'en'
# original_text = 'To be, or not to be, that is the question!'
# shift = 17
# print(caesar_cryp(original_text, shift, language, en_or_de))
#
# en_or_de = '-'
# language = 'ru'
# original_text = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
# shift = 7
# print(caesar_cryp(original_text, shift, language, en_or_de))
#
# en_or_de = '-'
# language = 'en'
# original_text = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
# shift = 25
# print(caesar_cryp(original_text, shift, language, en_or_de))

# en_or_de = '-'
# language = 'en'
# original_text = 'Hawnj pk swhg xabkna ukq nqj.'
# for shift in range(26):
#     print(shift, '-', caesar_cryp(original_text, shift, language, en_or_de))
# # 23 - Learn to walk before you run.

en_or_de = '+'
language = 'en'
original_text = input('Введите текст: ').split()
crypt_text = []
for txt in original_text:
    word = txt
    for s in symbols:
        word = word.replace(s, '')  # чистим текстовый элемент от символов чтобы потом посчитать сдвиг
    crypt_text.append(caesar_cryp(txt, len(word), language, en_or_de))
crypt_text = ' '.join(crypt_text)
print(crypt_text)