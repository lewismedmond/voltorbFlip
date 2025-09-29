from voltorbflip.tile import Tile
import numpy as np
import pygame
import pickle
import os



pygame.init()

class RLPlayer():
    def __init__(self, GAME_SIZE):      
        self.move_sequence = []

        q_table_file = "voltorbflip/q_table.pkl"
        if os.path.exists(q_table_file):
            with open(q_table_file, "rb") as f:  # loading dictionary of (board, state) -> weights
                self.q_table = pickle.load(f)
        else:
            self.q_table = {} 
            with open(q_table_file, "wb") as f:
                pickle.dump(self.q_table, f)

        self.player_board = np.zeros((GAME_SIZE, GAME_SIZE))
        self.score = 1
    def select_move(self):
        coords = np.argwhere(self.player_board == 0)
        if coords.size == 0:
            return None
        return tuple(coords[np.random.choice(len(coords))])
    def play_move(self, chosen_move, currentBoard, all_sprites):

        self.move_sequence.append((self.player_board,chosen_move))

        tile_value = currentBoard[chosen_move[0]][chosen_move[1]]
        self.player_board[chosen_move[0]][chosen_move[1]] = tile_value
        self.score += tile_value
        for sprite in all_sprites:
            if(sprite.col == chosen_move[0] and sprite.row == chosen_move[1]):
                sprite.reveal_tile()
        
    
    def set_score(self, score):
        self.score = score


    def update_weights(self):
        for i, (board, action) in enumerate(self.move_sequence):
            log = tuple(board.flatten()), action
            if log not in self.q_table:
                self.q_table[log] = 50
            self.q_table[log] += self.score
            with open("voltorbflip/q_table.pkl", "wb") as f:
                pickle.dump(self.q_table, f)
