# На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется
# список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
data = input().split()
for i in range(len(data)):
    data[i] = int(data[i])
min_, min_index = min(data), data.index(min(data))
max_, max_index = max(data), data.index(max(data))
data[min_index], data[max_index] = max_, min_
print(*data)