func = lambda x: x[0] in 'aA' and x[-1] in 'aA'

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))