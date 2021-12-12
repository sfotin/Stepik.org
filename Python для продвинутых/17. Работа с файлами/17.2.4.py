from functools import reduce
file = open('numbers.txt')
content = file.readlines()
content = map(lambda x: int(x.strip()), content)
print(reduce(lambda x,y: x + y, content, 0))
file.close()


file = open('numbers.txt')
print(sum(map(int, file)))
file.close()
