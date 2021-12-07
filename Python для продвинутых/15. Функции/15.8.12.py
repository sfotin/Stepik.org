from functools import reduce

def evaluate(c, x):
    p = list(range(len(c) - 1, -1, -1))  # список степеней
    nums = list(map(lambda i, p, c: c * (i ** p), [x] * len(c), p, c))  # список элементов многочлена
    return reduce(lambda num1, num2: num1 + num2, nums, 0)  # складываем все элементы

coefficients = [int(c) for c in input().split()]
x = int(input())
print(evaluate(coefficients, x))
