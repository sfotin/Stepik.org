# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с
# необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента
# строковое значение пароля password и возвращает значение True если пароль является
# действительным паролем BEEGEEK банка и False в противном случае.

# объявление функции
def is_valid_password(password):
    check_mask = [0, 0, 0]
    password = password.split(':')
    if password[0][:] == password[0][::-1]:
        check_mask[0] = 1
    if len([i for i in range(1, int(password[1]) + 1) if int(password[1]) % i == 0]) == 2:
        check_mask[1] = 1
    if int(password[2]) % 2 == 0:
        check_mask[2] = 1
    return check_mask == [1, 1, 1] and len(password) == 3

# считываем данные
#psw = input()

# вызываем функцию
#print(is_valid_password(psw))
print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))