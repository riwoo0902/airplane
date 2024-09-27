import pygame
import random
from pygame.locals import *
from arctutus import *
from redspaceship import *
from spaceship import *
from backgrond import *
from arctutus import *
from status import *
from intro import *
from ending import *
class SpaceWar():
    runstart = True
    run = True,True
    WIDTH = 1500
    HEIGHT = 800 
    statusActivation = 0
    ending = None
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SpaceWar")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT)) 
        self.con = Confing()
        self.con.spaceship = {'HP':100,'maxHP':100,'level':0,'reincarnation':0,'damage':10,'speed':5,'defense':0,'attackspeed':1000,'nol': 1, 'luck':5,'experience':0,'point':10000000,'weapontype':0,'circle':700,}
        self.con.redspaceship = {'hp':10,'damage': 2,'speed':3,'defense':0}
        self.spaceship = Spaceship(self.screen,self.con.spaceship)
        self.actutus = Arctutus(self.screen,self.con,self.spaceship)
        self.bg = Backgrond(self.screen)
        self.status = Status(self.screen,(0,0),self.con.spaceship)
        self.intro = Intro(self.screen)
        self.ending = Ending(self.screen)
        pygame.mixer.music.load(f'./sound/spacebg.wav')
        pygame.mixer.music.set_volume(100)
    #이벤트 확인 및 처리 함수
    def eventkey(self):
        if self.actutus.ending == 'happyending':
            self.run = False
        elif self.spaceship.gameover() == 'gameover':
            self.run = False
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

    def loop(self):
        pygame.mixer.music.play(-1)
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
        pygame.mixer.music.pause()  

while True:
    main = SpaceWar()
    main.intro.loop()
    main.loop()
    main.ending.loop(main.actutus.ending)
    del Redspaceship.greenragers
    Redspaceship.greenragers = []
    del Arctutus.redspaceships
    Arctutus.redspaceships = []
    del Spaceship.ragers
    Spaceship.ragers = []