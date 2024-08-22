import pygame
import random
from config import *
class Weapon():
    def __init__(self, screen,rec):
        self.screen = screen
        if type == 0:
            self.img = pygame.image.load('./images/machinegun.png').convert_alpha()
        elif type == 1:
            self.img = pygame.image.load('./images/ragerrun.png').convert_alpha()
        elif type == 2:
            self.img = pygame.image.load('./images/machinegun.png').convert_alpha()
        elif type == 3:
            self.img = pygame.image.load('./images/machinegun.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (90,40))
        self.rec = self.img.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]
        
        
    
         
    def draw(self):
        pass


