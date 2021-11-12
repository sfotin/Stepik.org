rules_dict = {'execute': 'X', 'read': 'R', 'write': 'W'}
files = {}
for _ in range(int(input())):
    file_name, *rules = input().split()
    files.setdefault(file_name, rules)

for _ in range(int(input())):
    command, f_name = input().split()
    print('OK' if rules_dict[command] in files[f_name] else 'Access denied')
