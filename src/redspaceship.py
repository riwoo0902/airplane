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
        self.weaponattackspeedeffect = 0
    def checkCollision(self, ragers,damage): #충돌했는지 확인
        for i, arr in enumerate(ragers):            
            if self.rec.colliderect(arr.rec):
                centerx = arr.rec.centerx
                centery = arr.rec.centery
                if self.weapontype == 1:
                    self.weaponattackspeedeffect = 0.8
                elif self.weapontype == 2:
                    self.weaponattackspeedeffect = 2
                else:
                    self.weaponattackspeedeffect = 1
                    
                self.hp -= damage * self.weaponattackspeedeffect - self.defense
                return centerx,centery,i
        return None,None,None

    def draw(self):
        if (self.rec.x) < 1500:  
            self.rec.x += self.speed
            self.screen.blit(self.img, self.rec)
            return False
        else:
            return True