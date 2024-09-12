import pygame

class Redspaceship():

    def __init__(self, screen,con,rec,weapontype,type):
        self.screen = screen
        self.type = type
        if self.type == 'normal':
            img = pygame.image.load('./images/redspaceship.png').convert_alpha()
            self.img = pygame.transform.scale(img, (150,75))
        elif self.type == 'meteorite':
            img = pygame.image.load('./images/meteorite.png').convert_alpha()
            self.img = pygame.transform.scale(img, (400,100))
        self.con = con
        if self.type == 'normal':
            self.hp = self.con['hp']
        elif self.type == 'meteorite':
            self.hp = self.con['hp']*3
        self.damage = self.con['damage']
        self.speed = self.con['speed']
        self.defense = self.con['defense']
        self.rec = self.img.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]
        self.weapontype = weapontype
        self.weapondamageeffect = 0
        self.hpimg = pygame.image.load("./images/hp.png")
        self.hpimg2 = pygame.image.load("./images/hp1.png")

    def checkCollision(self, ragers,damage): #충돌했는지 확인
        for i, arr in enumerate(ragers):
            if self.rec.colliderect(arr.rec):
                centerx = arr.rec.centerx
                centery = arr.rec.centery
                if self.weapontype == 1:
                    self.weapondamageeffect = 0.8
                elif self.weapontype == 2:
                    self.weapondamageeffect = 2
                else:
                    self.weapondamageeffect = 1

                self.hp -= damage * self.weapondamageeffect - self.defense
                return centerx,centery,i
        return None,None,None

    def radioactivecirclacheckCollision(self, radioactiverec,damage): #충돌했는지 확인
        if self.rec.colliderect(radioactiverec):
            centerx2 = radioactiverec.x
            centery2 = radioactiverec.y
            self.hp -= damage/200
            return centerx2,centery2
        return None,None

    def draw(self):
        if self.type == 'normal':
            self.img_hp = pygame.transform.scale(self.hpimg ,(((self.hp/self.con['hp'])*100), 10))  
            self.img_hp2 = pygame.transform.scale(self.hpimg2 ,(108, 18))
        elif self.type == 'meteorite':
            self.img_hp = pygame.transform.scale(self.hpimg ,(((self.hp/(self.con['hp']*3))*400), 10))  
            self.img_hp2 = pygame.transform.scale(self.hpimg2 ,(408, 18))
        self.screen.blit(self.img_hp2, (self.rec.x+30,self.rec.y-24))   
        self.screen.blit(self.img_hp, (self.rec.x+34,self.rec.y-20))
        if (self.rec.x) < 1500:  
            if self.type == 'meteorite':
                self.rec.x += self.speed/3
            else:
                self.rec.x += self.speed
            self.screen.blit(self.img, self.rec)
            return False
        else:
            return True