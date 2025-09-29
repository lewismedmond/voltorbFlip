
import pygame
from sys import exit
from voltorbflip.boardGenerator import generate_new_board, generate_keys, draw_keys
from voltorbflip.tile import Tile
from voltorbflip.agents.random_agent import RandomPlayer
from voltorbflip.agents.rl_agent import RLPlayer
import time

def run_game():
    pygame.init()

    GAME_SIZE = 3
            
    current_board = generate_new_board(GAME_SIZE)    #  Create the new board with GAME_SIZE rows/columns
    col_keys, row_keys = generate_keys(current_board)   #  Sum voltorbs and points across rows and down columns

    game_over = False


    screen = pygame.display.set_mode((GAME_SIZE * 47 + 50, GAME_SIZE * 47 + 50)) 
    screen.fill((100,255,100))

    game_font = pygame.font.SysFont("Pixel Emulator", 16)
    pygame.display.set_caption("Voltorb Flip")

    clock = pygame.time.Clock() # Initialize clock for controlling frame rate

    all_sprites = pygame.sprite.Group()
    for i in range(GAME_SIZE**2):
        all_sprites.add(Tile((i % GAME_SIZE), (i // GAME_SIZE), current_board[i % GAME_SIZE][i // GAME_SIZE]))  # Creating all tiles and fitting them to grid


    rl_player = RLPlayer(GAME_SIZE)
            

    draw_keys(col_keys, row_keys, GAME_SIZE, game_font, screen)


    while True:
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
                break

            if current_board[next_move[0]][next_move[1]] == -1: # check if bomb has been flipped
                rl_player.set_score(0)
                game_over = True
                rl_player.update_weights()
                
            time.sleep(1)    


            rl_player.play_move(next_move, current_board, all_sprites)  # player updates their board with new information

        pygame.draw.rect(screen, (100, 255, 100), pygame.Rect(GAME_SIZE * 47,GAME_SIZE * 47, 50, 50))
        screen.blit(game_font.render(str(rl_player.score), True, (0, 0, 0)), (GAME_SIZE * 47 + 15,GAME_SIZE * 47 + 15))  # render player score
        all_sprites.draw(screen) # Sprite rendering
        clock.tick(30)  # Limit frame rate to 30 FPS

        


        
        pygame.display.update()  # update screen

