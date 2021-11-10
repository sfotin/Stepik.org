m, n, = int(input()), int(input())
math_set = {input() for _ in range(m)}
it_set = {input() for _ in range(n)}

print(len(math_set - it_set))
