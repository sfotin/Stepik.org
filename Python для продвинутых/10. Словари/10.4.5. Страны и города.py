countries = {}
for _ in range(int(input())):
    country, *cities = input().split()
    countries[country] = cities

for _ in range(int(input())):
    request = input()
    for key, value in countries.items():
        if request in value:
            print(key)
