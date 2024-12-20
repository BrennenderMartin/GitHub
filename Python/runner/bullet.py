"""Bullet / Obstacle class,  so it isnt all bunched into one file"""
import constants as c
import pygame as pg

#create bullet class
class Bullet(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Python/runner/images/zombie_stand.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        self.rect.y -= c.speed
        
        if c.score % 10 == 0 and c.score != 0 and c.rate > 10 and c.active is True:
            c.rate -= 10
            c.active = False
        elif c.score % 10 == 1:
            c.active = True
        
        check = True
        if c.score >= 150 and check is True:
            c.speed = 50
            check = False
        
        if self.rect.y <= 0:
            c.score += 1
            c.speed += 0.1
            
            print(f"Dein Score ist: {c.score}")
            self.kill()
