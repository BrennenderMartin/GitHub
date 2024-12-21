import pygame as pg 
import params as p
import constants as c
from classes import(player as pl, 
                    bullet as b)

screen = pg.display.set_mode((p.screen_width, p.screen_height))
pg.display.set_caption(p.title)

clock = pg.time.Clock()

player = pl.Player((100, 200))
bullet = b.Bullet((100, 400))

group = pg.sprite.Group()

group.add(player, bullet)