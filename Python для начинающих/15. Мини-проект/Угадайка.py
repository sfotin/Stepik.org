import random, math

def how_many_attempts(n):
    return math.ceil(math.log2(n))

def is_valid(num, n_range):
    return num.isdigit() and 1 <= int(num) <= n_range

def play_the_game(answer):
    return answer.lower() in 'lf yes da да поиграем давай еще ещё'

def ugadayka(n_range, n):
    if n == 'start':
        pass
    elif not is_valid(n, n_range):
        print(f'А может быть все-таки введем целое число от 1 до {n_range}?')
    else:
        n = int(n)
        if n == num:
            return True
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')

play_again = 'д'
while play_the_game(play_again):
    print(f" \n {'*' * 8} Добро пожаловать в числовую угадайку {'*' * 8} \n ")
    range_ = int(input('Задайте диапазон от 1 до ??? - '))
    num = random.randint(1, range_)
    attempts = how_many_attempts(range_)
    print(f'Я загадала число, которое можно угадать со 100% вероятностью '
          f'за {attempts} попытки')

    i = 0
    answer = 'start'
    while not ugadayka(range_, answer) and i != attempts:
        i += 1
        print(f'\nПопытка {i} из {attempts}:')
        answer = input(f'Введите число от 1 до {range_} - ')

    if int(answer) == num:
        print('Вы угадали, поздравляем!')
    else:
        print(f'\nСожалеем, но все попытки кончились. Я загадала {num}')

    play_again = input('\nПоиграем ещё?')

print('\n' + 'Спасибо, что играли в числовую угадайку. Еще увидимся...')