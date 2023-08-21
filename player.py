import pygame
class player:
    def __init__(self,game,name):
        """Initialize the ship and set its starting position."""
        self.name = name
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/Users/Hello/CODE/python practice/gamed/ship.png')
        self.image2 = pygame.image.load('C:/Users/Hello/CODE/python practice/gamed/ship copy.png')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed = 2
        self.playertime = 0
        self.inv = False
    def update(self):
        self.playertime += 1
        if self.playertime < 200:
            self.inv = True
        else:
            self.inv = False
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
           
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
           
        if self.moving_up:
            self.y -= self.speed
           
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
            
        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.playertime=0
    
    def blitme2(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image2, self.rect)
    def center_ship2(self):
        """Center the ship on the screen."""
        self.rect.bottomleft = self.screen_rect.bottomleft
        self.x = float(self.rect.x)