import pygame

class Redspaceship():


    def __init__(self, screen,img,con,rec,weapontype):
        self.screen = screen
        self.img = img
        self.con = con
        self.hp = self.con['hp']
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
        self.img_hp = pygame.transform.scale(self.hpimg ,(((self.hp/self.con['hp'])*100), 10))  
        self.img_hp2 = pygame.transform.scale(self.hpimg2 ,(108, 18))
        self.screen.blit(self.img_hp2, (self.rec.x+30,self.rec.y-24))   
        self.screen.blit(self.img_hp, (self.rec.x+34,self.rec.y-20))
        if (self.rec.x) < 1500:  
            self.rec.x += self.speed
            self.screen.blit(self.img, self.rec)
            return False
        else:
            return True