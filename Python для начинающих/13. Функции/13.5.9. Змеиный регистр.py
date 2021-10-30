# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента
# строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

# объявление функции
def convert_to_python_case(text):
    text = list(text)
    print(text)
    for t in range(1, len(text)):
        if text[t] == text[t].upper() and not text[t].isdigit():
            text[t - 1] += "_"
    return ''.join(text).lower()
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))
print(convert_to_python_case('ConvertToInt32'))
print(convert_to_python_case('IsPrimeNumber'))