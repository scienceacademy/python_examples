import math
# board[row][column]
board = [[2, 2, 0],
         [2, 2, 0],
         [2, 1, 1]]

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
print_board()
winner = check_board()
if winner:
    print(f"Winner: {players[winner]}")