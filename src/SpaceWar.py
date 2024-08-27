import pygame
import random
from pygame.locals import *
from arctutus import *
from redspaceship import *
from spaceship import *
from backgrond import *
from arctutus import *
from status import *
from radioactive import*
class SpaceWar():
    runstart = True
    run = True
    WIDTH = 1500
    HEIGHT = 800
    statusActivation = 0
    
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SpaceWar")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) 
        self.con = Confing()
        self.spaceship = Spaceship(self.screen,self.con.spaceship)
        self.actutus = Arctutus(self.screen,self.con,self.spaceship)
        self.bg = Backgrond(self.screen)
        self.status = Status(self.screen,(0,0),self.con.spaceship)              
    #이벤트 확인 및 처리 함수
    def eventkey(self):
        for event in pygame.event.get():
            if event.type == QUIT:#닫기버튼
                self.run = False
            if event.type == pygame.KEYDOWN:#키를 눌렀을때
                if event.key == pygame.K_ESCAPE:
                    self.run = False   
                if event.key == pygame.K_e:
                    if self.statusActivation == 0:
                        self.statusActivation = 1
                    else:
                        self.statusActivation = 0
        self.run = self.spaceship.gameover()
        
    def loop(self):
        while self.run:
            self.eventkey() 
            self.bg.draw() 
            if self.statusActivation == 1:
                self.status.draw()
            else:
                self.actutus.draw()
                self.spaceship.draw()    
            self.spaceship.drawhp()
            pygame.display.update() 
            self.clock.tick(200) 

main = SpaceWar()
main.loop()