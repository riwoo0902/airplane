import pygame

class Status():
    def __init__(self, screen,rec):
        self.screen = screen
        self.img = pygame.image.load('./images/status.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (1500,800))
        self.rec = self.img.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]
        
    def draw(self):
        self.screen.blit(self.img, (0,0))

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        