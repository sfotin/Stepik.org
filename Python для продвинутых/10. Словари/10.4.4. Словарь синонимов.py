my_dict = {}
for _ in range(int(input())):
    key, value = input().split()
    my_dict[key] = value

word = input()
for key, value in my_dict.items():
    if key == word:
        print(value)
    elif value == word:
        print(key)
