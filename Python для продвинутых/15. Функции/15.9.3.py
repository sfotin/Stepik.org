abscissas = map(lambda x: float(x), input().split())
ordinates = map(lambda x: float(x), input().split())
applicates = map(lambda x: float(x), input().split())

print(all(map(lambda x, y, z: x**2 + y**2 + z**2 <= 4, abscissas, ordinates, applicates)))
