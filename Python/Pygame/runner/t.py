import constants as c
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
font = pygame.font.Font(None, 36)

text = f"Score: {c.score}\nRate: {c.rate}\nMov: {c.mov}"
lines = text.split('\n')

# Position
line_height = 40

def render_lines(x, y):
    for line in lines:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (x, y))
        y += line_height  # Gehe zur nächsten Zeile

render_lines(50, 50)

pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
