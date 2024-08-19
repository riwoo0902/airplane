import pygame

class Status():
    def __init__(self, screen,rec,con):
        self.screen = screen
        self.con = con
        self.img = pygame.image.load('./images/statusscreen.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (1500,800))
        self.img.set_alpha(100)
        self.rec = self.img.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]
        self.Font = pygame.font.SysFont(None, 50)

        self.statusupimg = pygame.image.load('./images/status+-.png')
        self.statusupimg = pygame.transform.scale(self.statusupimg, (120,35))
        
        
    def statusup(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pass
                    
                    
                    
            
        
        
        
    def draw(self):
        self.screen.blit(self.img, (0,0))
        self.Text = self.Font.render("maxhp:" + str(self.con['maxHP']), True, (0,0,0))
        self.screen.blit(self.Text, (100,100))
        self.Text = self.Font.render("damage:" + str(self.con['damage']), True, (0,0,0))
        self.screen.blit(self.Text, (100,200))
        self.Text = self.Font.render("defense:" + str(self.con['defense']), True, (0,0,0))
        self.screen.blit(self.Text, (100,300))
        self.Text = self.Font.render("speed:" + str(self.con['speed']), True, (0,0,0))
        self.screen.blit(self.Text, (100,400))
        self.Text = self.Font.render("attackspeed:" + str(self.con['attackspeed']), True, (0,0,0))
        self.screen.blit(self.Text, (100,500))
        self.Text = self.Font.render("nol:" + str(self.con['nol']), True, (0,0,0))
        self.screen.blit(self.Text, (100,600))
        self.Text = self.Font.render("reincarnation:" + str(self.con['reincarnation']), True, (0,0,0))
        self.screen.blit(self.Text, (100,700))
        self.Text = self.Font.render("luck:" + str(self.con['luck']), True, (0,0,0))
        self.screen.blit(self.Text, (500,100))
        
        self.screen.blit(self.statusupimg, (330,100))
        self.screen.blit(self.statusupimg, (330,200))
        self.screen.blit(self.statusupimg, (330,300))
        self.screen.blit(self.statusupimg, (330,400))
        self.screen.blit(self.statusupimg, (430,500))
        self.screen.blit(self.statusupimg, (330,600))
        self.screen.blit(self.statusupimg, (430,700))
        self.screen.blit(self.statusupimg, (650,100))
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        