import pygame
import pandas as pd

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Federpendel Animation")

bg_color = (31, 39, 51)
obj_color = (255, 0, 0)

width = 50
x_pos = (SCREEN_WIDTH - width) // 2
y_pos = SCREEN_HEIGHT / 2

clock = pygame.time.Clock()

df = pd.read_csv("results_anim.csv")
counter = 0
started = False

run = True
while run:
    # EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                started = not started

    if started:
        y_pos = SCREEN_HEIGHT / 2 + df['h'][counter] * 20
        if counter < len(df) - 1:
            counter += 1
        else:
            started = False
            counter = 0
    else:
        y_pos = SCREEN_HEIGHT / 2
    
    screen.fill((bg_color))
    # Draw a circle instead of a rectangle
    pygame.draw.circle(screen, obj_color, (x_pos + width // 2, int(y_pos)), width // 2)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()