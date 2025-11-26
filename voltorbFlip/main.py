
import pygame
from sys import exit
from boardGenerator import Board
from tile import Tile
from agents.random_agent import RandomPlayer

from boardRender import draw_keys
import time
import csv


def play_one_game(GAME_SIZE, agent = None, render = False):
    
    board = Board(GAME_SIZE)

    if render:
        pygame.init()
        pygame.display.set_caption("Voltorb Flip")
        clock = pygame.time.Clock() # Initialize clock for controlling frame rate
        game_font = pygame.font.SysFont("Pixel Emulator", 16)
        screen = pygame.display.set_mode((GAME_SIZE * 47 + 50, GAME_SIZE * 47 + 50))
        screen.fill((100,255,100))

        all_sprites = pygame.sprite.Group()
        for i in range(GAME_SIZE**2):
            all_sprites.add(Tile((i % GAME_SIZE), (i // GAME_SIZE), board.board[i % GAME_SIZE][i // GAME_SIZE]))  # Creating all tiles and fitting them to grid
        
        draw_keys(board.col_keys, board.row_keys, GAME_SIZE, game_font, screen)

    if agent == None:
        pass
        #play_human_game(GAME_SIZE, render)
    else:
        game_over = False
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            game_over = play_one_move(agent, board, all_sprites)

            if render:
                pygame.draw.rect(screen, (100, 255, 100), pygame.Rect(GAME_SIZE * 47,GAME_SIZE * 47, 50, 50))
                #screen.blit(game_font.render(str(rl_player.score), True, (0, 0, 0)), (GAME_SIZE * 47 + 15,GAME_SIZE * 47 + 15))  # render player score
                all_sprites.draw(screen) # Sprite rendering
                clock.tick(30)  # Limit frame rate to 30 FPS
                pygame.display.update()  # update screen
            
            
    
def play_one_move(agent, board, all_sprites = None):
        time.sleep(1)
        
        available_moves = board.available_moves
        if(len(available_moves) == 0):
            return True
        
        current_state = board.state
        action = agent.select_action(current_state, available_moves)
        if all_sprites is not None:
            for sprite in all_sprites:
                if(sprite.col == action[0] and sprite.row == action[1]):  # reveal chosen tile
                    sprite.reveal_tile()

        
        reward = board.play(action)
        agent.step(current_state, action, reward, board.state, board.available_moves)
        for tile in all_sprites:
                    if tile.col == action[0] and tile.row == action[1]:  # reveal chosen tile
                        tile.reveal_tile()
        return False


#GAME_SIZE = 2  # set row/column count
#rl_player = RLPlayer(GAME_SIZE)  # initialise rl agent


#score_log = []

#for i in range(10000):
#
#    if(i % 500 == 0 and i != 0):
#        with open("voltorbflip/scores.csv", "a", newline = "") as f:
#            writer = csv.writer(f)
#            writer.writerows(score_log)
#            score_log = []

    





   
     # draw the column and row keys

#    while True and not game_over:
#        
            #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #    pos = pygame.mouse.get_pos()
            #    for tile in all_sprites:
            #        if tile.rect.collidepoint(pos) and not tile.revealed:
            #            tile.reveal_tile()
#        if not game_over:
            
#            next_move = rl_player.select_move()  # player selects next move 

 #           if next_move == None:
 #               game_over = True
 #               rl_player.update_weights()
 #               score_log.append([rl_player.score])
 #               break

 #           if current_board[next_move[0]][next_move[1]] == -1: # check if bomb has been flipped
 #               rl_player.set_score(-1)
 #               game_over = True
 #               rl_player.update_weights()
 #               score_log.append([rl_player.score])
                
                


#            rl_player.play_move(next_move, current_board, all_sprites)  # player updates their board with new information
#            if rl_player.score == AVAILABLE_SCORE:
#                game_over = True
#                rl_player.update_weights()
#                score_log.append([rl_player.score])

        

        
        

        

