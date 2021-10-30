ln = input()
n_i = '87654321'.index(ln[1])
n_j = 'abcdefgh'.index(ln[0])

board = [['.'] * 8 for _ in range(8)]
board[n_i][n_j] = 'N'

for i in range(8):
    for j in range(8):
        if (n_i - i)**2 + (n_j - j)**2 == 5:
            board[i][j] = '*'

for row in board:
    print(*row)
