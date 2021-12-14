result = 0
file = open('prices.txt', 'r', encoding='utf-8')
for line in file.readlines():
    line = list(line.split())
    result += int(line[1]) * int(line[2])
file.close()
print(result)
