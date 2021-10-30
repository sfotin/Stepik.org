players = ['Тимур', 'Руслан']
game = [input(), input()]
if 'камень' in game and 'бумага' in game or 'камень' in game and 'Спок' in game:
    players.pop(game.index('камень'))
elif 'ящерица' in game and 'камень' in game or 'ящерица' in game and 'ножницы' in game:
    players.pop(game.index('ящерица'))
elif 'Спок' in game and 'ящерица' in game or 'Спок' in game and 'бумага' in game:
    players.pop(game.index('Спок'))
elif 'ножницы' in game and 'Спок' in game or 'ножницы' in game and 'камень' in game:
    players.pop(game.index('ножницы'))
elif 'бумага' in game and 'ножницы' in game or 'бумага' in game and 'ящерица' in game:
    players.pop(game.index('бумага'))
print(players[0] if len(players) == 1 else 'ничья')
