from tile import Tile
import numpy as np
import pygame

pygame.init()

class Player():
    def __init__(self, strategy, GAME_SIZE):
        self.strategy = strategy
        self.player_board = np.zeros((GAME_SIZE, GAME_SIZE))
    def select_move(self):
        if (self.strategy == "random"):
            coords = np.argwhere(self.player_board == 0)
            return tuple(coords[np.random.choice(len(coords))])
    def play_move(self, chosen_move):
        self.player_board[chosen_move[0]][chosen_move[1]] = 1

    
    

def play_move(random_player, chosen_move, GAME_SIZE, all_sprites):
    for sprite in all_sprites:
        if(sprite.row == chosen_move[0] and sprite.col == chosen_move[1]):
            sprite.reveal_tile()
    random_player.play_move(chosen_move)
