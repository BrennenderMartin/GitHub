import pygame as pg
import params as p
import variables as v
import functions as f

pg.init()

p.run = True
while p.run:
    
    #setup (v)
    v.clock.tick(p.FPS)
    v.screen.fill(p.BG)
    
    pressed = False
    if pg.KEYDOWN:
        pressed = True
    elif pg.KEYUP:
        pressed = False
    
    # Tasten abfragen
    keys = pg.key.get_pressed()
    scroll_x, scroll_y = v.player.update(keys, p.bg_offset_x, p.bg_offset_y)

    # Hintergrund-Offset aktualisieren
    p.bg_offset_x += scroll_x
    p.bg_offset_y += scroll_y
    
    v.screen.blit(v.background_image, (-p.bg_offset_x, -p.bg_offset_y))
    
    #pg.draw.circle(v.screen, p.BLACK, (0, 0), 320)
    
    for obstacle in v.obstacles:
        v.screen.blit(obstacle.image, (obstacle.rect.x - p.bg_offset_x, obstacle.rect.y - p.bg_offset_y))
        """
        if v.player.rect.colliderect(obstacle.rect.move(-p.bg_offset_x, -p.bg_offset_y)) and pressed:
            print("Moving Kollision!")
        elif v.player.rect.colliderect(obstacle.rect.move(-p.bg_offset_x, -p.bg_offset_y)):
            print("Kollision!")"""
    
    if pg.sprite.spritecollide(v.player, v.obstacles, False) and pressed:
        print("Moving Kollision!")
    elif pg.sprite.spritecollide(v.player, v.obstacles, False):
        print("Kollision!")
    
    
    #functions (f)
    f.draw()
    #f.update()
    
    #event handler
    for event in pg.event.get():
        #QUIT
        if event.type == pg.QUIT:
            p.run = False

    pg.display.flip()

pg.quit()
