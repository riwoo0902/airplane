import pygame
class Redspaceship():
    
    
    def __init__(self, screen,rec):
        self.screen = screen
        self.redspaceship = pygame.image.load('./images/redspaceship.png').convert_alpha()
        self.redspaceship = pygame.transform.scale(self.redspaceship, (150,100))
        self.rec = self.redspaceship.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]

        
    def draw(self):
        if (self.rec.x) < 1500:  
            self.rec.x += 1
            self.screen.blit(self.redspaceship, self.rec)
            return False
        else:
            return True