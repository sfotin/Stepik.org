# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку
# text и возвращает значение True если указанный текст является палиндромом и False
# в противном случае.
#
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
#
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми,
# а также игнорируйте пробелы, а также символы , . ! ? -.

# объявление функции
def is_palindrome(text):
    txt = [i.lower() for i in text if i not in ',.!?- ']
    return txt == txt[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))