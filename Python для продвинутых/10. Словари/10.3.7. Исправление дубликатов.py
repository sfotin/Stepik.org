sym_dict = {}
for i in input().split():
    sym_dict[i] = sym_dict.get(i, -1) + 1
    print(i if sym_dict[i] == 0 else f'{i}_{sym_dict[i]}', end=' ')

    # if sym_dict[i] == 0:
    #     print(i, end=' ')
    # else:
    #     print(f'{i}_{sym_dict[i]}', end=' ')
