import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.player = game.player1
        self.color = (60, 60, 60)
        self.rect = pygame.Rect(0, 0, 10,10)
        self.rect.midtop = self.player.rect.midtop
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    def update(self):
        self.y -=2
        self.x -= 0
        self.rect.y = self.y
        self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bullet2(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.player = game.player2
        self.color = (60, 60, 60)
        self.rect = pygame.Rect(0, 0, 10,10)
        self.rect.midtop = self.player.rect.midtop
        
        self.y = float(self.rect.y)
    def update(self):
        self.y -=2
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)