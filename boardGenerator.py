import numpy as np
import random

def generate_new_board(size):
    board = np.zeros((size,size), dtype=int)
    for i in range(size):
        for j in range(size):
            rand = random.random()
            if rand < 0.3:
                board[i][j] = -1  # Voltorb
            elif rand < 0.7:
                board[i][j] = 1   # 1 point
            elif rand < 0.9:
                board[i][j] = 2   # 2 points
            else:
                board[i][j] = 3   # 3 points    
    return board

def generate_hint(board):
    row_hints = []
    col_hints = []
    size = len(board[0])
    for i in range(size):
        row_voltorbs = np.sum(board[:,i] == -1)
        row_points = np.sum(board[:,i][board[:,i] > 0])
        row_hints.append((row_voltorbs, row_points))
        
        col_voltorbs = np.sum(board[i] == -1)
        col_points = np.sum(board[i][board[i] > 0])
        col_hints.append((col_voltorbs, col_points))
    return col_hints, row_hints