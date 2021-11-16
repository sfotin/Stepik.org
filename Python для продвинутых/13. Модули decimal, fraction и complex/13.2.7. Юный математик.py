from fractions import Fraction as F
import math

n = int(input())
f = [F(i, n - i) for i in range(1, (n+1)//2) if math.gcd(i, n-i) == 1]
print(max(f))
