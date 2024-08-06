import pygame

class rager():
    def __init__(self, screen,rec):#ret : 화살이 시작될 위치값
        self.screen = screen
        self.rager = pygame.image.load('./images/rager.png').convert_alpha()
        self.rager = pygame.transform.scale(self.rager, (90,40))
        self.rec = self.rager.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]

        
    def draw(self):
        if (self.rec.x) > 0:  
            self.rec.x -= 7.5
            self.screen.blit(self.rager, self.rec)
            return False
        else:
            return True