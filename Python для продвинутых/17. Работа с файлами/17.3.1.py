with open('text.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    print(line[::-1])
