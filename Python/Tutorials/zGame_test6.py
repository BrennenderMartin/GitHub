import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
x = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working with Shapes")

run = True
while run:

    screen.fill((255, 255, 255))

    if pygame.mouse.get_pressed()[0] == True:
        x += 0.001
    elif pygame.mouse.get_pressed()[2] == True:
        x -= 0.001
    
    pos = pygame.mouse.get_pos()

    pygame.draw.rect(screen, (255, 0, 0), (200, 100, 150, 150), width=5, border_bottom_right_radius=50, border_top_left_radius=25)
    pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)
    pygame.draw.circle(screen, (255, 255, 0), (300, 200), 75, draw_top_right=True, draw_bottom_left=True)
    pygame.draw.ellipse(screen, (0, 0, 255), (200, 150, 150, 75))
    pygame.draw.arc(screen, (0, 255, 255), (200, 100, 150, 150), 0, x, width=5)
    pygame.draw.line(screen, (255, 0, 255), (300, 200), pos)
    pygame.draw.polygon(screen, (100, 100, 100), ((100, 200), (200, 300), (500, 100), (200, 250)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()