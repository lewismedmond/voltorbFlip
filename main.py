
import pygame
from sys import exit
from boardGenerator import generate_new_board, generate_hint
from tile import Tile

pygame.init()

GAME_SIZE = 7
        
currentBoard = generate_new_board(GAME_SIZE)
colKeys, rowKeys = generate_hint(currentBoard)




screen = pygame.display.set_mode((GAME_SIZE * 47 + 50, GAME_SIZE * 47 + 50)) 
screen.fill((100,255,100))
pygame.display.set_caption("Voltorb Flip")

clock = pygame.time.Clock() # Initialize clock for controlling frame rate


all_sprites = pygame.sprite.Group()
for i in range(GAME_SIZE**2):
    all_sprites.add(Tile(6 + 47 * (i % GAME_SIZE), 6 + 47 * (i // GAME_SIZE), currentBoard[i % GAME_SIZE][i // GAME_SIZE]))  # Fitting tiles to the grid


gameFont = pygame.font.SysFont("Pixel Emulator", 16)
        

for i,(voltorb, score) in enumerate(colKeys):
    voltorbCount = gameFont.render(str(voltorb), True, (0,0,0))
    pointTotal = gameFont.render(str(score).zfill(2), True, (0,0,0))
    screen.blit(voltorbCount, (i * 47 + 34, (GAME_SIZE) * 47 + 26))  # Positioning key in the right place
    screen.blit(pointTotal, (i * 47 + 22, (GAME_SIZE) * 47 + 6))

for i,(voltorb, score) in enumerate(rowKeys):
    voltorbCount = gameFont.render(str(voltorb), True, (0,0,0))
    pointTotal = gameFont.render(str(score).zfill(2), True, (0,0,0))
    screen.blit(voltorbCount, ((GAME_SIZE) * 47 + 30, i*47 + 27))  # Positioning key in the right place
    screen.blit(pointTotal, ((GAME_SIZE) * 47 + 20, i*47+7))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for tile in all_sprites:
                if tile.rect.collidepoint(pos) and not tile.revealed:
                    tile.revealTile()

    all_sprites.draw(screen) # Sprite rendering
    clock.tick(30)  # Limit frame rate to 30 FPS
    pygame.display.update()
