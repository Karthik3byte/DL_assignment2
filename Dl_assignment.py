import requests

import math


board = [
    [1, 6, 3],
    [2, 1, 3],
    [5, 8, 0]
]

def is_terminal(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return True
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return True
    if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:
        return True
    for row in board:
        if 0 in row:
            return False  

def minimax(board, depth, maximizing_player):
    if is_terminal(board) or depth == 0:
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    eval = minimax(board, depth - 1, False)
                    board[i][j] = 0
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    eval = minimax(board, depth - 1, True)
                    board[i][j] = 0
                    min_eval = min(min_eval, eval)
        return min_eval

def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            if board[i][0] == 1:
                return 10
            else:
                return -10
        if board[0][i] == board[1][i] == board[2][i] != 0:
            if board[0][i] == 1:
                return 10
            else:
                return -10
    if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:
        if board[1][1] == 1:
            return 10
        else:
            return -10
    return 0 

best_move_value = minimax(board, 2, True)  
print("Best move value:", best_move_value)
