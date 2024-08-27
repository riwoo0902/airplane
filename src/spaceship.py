import pygame

from rager import *
from config import *
from radioactive import*
class Spaceship():
    
    
    ragers = []
    def __init__(self, screen,con):
        self.screen = screen
        self.Font = pygame.font.SysFont(None, 50)
        self.img = pygame.image.load('./images/spaceship.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (250,150))
        self.hpimg = pygame.image.load("./images/hp.png")
        self.hpimg2 = pygame.image.load("./images/hp1.png")
        self.con = con        
        # self.level = self.con['level']
        # self.hp = self.con['HP']
        # self.maxhp = self.con['maxHP']
        # self.damage = self.con['damage']
        # self.speed = self.con['speed']
        # self.defense = self.con['defense']
        # self.attackspeed = self.con['attackspeed']
        # self.nol = self.con['nol']
        # self.reincarnation = self.con['reincarnation']
        # self.luck = self.con['luck']
        # self.experience = self.con['experience']
        self.rec = self.img.get_rect()
        self.rec.x = 1000 
        self.rec.y = 350
        self.lagertime1 = 0
        self.lagertime2 = 0
        self.weaponattackspeedeffect = 1
        self.Radioactiverecx = self.rec.x
        self.Radioactiverecy = self.rec.y
        
        
    def eventkey(self):            
        key_pressed = pygame.key.get_pressed()  
        if key_pressed[pygame.K_w]:
            self.rec.y -= self.con['speed']
        if key_pressed[pygame.K_s]:
            self.rec.y += self.con['speed'] 
        if key_pressed[pygame.K_a]:
            self.rec.x -= self.con['speed'] 
        if key_pressed[pygame.K_d]:
            self.rec.x += self.con['speed'] 
            
        if self.rec.x <0:
            self.rec.x = 0
        if self.rec.x >1250:
            self.rec.x = 1250
        if self.rec.y <0:
            self.rec.y = 0
        if self.rec.y >650:
            self.rec.y = 650
        
        if self.con['weapontype'] != 3:
            if key_pressed[pygame.K_SPACE]:
                self.lagertime2 =pygame.time.get_ticks()
                
                if self.con['weapontype'] == 1:
                    self.weaponattackspeedeffect = 2                                  
                elif self.con['weapontype'] == 2:                                      
                    self.weaponattackspeedeffect = 0.8  
                elif self.con['weapontype'] == 0:   
                    self.weaponattackspeedeffect = 1
                if self.lagertime2 - self.lagertime1 >= self.con['attackspeed']/self.weaponattackspeedeffect:
                    self.lagertime1 =pygame.time.get_ticks()
                    self.ragers.append(rager(self.screen,(self.rec.x,self.rec.y+54),self.con['weapontype'])) 
            else:
                self.lagertime2 =pygame.time.get_ticks()
    def ragermove(self):
        for i, rager in enumerate(self.ragers):
            if rager.draw():  
                del self.ragers[i]  

    def radioactivecontamination(self):
        if self.con['weapontype'] == 3:
            self.Radioactiverecx = self.rec.x
            self.Radioactiverecy = self.rec.y
            Radioactive.radioactivecontamination(self)
        
        
        
        
        
        
        
        
        

    def drawhp(self):
        self.img_hp = pygame.transform.scale(self.hpimg ,(((self.con['HP']/self.con['maxHP'])*300), 25))  
        self.img_hp2 = pygame.transform.scale(self.hpimg2 ,(320, 45))
        self.Text = self.Font.render("level:" + str(self.con['level']), True, (120,120,120))
        self.Text2 = self.Font.render("point:" + str(self.con['point']), True, (120,120,120))
        self.screen.blit(self.img_hp2, (10,20))   
        self.screen.blit(self.img_hp, (20,30))                             
        self.screen.blit(self.Text, (400,20))
        self.screen.blit(self.Text2, (600,20))
    
    
    def levelup(self):
        self.con['experience'] += 1
        if self.con['level']+2 <= self.con['experience']:
            self.con['experience'] -= self.con['level']+2
            self.con['level'] += 1
            self.con['point'] += self.con['luck']
            self.con['point'] += round(self.con['point'])
    
    
    def gameover(self):
        if self.con['HP'] <= 0:
            return False
        return True
    
    
    
    

    
    def draw(self):
        self.con['HP'] += self.con['reincarnation']
        if self.con['HP'] > self.con['maxHP']:
            self.con['HP'] = self.con['maxHP']
        self.eventkey()
        self.radioactivecontamination()
        self.ragermove()
        self.screen.blit(self.img, self.rec)
        
        
        
        
        
        
        
        
        
        