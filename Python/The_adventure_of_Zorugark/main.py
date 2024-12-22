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
    
    
    # Tasten abfragen
    keys = pg.key.get_pressed()
    scroll_x, scroll_y = v.player.update(keys, p.bg_offset_x, p.bg_offset_y)

    # Hintergrund-Offset aktualisieren
    p.bg_offset_x += scroll_x
    p.bg_offset_y += scroll_y
    
    v.screen.blit(v.background_image, (-p.bg_offset_x, -p.bg_offset_y))
    
    pg.draw.circle(v.screen, p.BLACK, (0, 0), 320)
    
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
