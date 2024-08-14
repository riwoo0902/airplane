import pygame

from rager import *
from config import *

class Spaceship():
    
    
    ragers = []
    def __init__(self, screen,con):
        self.screen = screen
        self.img = pygame.image.load('./images/spaceship.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (250,150))
        self.hpimg = pygame.image.load("./images/hp.png")
        self.hpimg2 = pygame.image.load("./images/hp1.png")
        self.con = con        
        self.level = self.con['level']
        self.hp = self.con['HP']
        self.maxhp = self.con['maxHP']
        self.damage = self.con['damage']
        self.speed = self.con['speed']
        self.defense = self.con['defense']
        self.attackspeed = self.con['attackspeed']
        self.nol = self.con['nol']
        self.reincarnation = self.con['reincarnation']
        self.luck = self.con['luck']
        self.experience = self.con['experience']
        self.rec = self.img.get_rect()
        self.rec.x = 1000 
        self.rec.y = 350
        self.lagertime1 = 0
        self.lagertime2 = 0
        
    def eventkey(self):            
        key_pressed = pygame.key.get_pressed()  
        if key_pressed[pygame.K_w]:
            self.rec.y -= self.speed 
        if key_pressed[pygame.K_s]:
            self.rec.y += self.speed 
        if key_pressed[pygame.K_a]:
            self.rec.x -= self.speed 
        if key_pressed[pygame.K_d]:
            self.rec.x += self.speed 
            
        if self.rec.x <0:
            self.rec.x = 0
        if self.rec.x >1250:
            self.rec.x = 1250
        if self.rec.y <0:
            self.rec.y = 0
        if self.rec.y >650:
            self.rec.y = 650
        
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
            else:
                pass   
    def checkCollision(self, ragers,damage): #충돌했는지 확인
        for i, arr in enumerate(ragers):            
            if self.rec.colliderect(arr.rec):
                centerx = arr.rec.centerx
                centery = arr.rec.centery
                self.hp -= damage
                return centerx,centery,i
        return None,None,None
    
    def drawhp(self):
        self.img_hp = pygame.transform.scale(self.hpimg ,(((self.hp/self.maxhp)*300), 25))  
        self.img_hp2 = pygame.transform.scale(self.hpimg2 ,(320, 45))
        self.screen.blit(self.img_hp2, (10,20))                                
        self.screen.blit(self.img_hp, (20,30))
        
    def levelup(self):
        self.experience += 1
        if self.level+5 <= self.experience:
            self.experience -= self.level+5
            self.level += 1
        print(self.level,self.experience)
    
    def gameover(self):
        if self.hp <= 0:
            return False
        return True
    
    def draw(self):
        self.eventkey()
        self.ragermove()
        self.drawhp()
        self.screen.blit(self.img, self.rec)

