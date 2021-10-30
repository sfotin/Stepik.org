# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num
# и возвращает первое простое число большее числа num.
#
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
#
# Примечание 2. Следующий программный код:
def is_prime(num):
    dev = [i for i in range(1, num + 1) if num % i == 0]
    return len(dev) == 2


def get_next_prime(num):
    i = num + 1
    while not is_prime(i):
        i += 1
    return i


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
