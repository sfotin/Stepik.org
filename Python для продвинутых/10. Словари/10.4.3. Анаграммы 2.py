symbols1 = [i for i in input().lower() if i not in ' .,!?:;-']
symbols2 = [i for i in input().lower() if i not in ' .,!?:;-']
sym_dict = {i:symbols1.count(i) for i in symbols1}
for i in symbols2:
    sym_dict[i] = sym_dict.get(i, 0) - 1
print('YES' if set(sym_dict.values()) == {0} else 'NO')
