m, n = int(input()), int(input())
students_data = [input() for _ in range(m + n)]
students_set = set(students_data)
intersection = (m + n - len(students_set)) * 2
if intersection == (m + n):
    print('NO')
else:
    print(m + n - intersection)
