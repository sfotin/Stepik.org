from fractions import Fraction as F
from math import *

n = int(input())
result = [F(i, j) for i in range(1, n) for j in range(2, n + 1) if i < j and gcd(i, j) == 1]
print(*sorted(result), sep='\n')
