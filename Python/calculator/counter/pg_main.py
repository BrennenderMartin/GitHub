import pygame

pygame.init()

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 400

#define colours
BG = (60, 114, 228)
TEXT_COL = (246, 247, 246)

counter = 0

#define font
font_size = 60
font = pygame.font.SysFont("Futura", font_size)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CC")

turret_original = pygame.image.load("Python/calculator/counter/img/arrow.png").convert_alpha()

sprite_up = pygame.transform.rotate(turret_original, -90)
sprite_up_rect = sprite_up.get_rect(center = (100, 100))

sprite_down = pygame.transform.rotate(turret_original, 90)
sprite_down_rect = sprite_up.get_rect(center = (100, 300))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    img_rect = img.get_rect(center = (x, y))
    screen.blit(img, img_rect)


def count_up(counter):
    # count up
    counter += 1
    draw_text(str(counter), font, TEXT_COL, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    return counter

def count_down(counter):
    #count down
    counter -= 1
    draw_text(str(counter), font, TEXT_COL, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    return counter

run = True
while run:

    screen.fill(BG)
    
    screen.blit(sprite_up, sprite_up_rect)
    screen.blit(sprite_down, sprite_down_rect)
    draw_text(str(counter), font, TEXT_COL, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                counter = count_up(counter)
                print(counter)
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                counter = count_down(counter)
                print(counter)
        
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

pygame.quit()