import pygame
import random
from arctutus import *
from redspaceship import *
from spaceship import *
from config import *
from greenreager import *
import math
class Arctutus():
    redspaceships = []
    summontime = 0
    summontime3 = 0
    summontime4 = 0
    experience = 0
    dam = 0
    def __init__(self,screen,con,spaceship):
        self.screen = screen
        self.con = con
        self.spaceship = spaceship
        self.Font = pygame.font.SysFont(None, 100)
        self.Font2 = pygame.font.SysFont(None, 50)
        self.summontime2 = 2000
        self.redsummoning = 0
        self.stage = 0
        self.stagetime = 0
        self.giveexp = 1
        self.crashingsound = pygame.mixer.Sound(f'./sound/crashing.wav')
        self.crashingsound.set_volume(0.5)
    def redspaceshipmove(self):
        if self.summontime2 > 0:
            if pygame.time.get_ticks() - self.summontime >= self.summontime2:
                self.summontime2 -= 3
                self.redsummoning += 1
                self.summontime = pygame.time.get_ticks()
                self.redspaceships.append(Redspaceship(self.screen,self.con.redspaceship,(-150,random.randint(50,700)),self.spaceship.con['weapontype'],'normal'))
        if self.stage > 1:
            if pygame.time.get_ticks() - self.summontime3 >= 10000:
                self.summontime3 = pygame.time.get_ticks()
                self.redspaceships.append(Redspaceship(self.screen,self.con.redspaceship,(-400,random.randint(0,700)),self.spaceship.con['weapontype'],'meteorite'))
        if self.stage > 2:
            if pygame.time.get_ticks() - self.summontime3 >= 4000:
                self.summontime3 = pygame.time.get_ticks()
                self.redspaceships.append(Redspaceship(self.screen,self.con.redspaceship,(-150,random.randint(0,700)),self.spaceship.con['weapontype'],'greenship'))  
        if self.stage > 3:
            if pygame.time.get_ticks() - self.summontime4 >= 7000:
                self.summontime4 = pygame.time.get_ticks()
                self.redspaceships.append(Redspaceship(self.screen,self.con.redspaceship,(-150,random.randint(0,700)),self.spaceship.con['weapontype'],'bomdship')) 

        if self.redsummoning == 1:
            self.stage = 4
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 10
            self.giveexp = 1
        elif self.redsummoning == 50:
            self.stage = 2
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 15
            self.giveexp = 2
        elif self.redsummoning == 111:
            self.stage = 3
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 30
            self.giveexp = 3
        elif self.redsummoning == 222:
            self.stage = 4
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 60
            self.giveexp = 4
        elif self.redsummoning == 333:
            self.stage = 5
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 100
            self.giveexp = 5
        elif self.redsummoning == 444:
            self.stage = 6
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 300
            self.giveexp = 6
        elif self.redsummoning == 555:
            self.stage = 7
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 1000
            self.giveexp = 7
        elif self.redsummoning == 666:
            self.stage = 8
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 10000
            self.giveexp = 8

        for i, ship in enumerate(self.redspaceships):
            if ship.draw():
                del self.redspaceships[i] 
            else:
                centerx,centery,rager_idex = ship.checkCollision(self.spaceship.ragers,self.spaceship.con['damage'])
                centerx2,centery2 = ship.radioactivecirclacheckCollision(self.spaceship.radioactiverec,self.spaceship.con['damage'])
                if centerx != None:#총알과 충돌
                    del self.spaceship.ragers[rager_idex]
                    if ship.hp <= 0:
                        del self.redspaceships[i]
                        if ship.type == 'bomdship':
                            ship.summon('energyball')
                        else:
                            self.spaceship.levelup(self.giveexp)

                elif centerx2 != None:#방사능과 충돌
                    if ship.hp <= 0:
                        del self.redspaceships[i]
                        if ship.type == 'bomdship':
                            ship.summon('energyball')
                        else:
                            self.spaceship.levelup(self.giveexp)
                        
                if ship.rec.colliderect(self.spaceship.rec):#우주선과 충돌
                    self.dam = ship.hp - self.spaceship.con['defense']
                    if self.dam < 1:
                        self.dam = 1
                    self.spaceship.con['HP'] -= self.dam
                    del self.redspaceships[i]  
                    self.crashingsound.play()
                
        for i, grager in enumerate(Redspaceship.greenragers):
            if grager.draw():
                del Redspaceship.greenragers[i] 
            else:
                centerx,centery,rager_idex = self.spaceship.checkCollisiongr(Redspaceship.greenragers,self.con.redspaceship['damage'])
                if centerx != None:
                    del Redspaceship.greenragers[i]

    def draw(self):
        self.redspaceshipmove()
        if pygame.time.get_ticks() - self.stagetime < 3000:
            self.Text = self.Font.render(f"stage {self.stage}", True, (255,255,255))
            self.screen.blit(self.Text, (600,350))
        self.Text2 = self.Font2.render(f"stage: {self.stage}", True, (120,120,120))
        self.screen.blit(self.Text2, (1300,20))