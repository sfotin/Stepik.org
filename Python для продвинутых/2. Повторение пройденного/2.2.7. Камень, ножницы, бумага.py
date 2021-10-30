players = ['Тимур', 'Руслан']
game = [input(), input()]
if 'камень' in game and 'бумага' in game:
    players.pop(game.index('камень'))
elif 'камень' in game and 'ножницы' in game:
    players.pop(game.index('ножницы'))
elif 'бумага' in game and 'ножницы' in game:
    players.pop(game.index('бумага'))
print(players[0] if len(players) == 1 else 'ничья')
