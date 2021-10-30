weight, height = float(input()), float(input())

bmi = weight / height**2  # Индекс Массы Тела
print(bmi)

if 18.5 <= bmi <= 25:
    print('Оптимальная масса')
elif bmi < 18.5:
    print('Недостаточная масса')
elif bmi > 25:
    print('Избыточная масса')
