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
        self.statusupimg = pygame.image.load('./images/status-.png')
        self.statusupimg = pygame.transform.scale(self.statusupimg, (60,35))
        self.statusupimg2 = pygame.image.load('./images/status+.png')
        self.statusupimg2 = pygame.transform.scale(self.statusupimg2, (60,35))
        
    def statusup(self):
        pos = pygame.mouse.get_pos()
        statusupdown = [[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h],[self.a2,self.b2,self.c2,self.d2,self.e2,self.f2,self.g2,self.h2]]
        for i in range(2):
            for l in range(8):
                if  statusupdown[i][l].collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                    if l == 0:
                        j = 'maxHP'
                    elif l == 1:
                        j = 'damage'
                    elif l == 2:
                        j = 'defense'
                    elif l == 3:
                        j = 'speed'
                    elif l == 4:
                        j = 'attackspeed'
                    elif l == 5:
                        j = 'nol'
                    elif l == 6:
                        j = 'reincarnation'
                    elif l == 7:
                        j = 'luck'
                        
                    if i == 0:
                        pass
                    elif i == 1:
                        self.con[j] += 1
                        self.con['point'] -= 1
                        


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
        
                                 
        self.a = self.screen.blit(self.statusupimg, (330,100))
        self.b = self.screen.blit(self.statusupimg, (330,200))
        self.c = self.screen.blit(self.statusupimg, (330,300))
        self.d = self.screen.blit(self.statusupimg, (330,400))
        self.e = self.screen.blit(self.statusupimg, (430,500))
        self.f = self.screen.blit(self.statusupimg, (330,600))
        self.g = self.screen.blit(self.statusupimg, (430,700))
        self.h = self.screen.blit(self.statusupimg, (650,100))
        
        self.a2 = self.screen.blit(self.statusupimg2, (400,100))
        self.b2 = self.screen.blit(self.statusupimg2, (400,200))
        self.c2 = self.screen.blit(self.statusupimg2, (400,300))
        self.d2 = self.screen.blit(self.statusupimg2, (400,400))
        self.e2 = self.screen.blit(self.statusupimg2, (500,500))
        self.f2 = self.screen.blit(self.statusupimg2, (400,600))
        self.g2 = self.screen.blit(self.statusupimg2, (500,700))
        self.h2 = self.screen.blit(self.statusupimg2, (720,100))
        self.statusup()
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        