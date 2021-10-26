import math
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
players = [" ", "X", "O"]

def print_board():
    print("  0 1 2")
    for n, row in enumerate(board):
        print(f"{n} ", end="")
        for col in row:
            print(f"{players[col]} ", end="")
        print()

def is_winner(line):
    if math.prod(line) in [1, 8]:
        return True
    return False

def check_board():
    # horizontal
    for row in board:
        if is_winner(row):
            return row[0]
    # vertical
    for i in range(3):
        col = [row[i] for row in board]
        if is_winner(col):
            return col[0]
    # diagonal \
    line = [board[0][0], board[1][1], board[2][2]]
    if is_winner(line):
        return line[0]
    # diagonal /
    line = [board[2][0], board[1][1], board[0][2]]
    if is_winner(line):
        return line[0]
    # no spaces left
    total = math.prod([math.prod(row) for row in board])
    if total != 0:
        return -1

def is_valid(move):
    row = move // 10
    col = move % 10
    if (0 > row > 2) or (0 > col > 2):
        return False
    if board[row][col] == 0:
        return True
        
def get_move():
    while True:
        try:
            move = int(input("Move: "))
        except:
            continue
        if is_valid(move):
            board[move//10][move%10] = player
            return
        else:
            print("invalid move")
    
player = 1
while True:
    print_board()
    get_move()
    winner = check_board()
    if winner == -1:
        print("Tie")
        break
    elif winner:
        print(f"Winner: {players[winner]}")
        break
    if player == 1:
        player = 2
    else:
        player = 1