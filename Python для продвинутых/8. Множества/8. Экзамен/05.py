m, n = int(input()), int(input())
home_lib = {input() for _ in range(m)}

for _ in range(n):
    print(('NO', 'YES')[input() in home_lib])
