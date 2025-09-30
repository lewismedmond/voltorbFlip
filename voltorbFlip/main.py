
import pygame
from sys import exit
from voltorbflip.boardGenerator import generate_new_board, generate_keys, draw_keys
from voltorbflip.tile import Tile
from voltorbflip.agents.random_agent import RandomPlayer
from voltorbflip.agents.rl_agent import RLPlayer
import time
import csv


def run_game():

    GAME_SIZE = 2  # set row/column count
    rl_player = RLPlayer(GAME_SIZE)  # initialise rl agent

    pygame.init()
    pygame.display.set_caption("Voltorb Flip")
    clock = pygame.time.Clock() # Initialize clock for controlling frame rate
    game_font = pygame.font.SysFont("Pixel Emulator", 16)
    score_log = []

    for i in range(10000):

        if(i % 500 == 0 and i != 0):
            with open("voltorbflip/scores.csv", "a", newline = "") as f:
                writer = csv.writer(f)
                writer.writerows(score_log)
                score_log = []

        rl_player.reset_game(GAME_SIZE)
        current_board = generate_new_board(GAME_SIZE)    #  Create the new board with GAME_SIZE rows/columns
        col_keys, row_keys = generate_keys(current_board)   #  Sum voltorbs and points across rows and down columns

        AVAILABLE_SCORE = 1
        for i in range(GAME_SIZE**2):
            if current_board[i % GAME_SIZE][i // 5] > 0:
                AVAILABLE_SCORE += current_board[i % GAME_SIZE][i // 5]

        rl_player.initialise_features(GAME_SIZE, col_keys, row_keys)
        game_over = False


        screen = pygame.display.set_mode((GAME_SIZE * 47 + 50, GAME_SIZE * 47 + 50)) 
        screen.fill((100,255,100))

        all_sprites = pygame.sprite.Group()
        for i in range(GAME_SIZE**2):
            all_sprites.add(Tile((i % GAME_SIZE), (i // GAME_SIZE), current_board[i % GAME_SIZE][i // GAME_SIZE]))  # Creating all tiles and fitting them to grid
        
        #draw_keys(col_keys, row_keys, GAME_SIZE, game_font, screen) # draw the column and row keys

        while True and not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #    pos = pygame.mouse.get_pos()
                #    for tile in all_sprites:
                #        if tile.rect.collidepoint(pos) and not tile.revealed:
                #            tile.reveal_tile()
            if not game_over:
                
                next_move = rl_player.select_move()  # player selects next move 

                if next_move == None:
                    game_over = True
                    rl_player.update_weights()
                    score_log.append([rl_player.score])
                    break

                if current_board[next_move[0]][next_move[1]] == -1: # check if bomb has been flipped
                    rl_player.set_score(-1)
                    game_over = True
                    rl_player.update_weights()
                    score_log.append([rl_player.score])
                    
                #time.sleep(1)    


                rl_player.play_move(next_move, current_board, all_sprites)  # player updates their board with new information
                if rl_player.score == AVAILABLE_SCORE:
                    game_over = True
                    rl_player.update_weights()
                    score_log.append([rl_player.score])

            #pygame.draw.rect(screen, (100, 255, 100), pygame.Rect(GAME_SIZE * 47,GAME_SIZE * 47, 50, 50))
            #screen.blit(game_font.render(str(rl_player.score), True, (0, 0, 0)), (GAME_SIZE * 47 + 15,GAME_SIZE * 47 + 15))  # render player score
            #all_sprites.draw(screen) # Sprite rendering
            #clock.tick(30)  # Limit frame rate to 30 FPS
            #pygame.display.update()  # update screen

        
        

        

