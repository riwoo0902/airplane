import pygame
class Ending():
    def __init__(self,screen):
        self.screen = screen
        self.endingon = True
        self.clock = pygame.time.Clock()
        self.Font = pygame.font.SysFont('malgungothic', 50)
        self.img = pygame.image.load('./images/operate.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (1600,800)) 
        self.texty = 0
        self.skiptext = self.Font.render("Tab을 눌러 재시작", True, (255,255,255))
        
    def endingdraw(self):
        if self.ending == 'happyending':
            self.text = self.Font.render("해피앤딩", True, (255,255,255))
        else:
            self.text = self.Font.render("멸망앤딩", True, (255,255,255))
        if self.texty < 800:
            self.screen.blit(self.text,(600,self.texty))
            self.texty += 1
        if self.texty == 800:
            self.endingon = False


    def eventkey(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#닫기버튼
                self.endingon = False
            if event.type == pygame.KEYDOWN:#키를 눌렀을때
                if event.key == pygame.K_TAB:
                    self.endingon = False   
    def loop(self,ending):
        self.ending = ending
        while self.endingon:
            self.screen.fill((0,0,0))
            self.screen.blit(self.skiptext,(1050,700))   
            self.eventkey()
            self.endingdraw()
            pygame.display.update()
            self.clock.tick(60)