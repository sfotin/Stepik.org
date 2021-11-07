words = [set(x) for x in input().split()]
print(('NO', 'YES')[words[0] == words[1] == words[2]])
