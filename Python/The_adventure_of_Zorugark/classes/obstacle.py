import pygame as pg 

# Sprite-Klasse
class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((64, 64))  # Beispiel: Quadratischer Sprite
        self.image.fill((255, 0, 0))  # Rot gefärbt
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Globale Position relativ zum Hintergrund