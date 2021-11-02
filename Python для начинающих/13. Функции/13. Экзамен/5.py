# Напишите функцию get_month(language, number), которая принимает на вход два аргумента
# language – язык ru или en и number – номер месяца (от 1 до 12) и возвращает название
# месяца на русском или английском языке.


def get_month(language, number):
    ru_month = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    en_month = ['', 'january', 'february', 'march', 'april', 'may', 'june',
                'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'ru':
        return ru_month[number]
    elif language == 'en':
        return en_month[number]

print(get_month('ru', 1))
print(get_month('ru', 12))
print(get_month('en', 1))
print(get_month('en', 10))