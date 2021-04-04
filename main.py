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
select_font = pygame.font.SysFont('Arial', 20, False, False)
select_fonti = pygame.font.SysFont('Arial', 20, False, True)

# Define the images used in the cutscene
youtube = pygame.image.load("Youtube.PNG")
moneyad = pygame.image.load("Free Money.jpg")
moneyad = pygame.transform.scale(moneyad, (282, 124))
cursor = pygame.image.load("cursor.PNG")
cursor.set_colorkey(RED)
downloads = pygame.image.load("downloads.PNG")

# Define the logos used in the select screen
wlogo = pygame.image.load("wlogo.png")
mlogo = pygame.image.load("mlogo.png")
llogo = pygame.image.load("llogo.png")
wlogo.set_colorkey(WHITE)
mlogo.set_colorkey(WHITE)
llogo.set_colorkey((255, 0, 0))

# Define the images used in the actual game
background0 = pygame.image.load("windows.png")
background1 = pygame.image.load("mac.jpg")
background2 = pygame.image.load("linux.png")

virus0 = pygame.image.load("Virus.png")
virus1 = pygame.image.load("Angry.png")
virus2 = pygame.image.load("Angrier.png")
virus3 = pygame.image.load("VeryAngry.png")
virus0.set_colorkey(WHITE)
virus1.set_colorkey(WHITE)
virus2.set_colorkey(WHITE)
virus3.set_colorkey(WHITE)

wantivirus = pygame.image.load("wantivirus.png")
wantivirus.set_colorkey(WHITE)

light_bullet = pygame.image.load("green_bullet.png")
light_bullet.set_colorkey(RED)
ball_bullet = pygame.image.load("ball_bullet.png")
ball_bullet.set_colorkey(WHITE)


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

def Select():
    running = True
    wlogo_rect = wlogo.get_rect(center = (150, 400))
    mlogo_rect = mlogo.get_rect(center = (478, 400))
    llogo_rect = llogo.get_rect(center = (806, 400))
    while running:
         click = False
         screen.fill(PURPLE) #956, 512
         center_text("Choose your Operating System", subtitle_font, RED, screen, 478, 30)
         center_text("Windows", menu_font, BLACK, screen, 150, 100)
         center_text("Mac", menu_font, BLACK, screen, 478, 100)
         center_text("Linux", menu_font, BLACK, screen, 806, 100)
         center_text("The most popular OS", select_font, BLACK, screen, 150, 150)
         center_text("Over 83% of all computer viruses", select_font, BLACK, screen, 150, 180)
         center_text("are targeted at Windows computers.", select_font, BLACK, screen, 150, 210)
         center_text("1 Life", select_fonti, BLACK, screen, 150, 270)
         center_text("Default", select_fonti, BLACK, screen, 150, 300)
         center_text("Only 5-10% of computers run Mac OS", select_font, BLACK, screen, 478, 150)
         center_text("As such, Mac computers are not an", select_font, BLACK, screen, 478, 180)
         center_text("appealing target for most viruses.", select_font, BLACK, screen, 478, 210)
         center_text("3 Lives", select_fonti, BLACK, screen, 478, 270)
         center_text("Easy Mode", select_fonti, BLACK, screen, 478, 300)
         center_text("Less than 2% of computer use Linux", select_font, BLACK, screen, 806, 150)
         center_text("In addition, this open source OS", select_font, BLACK, screen, 806, 180)
         center_text("is constantly changing and can be", select_font, BLACK, screen, 806, 210)
         center_text("customized easily.", select_font, BLACK, screen, 806, 240)
         center_text("As many lives as you need", select_fonti, BLACK, screen, 806, 270)
         center_text("Practice Mode", select_fonti, BLACK, screen, 806, 300)
         screen.blit(wlogo, wlogo_rect)
         screen.blit(mlogo, mlogo_rect)
         screen.blit(llogo, llogo_rect)
         for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                  click = True
         mx, my = pygame.mouse.get_pos()
         if wlogo_rect.collidepoint(mx, my) and click == True:
             return 0
         elif mlogo_rect.collidepoint(mx, my) and click == True:
             return 1
         elif llogo_rect.collidepoint(mx, my) and click == True:
             return 2
         pygame.display.update()
         clock.tick(30)


pygame.display.set_caption("TerribleGame.exe")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while True:
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
        screen = pygame.display.set_mode((956, 512))
        OS = Select()
        Cutscene()
        screen = pygame.display.set_mode((800, 800))
        break
    center_text("TerribleGame.exe", title_font, RED, screen, 400, 200)
    center_text("Play", menu_font, BLACK, screen, 400, 500)
    center_text("Rules", menu_font, BLACK, screen, 400, 650)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(30)

# Assign some variables that are needed in the game
virus = virus0
virusHP = 1000
virus_x = 400
virus_y = 200
virus_x_move = 10
virus_y_move = 2

player_x = 400
player_y = 600
player_x_speed = 5
player_y_speed = 5
player_x_move = 0
player_y_move = 0
player_rect = pygame.Rect(0, 0, 20, 20)

if OS == 0:
    background = background0
    playerHP = 1

# Function for virus movement
def virus_move(virus, x, y, xmove, ymove):
    x += xmove
    y += ymove
    if x > 760 or x < 40:
        xmove *= -1
    if y < 40 or y > 360:
        ymove *= -1
    return virus.get_rect(center = (x, y)), x, y, xmove, ymove
    
class light_bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, dest_x, dest_y):
        super().__init__()
        self.image = light_bullet.convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movex = ((dest_x-x)/30)
        self.movey = ((dest_y-y)/30)
    def update(self):
        self.rect.x += self.movex
        self.rect.y += self.movey

bullet_list = pygame.sprite.Group()

while(True):
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player_x_move -= player_x_speed
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player_x_move += player_x_speed
            if event.key == pygame.K_UP or event.key == ord('w'):
                player_y_move -= player_y_speed
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player_y_move += player_y_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
               player_x_move += player_x_speed
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
               player_x_move -= player_x_speed
            if event.key == pygame.K_UP or event.key == ord('w'):
               player_y_move += player_y_speed
            if event.key == pygame.K_DOWN or event.key == ord('s'):
               player_y_move -= player_y_speed
    player_x += player_x_move
    player_y += player_y_move
    virus_rect, virus_x, virus_y, virus_x_move, virus_y_move = virus_move(virus, virus_x, virus_y, virus_x_move, virus_y_move)
    pygame.draw.line(screen, ORANGE, (0, 400), (800, 400), 2)
    player_rect.center = (player_x, player_y)
    pygame.draw.rect(screen, RED, player_rect)
    screen.blit(virus, virus_rect)

    if pygame.time.get_ticks()%2 == 0:
        bullet = light_bullets(virus_x, virus_y, player_x, player_y)
        bullet_list.add(bullet)

    bullet_list.update()
    bullet_list.draw(screen)

    pygame.display.update()
    clock.tick(30)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit() 