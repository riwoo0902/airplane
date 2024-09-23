import pygame

class Greenrager():
    def __init__(self, screen,rec,con,type,energyballtype):
        self.screen = screen
        self.con = con
        self.type = type
        self.energyballtype = energyballtype
        if self.type == 'greenrager':
            self.img = pygame.image.load('./images/greenrager.png').convert_alpha()
            self.img = pygame.transform.scale(self.img, (90,14))
        elif self.type == 'energyball':
            self.img = pygame.image.load('./images/energyball.png').convert_alpha()
            self.img = pygame.transform.scale(self.img, (50,50))
        self.rec = self.img.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]

    def draw(self):
        if (self.rec.x) < 1500:
            self.screen.blit(self.img, self.rec)
            if self.type == 'greenrager':
                self.rec.x += 5
            elif self.type == 'energyball':
                self.rec.x += 5
            if self.energyballtype != 0:
                if self.energyballtype == 1:
                    self.rec.y -= 2
                elif self.energyballtype == 2:
                    self.rec.y -= 1
                elif self.energyballtype == 4:
                    self.rec.y += 1
                elif self.energyballtype == 5:
                    self.rec.y += 2
            return False
        else:
            return True