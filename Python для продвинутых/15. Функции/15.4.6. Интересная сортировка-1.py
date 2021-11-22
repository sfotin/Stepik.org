def sum_num(num):
    return sum([int(n) for n in str(num)])

numbers = [int(num) for num in input().split()]
numbers.sort(key=sum_num)
print(*numbers)
