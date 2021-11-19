numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
cnumbers = {c: abs(c) for c in numbers}
for key, value in cnumbers.items():
    if value == max(cnumbers.values()):
        print(key, value, sep='\n')

# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j,
#            1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
# result = 0
#
# for num in numbers:
#     if abs(num) > abs(result):
#         result = num
#
# print(result, abs(result), sep='\n')