# На вход программе подаются две строки текста, содержащие целые числа. Из данных строк формируются списки чисел L и M.
# Напишите программу, которая создает третий список, элементами которого являются суммы соответствующих элементов
# списков L и M. Далее программа должна вывести каждый элемент полученного списка на одной строке через 1 пробел.

s1, s2 = input().split(), input().split()
print(*[int(s1[i]) + int(s2[i]) for i in range(len(s1))])