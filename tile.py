import pygame

pygame.__init__()

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