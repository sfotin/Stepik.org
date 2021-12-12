from random import randint as r
file_name = 'lines.txt'
file = open(file_name, 'r', encoding='utf-8')
content = file.readlines()
line = r(0, len(content) - 1)
print(content[line].strip())
file.close()
