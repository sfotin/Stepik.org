def print_products(*args):
    i = 0
    for elem in args:
        if type(elem) == str and len(elem) != 0:
            i += 1
            print(f'{i}) {elem}')
    if i == 0:
        print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')