import pygame

class Intro():

    def __init__(self,screen):
        self.screen = screen
        self.introon = True
        self.clock = pygame.time.Clock()
        self.Font = pygame.font.SysFont('malgungothic', 50)
        self.stagetime = 0
        self.texty = 0
        self.img = pygame.image.load('./images/operate.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (1600,800)) 
        self.text = self.Font.render("스토리", True, (255,255,255))
        self.skiptext = self.Font.render("Tab을 눌러 스킵", True, (255,255,255))

    def introdraw(self):
        if self.texty < 800:
            self.screen.blit(self.text,(600,self.texty))
            self.texty += 1
        if self.texty == 800:
            self.stagetime = pygame.time.get_ticks()

    def operate(self):
            if pygame.time.get_ticks() - self.stagetime < 7000:
                self.screen.blit(self.img, (0,0))
            else:
                self.introon = False

    def eventkey(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#닫기버튼
                self.introon = False
            if event.type == pygame.KEYDOWN:#키를 눌렀을때
                if event.key == pygame.K_TAB:
                    self.introon = False

    def loop(self):
        while self.introon:
            self.screen.fill((0,0,0))
            self.eventkey()
            self.screen.blit(self.skiptext,(1050,700))   
            if self.texty != 800:
                self.introdraw()
            if self.texty == 800:
                self.operate()
            pygame.display.update()
            self.clock.tick(60)