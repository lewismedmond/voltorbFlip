from voltorbflip.tile import Tile
import numpy as np
import pygame




pygame.init()

class RandomPlayer():
    def __init__(self, GAME_SIZE):      
        self.player_board = np.zeros((GAME_SIZE, GAME_SIZE))
        self.score = 1
    def select_move(self):
        coords = np.argwhere(self.player_board == 0)
        print(coords)
        if coords.size == 0:
            return None
        return tuple(coords[np.random.choice(len(coords))])
    def play_move(self, chosen_move, currentBoard, all_sprites):
        tile_value = currentBoard[chosen_move[0]][chosen_move[1]]
        self.player_board[chosen_move[0]][chosen_move[1]] = tile_value
        self.score += tile_value
        for sprite in all_sprites:
            if(sprite.col == chosen_move[0] and sprite.row == chosen_move[1]):
                sprite.reveal_tile()
    def set_score(self, score):
        self.score = score

    
    

