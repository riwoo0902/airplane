import pygame
from pygame.locals import *


class SpaceWar():
    run = True
    WIDTH = 400
    HEIGHT = 400
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("SpaceWar")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) 


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
                
    def loop(self):
        while self.run:
            self.screen.fill((255, 255, 255)) 
            self.eventkey() 
            pygame.display.update() 
            self.clock.tick(60) 
            
main = SpaceWar()
main.loop()