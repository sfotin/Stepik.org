sales = {}

for _ in range(int(input())):
    name, product, quantity = input().split()
    sales[name] = sales.get(name, {})
    sales[name][product] = sales[name].get(product, 0) + int(quantity)

for name, shop in sorted(sales.items()):
    print(f'{name}:')
    for product, quantity in sorted(shop.items()):
        print(product, quantity)
