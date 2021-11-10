m, n = int(input()), int(input())
math_set = {input() for _ in range(m)}
it_set = {input() for _ in range(n)}
len_set1 = len((math_set | it_set) - (math_set & it_set))

print(len_set1 if len_set1 > 0 else 'NO')
