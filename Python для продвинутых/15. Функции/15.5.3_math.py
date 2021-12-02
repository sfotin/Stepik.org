value = [1, 2, 3, 4, 5]
try:
    value = value[5]/0
except (IndexError, ZeroDivisionError):
    print('Python', end=' ')
else:
    print('else', end=' ')
finally:
    print('finally', end=' ')