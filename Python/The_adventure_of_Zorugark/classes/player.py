import pygame as pg
import params as p
import constants as c 
import variables as v
import functions as f


class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(p.path + "adventurer_stand.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.mask = pg.mask.from_surface(self.image)