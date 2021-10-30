quantity = int(input())
quarters = [0, 0, 0, 0]

for i in range(quantity):
    x, y = [int(xy) for xy in input().split()]
    if x > 0 and y > 0:
        quarters[0] += 1
    elif x < 0 and y > 0:
        quarters[1] += 1
    elif x < 0 and y < 0:
        quarters[2] += 1
    elif x > 0 and y < 0:
        quarters[3] += 1

print(f'Первая четверть: {quarters[0]}',
      f'Вторая четверть: {quarters[1]}',
      f'Третья четверть: {quarters[2]}',
      f'Четвертая четверть: {quarters[3]}', sep='\n')
