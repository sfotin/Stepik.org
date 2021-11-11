phone_book = {}
for _ in range(int(input())):
    phone, name = input().split()
    phone_book.setdefault(name, []).append(phone)

for _ in range(int(input())):
    print(*phone_book.get(input().capitalize(), ['абонент не найден']))

