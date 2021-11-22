# from math import *
#
# def pow2_x(x):
#     return int(pow(x, 2))
#
# def pow3_x(x):
#     return int(pow(x, 3))
#
# def sqrt_x(x):
#     return sqrt(x)
#
# def abs_x(x):
#     return int(abs(x))
#
# def sin_x(x):
#     return sin(x)
#
# commands = {'квадрат': pow2_x, 'куб': pow3_x, 'корень': sqrt_x, 'модуль': abs_x, 'синус': sin_x}
# num = int(input())
# print(commands[input()](num))
#
#

import math

def pwr(p):
  def numpower(n):
    return n**p
  return numpower

commands = {"квадрат": pwr(2), "куб": pwr(3), "корень": pwr(0.5), "модуль": abs, "синус": math.sin}

n = int(input())
command = input()
print(commands[command](n))
