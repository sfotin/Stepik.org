buttons = {'1': '.,?!:',
           '2': 'ABC',
           '3': 'DEF',
           '4': 'GHI',
           '5': 'JKL',
           '6': 'MNO',
           '7': 'PQRS',
           '8': 'TUV',
           '9': 'WXYZ',
           '0': ' '}

text = input().upper()

for t in text:
    for key, value in buttons.items():
        if t in value:
            print(key * (value.index(t) + 1), end='')
