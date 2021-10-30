ls = []
for _ in range(int(input())):
    ls.append(int(input()))
del ls[1::2]
print(ls)