import pygame as pg
import sys

# Pygame initialisieren
pg.init()

# Fenstergröße
window_width, window_height = 800, 400
screen = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Scrollender Hintergrund")

# Farben
WHITE = (255, 255, 255)

# Hintergrundbild laden
background = pg.image.load("Python/The_adventure_of_Zorugark/source/images/map.png")  # Bild größer als Fenster
bg_width, bg_height = background.get_size()

# Charakter erstellen
char = pg.Surface((50, 50))
char.fill((255, 0, 0))  # Roter Charakter
char_x, char_y = window_width // 2, window_height // 2  # Startposition im Fenster
char_speed = 5

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
    if keys[pg.K_LEFT]:
        char_x -= char_speed
        if char_x < window_width // 2 and bg_offset_x > 0:
            char_x = window_width // 2  # Halte den Charakter in der Mitte
            bg_offset_x -= char_speed  # Scrolle den Hintergrund
    if keys[pg.K_RIGHT]:
        char_x += char_speed
        if char_x > window_width // 2 and bg_offset_x < bg_width - window_width:
            char_x = window_width // 2
            bg_offset_x += char_speed
    if keys[pg.K_UP]:
        char_y -= char_speed
        if char_y < window_height // 2 and bg_offset_y > 0:
            char_y = window_height // 2
            bg_offset_y -= char_speed
    if keys[pg.K_DOWN]:
        char_y += char_speed
        if char_y > window_height // 2 and bg_offset_y < bg_height - window_height:
            char_y = window_height // 2
            bg_offset_y += char_speed

    # Bildschirm aktualisieren
    screen.fill(WHITE)

    # Hintergrund zeichnen (Offset berücksichtigen)
    screen.blit(background, (-bg_offset_x, -bg_offset_y))

    # Charakter zeichnen
    screen.blit(char, (char_x, char_y))

    # Display aktualisieren
    pg.display.flip()
    clock.tick(60)

# Pygame beenden
pg.quit()
sys.exit()
