
import pygame
from sys import exit
from boardGenerator import generate_new_board, generate_keys, draw_keys
from tile import Tile
from player import Player, play_move
import time

pygame.init()

GAME_SIZE = 7
        
currentBoard = generate_new_board(GAME_SIZE)
col_keys, row_keys = generate_keys(currentBoard)




screen = pygame.display.set_mode((GAME_SIZE * 47 + 50, GAME_SIZE * 47 + 50)) 
screen.fill((100,255,100))
game_font = pygame.font.SysFont("Pixel Emulator", 16)

pygame.display.set_caption("Voltorb Flip")

clock = pygame.time.Clock() # Initialize clock for controlling frame rate


all_sprites = pygame.sprite.Group()
for i in range(GAME_SIZE**2):
    all_sprites.add(Tile((i % GAME_SIZE), (i // GAME_SIZE), currentBoard[i % GAME_SIZE][i // GAME_SIZE]))  # Fitting tiles to the grid


new_player = Player("random", GAME_SIZE)
        

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
    next_move = Player.select_move(new_player)
    time.sleep(1)
    play_move(new_player, next_move, GAME_SIZE, all_sprites)
    all_sprites.draw(screen) # Sprite rendering
    clock.tick(30)  # Limit frame rate to 30 FPS
    pygame.display.update()
