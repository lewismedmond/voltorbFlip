import numpy as np
import random


class Board:
    def __init__(self, size):
        self.size = size
        self.board = generate_new_board(size)
        self.col_keys, self.row_keys = generate_keys(self.board)
        self.available_moves = [(i,j) for i in range(size) for j in range(size)]
        self.state = np.zeros((size, size), dtype=int)  # 0: unflipped, -1: voltorb, 1/2/3: points
    def play(self, action):
        self.available_moves.remove(action)
        self.state[action] = self.board[action]
        return self.board[action]


def generate_new_board(size):
    board = np.zeros((size,size), dtype=int)
    for i in range(size):
        for j in range(size):
            rand = random.random()
            if rand < 0.2:
                board[i][j] = -1  # Voltorb
            elif rand < 0.6:
                board[i][j] = 1   # 1 point
            elif rand < 0.8:
                board[i][j] = 2   # 2 points
            else:
                board[i][j] = 3   # 3 points    
    return board

def generate_keys(board):
    row_keys = []
    col_keys = []
    size = len(board[0])
    for i in range(size):
        row_voltorbs = np.sum(board[:,i] == -1)
        row_points = np.sum(board[:,i][board[:,i] > 0])
        row_keys.append((row_voltorbs, row_points))
        
        col_voltorbs = np.sum(board[i] == -1)
        col_points = np.sum(board[i][board[i] > 0])
        col_keys.append((col_voltorbs, col_points))
    return col_keys, row_keys




