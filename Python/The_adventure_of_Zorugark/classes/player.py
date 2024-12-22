import pygame as pg
import params as p
import variables as v
import functions as f


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(f.path(p.path_player)).convert_alpha()
        self.image = pg.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self, keys, bg_offset_x, bg_offset_y):
        x = 0
        y = 0
        if keys[pg.K_a]:
            self.rect.x -= p.player_speed
            if self.rect.x < p.SCREEN_WIDTH // 2 and bg_offset_x > 0:
                self.rect.x = p.SCREEN_WIDTH // 2
                x -= p.player_speed
        
        if keys[pg.K_d]:
            self.rect.x += p.player_speed
            if self.rect.x > p.SCREEN_WIDTH // 2 and bg_offset_x < v.bg_width - p.SCREEN_WIDTH:
                self.rect.x = p.SCREEN_WIDTH // 2
                x += p.player_speed
        
        if keys[pg.K_w]:
            self.rect.y -= p.player_speed
            if self.rect.y < p.SCREEN_HEIGHT // 2 and bg_offset_y > 0:
                self.rect.y = p.SCREEN_HEIGHT // 2
                y -= p.player_speed
        
        if keys[pg.K_s]:
            self.rect.y += p.player_speed
            if self.rect.y > p.SCREEN_HEIGHT // 2 and bg_offset_y < v.bg_height - p.SCREEN_HEIGHT:
                self.rect.y = p.SCREEN_HEIGHT // 2
                y += p.player_speed
        return x, y
