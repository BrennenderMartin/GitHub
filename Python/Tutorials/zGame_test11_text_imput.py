import pygame

pygame.init()

#define screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text Input")

#define colours
BG = (60, 114, 228)
TEXT_COL = (246, 247, 246)

#define font
font_size = 60
font = pygame.font.SysFont("Futura", font_size)

#create empty string
text = [""]

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  width = img.get_width()
  screen.blit(img, (x - (width / 2), y))

#game loop
run = True
while run:

  #update background
  screen.fill(BG)

  #display typed input
  for row, line in enumerate(text):
    draw_text(line, font, TEXT_COL, SCREEN_WIDTH / 2, 200 + (row * font_size))

  #event handler
  for event in pygame.event.get():
    #handle text input
    if event.type == pygame.TEXTINPUT:
      text[-1] += event.text

    #handle special keys
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_BACKSPACE:
        text[-1] = text[-1][:-1]
        if len(text[-1]) == 0:
          if len(text) > 1:
            text = text[:-1]
      elif event.key == pygame.K_RETURN:
        text.append("")

    #quit program
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()