import pygame
import sys
from player import player
from enemy import Enemy
from bullet import Bullet
from bullet import Bullet2
from time import sleep
pygame.mixer.init()
song = pygame.mixer.Sound("beat 98 (ship game).mp3")
class game2d:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("samir game")
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.player1 = player(self,"player1")
        self.player2 = player(self,"player2")
        self.enemy = Enemy(self)
        #self.enemy.enemytype
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        #self.bullets2 = pygame.sprite.Group()
        self.bg_color = (200, 200, 200)
        self.time = 0
        self.enemyhealth = 2
        #elf.createenemy()
        
    
    def run_game(self):
        song.play()
        while True:
            
            self._check_events()
            self.player1.update()
            self.player2.update()
            self.updateenemy()
            self._update_bullets()
            self.update_screen()
            self.timer()
            #self.checkcollisions()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        """Respond to keypresses."""    
        if event.key == pygame.K_d:
            self.player1.moving_right = True
        elif event.key == pygame.K_a:
            self.player1.moving_left = True
        elif event.key == pygame.K_w:
            self.player1.moving_up = True
        elif event.key == pygame.K_s:
            self.player1.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        
        if event.key == pygame.K_RIGHT:
            self.player2.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player2.moving_left = True
        elif event.key == pygame.K_UP:
            self.player2.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player2.moving_down = True
        
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_m:
            self._fire_bullet2()
        elif event.key == pygame.K_f:
            self.player1.playertime =0
    
    def _check_keyup_events(self, event):
        #Respond to key releases.
        if event.key == pygame.K_d:
            self.player1.moving_right = False
        elif event.key == pygame.K_a:
            self.player1.moving_left = False
        elif event.key == pygame.K_w:
            self.player1.moving_up = False
        elif event.key == pygame.K_s:
            self.player1.moving_down = False

        if event.key == pygame.K_RIGHT:
            self.player2.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player2.moving_left = False
        elif event.key == pygame.K_UP:
            self.player2.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player2.moving_down = False

    def enemy1(self):
        enemy = Enemy(self); enemy.x = 0;enemy.y = 0;self.enemies.add(enemy) 
        enemy2 = Enemy(self); enemy2.x = 500;enemy2.y = 20;self.enemies.add(enemy2) 
        enemy3 = Enemy(self); enemy3.x = 1000;enemy3.y = 140;self.enemies.add(enemy3) 
    def enemy2(self):
       enemy3 = Enemy(self);enemy3.x = -200; enemy3.y = 400;enemy3.enemytype = 2; self.enemies.add(enemy3)
       enemy = Enemy(self);enemy.x = -200; enemy.y = 600;enemy.enemytype = 2; self.enemies.add(enemy)
       enemy2 = Enemy(self);enemy2.x = -400; enemy2.y = 600;enemy2.enemytype = 2; self.enemies.add(enemy2)
         
    def enemy3(self):
        enemy3 = Enemy(self);enemy3.x = 200; enemy3.y = 100;enemy3.enemytype = 3; self.enemies.add(enemy3)
       
        enemy2 = Enemy(self);enemy2.x = 600; enemy2.y = 100;enemy2.enemytype = 3; self.enemies.add(enemy2)
       
        enemy5 = Enemy(self);enemy5.x = 1000; enemy5.y = 100;enemy5.enemytype = 3; self.enemies.add(enemy5)

        enemy = Enemy(self);enemy.x = 1200; enemy.y = 100;enemy.enemytype = 3; self.enemies.add(enemy)
    def enemy4(self):
        enemy = Enemy(self); enemy.x = 0;enemy.y = 0;self.enemies.add(enemy) 
        enemy2 = Enemy(self); enemy2.x = 500;enemy2.y = 0;self.enemies.add(enemy2) 
        enemy3 = Enemy(self); enemy3.x = 1000;enemy3.y = 0;self.enemies.add(enemy3) 
        enemy4 = Enemy(self); enemy4.x = 750;enemy4.y = 0;self.enemies.add(enemy4) 
    def enemy5(self):
        enemy3 = Enemy(self);enemy3.x = -200; enemy3.y = 300;enemy3.enemytype = 2; self.enemies.add(enemy3)
        enemy = Enemy(self);enemy.x = -400; enemy.y = 500;enemy.enemytype = 2; self.enemies.add(enemy)
        enemy2 = Enemy(self);enemy2.x = -600; enemy2.y = 500;enemy2.enemytype = 2; self.enemies.add(enemy2)
        enemy4 = Enemy(self);enemy4.x = -200; enemy4.y = 600;enemy4.enemytype = 2; self.enemies.add(enemy4)
        enemy5 = Enemy(self);enemy5.x = -500; enemy5.y = 600;enemy5.enemytype = 2; self.enemies.add(enemy5)
       
        
       

        



    def updateenemy(self):
        self.enemies.update()
        if pygame.sprite.spritecollideany(self.player1, self.enemies):
            if self.player1.inv == False:
                self.player1.center_ship()
                sleep(2)
        if pygame.sprite.spritecollideany(self.player2, self.enemies):
            if self.player2.inv == False:
                self.player2.center_ship()
       
            
            

    def _fire_bullet(self):   
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _fire_bullet2(self):   
        new_bullet2 = Bullet2(self)
        #self.bullets.rect.midtop = self.player2.rect.midtop
        self.bullets.add(new_bullet2)
        #print("bullet fired")
    
    

    def _update_bullets(self):
        self.bullets.update()
        #self.bullets2.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                #print(len(self.bullets))
        pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
    
    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.player1.blitme()
        self.player2.blitme2()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemies.draw(self.screen)
        #for bullet2 in self.bullets2.sprites():
          #  bullet2.draw_bullet()
        pygame.display.flip()

    def timer(self):
        self.time += 1
        if self.time == 100:  self.enemy3()  
        if self.time == 500: self.enemy1()
        if self.time == 1000: self.enemy2()
        if self.time == 1500: self.enemy4()
        if self.time == 2000: self.enemy5()
        if self.time == 3000: self.time = 0
            
        

    
        
if __name__ == '__main__':
 # Make a game instance, and run the game.
 g2 = game2d()
 g2.run_game()
 