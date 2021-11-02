# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы
# используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.
# Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку
# текста на английском языке и возвращает значение True если текст является панграммой
# и False в противном случае.
# Примечание 1. Гарантируется, что введенная строка содержит только буквы английского алфавита.


def is_pangram(text):
    return len([i for i in 'qwertyuiopasdfghjklzxcvbnm ' if i not in text.lower()]) == 0

print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The five boxing wizards jump quickly'))
print(is_pangram('The quick brown fox jumps over the lazy dog'))
print(is_pangram('Crazy Fredrick bought many very exquisite opal jewels'))
print(is_pangram('jsdfhsadfhkljsad'))
print(is_pangram('Crazy Fredrick bought many very exquisite opal jewel'))
print(is_pangram('razy Fredrick bought many very exquisite opal'))