import pygame
from pygame.locals import *


class SpaceWar():
    run = True
    WIDTH = 1500
    HEIGHT = 800
    backgrondxy = [0,0]
    backgrondxy2 = [-WIDTH,0]
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("SpaceWar")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) 
        self.backgrond = pygame.image.load('./images/background.png').convert_alpha()
        self.backgrond1 = pygame.transform.scale(self.backgrond, (self.WIDTH,self.HEIGHT))
        self.backgrond2 = pygame.transform.scale(self.backgrond, (self.WIDTH,self.HEIGHT))

    #이벤트 확인 및 처리 함수
    def eventkey(self):
        for event in pygame.event.get():
            if event.type == QUIT:#닫기버튼
                self.run = False
                
            if event.type == pygame.KEYDOWN:#키를 눌렀을때
                if event.key == pygame.K_ESCAPE:
                    self.run = False
                if event.key == pygame.K_SPACE:
                    pass
                
    def backgrondmove(self):
        self.backgrondxy[0] += 0.5
        self.backgrondxy2[0] += 0.5
        if self.backgrondxy[0] == self.WIDTH:
            self.backgrondxy = [0,0]
            self.backgrondxy2 = [-self.WIDTH,0]
        self.screen.blit(self.backgrond1, self.backgrondxy)
        self.screen.blit(self.backgrond2, self.backgrondxy2)
    def loop(self):
        while self.run:
            self.screen.fill((255, 255, 255)) 
            self.eventkey() 
            self.backgrondmove()
            pygame.display.update() 
            self.clock.tick(400) 
    
    
        
        
main = SpaceWar()
main.loop()