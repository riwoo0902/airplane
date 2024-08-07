import pygame

from rager import *

class Spaceship():
    

    ragers = []
    def __init__(self, screen):
        self.screen = screen
        self.img = pygame.image.load('./images/spaceship.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (225,150))
        self.rec = self.img.get_rect()
        self.rec.x = 1000 
        self.rec.y = 350
        self.lagertime1 = 0
        self.lagertime2 = 0
    def eventkey(self):            
        key_pressed = pygame.key.get_pressed()  
        if key_pressed[pygame.K_w]:
            self.rec.y -= 1
        if key_pressed[pygame.K_s]:
            self.rec.y += 1
        if key_pressed[pygame.K_a]:
            self.rec.x -= 1
        if key_pressed[pygame.K_d]:
            self.rec.x += 1    
            
        if self.rec.x <0:
            self.rec.x = 0
        if self.rec.x >self.screen.get_width():#1275:
            self.rec.x = self.screen.get_width()
        if self.rec.y <0:
            self.rec.y = 0
        if self.rec.y >self.screen.get_height():#650
            self.rec.y = self.screen.get_height()
        
        if key_pressed[pygame.K_SPACE]:
            self.lagertime2 =pygame.time.get_ticks()
           
            if self.lagertime2 - self.lagertime1 >= 1000:
                self.lagertime1 =pygame.time.get_ticks()
                self.ragers.append(rager(self.screen,(self.rec.x,self.rec.y+54))) 
        else:
            self.lagertime2 =pygame.time.get_ticks()
        
    def ragermove(self):
        for i, rager in enumerate(self.ragers):
            if rager.draw():  
                del self.ragers[i] 
    def draw(self):
        self.eventkey()
        self.ragermove()
        self.screen.blit(self.img, self.rec)
