from decimal import *
num = Decimal(input())
d = num.as_tuple()
max = max(d.digits)
min = min(d.digits)
if -1 < num < 1: min = 0
print(min + max)
