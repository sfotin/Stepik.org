text = input()
q_i = '87654321'.index(text[1])
q_j = 'abcdefgh'.index(text[0])
n = 8
board = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == q_i or j == q_j:
            board[i][j] = '*'
        elif (i - q_i)**2 == (j - q_j)**2:
            board[i][j] = '*'
board[q_i][q_j] = 'Q'

for row in board:
    print(*row)
