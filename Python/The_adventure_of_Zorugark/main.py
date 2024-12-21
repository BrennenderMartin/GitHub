import pygame as pg
import params as p
import constants as c 
import variables as v
import functions as f

pg.init()

c.RUN = True
while c.RUN:
    
    #setup (v)
    v.clock.tick(p.FPS)
    v.screen.fill(c.BG)

    #functions (f)
    f.draw()
    f.update()
    
    #v.screen.fill((0, 0, 0))
    
    #event handler
    for event in pg.event.get():
        #QUIT
        if event.type == pg.QUIT:
            c.RUN = False

    pg.display.flip()

pg.quit()
