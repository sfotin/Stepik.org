def mean(*args):
    numbers = [i for i in args if type(i) == int or type(i) == float]
    if len(numbers) == 0:
        result = 0
    else:
        result = sum(numbers) / len(numbers)
    return float(result)


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
