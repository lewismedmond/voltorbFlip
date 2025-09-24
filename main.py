
import pygame
from sys import exit
from boardGenerator import generate_new_board, generate_hint

pygame.init()
        
currentBoard = generate_new_board()
colKeys, rowKeys = generate_hint(currentBoard)

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, value):
        super().__init__()
        self.image = pygame.image.load("Graphics/blankTile.png")
        self.rect = self.image.get_rect(topleft = (x,y))
        self.value = value
        self.revealed = False
    def revealTile(self):
        self.revealed = True
        if(self.value == -1):
            self.image = pygame.image.load("Graphics/bombTile.png")
        if(self.value == 1):
            self.image = pygame.image.load("Graphics/one.png")
        if(self.value == 2):
            self.image = pygame.image.load("Graphics/two.png")
        if(self.value == 3):
            self.image = pygame.image.load("Graphics/three.png")

all_sprites = pygame.sprite.Group()
screen = pygame.display.set_mode((288,288))
pygame.display.set_caption("Voltorb Flip")
clock = pygame.time.Clock() # Initialize clock for controlling frame rate

for i in range(25):
    all_sprites.add(Tile(6 + 47 * (i % 5), 6 + 47 * (i // 5), currentBoard[i % 5][i // 5]))  # Fitting tiles to the grid


gameFont = pygame.font.SysFont("Pixel Emulator", 16)






board_surface = pygame.image.load("Graphics/emptyBoard.png")
screen.blit(board_surface, (0, 0))         

for i,(voltorb, score) in enumerate(colKeys):
    voltorbCount = gameFont.render(str(voltorb), True, (0,0,0))
    pointTotal = gameFont.render(str(score).zfill(2), True, (0,0,0))
    screen.blit(voltorbCount, (i * 47 + 34, 261))  # Positioning key in the right place
    screen.blit(pointTotal, (i * 47 + 22, 241))

for i,(voltorb, score) in enumerate(rowKeys):
    voltorbCount = gameFont.render(str(voltorb), True, (0,0,0))
    pointTotal = gameFont.render(str(score).zfill(2), True, (0,0,0))
    screen.blit(voltorbCount, (270, i*47 + 27))  # Positioning key in the right place
    screen.blit(pointTotal, (258, i*47+7))


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
