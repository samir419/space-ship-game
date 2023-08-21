import pygame
from pygame.sprite import Sprite
class Enemy(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('C:/Users/Hello/CODE/python practice/gamed/alien.png')
        #self.rect = self.image.get_rect()
        self.enemytype = 1
        self.rect = self.image.get_rect()
        #self.rect.midtop = self.screen_rect.midtop
        self.rect.x 
        self.rect.y 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.xdirection = 1
        self.ydirection = 1
        self.etime = 0
        self.zerodir = 0

    def update(self):
        if self.enemytype == 1:
            self.behavior()
        elif self.enemytype == 2:
           self.behavior2()
        elif self.enemytype == 3:
            self.behavior3()
    
       
    def behavior(self):
        self.y += self.ydirection
        self.x += self.xdirection
        self.rect.y = self.y
        self.rect.x = self.x
        self.etime += 1
        if self.x == self.screen_rect.right:
            self.xdirection *= -1
        if self.y == self.screen_rect.bottom:
            self.ydirection *= -1
        if self.x == self.screen_rect.left:
            self.xdirection *= -1
        if self.y == self.screen_rect.top:
            self.ydirection *= -1
            

    def behavior2(self):
        self.y += 0
        self.x += self.xdirection
        self.rect.y = self.y
        self.rect.x = self.x
        self.etime += 1
       
        if self.etime == 1800:
            self.xdirection *= -1
            self.etime = 0

    def behavior3(self):
        self.y += self.ydirection
        self.x += self.xdirection*self.zerodir
        self.rect.y = self.y
        self.rect.x = self.x
        self.etime += 1
       
        if self.y == self.screen_rect.bottom:
            self.ydirection *= -1
            self.zerodir = 1
        if self.y == self.screen_rect.top:
            self.ydirection *= -1
            self.zerodir = 0
        if self.x == self.screen_rect.left:
            self.xdirection *= -1
        if self.x == self.screen_rect.right:
            self.xdirection *= -1
            

    def blitenemy(self):
        self.screen.blit(self.image, self.rect)


class Enemytwo(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        #self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('C:/Users/Hello/CODE/python practice/gamed/alien.png')
        #self.rect = self.image.get_rect()
        self.etype =1
        self.rect = self.image.get_rect()
        #self.rect.midtop = self.screen_rect.midtop
        self.rect.x 
        self.rect.y 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.xdirection = 1
        self.ydirection = 1
        self.etime = 0
        

    def update(self):
        
        if self.etype == 1:
            self.behavior()
        elif self.etype == 2:
            self.behavior2()
        

       
    def behavior(self):
        self.y += self.ydirection
        self.x += self.xdirection
        self.rect.y = self.y
        self.rect.x = self.x
        self.etime += 1
        if self.etime == 400:
            self.xdirection *= -1
        if self.etime == 800:
            self.ydirection *= -1
        if self.etime == 1200:
            self.xdirection *= -1
        if self.etime == 1600:
            self.ydirection *= -1
            self.etime = 0
    def behavior2(self):
        self.y += 0
        self.x += 1
        self.rect.y = self.y
        self.rect.x = self.x
        self.etime += 1
        if self.etime == 800:
            self.xdirection *= -1
        
        if self.etime == 1600:
            self.xdirection *= -1
            self.etime = 0

    def blitenemy(self):
        self.screen.blit(self.image, self.rect)