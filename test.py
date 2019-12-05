import random
board = []
for x in range(10):
    board.append([])
    for y in range(5):
        if random.randint(0, 1) == 0:
            board[x].append('~')
        else:
            board[x].append('`')
print(board)
