import pygame
import random
from pygame.locals import *
from redspaceship import *
from spaceship import *
from backgrond import *
class SpaceWar():
    run = True
    WIDTH = 1500
    HEIGHT = 800
    redspaceships = []
    summontime = 0
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("SpaceWar")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) 
        self.spaceship = Spaceship(self.screen)
        self.bg = Backgrond(self.screen)
        
    #이벤트 확인 및 처리 함수
    def eventkey(self):
        for event in pygame.event.get():
            if event.type == QUIT:#닫기버튼
                self.run = False
                
            if event.type == pygame.KEYDOWN:#키를 눌렀을때
                if event.key == pygame.K_ESCAPE:
                    self.run = False                
                            
    def redspaceshipmove(self):        
        if pygame.time.get_ticks() - self.summontime >= 3000:
            self.summontime = pygame.time.get_ticks()
            self.redspaceships.append(Redspaceship(self.screen,(-225,random.randint(0,700))))   
                      
        for i, ship in enumerate(self.redspaceships):
            if ship.draw():  
                del self.redspaceships[i] 
                
    def loop(self):
        while self.run:
            self.bg.draw()
            self.eventkey() 
            self.redspaceshipmove()
            self.spaceship.draw()            
            pygame.display.update() 
            self.clock.tick(400) 

main = SpaceWar()
main.loop()