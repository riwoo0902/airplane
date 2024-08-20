import pygame
import random
from arctutus import *
from redspaceship import *
from spaceship import *
from config import *
from weapon import *
class Arctutus():
    redspaceships = []
    summontime = 0
    experience = 0
    dam = 0
    def __init__(self,screen,con,spaceship) -> None:
        self.screen = screen
        self.con = con
        self.spaceship = spaceship
        img_redspaceship = pygame.image.load('./images/redspaceship.png').convert_alpha()
        self.img_redspaceship = pygame.transform.scale(img_redspaceship, (150,75))
        
    def redspaceshipmove(self):        
        if pygame.time.get_ticks() - self.summontime >= 3000:
            self.summontime = pygame.time.get_ticks()
            self.redspaceships.append(Redspaceship(self.screen,self.img_redspaceship,self.con.redspaceship,(-225,random.randint(50,700))))

        for i, ship in enumerate(self.redspaceships):
            if ship.draw():
                del self.redspaceships[i] 
            else:
                centerx,centery,rager_idex = ship.checkCollision(self.spaceship.ragers,self.spaceship.con['damage'])
                if centerx != None:
                    del self.spaceship.ragers[rager_idex]
                    if ship.hp <= 0:
                        del self.redspaceships[i]
                        self.spaceship.levelup()
                        self.weapondrop()
                        
                else:
                    if ship.rec.colliderect(self.spaceship.rec):
                        self.dam = ship.hp - self.spaceship.con['defense']
                        if self.dam < 1:
                            self.dam = 1
                        self.spaceship.con['HP'] -= self.dam
                        print(self.dam)
                        del self.redspaceships[i] 
                        
    def weapondrop(self):
        if random.randint(1,20000/self.spaceship.con['luck']) == 1:
            print('weapondrop')       
                        
    def draw(self):
        self.redspaceshipmove()
        