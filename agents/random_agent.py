from tile import Tile
import numpy as np
import pygame

pygame.init()

class RandomPlayer():
    def __init__(self, GAME_SIZE):
        self.player_board = np.zeros((GAME_SIZE, GAME_SIZE))
    def select_move(self):
        coords = np.argwhere(self.player_board == 0)
        if coords.size == 0:
            return None
        return tuple(coords[np.random.choice(len(coords))])
    def play_move(self, chosen_move, currentBoard, all_sprites):
        self.player_board[chosen_move[0]][chosen_move[1]] = currentBoard[chosen_move[0]][chosen_move[1]]
        for sprite in all_sprites:
            if(sprite.row == chosen_move[0] and sprite.col == chosen_move[1]):
                sprite.reveal_tile()

    
    

