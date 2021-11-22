def sort_by_index(index):
    def index_sort(athlete):
        return athlete[index - 1]
    return index_sort

athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

index_key = sort_by_index(int(input()))
for data in sorted(athletes, key=index_key):
    print(*data)
