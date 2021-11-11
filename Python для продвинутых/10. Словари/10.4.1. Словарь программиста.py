it_dict = {}
for i in range(int(input())):
    text = input()
    it_dict[text[:text.index(': ')].upper()] = text[text.index(': ') + 2:]

for i in range(int(input())):
    print(it_dict.get(input().upper(), 'Не найдено'))


# for _ in range(int(input())):
#     key, value = input().split(': ')
#     mydict[key.lower()] = value