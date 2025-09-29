import numpy as np
import random

def generate_new_board(size):
    board = np.zeros((size,size), dtype=int)
    for i in range(size):
        for j in range(size):
            rand = random.random()
            if rand < 0.1:
                board[i][j] = -1  # Voltorb
            elif rand < 0.6:
                board[i][j] = 1   # 1 point
            elif rand < 0.9:
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


def draw_keys(col_keys, row_keys, GAME_SIZE, font, screen):
    for i,(voltorb, score) in enumerate(col_keys):
        voltorbCount = font.render(str(voltorb), True, (0,0,0))
        pointTotal = font.render(str(score).zfill(2), True, (0,0,0))
        screen.blit(voltorbCount, (i * 47 + 34, (GAME_SIZE) * 47 + 26))  # Positioning key in the right place
        screen.blit(pointTotal, (i * 47 + 22, (GAME_SIZE) * 47 + 6))

    for i,(voltorb, score) in enumerate(row_keys):
        voltorbCount = font.render(str(voltorb), True, (0,0,0))
        pointTotal = font.render(str(score).zfill(2), True, (0,0,0))
        screen.blit(voltorbCount, ((GAME_SIZE) * 47 + 30, i*47 + 27))  # Positioning key in the right place
        screen.blit(pointTotal, ((GAME_SIZE) * 47 + 20, i*47+7))
