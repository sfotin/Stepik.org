from functools import reduce
file = open('nums.txt')
content = list(filter(lambda x: len(x) > 0, map(lambda x: x.strip(), file.readlines())))
print(reduce(lambda x, y: int(x) + int(y), content, 0))
file.close()


file = open('nums.txt')
print(file.read().split())
print(sum(map(int, file.read().split())))
file.close()
