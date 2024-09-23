import pygame

class Greenrager():
    def __init__(self, screen,rec,con,type,energyballtype,spaceshiprecy,bossrecx):
        self.screen = screen
        self.con = con
        self.type = type
        self.energyballtype = energyballtype
        self.bossenergyballscale = 1
        self.spaceshiprecy = spaceshiprecy
        self.bossrecx = bossrecx
        if self.type == 'greenrager':
            self.img = pygame.image.load('./images/greenrager.png').convert_alpha()
            self.img2 = pygame.transform.scale(self.img, (90,14))
        elif self.type == 'energyball':
            self.img = pygame.image.load('./images/energyball.png').convert_alpha()
            self.img2 = pygame.transform.scale(self.img, (50,50))
        elif self.type == 'bossenergyball':
            self.img = pygame.image.load('./images/energyball.png').convert_alpha()
            self.img2 = pygame.transform.scale(self.img, (self.bossenergyballscale,self.bossenergyballscale))
        elif self.type == 'bigbossenergyball':
            self.img = pygame.image.load('./images/energyball.png').convert_alpha()
            self.img2 = pygame.transform.scale(self.img, (600,600))    
        self.rec = self.img2.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]

    def draw(self):
        if (self.rec.x) < 1500:
            if self.type == 'greenrager':
                self.rec.x += 5
            elif self.type == 'energyball':
                self.rec.x += 5
            elif self.type == 'bossenergyball':
                if self.bossenergyballscale != 100:
                    self.bossenergyballscale += 1
                    self.img2 = pygame.transform.scale(self.img, (self.bossenergyballscale,self.bossenergyballscale))
                    self.rec = self.img2.get_rect()
                    self.rec.x = self.bossrecx +300
                    self.rec.y = self.spaceshiprecy
                else:
                    self.rec.x += 15
            elif self.type == 'energyball':
                self.rec.x += 2
            if self.energyballtype != 0:
                if self.energyballtype == 1:
                    self.rec.y -= 2
                elif self.energyballtype == 2:
                    self.rec.y -= 1
                elif self.energyballtype == 4:
                    self.rec.y += 1
                elif self.energyballtype == 5:
                    self.rec.y += 2
            self.screen.blit(self.img2, self.rec)
                    
            return False
        else:
            return True