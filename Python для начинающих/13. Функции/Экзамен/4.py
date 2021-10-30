# Напишите функцию number_to_words(num), которая принимает в качестве аргумента натуральное
# число num и возвращает его словесное описание на русском языке.

def number_to_words(num):
    dozens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
              'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    tens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
            'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    units = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    if num < 10:
        return units[num]
    elif 10 <= num < 20:
        return tens[num % 10]
    elif 20 <= num <= 99:
        if num % 10 == 0:
            sep = ''
        else:
            sep = ' '
        return dozens[num // 10] + sep + units[num % 10]


# print(number_to_words(1))
# print(number_to_words(2))
# print(number_to_words(3))
# print(number_to_words(4))
# print(number_to_words(5))
# print(number_to_words(6))
# print(number_to_words(7))
# print(number_to_words(8))
# print(number_to_words(9))
# print(number_to_words(10))
# print(number_to_words(11))
# print(number_to_words(12))
# print(number_to_words(13))
# print(number_to_words(14))
# print(number_to_words(15))
# print(number_to_words(16))
# print(number_to_words(17))
# print(number_to_words(18))
# print(number_to_words(19))
print(number_to_words(20))
print(number_to_words(25))
print(number_to_words(30))
print(number_to_words(34))
print(number_to_words(85))
print(number_to_words(90))
print(number_to_words(99))