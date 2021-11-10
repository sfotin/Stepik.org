n = int(input())
city = {input() for i in range(n)}

print(('OK', 'REPEAT')[input() in city])
