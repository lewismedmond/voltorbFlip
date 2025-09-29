import pygame

pygame.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self, col, row, value):
        super().__init__()
        self.image = pygame.image.load("Graphics/blankTile.png")
        self.rect = self.image.get_rect(topleft = (6 + 47 * col, 6 + 47 * row))
        self.value = value
        self.row = row
        self.col = col
        self.revealed = False
    def reveal_tile(self):
        self.revealed = True
        if(self.value == -1):
            self.image = pygame.image.load("Graphics/bombTile.png")
        if(self.value == 1):
            self.image = pygame.image.load("Graphics/one.png")
        if(self.value == 2):
            self.image = pygame.image.load("Graphics/two.png")
        if(self.value == 3):
            self.image = pygame.image.load("Graphics/three.png")