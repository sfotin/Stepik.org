print(all(map(lambda x: int(x) <= 255 if x.isdigit() else False, input().split('.'))))
