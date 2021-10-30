text = input().split()
list = [[]]
for window in range(len(text)):  # размер "окна" - количество элементов в подсписке
    sublist = []  # заводим пустой контейнер
    for i in range(len(text) - window):  # количество подсписков
        sublist.append(text[i:i + window + 1])  # добавляем согласно размера окна...
    list.extend(sublist)  # ... и скидываем подсписок в список
print(list)
