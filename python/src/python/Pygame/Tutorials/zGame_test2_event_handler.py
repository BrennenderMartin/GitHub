import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            print("Key has been pressed")
        
        if event.type == pygame.KEYUP:
            print("Key has been released")
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Click")
        
        if event.type == pygame.MOUSEBUTTONUP:
            print("Release")
        
        if event.type == pygame.MOUSEMOTION:
            print("Mouse is moving")
    
pygame.quit()