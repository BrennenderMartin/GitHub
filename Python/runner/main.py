"""This is gonna be the runner Fishi wanted us to finish in Scrath in Python [thums-up Emoji]"""
import constants as c
import variables as v
import soldier as s 
import bullet as b 
import random as r
import pygame as pg

"""Important settings for user"""
background_path = "Python/runner/images/background.png"
player_pos = (c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 4)

screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Fishies Runner")

background_image = pg.image.load(background_path)
background_image = pg.transform.scale(background_image, (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

pg.init()

#objects
soldier = s.Soldier(player_pos)

soldier_group = pg.sprite.Group()
enemy_group = pg.sprite.Group()

soldier_group.add(soldier)

#pg setup
clock = pg.time.Clock()
tick_counter = 0

font = pg.font.Font(None, 20)

def render_lines(x, y):
    c.speed = round(c.speed, 1)
    text= f"Score: {c.score} \nRate: {c.rate} \nSpeed: {c.speed}" #inactive: \nActive: {c.active}
    lines = text.split('\n')
    line_height = 30
    for line in lines:
        text_surface = font.render(line, True, c.BLACK)
        screen.blit(text_surface, (x, y))
        y += line_height  # Gehe zur nächsten Zeile



def create_enemy():
    pos = (r.randint(50, 750), 600)
    enemy = b.Bullet(pos)
    enemy_group.add(enemy)

#main loop
run = True
while run:
    
    clock.tick(c.FPS)
    screen.fill((255, 255, 255))
    
    screen.blit(background_image, (0, 0))
    render_lines(10, 10)
    
    tick_counter += 1
    if tick_counter >= c.rate:
        create_enemy()
        tick_counter = 0
    
    if pg.sprite.spritecollide(soldier, enemy_group, False):
        col = c.BLUE
        if pg.sprite.spritecollide(soldier, enemy_group, False, pg.sprite.collide_mask):
            col = c.RED
            print("Verloren!")
            run = False
    else:
        col = c.GREEN

    enemy_group.update()

    soldier_group.draw(screen)
    enemy_group.draw(screen)

    #pg.draw.rect(screen, c.WHITE, soldier.rect, 1)
    
    key = pg.key.get_pressed()
    if key[pg.K_a] == True:
        soldier.rect.move_ip(-c.speed, 0)
    elif key[pg.K_d] == True:
        soldier.rect.move_ip(c.speed, 0)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    pg.display.flip()

pg.quit()
