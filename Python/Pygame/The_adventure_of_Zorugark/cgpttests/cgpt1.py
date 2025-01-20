import pygame as pg
import sys

# Pygame initialisieren
pg.init()

# Fenstergröße
window_width, window_height = 600, 600
screen = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Scrollbarer Hintergrund mit Sprites und Kollision")

# Hintergrundbild laden (größer als Fenster)
background = pg.image.load("Python/The_adventure_of_Zorugark/source/images/map.png").convert_alpha()
bg_width, bg_height = background.get_size()

# Sprite-Klasse
class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((64, 64))  # Beispiel: Quadratischer Sprite
        self.image.fill((255, 0, 0))  # Rot gefärbt
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Globale Position relativ zum Hintergrund

# Charakter-Klasse
class Character(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((40, 40))  # Quadratischer Charakter
        self.image.fill((0, 255, 0))  # Grün gefärbt
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Startposition im Fenster

    def update(self, keys, bg_offset_x, bg_offset_y):
        char_speed = 5
        move_x, move_y = 0, 0
        if keys[pg.K_LEFT]:
            move_x = -char_speed
        if keys[pg.K_RIGHT]:
            move_x = char_speed
        if keys[pg.K_UP]:
            move_y = -char_speed
        if keys[pg.K_DOWN]:
            move_y = char_speed

        # Begrenzung durch den Hintergrund
        new_offset_x = bg_offset_x + move_x
        new_offset_y = bg_offset_y + move_y
        if 0 <= new_offset_x <= bg_width - window_width:
            bg_offset_x = new_offset_x
        if 0 <= new_offset_y <= bg_height - window_height:
            bg_offset_y = new_offset_y

        return bg_offset_x, bg_offset_y

# Sprites erstellen
all_sprites = pg.sprite.Group()
obstacles = pg.sprite.Group()

# Hindernisse platzieren (globale Positionen relativ zum Hintergrund)
obstacle_positions = [(200, 200), (400, 400), (800, 500), (300, 700)]
for pos in obstacle_positions:
    obstacle = Obstacle(*pos)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Charakter-Sprite
character = Character(window_width // 2, window_height // 2)
all_sprites.add(character)

# Hintergrund-Offset (Scroll-Position)
bg_offset_x, bg_offset_y = 0, 0

# Hauptspiel-Schleife
clock = pg.time.Clock()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Tasten abfragen
    keys = pg.key.get_pressed()

    # Charakter-Position (Hintergrund-Offset aktualisieren)
    bg_offset_x, bg_offset_y = character.update(keys, bg_offset_x, bg_offset_y)

    # Bildschirm aktualisieren
    screen.fill((0, 0, 0))  # Schwarzer Hintergrund
    screen.blit(background, (-bg_offset_x, -bg_offset_y))  # Hintergrund scrollen

    # Hindernisse zeichnen (Position relativ zum Scroll-Offset)
    for obstacle in obstacles:
        screen.blit(obstacle.image, (obstacle.rect.x - bg_offset_x, obstacle.rect.y - bg_offset_y))

    # Charakter zeichnen
    screen.blit(character.image, character.rect)

    # Kollision prüfen
    for obstacle in obstacles:
        if character.rect.colliderect(obstacle.rect.move(-bg_offset_x, -bg_offset_y)):
            print("Kollision!")

    # Display aktualisieren
    pg.display.flip()
    clock.tick(60)

# Pygame beenden
pg.quit()
sys.exit()
