import pygame
import random
from arctutus import *
from redspaceship import *
from spaceship import *
from config import *
import math
class Arctutus():
    redspaceships = []
    summontime = 0
    experience = 0
    dam = 0
    def __init__(self,screen,con,spaceship):
        self.screen = screen
        self.con = con
        self.spaceship = spaceship
        img_redspaceship = pygame.image.load('./images/redspaceship.png').convert_alpha()
        self.img_redspaceship = pygame.transform.scale(img_redspaceship, (150,75))
        self.Font = pygame.font.SysFont(None, 100)
        self.Font2 = pygame.font.SysFont(None, 50)
        self.summontime2 = 2000
        self.redsummoning = 0
        self.stage = 0
        self.stagetime = 0
    def redspaceshipmove(self):   
        if self.summontime2 > 0:     
            if pygame.time.get_ticks() - self.summontime >= self.summontime2:
                self.summontime2 -= 3
                self.redsummoning += 1
                self.summontime = pygame.time.get_ticks()
                self.redspaceships.append(Redspaceship(self.screen,self.img_redspaceship,self.con.redspaceship,(-225,random.randint(50,700)),self.spaceship.con['weapontype']))

        if self.redsummoning == 1:
            self.stage = 1
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 10
        elif self.redsummoning == 111:
            self.stage = 2
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 20
        elif self.redsummoning == 222:
            self.stage = 3
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 30
        elif self.redsummoning == 333:
            self.stage = 4
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 40
        elif self.redsummoning == 444:
            self.stage = 5
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 50
        elif self.redsummoning == 555:
            self.stage = 6
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 100
        elif self.redsummoning == 666:
            self.stage = 7
            self.stagetime = pygame.time.get_ticks()
            self.con.redspaceship['hp'] = 5000


        for i, ship in enumerate(self.redspaceships):
            if ship.draw():
                del self.redspaceships[i] 
            else:
                centerx,centery,rager_idex = ship.checkCollision(self.spaceship.ragers,self.spaceship.con['damage'])
                centerx2,centery2 = ship.radioactivecirclacheckCollision(self.spaceship.radioactiverec,self.spaceship.con['damage'])
                if centerx != None:
                    del self.spaceship.ragers[rager_idex]
                    if ship.hp <= 0:
                        del self.redspaceships[i]
                        self.spaceship.levelup()

                elif centerx2 != None:
                    if ship.hp <= 0:
                        del self.redspaceships[i]
                        self.spaceship.levelup()

                if ship.rec.colliderect(self.spaceship.rec):
                    self.dam = ship.hp - self.spaceship.con['defense']
                    if self.dam < 1:
                        self.dam = 1
                    self.spaceship.con['HP'] -= self.dam
                    del self.redspaceships[i]  

    def draw(self):
        self.redspaceshipmove()
        if pygame.time.get_ticks() - self.stagetime < 3000:
            self.Text = self.Font.render(f"stage {self.stage}", True, (255,255,255))
            self.screen.blit(self.Text, (600,350))
        self.Text2 = self.Font2.render(f"stage: {self.stage}", True, (120,120,120))
        self.screen.blit(self.Text2, (1300,20))