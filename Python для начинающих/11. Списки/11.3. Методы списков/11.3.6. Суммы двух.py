n , first_digit = int(input()), int(input())
ls = []
for _ in range(n - 1):
    second_digit = int(input())
    ls.append(first_digit + second_digit)
    first_digit = second_digit
print(ls)