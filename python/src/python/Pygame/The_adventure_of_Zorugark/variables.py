import pygame as pg 
import params as p
import functions as f
from classes import(player as pl, 
                    bullet as b,
                    obstacle as o)

screen = pg.display.set_mode((p.SCREEN_WIDTH, p.SCREEN_HEIGHT))
pg.display.set_caption(p.title)

background_image = pg.image.load(f.path(p.path_bg))
#background_image = pg.transform.scale(background_image, (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
bg_width, bg_height = background_image.get_size()

clock = pg.time.Clock()

player = pl.Player(p.player_x, p.player_y)
#bullet = b.Bullet((200, 300))

group = pg.sprite.Group()

obstacles = pg.sprite.Group()

# Hindernisse platzieren (globale Positionen relativ zum Hintergrund)
obstacle_positions = [(192, 128), (128, 192), (800, 500), (300, 700)]
for pos in obstacle_positions:
    obstacle = o.Obstacle(*pos)
    obstacles.add(obstacle)

group.add(player)