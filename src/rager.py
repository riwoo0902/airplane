import pygame

class rager():
    def __init__(self, screen,rec):
        self.screen = screen
        self.img = pygame.image.load('./images/rager.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (90,40))
        self.rec = self.img.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]

        
    def draw(self):
        if (self.rec.x) > 0:  
            self.rec.x -= 7.5
            self.screen.blit(self.img, self.rec)
            return False
        else:
            return True