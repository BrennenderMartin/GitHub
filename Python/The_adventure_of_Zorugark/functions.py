import pygame as pg
import params as p
import variables as v

def path(path):
    path = p.root + path + ".png"
    return path

def update():
    v.group.update()

def draw():
    v.group.draw(v.screen)
