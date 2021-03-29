""" 
A basic pygame template
"""
 
import pygame, sys

pygame.init()
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
ORANGE   = (255, 128, 0)
DARKGREEN = (0, 153, 0)
PURPLE =  (127, 0, 255)
YELLOW = (255, 255, 0)
LIGHTGREY = (192, 192, 192)
DARKGREY = (100, 100, 100)
 
# Define some fonts
title_font = pygame.font.SysFont('Oswald', 100, True, True)
subtitle_font = pygame.font.SysFont('Oswald', 80, False, True)
menu_font = pygame.font.SysFont('Georgia', 50, False, False)
scene_font = pygame.font.SysFont('Impact', 30, False, False)
text_font = pygame.font.SysFont('Arial', 30, False, False)
text_fonti = pygame.font.SysFont('Arial', 30, False, True)


# Set the width and height of the screen [width, height]
size = (800, 800)
screen = pygame.display.set_mode(size)

def center_text (text, font, color, surface, x, y):
    texts = font.render(text, 1, color)
    textrect = texts.get_rect(center = [x, y])
    surface.blit(texts, textrect)

def draw_text (text, font, color, surface, x, y):
    texts = font.render(text, 1, color)
    textrect = texts.get_rect(topleft = [x, y])
    surface.blit(texts, textrect)

def Rules():
    running = True
    while running:
         screen.fill(PURPLE)
         center_text("How To Play", subtitle_font, RED, screen, 400, 100)
         center_text("Use WASD or Arrow Keys to move your character", text_font, BLACK, screen, 400, 300)
         center_text("Just DODGE", text_fonti, BLACK, screen, 400, 350)
         center_text("If it looks like it can hurt you, it probably will", text_font, BLACK, screen, 400, 400)
         center_text("Press ESC to go back", text_font, BLACK, screen, 400, 750)
         for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
         pygame.display.update()
         clock.tick(30)

pygame.display.set_caption("TerribleGame.exe")
Menu = True
Cutscene = False
Game = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while Menu:
    # --- Main event loop
    click = False
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            pygame.quit() # Flag that we are done so we exit this loop
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
            
    # --- Game logic should go here
 
    # --- Drawing code should go here
     
    # First, clear the screen to white or whatever background colour. 
    # Don't put other drawing commands above this, or they will be erased with this command.
    mx, my = pygame.mouse.get_pos()
    screen.fill(PURPLE)
    play_button = pygame.Rect(300, 450, 200, 100)
    pygame.draw.rect(screen, (LIGHTGREY), play_button)
    help_button = pygame.Rect(300, 600, 200, 100)
    pygame.draw.rect(screen, (LIGHTGREY), help_button)
    if help_button.collidepoint((mx, my)) and click:
        Rules()
    if play_button.collidepoint((mx, my)) and click:
        Cutscene()
        Game = True
        break
    center_text("TerribleGame.exe", title_font, RED, screen, 400, 200)
    center_text("Play", menu_font, BLACK, screen, 400, 500)
    center_text("Rules", menu_font, BLACK, screen, 400, 650)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(30)



# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit() 