# def tuple_nums(nums):
#     return [(sum([int(i) for i in str(n)]), n) for n in nums]
#
#
# numbers = [int(n) for n in input().split()]
# sort_numbers = sorted(tuple_nums(numbers))
# for num in sort_numbers:
#     print(num[1], end=' ')

def comparator(n):
    return sum([int(i) for i in str(n)]), n

numbers = [int(i) for i in input().split()]

print(*sorted(numbers, key=comparator))
