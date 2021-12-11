numbers = list(range(int(input()), int(input()) + 1))
numbers = filter(lambda x: not '0' in str(x), numbers)
list_nums = map(lambda x: x if all([not x % int(i) for i in str(x)]) else 0, numbers)
list_nums = filter(lambda x: x > 0, list_nums)
print(*list_nums)

# def check(num):
#     return all(map(lambda x: int(x) and num % int(x) == 0, str(num)))
#
# a, b = int(input()), int(input())
# seq = range(a, b + 1)
# print(*list(filter(check, seq)))
