import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#clicked = False

run = True
while run:
    '''
    if pygame.mouse.get_pressed()[0] == True:
        print("Left mouse clicked")
    if pygame.mouse.get_pressed()[2] == True:
        print("Right mouse clicked")
    '''
    pos = pygame.mouse.get_pos()
    print(pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
    
    if clicked == True:
        print(clicked)
    '''

pygame.quit()