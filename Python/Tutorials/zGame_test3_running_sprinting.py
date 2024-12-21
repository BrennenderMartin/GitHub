import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
'''
running = False
sprinting = False
'''
run = True
while run:

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True and key[pygame.K_LSHIFT] == True:
        print("Sprinting")
    elif key[pygame.K_a] == True:
        print("Running")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                running = True
            if event.key == pygame.K_LSHIFT:
                sprinting = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                running = False
            if event.key == pygame.K_LSHIFT:
                sprinting = False
        '''
        
    '''
    if sprinting == True and running == True:
        print("Sprinting")
    elif running == True:
        print("Running")
    '''
        
    
pygame.quit()