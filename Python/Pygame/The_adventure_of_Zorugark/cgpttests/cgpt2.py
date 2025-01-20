import pygame as pg
import sys

# Pygame initialisieren
pg.init()

# Fenstergröße
window_width, window_height = 600, 600
screen = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Scrollbarer Hintergrund mit Hindernissen")

# Hintergrundbild (größer als das Fenster)
background = pg.Surface((1200, 1200))  # Beispiel: 1200x1200 Hintergrund
background.fill((100, 100, 255))  # Blau gefärbt
bg_width, bg_height = background.get_size()

# Obstacle-Klasse
class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y, width=50, height=50):
        super().__init__()
        self.image = pg.Surface((width, height))  # Hindernisgröße
        self.image.fill((255, 0, 0))  # Rot gefärbt
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Globale Position relativ zum Hintergrund

# Charakter-Klasse
class Character(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((40, 40))  # Charaktergröße
        self.image.fill((0, 255, 0))  # Grün gefärbt
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Startposition im Fenster

    def update(self, keys, bg_offset_x, bg_offset_y, obstacles):
        char_speed = 5
        x, y = bg_offset_x, bg_offset_y  # Startwerte der Offsets

        # Tasten abfragen
        if keys[pg.K_LEFT]:
            x -= char_speed
        if keys[pg.K_RIGHT]:
            x += char_speed
        if keys[pg.K_UP]:
            y -= char_speed
        if keys[pg.K_DOWN]:
            y += char_speed

        # Kollisionserkennung
        for obstacle in obstacles:
            obstacle_rect = obstacle.rect.move(-x, -y)
            if self.rect.colliderect(obstacle_rect):
                # Bewegung blockieren
                if keys[pg.K_LEFT]:
                    x = bg_offset_x
                if keys[pg.K_RIGHT]:
                    x = bg_offset_x
                if keys[pg.K_UP]:
                    y = bg_offset_y
                if keys[pg.K_DOWN]:
                    y = bg_offset_y

        # Hintergrund-Offsets aktualisieren
        return x, y


# Gruppen erstellen
all_sprites = pg.sprite.Group()
obstacles = pg.sprite.Group()

# Hindernisse erstellen
obstacle_positions = [(200, 200), (400, 400), (800, 500), (300, 700)]
for pos in obstacle_positions:
    obstacle = Obstacle(*pos)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Charakter erstellen
character = Character(window_width // 2, window_height // 2)
all_sprites.add(character)

# Hintergrund-Offsets
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

    # Charakter-Update
    bg_offset_x, bg_offset_y = character.update(keys, bg_offset_x, bg_offset_y, obstacles)

    # Hintergrund zeichnen
    screen.blit(background, (-bg_offset_x, -bg_offset_y))

    # Hindernisse zeichnen
    for obstacle in obstacles:
        screen.blit(obstacle.image, (obstacle.rect.x - bg_offset_x, obstacle.rect.y - bg_offset_y))

    # Charakter zeichnen
    screen.blit(character.image, character.rect)

    # Display aktualisieren
    pg.display.flip()
    clock.tick(60)

# Pygame beenden
pg.quit()
sys.exit()
