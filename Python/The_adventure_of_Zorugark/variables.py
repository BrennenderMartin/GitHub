import pygame as pg 
import params as p
import functions as f
from classes import(player as pl, 
                    bullet as b)

screen = pg.display.set_mode((p.screen_width, p.screen_height))
pg.display.set_caption(p.title)

background_image = pg.image.load(f.path(p.path_bg))
#background_image = pg.transform.scale(background_image, (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

clock = pg.time.Clock()

player = pl.Player(p.player_spawn)
bullet = b.Bullet((200, 300))

group = pg.sprite.Group()

group.add(player, bullet)