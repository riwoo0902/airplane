import pygame
import random
from pygame.locals import *
from arctutus import *
from  redspaceship import *
from spaceship import *
from backgrond import *
from arctutus import *
class SpaceWar():
    run = True
    WIDTH = 1500
    HEIGHT = 800    
    
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("SpaceWar")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) 
        self.con = Confing()
        self.spaceship = Spaceship(self.screen,self.con.spaceship)
        self.actutus = Arctutus(self.screen,self.con,self.spaceship)
        self.bg = Backgrond(self.screen)
        
    #이벤트 확인 및 처리 함수
    def eventkey(self):
        for event in pygame.event.get():
            if event.type == QUIT:#닫기버튼
                self.run = False
                
            if event.type == pygame.KEYDOWN:#키를 눌렀을때
                if event.key == pygame.K_ESCAPE:
                    self.run = False                
        self.run = self.spaceship.gameover()
   
    def loop(self):
        while self.run:
            self.eventkey() 
            self.bg.draw()
            
            self.actutus.draw()
            
            self.spaceship.draw()    
                    
            pygame.display.update() 
            self.clock.tick(200) 

main = SpaceWar()
main.loop()