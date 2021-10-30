word = input() + ' запретил букву'
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for alpha in alphabet:
    if alpha in word:
        word = word.strip().replace('  ', ' ')
        print(word, alpha)
        word = word.replace(alpha, '')
