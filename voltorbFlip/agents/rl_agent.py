import numpy as np
import pygame
import pickle
import os
import random


pygame.init()

class RLPlayer():
    def __init__(self, GAME_SIZE):
        self.ALPHA = 0.1  # learning rate       
        q_table_file = "voltorbflip/q_table.pkl"
        if os.path.exists(q_table_file):
            with open(q_table_file, "rb") as f:  # loading dictionary of (board, state) -> weights
                self.q_table = pickle.load(f)
        else:
            self.q_table = {} 
            with open(q_table_file, "wb") as f:
                pickle.dump(self.q_table, f)

    def select_action(self, current_state, available_moves):
        ## epsilon-greedy action selection. currently using random selection
        return random.choice(available_moves)

    def step(self, current_state, action, reward, next_state, available_moves):
        ### update q-table using bellman equation
        current_key = tuple(map(tuple, current_state.tolist()))
        next_key = tuple(map(tuple, next_state.tolist()))
        # bellman equation:
        if(current_key not in self.q_table):
            self.q_table[current_key] = {a: 0 for a in (available_moves + [action])}

        if(next_key not in self.q_table):
            self.q_table[next_key] = {a: 0 for a in available_moves}

        #### need to decide on initial q values.
        # currently everything will be set to 1 so without any rewards, the q values can never change

        self.q_table[current_key][action] = self.q_table[current_key][action] + self.ALPHA * (reward + max([self.q_table[next_key][next_action] for next_action in available_moves]) - self.q_table[current_key][action])
        pass

        
    def initialise_features(self, GAME_SIZE, col_keys, row_keys):
        self.row_keys = row_keys
        self.col_keys = col_keys
        #self.sort_keys() # sorting the player's key information to take advantage of identical boards up to permutation of rows/cols 

    def play_move(self, chosen_move, currentBoard, all_sprites):

        self.move_sequence.append((self.col_keys, self.row_keys, chosen_move))

        tile_value = currentBoard[chosen_move[0]][chosen_move[1]]
        self.player_board[chosen_move[0]][chosen_move[1]] = tile_value
        self.update_current_info(chosen_move)
        self.score += tile_value
        
    
    def update_current_info(self, chosen_move):
        if self.player_board[chosen_move[0]][chosen_move[1]] == -1:
            self.row_keys[chosen_move[1]] = (self.row_keys[chosen_move[1]][0] - 1, self.row_keys[chosen_move[1]][1])  # update voltorbs left
            self.col_keys[chosen_move[0]] = (self.col_keys[chosen_move[1]][0] - 1, self.col_keys[chosen_move[1]][1]) 
        else:
            self.row_keys[chosen_move[1]] = (self.row_keys[chosen_move[1]][0], self.row_keys[chosen_move[1]][1] - self.player_board[chosen_move[0]][chosen_move[1]])  # update points left
            self.col_keys[chosen_move[0]] = (self.col_keys[chosen_move[1]][0], self.col_keys[chosen_move[1]][1] - self.player_board[chosen_move[0]][chosen_move[1]]) 
        

    def set_score(self, score):
        self.score = score


    def update_weights(self):
        alpha = 0.5
        for i, (col_keys, row_keys, action) in enumerate(self.move_sequence):
            key = (tuple(col_keys), tuple(row_keys), tuple(action))
            if key not in self.q_table:
                self.q_table[key] = 1
            if self. score > 0:
                self.q_table[key] = int(self.q_table[key] + alpha * (self.score - self.q_table[key]))   # increment weights of selected tiles according to the score
            else:
                if i == len(self.move_sequence):
                    self.q_table[key] = int(self.q_table[key]/2)  # half the weight of the bomb selected

    def choose_move_from(self, coords):
        boundaries = [0]
        for coordinate in coords:
            key = (tuple(self.col_keys), tuple(self.row_keys), tuple(coordinate))
            if key not in self.q_table:  # add state, action to dictionary if not present and initialise with weight 1
                self.q_table[key] = 1
            boundaries.append(boundaries[len(boundaries)-1] + self.q_table[key])
        
        count = random.randrange(boundaries[len(boundaries)-1])
        for i, boundary in enumerate(boundaries):
            if(count <= boundary):   # randomly choose a tile to flip according to their relative weights
                return coords[i-1]

    #def sort_board(self):  
    #    sorted = False
    #    while not sorted:
    #        sorted = True
    #        for i in range(len(self.col_keys)):
    #            if 2**self.col_keys[i][0] * 3**self.col_keys[i][1] > 2**self.col_keys[i + 1][0] * 3**self.col_keys[i + 1][1]:  
    #                temp = self.col_keys[i]
    #                self.col_keys[i] = self.col_keys[i + 1]
    #                self.col_keys[i + 1] = temp
    #                sorted = False
    #    
    #    sorted = False
    #    while not sorted:
    #        sorted = True
    #        for i in range(len(self.row_keys)):
    #            if 2**self.row_keys[i][0] * 3**self.row_keys[i][1] > 2**self.row_keys[i + 1][0] * 3**self.row_keys[i + 1][1]:
    #                temp = self.row_keys[i]
    #                self.row_keys[i] = self.row_keys[i + 1]
    #                self.row_keys[i + 1] = temp
    #                sorted = False


