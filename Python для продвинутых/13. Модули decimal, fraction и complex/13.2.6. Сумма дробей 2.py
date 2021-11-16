from fractions import Fraction as F
from math import factorial

n = int(input())
result = 0
for i in range(1, n + 1):
    result += F(1, factorial(i))
print(result)
