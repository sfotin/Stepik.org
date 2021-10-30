price = 60  # цена символа в копейках
text = input()
cost = len(text) * price
print(f'{cost // 100} р. {cost % 100} коп.')