import pygame

class rager():
    def __init__(self, screen,rec,weapontype):
        self.screen = screen
        self.weapontype = weapontype
        if self.weapontype == 2:
            self.img = pygame.image.load('./images/rager.png').convert_alpha()
            self.img = pygame.transform.scale(self.img, (90,14)) 
        else:
            self.img = pygame.image.load('./images/machinegunbullet.png').convert_alpha()
            self.img = pygame.transform.scale(self.img, (50,7))
        self.rec = self.img.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]+20


    def draw(self):
        if (self.rec.x) > 0:  
            
            if self.weapontype == 2:
                self.rec.x -= 7.5
                self.screen.blit(self.img, self.rec)
            else:
                self.screen.blit(self.img, (self.rec.x,self.rec.y))
                self.rec.x -= 15
            return False
        else:
            return True