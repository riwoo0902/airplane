import pygame

from rager import *
from config import *
class Spaceship():

    ragers = []
    def __init__(self, screen,con):
        self.screen = screen
        self.Font = pygame.font.SysFont(None, 50)
        self.img = pygame.image.load('./images/spaceship.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (300,100))               #1280 387
        self.hpimg = pygame.image.load("./images/hp.png")
        self.hpimg2 = pygame.image.load("./images/hp1.png")
        self.img2 = pygame.image.load('./images/radioactivity.png').convert_alpha()
        self.img2.set_alpha(150)
        self.con = con        
        self.rec = self.img.get_rect()
        self.rec.x = 1000 
        self.rec.y = 350
        self.lagertime1 = 0
        self.lagertime2 = 0
        self.weaponattackspeedeffect = 1
        self.img2 = pygame.transform.scale(self.img2, (self.con['circle'],self.con['circle']))
        self.radioactiverec = self.img2.get_rect()
        self.radioactiverec.x = 2000
        self.radioactiverec.y = 400
        self.radioactivecircla = self.screen.blit(self.img2, (2000,400))
        self.levelupsound = pygame.mixer.Sound(f'./sound/levelup.wav')
        self.machinegunsound = pygame.mixer.Sound(f'./sound/machinegun.wav')
        self.machinegunsound.set_volume(0.2)
        self.lasergunsound = pygame.mixer.Sound(f'./sound/laser.wav')
        self.lasergunsound.set_volume(0.5)
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
        if self.rec.x >1200:
            self.rec.x = 1200
        if self.rec.y <0:
            self.rec.y = 0
        if self.rec.y >700:
            self.rec.y = 700

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
                    self.ragers.append(rager(self.screen,(self.rec.x,self.rec.y+45),self.con['weapontype'])) 
                    if self.con['weapontype'] == 2:
                        self.lasergunsound.play()
                    else:
                        self.machinegunsound.play()
            else:
                self.lagertime2 =pygame.time.get_ticks()
    def ragermove(self):
        for i, rager in enumerate(self.ragers):
            if rager.draw():  
                del self.ragers[i]  

    def radioactive(self):
        if self.con['weapontype'] == 3:
            self.img2 = pygame.transform.scale(self.img2, (self.con['circle'],self.con['circle']))
            self.radioactiverec.x = self.rec.x-int((self.con['circle'] - 250)/2)
            self.radioactiverec.y = self.rec.y-int((self.con['circle'] - 150)/2)
            self.radioactivecircla = self.screen.blit(self.img2, (self.radioactiverec.x,self.radioactiverec.y))  

    def drawhp(self):
        if self.con['HP'] > 0:
            self.img_hp = pygame.transform.scale(self.hpimg ,(((self.con['HP']/self.con['maxHP'])*300), 25))  
            self.img_hp2 = pygame.transform.scale(self.hpimg2 ,(320, 45))
            self.Text = self.Font.render("level:" + str(self.con['level']), True, (120,120,120))
            self.Text2 = self.Font.render("point:" + str(self.con['point']), True, (120,120,120))
            self.screen.blit(self.img_hp2, (10,20))   
            self.screen.blit(self.img_hp, (20,30))                             
            self.screen.blit(self.Text, (400,20))
            self.screen.blit(self.Text2, (600,20))

    def levelup(self,experience):
        self.con['experience'] += experience
        if self.con['level']+2 <= self.con['experience']:
            self.con['experience'] -= self.con['level']+2
            self.con['level'] += 1
            self.con['point'] += self.con['luck']
            self.con['point'] = round(self.con['point'])
            self.levelupsound.play()
    
    def gameover(self):
        if self.con['HP'] <= 0:
            return False
        return True
    
    def checkCollisiongr(self, greenragers,damage): #충돌했는지 확인
        for i, greenrager in enumerate(greenragers):
            if self.rec.colliderect(greenrager.rec):
                centerx = greenrager.rec.centerx
                centery = greenrager.rec.centery
                if greenrager.type == 'greenrager':
                    self.con['HP'] -= damage 
                elif greenrager.type == 'energyball':
                    self.con['HP'] -= damage * 3
                return centerx,centery,i
        return None,None,None
    
    def draw(self):
        self.con['HP'] += self.con['reincarnation']
        if self.con['HP'] > self.con['maxHP']:
            self.con['HP'] = self.con['maxHP']
        self.eventkey()
        self.radioactive()
        self.ragermove()
        self.screen.blit(self.img, self.rec)