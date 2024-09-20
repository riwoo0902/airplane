import pygame

class Greenrager():
    def __init__(self, screen,rec,con,type):
        self.screen = screen
        self.con = con
        self.type = type
        if self.type == 'greenrager':
            self.img = pygame.image.load('./images/greenrager.png').convert_alpha()
            self.img = pygame.transform.scale(self.img, (90,14))
        elif self.type == 'energyball':
            self.img = pygame.image.load('./images/energyball.png').convert_alpha()
            self.img = pygame.transform.scale(self.img, (90,90))
        self.rec = self.img.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]

    def draw(self):
        if (self.rec.x) < 1500:
            self.screen.blit(self.img, self.rec)
            self.rec.x += 5
            return False
        else:
            return True