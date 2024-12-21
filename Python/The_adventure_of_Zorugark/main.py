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
    
    v.screen.blit(v.background_image, (0, 0))
    
    #functions (f)
    f.draw()
    f.update()
    
    #movement and keypresses
    key = pg.key.get_pressed()
    if key[pg.K_a] == True:
        v.player.rect.move_ip(-p.player_speed, 0)
    if key[pg.K_d] == True:
        v.player.rect.move_ip(p.player_speed, 0)
    if key[pg.K_w] == True:
        v.player.rect.move_ip(0, -p.player_speed)
    if key[pg.K_s] == True:
        v.player.rect.move_ip(0, p.player_speed)
    
    #event handler
    for event in pg.event.get():
        #QUIT
        if event.type == pg.QUIT:
            p.run = False

    pg.display.flip()

pg.quit()
