# На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел.
# Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.
data = input().split()
for i in range(len(data)):
    data[i] = int(data[i])
data.sort()
print(*data)
data.sort(reverse=True)
print(*data)