"""Soldier / Player class, so it isnt all bunched into one file"""
import pygame as pg

#create soldier class
class Soldier(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Python/runner/images/adventurer_stand.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.mask = pg.mask.from_surface(self.image)
