import pygame as pg
import params as p
import variables as v
import functions as f


class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(f.path(p.path_player)).convert_alpha()
        self.image = pg.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.mask = pg.mask.from_surface(self.image)
