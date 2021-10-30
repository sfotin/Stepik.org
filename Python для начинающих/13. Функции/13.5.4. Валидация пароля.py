# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое
# значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.
#
# Пароль является надежным если:
#
# его длина не менее 88 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.
def is_password_good(password):
    check = [0, 0, 0, 0]
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    nums = '1234567890'
    if not len(password) < 8:
        check[0] = 1
    for c in password:
        if c in letters.upper():
            check[1] = 1
        elif c in letters:
            check[2] = 1
        elif c in nums:
            check[3] = 1
    return sum(check) == 4

print(is_password_good(input()))
