import pygame

class Backgrond():
    def __init__(self, screen):
        self.screen = screen
        self.img = pygame.image.load('./images/background.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.screen.get_width(),self.screen.get_height()))
        
        self.rec = self.img.get_rect()
        self.rec.x = 0 
        self.rec.y = 0
        
        self.rec2 = self.img.get_rect()
        self.rec2.x = -self.screen.get_width() 
        self.rec2.y = 0
        
        self.update_delay = 0
        

            
    def draw(self):
        self.update_delay += 1
        if self.update_delay >= 2:
            self.rec.x += 1
            self.rec2.x += 1
            self.update_delay = 0
        
        if self.rec.x >= self.screen.get_width() :
            self.rec.x = 0
            self.rec2.x = -self.screen.get_width() 
            
        self.screen.blit(self.img, self.rec)
        self.screen.blit(self.img, self.rec2)   
        
        