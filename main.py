""" 
A basic pygame template
"""
 
import pygame, sys, random

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
LIGHTBLUE = (100 , 200, 255)
 
# Define some fonts
title_font = pygame.font.SysFont('Oswald', 100, True, True)
subtitle_font = pygame.font.SysFont('Oswald', 80, False, True)
menu_font = pygame.font.SysFont('Georgia', 50, False, False)
scene_font_impact = pygame.font.SysFont('Impact', 50, False, False)
scene_font = pygame.font.SysFont('Arial', 50, False, False)
text_font = pygame.font.SysFont('Arial', 30, False, False)
text_fonti = pygame.font.SysFont('Arial', 30, False, True)

youtube = pygame.image.load("Youtube.PNG")
moneyad = pygame.image.load("Free Money.jpg")
moneyad = pygame.transform.scale(moneyad, (282, 124))
cursor = pygame.image.load("cursor.PNG")
cursor.set_colorkey("WHITE")
downloads = pygame.image.load("downloads.PNG")
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

def Cutscene():
    screen = pygame.display.set_mode((956, 512))
    for i in range(255):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        shade = 255-i
        screen.fill((shade, shade, shade))
        center_text("Press SPACE now to skip scene", scene_font_impact, RED, screen, 478, 450)
        pygame.display.update()
        pygame.time.delay(15)
    screen.blit(youtube, (0, 0))
    pygame.display.update()
    pygame.time.delay(2000)
    screen.blit(moneyad, (956-282, 0))
    pygame.display.update()
    pygame.time.delay(2000)
    center_text(":o", scene_font_impact, BLACK, screen, 350, 200)
    pygame.display.update()
    pygame.time.delay(2000)
    screen.blit(youtube, (0, 0))
    screen.blit(moneyad, (956-282, 0))
    center_text("Free money??", scene_font, BLACK, screen, 350, 200)
    pygame.display.update()
    pygame.time.delay(2000)
    screen.blit(youtube, (0, 0))
    screen.blit(moneyad, (956-282, 0))
    center_text("I love free money!", scene_font, BLACK, screen, 350, 200)
    pygame.display.update()
    pygame.time.delay(2000)
    for i in range (31):
        screen.blit(youtube, (0, 0))
        screen.blit(moneyad, (956-282, 0))
        center_text("I love free money!", scene_font, BLACK, screen, 350, 200)
        screen.blit(cursor, (478+10*i, 256-6*i))
        pygame.display.update()
        pygame.time.delay(30)
    pygame.time.delay(500)
    screen.blit(downloads, (0, 0))
    screen.blit(cursor, (778,76))
    pygame.display.update()
    pygame.time.delay(2000)
    screen.blit(cursor, (778, 76))
    center_text("I wonder which one is the real one...", scene_font, BLACK, screen, 478, 400)
    pygame.display.update()
    pygame.time.delay(3000)
    screen.blit(downloads, (0,0))
    center_text("Better click them all just in case!", scene_font, BLACK, screen, 478, 400)
    screen.blit(cursor, (778,76))
    pygame.display.update()
    pygame.time.delay(1500)
    for i in range (100):
        screen.blit(downloads, (0,0))
        center_text("Better click them all just in case!", scene_font, BLACK, screen, 478, 400)
        screen.blit(cursor,(778-2.5*i, 76+0.2*i))
        screen.blit(cursor,(778-0.4*i, 76+2.1*i))
        screen.blit(cursor,(778-5.75*i, 76+1.6*i))
        screen.blit(cursor,(778-0.1*i, 76+3.1*i))
        pygame.display.update()
        pygame.time.delay(5)
    pygame.time.delay(3000)

    



pygame.display.set_caption("TerribleGame.exe")
Menu = True 
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
        screen = pygame.display.set_mode((800, 800))
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