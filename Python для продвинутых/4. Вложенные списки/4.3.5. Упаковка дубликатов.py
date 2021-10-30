text = 'w w w o r l d g g g g r e a t t e c c h e m g g p w w'.split()

double = []  # сюда будем складывать списки из дублей
temp = [text[0]]  # буферный список для аккумуляции дублей, сразу берём 1й элемент строки

for i in range(1, len(text)):  # идем по списку начиная со 2ого символа и до конца
    if text[i] == temp[-1]:
        temp.append(text[i])  # если текущий символ равен предыдущему, то аккумулируем
    else:
        double.append(temp)  # если нет, то скидываем подборку дублей в список списков дублей
        temp = []  # создаём новую ссылку - новый аккумулятор
        temp.append(text[i])  # добавляем в новый аккумулятор текущий символ
double.append(temp)  # в конце остаётся крайний аккумулятор, который не был присвоен

print(double)


# # лучшее решение с форума решений
# s, l = input().split(), []
# l.append([s[0]])
# x = 0
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         l[x].append(s[i])
#     else:
#         x += 1
#         l.append([s[i]])
# print(l)

