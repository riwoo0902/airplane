import pygame

class rager():
    def __init__(self, screen,rec):
        self.screen = screen
        self.img = pygame.image.load('./images/wave.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (50,200)) #90,40
        self.img.set_alpha(100)
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