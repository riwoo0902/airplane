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
        self.weaponslot = pygame.image.load('./images/hp1.png').convert_alpha()
        self.weaponslot = pygame.transform.scale(self.weaponslot, (400,400))
        self.weaponslot.set_alpha(200)
        self.Font = pygame.font.SysFont(None, 50)
        self.statusupimg = pygame.image.load('./images/status+.png')
        self.statusupimg = pygame.transform.scale(self.statusupimg, (60,30))
        self.machinegun = pygame.image.load('./images/machinegun.png').convert_alpha()
        self.machinegun = pygame.transform.scale(self.machinegun, (150,150))
        self.ragergun = pygame.image.load('./images/ragergun.png').convert_alpha()
        self.ragergun = pygame.transform.scale(self.ragergun, (230,60))
        self.radioactiveemitter = pygame.image.load('./images/radioactiveemitter.png').convert_alpha()
        self.radioactiveemitter = pygame.transform.scale(self.radioactiveemitter, (100,180))

    def statusup(self):
        pos = pygame.mouse.get_pos()
        statusupdown = [self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h]
        for l in range(8):
            if  statusupdown[l].collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                if self.con['point'] >= 1:
                    if l == 0:
                        self.con['maxHP'] += 1
                    elif l == 1:
                        self.con['damage'] += 0.2
                        self.con['damage'] = round(self.con['damage'],1)
                    elif l == 2:
                        self.con['defense'] += 0.1
                        self.con['defense'] = round(self.con['defense'],1)
                    elif l == 3:
                        self.con['speed'] += 0.1
                        self.con['speed'] = round(self.con['speed'],1)
                    elif l == 4:
                        if self.con['attackspeed'] > 100:
                            self.con['attackspeed'] -= 0.5
                        elif self.con['attackspeed'] <= 100:
                            self.con['attackspeed'] = 100
                            self.con['point'] += 1
                    elif l == 5:
                        self.con['nol'] += 0.001
                        self.con['nol'] = round(self.con['nol'],3)
                    elif l == 6:
                        self.con['reincarnation'] += 0.0005
                        self.con['reincarnation'] = round(self.con['reincarnation'],4)
                    elif l == 7:
                        self.con['luck'] += 0.2
                        self.con['luck'] = round(self.con['luck'],1)
                    self.con['point'] -= 1
                    self.con['point'] = round(self.con['point'])

    def weaponselection(self):
        if self.con['weapontype'] == 0:
            if self.con['level'] >= 15:
                self.screen.blit(self.machinegun,(450,150))
                self.screen.blit(self.ragergun,(670,190))
                self.screen.blit(self.radioactiveemitter,(550,440))
                self.Text = self.Font.render("Choice", True, (0,0,0))
                self.Text = pygame.transform.scale(self.Text, (100,40))
                self.a2 = self.screen.blit(self.Text, (480,350))
                self.b2 = self.screen.blit(self.Text, (730,350))
                self.c2 = self.screen.blit(self.Text, (550,640))
                pos = pygame.mouse.get_pos()
                weaponselection = [self.a2,self.b2,self.c2]
                for l in range(3):
                    if  weaponselection[l].collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                        self.con['weapontype'] = l+1
                        self.con['weaponlevel'] = 1
        else:
            if self.con['weapontype'] == 1:
                self.machinegun = pygame.transform.scale(self.machinegun, (340,340))
                self.screen.blit(self.machinegun,(990,90))
            elif self.con['weapontype'] == 2:
                self.ragergun = pygame.transform.scale(self.ragergun, (345,90))
                self.screen.blit(self.ragergun,(975,205))   
            elif self.con['weapontype'] == 3:
                self.radioactiveemitter = pygame.transform.scale(self.radioactiveemitter, (200,360))
                self.screen.blit(self.radioactiveemitter,(1050,70))    

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

        self.a = self.screen.blit(self.statusupimg, (350,100))
        self.b = self.screen.blit(self.statusupimg, (350,200))
        self.c = self.screen.blit(self.statusupimg, (350,300))
        self.d = self.screen.blit(self.statusupimg, (350,400))
        self.e = self.screen.blit(self.statusupimg, (450,500))
        self.f = self.screen.blit(self.statusupimg, (350,600))
        self.g = self.screen.blit(self.statusupimg, (450,700))
        self.h = self.screen.blit(self.statusupimg, (670,100))

        self.screen.blit(self.weaponslot,(950,50))


        self.statusup()
        self.weaponselection()