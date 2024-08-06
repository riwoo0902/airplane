import pygame
from pygame.locals import *
from rager import *

class SpaceWar():
    run = True
    WIDTH = 1500
    HEIGHT = 800
    backgrondxy = [0,0]
    backgrondxy2 = [-WIDTH,0]
    spaceshipxy = [1000,350]
    ragers = []
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("SpaceWar")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) 
        self.backgrond = pygame.image.load('./images/background.png').convert_alpha()
        self.backgrond = pygame.transform.scale(self.backgrond, (self.WIDTH,self.HEIGHT))
        self.spaceship = pygame.image.load('./images/spaceship.png').convert_alpha()
        self.spaceship = pygame.transform.scale(self.spaceship, (225,150))
        
        
        
        
    #이벤트 확인 및 처리 함수
    def eventkey(self):
        for event in pygame.event.get():
            if event.type == QUIT:#닫기버튼
                self.run = False
                
            if event.type == pygame.KEYDOWN:#키를 눌렀을때
                if event.key == pygame.K_ESCAPE:
                    self.run = False
        key_pressed = pygame.key.get_pressed()  
        if key_pressed[pygame.K_w]:
            self.spaceshipxy[1] -= 1
        if key_pressed[pygame.K_s]:
            self.spaceshipxy[1] += 1
        if key_pressed[pygame.K_a]:
            self.spaceshipxy[0] -= 1
        if key_pressed[pygame.K_d]:
            self.spaceshipxy[0] += 1    
        if key_pressed[pygame.K_SPACE]:
            self.ragers.append(rager(self.screen,(self.spaceshipxy[0],self.spaceshipxy[1]+54)))      
            
    def backgrondmove(self):
        self.backgrondxy[0] += 0.5
        self.backgrondxy2[0] += 0.5
        if self.backgrondxy[0] == self.WIDTH:
            self.backgrondxy = [0,0]
            self.backgrondxy2 = [-self.WIDTH,0]
        self.screen.blit(self.backgrond, self.backgrondxy)
        self.screen.blit(self.backgrond, self.backgrondxy2)
        
    def drawairplane(self):
        self.screen.blit(self.spaceship,self.spaceshipxy)
    
    def ragermove(self):
        for i, rager in enumerate(self.ragers):
            if rager.draw():  #이동하며 그린다.
                del self.ragers[i] #삭제
    def loop(self):
        while self.run:
            self.screen.fill((255, 255, 255)) 
            self.eventkey() 
            self.backgrondmove()
            self.ragermove()
            self.drawairplane()
            pygame.display.update() 
            self.clock.tick(400) 

main = SpaceWar()
main.loop()