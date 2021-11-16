# Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним решать задачи по программированию.

# from random import shuffle
# n = int(input())
# names = [input() for _ in range(n)]
# shuffle(names)
# friends = [f'{names[i]} - {names[(n + i + 1) % n]}' for i in range(n)]
# shuffle(friends)
# print(*friends, sep='\n')


from random import choice

names, rel, tmp = {input() for _ in range(int(input()))}, {}, 0
for name in names.copy():
    if names == {name}:
        rel[tmp], rel[name] = name, rel[tmp]
    else:
        rand_name = choice(list(names - {name}))
        rel[name] = rand_name
        names -= {rand_name}
        tmp = name
[print(k, '-', v) for k, v in rel.items()]
