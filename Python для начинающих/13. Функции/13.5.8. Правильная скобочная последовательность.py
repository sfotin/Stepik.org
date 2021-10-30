# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента
# непустую строку text, состоящую из символов ( и ) и возвращает значение True если
# поступившая на вход строка является правильной скобочной последовательностью и False
# в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только
# из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.

# объявление функции
def is_correct_bracket(text):
    count, i = 0, 0
    while count >= 0 and i < len(text):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
        i += 1
    print(count, i)
    return text.count('(') == text.count(')') and text[0] == '(' and i == len(text)

# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))
print(is_correct_bracket('((()))'))
print(is_correct_bracket(')(())('))
print(is_correct_bracket('())(()'))
