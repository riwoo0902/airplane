import pygame

class Greenrager():
    def __init__(self, screen,rec,con,type,energyballtype,spaceshiprec,bossrecx,bossmeteorittedirection):
        self.screen = screen
        self.con = con
        self.type = type
        self.energyballtype = energyballtype
        self.bossenergyballscale = 2
        if spaceshiprec != None:
            self.spaceshiprecx = spaceshiprec[0]
            self.spaceshiprecy = spaceshiprec[1]
        self.bossmeteorittedirection = bossmeteorittedirection
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
        elif self.type == 'bossmeteoritte':
            if self.bossmeteorittedirection == 1:
                self.img = pygame.image.load('./images/bossmeteorite.png').convert_alpha()
            elif self.bossmeteorittedirection == 2:
                self.img = pygame.image.load('./images/bossmeteorite2.png').convert_alpha()
            self.img2 = pygame.transform.scale(self.img, (150,600))    

        self.rec = self.img2.get_rect()
        self.rec.x = rec[0]
        self.rec.y = rec[1]
        if self.type == 'bossmeteoritte':
            self.rec.x = self.spaceshiprecx
            if self.bossmeteorittedirection == 1:
                self.rec.y = -600
            elif self.bossmeteorittedirection == 2:
                self.rec.y = 800

    def draw(self):
        if (self.rec.x) < 1500:
            if self.type == 'greenrager':
                self.rec.x += 5
            elif self.type == 'energyball':
                self.rec.x += 5
            elif self.type == 'bossenergyball':
                if self.bossenergyballscale != 100:
                    self.bossenergyballscale += 2
                    self.img2 = pygame.transform.scale(self.img, (self.bossenergyballscale,self.bossenergyballscale))
                    self.rec = self.img2.get_rect()
                    self.rec.x = self.bossrecx +300
                    self.rec.y = self.spaceshiprecy
                else:
                    self.rec.x += 15
            elif self.type == 'bossmeteoritte':
                if self.bossmeteorittedirection == 1:
                    self.rec.y += 3
                    if self.rec.y >= 800:
                        return True
                elif self.bossmeteorittedirection == 2:
                    self.rec.y -= 3
                    if self.rec.y <= -600:
                        return True
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