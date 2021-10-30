import random

# константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
appercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def make_chars(passwor_mask):  # создаёт набор символов по настройкам пользователя
    psw_chars = ''
    if passwor_mask[2] == 'y':
        psw_chars += digits
    if passwor_mask[3] == 'y':
        psw_chars += appercase_letters
    if passwor_mask[4] == 'y':
        psw_chars += lowercase_letters
    if passwor_mask[5] == 'y':
        psw_chars += punctuation
    if passwor_mask[6] == 'y':
        for c in 'il1Lo0O':
            psw_chars = psw_chars.replace(c, '')
    return psw_chars


def generate_password(length, psw_char):  # генерация пароля
    return ''.join(random.sample(psw_char, length))


# начало программы
default_mask = ['5', '24', 'y', 'y', 'y', 'y', 'y']
mask = ['', '', '', '', '', '', '']
mask[0] = input(f'Количество паролей для генерации? (default - {default_mask[0]}) - ')
mask[1] = input(f'Длина одного пароля? (y/n, default - {default_mask[1]}) - ')
mask[2] = input(f'Включать ли цифры 0123456789? (y/n, default - {default_mask[2]}) - ')
mask[3] = input(f'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n, default - {default_mask[3]}) - ')
mask[4] = input(f'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n, default - {default_mask[4]}) - ')
mask[5] = input(f'Включать ли символы !#$%&*+-=?@^_? (y/n, default - {default_mask[5]}) - ')
mask[6] = input(f'Исключать ли неоднозначные символы il1Lo0O? (y/n, default - {default_mask[6]}) - ')
for i in range(len(mask)):
    if mask[i] == '':
        mask[i] = default_mask[i]

chars = make_chars(mask)  # получаем набор символов генерации

print('\nГенерация паролей')
for _ in range(int(mask[0])):
    print(generate_password(int(mask[1]), chars))
