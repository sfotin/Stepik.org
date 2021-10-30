# Задача Иосифа Флавия
n = [i for i in range(1, int(input()) + 1)]  # список из номеров участников
k = int(input())  # каждый k-й выбывает
i = 0  # первый вода
while len(n) != 1:  # пока не останется один единственный
    kill = (i + k - 1) % len(n)  # Первый способ https://ru.wikipedia.org/wiki/Задача_Иосифа_Флавия
    i = kill  # новый вода
    n.pop(kill)
print(*n)
