""" 
A basic pygame template
"""
 
import pygame, sys, random, math

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

advirusi = pygame.image.load("Adware.png")
advirusi.set_colorkey(WHITE)
ranvirusi = pygame.image.load("Ransomware.png")
ranvirusi.set_colorkey(WHITE)
trovirusi = pygame.image.load("trojan.png")
trovirusi.set_colorkey(WHITE)
wormvirusi = pygame.image.load("Worm.png")
wormvirusi.set_colorkey(WHITE)
rootvirusi = pygame.image.load("Rootkit.png")
rootvirusi.set_colorkey(WHITE)

player_square = pygame.image.load("Player.png")

wantivirus = pygame.image.load("wantivirus.png")
wantivirus.set_colorkey(WHITE)
mantivirus = pygame.image.load("mantivirus.png")
mantivirus.set_colorkey(WHITE)
lantivirus = mantivirus

light_bullet = pygame.image.load("green_bullet.png")
light_bullet.set_colorkey(RED)
ball_bullet = pygame.image.load("ball_bullet.png")
ball_bullet.set_colorkey(WHITE)
binary_block = pygame.image.load("binary.jpg")
beyblade = pygame.image.load("beyblade.png")
beyblade.set_colorkey(WHITE)

error = pygame.image.load("Error Message.png")
wcrash = pygame.image.load("Windowscrash.png")
mcrash = pygame.image.load("Maccrash.jpg")


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
         center_text("Use WASD OR Arrow Keys to move your character", text_font, BLACK, screen, 400, 300)
         center_text("Please don't use both or bad thing will happen", text_font, BLACK, screen, 400, 340)
         center_text("Shoot by pressing or holding SPACE", text_font, BLACK, screen, 400, 380)
         center_text("The Red Square is your hitbox", text_font, BLACK, screen, 400, 420)
         center_text("Just DODGE", text_fonti, BLACK, screen, 400, 500)
         center_text("If it looks like it can hurt you, it probably will", text_font, BLACK, screen, 400, 540)
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
         center_text("5 Lives", select_fonti, BLACK, screen, 150, 270)
         center_text("Hard Mode", select_fonti, BLACK, screen, 150, 300)
         center_text("Only 5-10% of computers run Mac OS", select_font, BLACK, screen, 478, 150)
         center_text("As such, Mac computers are not an", select_font, BLACK, screen, 478, 180)
         center_text("appealing target for most viruses.", select_font, BLACK, screen, 478, 210)
         center_text("9 Lives, Less Enemies", select_fonti, BLACK, screen, 478, 270)
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
virus_HP = 800
virus_x = 400
virus_y = 200
virus_x_move = 4
virus_y_move = 0

player_x = 400
player_y = 600
player_x_speed = 8
player_y_speed = 8
player_x_move = 0
player_y_move = 0
player_rect = pygame.Rect(0, 0, 20, 20)

if OS == 0:
    background = background0
    playerHP = 5
    antivirus = wantivirus
    crash = wcrash
    enemy_mult = 1
if OS == 1:
    background = background1
    playerHP = 9
    antivirus = mantivirus
    crash = mcrash
    enemy_mult = 0.8
if OS == 2:
    background = background2
    playerHP = 9999
    antivirus = lantivirus
    enemy_mult = 1

# Function for virus movement
def virus_move(virus, x, y, xmove, ymove):
    x += xmove
    y += ymove
    if x > 760 or x < 40:
        xmove *= -1
    if y < 40 or y > 360:
        ymove *= -1
    return virus.get_rect(center = (x, y)), x, y, xmove, ymove

# Function that bullets use to move toward player
def Move(t0,t1,psx,psy,speed):
    global mx
    global my

    speed = speed

    distance = [t0 - psx+10, t1 - psy+10]
    norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
    direction = [distance[0] / norm, distance[1 ] / norm]

    bullet_vector = [direction[0] * speed, direction[1] * speed]
    return bullet_vector

# Function to make changing the virus's speed easier
def change_virus_speed(xspeed, yspeed, incrementx, incrementy):
    if xspeed >= 0:
        xspeed += incrementx
    if xspeed < 0:
        xspeed -= incrementx
    if yspeed >= 0:
        yspeed += incrementy
    if yspeed < 0:
        yspeed -= incrementy
    return xspeed, yspeed

# Game Over Function
def Game_Over():
    for i in range (50):
        screen.blit(error, (random.randint(-100, 700), random.randint(-50, 750)))
        pygame.display.update()
        pygame.time.delay(50)
    screen.blit(crash, (0,0))
    pygame.display.update()
    pygame.time.delay(2000)

# Victoy Funciton
def Victory():
    screen.blit(background, (0, 0))
    center_text("YOU DID IT!", title_font, WHITE, screen, 400, 400)
    pygame.display.update()
    pygame.time.delay(2500)
    screen.blit(background, (0, 0))
    center_text("now go away :c", menu_font, WHITE, screen, 400, 400)
    pygame.display.update()
    pygame.time.delay(1000)
    

# The sprite class for the light green bullets
class light_bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, dest_x, dest_y):
        super().__init__()
        self.image = light_bullet.convert()
        self.rect = self.image.get_rect()
        self.rect.width = self.rect.width -3
        self.rect.height = self.rect.height -6
        self.rect.center = (x, y)
        self.bullet_vector = Move(dest_x, dest_y, x, y, 15)
    def update(self):
        self.rect.centerx += self.bullet_vector[0]
        self.rect.centery += self.bullet_vector[1]

# Sprite class for the beyblade bullet
class beyblade_bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dest_x, dest_y, bounces, size, speed):
        super().__init__()
        self.original = size.convert()
        self.image = self.original
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.angle = 0
        self.bounces = bounces
        self.mask = pygame.mask.from_surface(self.original)
        self.bullet_vector = Move(dest_x, dest_y, x, y, speed)
    def update(self):
        self.angle -= 30
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.rect = self.image.get_rect(center = (self.rect.centerx+self.bullet_vector[0], self.rect.centery+self.bullet_vector[1]))
        if self.bounces > 0:
            if self.rect.centerx < 0 or self.rect.centerx > 800:
                self.bullet_vector[0]*=-1
                self.bounces-=1
            if self.rect.centery < 0 or self.rect.centery > 800:
                self.bullet_vector[1]*=-1
                self.bounces-=1
            

# The sprite class for the player's bullets
class player_bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 4, 20)
        self.rect.center = (x, y-20)
    def update(self):
        self.rect.centery -= 30

class advirus(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = advirusi.convert()
            self.rect = self.image.get_rect(center = (x, y))
            self.HP = 3
        def isAlive(self):
            if self.HP <= 0:
                self.kill()
        def update(self):
            pass

class ranvirus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = ranvirusi.convert()
        self.rect = self.image.get_rect(center = (x, y))
        self.HP = 3
        self.shoot_time = 2000
    def isAlive(self):
        if self.HP <= 0:
            self.kill()
    def update(self, player_x, player_y, dt):
        self.shoot(player_x, player_y, dt)
    def shoot(self, player_x, player_y, dt):
        self.shoot_time -= dt
        if(self.shoot_time <= 0):
            light = light_bullets(self.rect.centerx, self.rect.centery, player_x, player_y)
            bullet_list.add(light)
            self.shoot_time = 2000
            self.rect.centery += 3

class trovirus(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = trovirusi.convert()
        self.rect = self.image.get_rect(center = (x, 50))
        self.ymove = 1
        self.HP = 3
        self.shoot_time = 1500
    def isAlive(self):
        if self.HP <= 0 or self.rect.centery == 400:
            self.kill()
    def update(self, dt):
        self.shoot(dt)
        self.rect.centery += self.ymove
        if(self.rect.centery == 80):
            self.rect.centery = 800
            self.ymove = -1
    def shoot(self, dt):
        self.shoot_time -= dt
        if(self.shoot_time <= 0):
            light = light_bullets(self.rect.centerx, self.rect.centery, 0, self.rect.centery)
            bullet_list.add(light)
            light = light_bullets(self.rect.centerx, self.rect.centery, 800, self.rect.centery)
            bullet_list.add(light)
            self.shoot_time = 1500

def correct_speed(player_x_speed, player_y_speed):
     key = pygame.key.get_pressed()
     player_x_move = 0
     player_y_move = 0
     if key[pygame.K_w] or key[pygame.K_UP]:
        player_y_move -= player_y_speed
     if key[pygame.K_s] or key[pygame.K_DOWN]:
        player_y_move += player_y_speed
     if key[pygame.K_a] or key[pygame.K_LEFT]:
        player_x_move -= player_x_speed
     if key[pygame.K_d] or key[pygame.K_RIGHT]:
        player_x_move += player_x_speed
     return player_x_move, player_y_move
def AdHelp():
    running = True
    while running:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                  running = False
        screen.blit(background, (0, 0))
        screen.blit(advirusi, (380, 500))
        center_text("Adware", menu_font, WHITE, screen, 400, 200)
        center_text("Responsible for spamming users with", text_font, WHITE, screen, 400, 250)
        center_text("personalized ads to generate revenue", text_font, WHITE, screen, 400, 280)
        center_text("Doesn't actually hurt you, it's just really annoying", text_fonti, WHITE, screen, 400, 450)
        center_text("Press F to continue", menu_font, WHITE, screen, 400, 650)
        pygame.display.update()

def RanHelp():
    running = True
    while running:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                  running = False
        screen.blit(background, (0, 0))
        screen.blit(ranvirusi, (380, 500))
        center_text("Ransomware", menu_font, WHITE, screen, 400, 200)
        center_text("Steals your files or otherwise tricks", text_font, WHITE, screen, 400, 250)
        center_text("the user into paying ransom money to", text_font, WHITE, screen, 400, 280)
        center_text("resolve an issue or get their files back", text_font, WHITE, screen, 400, 310)
        center_text("(which almost never happens)", text_font, WHITE, screen, 400, 340)
        center_text("One of the most effective and common viruses", text_fonti, WHITE, screen, 400, 450)
        center_text("Press F to continue", menu_font, WHITE, screen, 400, 650)
        pygame.display.update()

def TroHelp():
    running = True
    while running:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                  running = False
        screen.blit(background, (0, 0))
        screen.blit(trovirusi, (380, 500))
        center_text("Trojan Virus", menu_font, WHITE, screen, 400, 200)
        center_text("Disguises itself as another program", text_font, WHITE, screen, 400, 250)
        center_text("to trick users into letting them in", text_font, WHITE, screen, 400, 280)
        center_text("Named after the Trojan Horse", text_font, WHITE, screen, 400, 310)

        center_text("How'd this get behind me?", text_fonti, WHITE, screen, 400, 450)
        center_text("Press F to continue", menu_font, WHITE, screen, 400, 650)
        pygame.display.update()

bullet_list = pygame.sprite.Group()
beyblade_list = pygame.sprite.Group()
player_bullet_list = pygame.sprite.Group()
enemies_list = pygame.sprite.Group()
virus_light_time = 0
virus_binary_time = 0
player_mask = pygame.mask.from_surface(player_square)
dt = 0
virus_spasm = 0
cooldown = 500
player_immune = 0
AdSpawn = False
RanSpawn = False
TroSpawn = False
WormSpawn = False
RootSpawn = False
AdFirst = True
RanFirst = True
TroFirst = True
WormFirst = True
RootFirst = True
AdTimer = 0
RanTimer = 0
TroTimer = 0
WormTimer = 0
RootTimer = 0
AdList = pygame.sprite.Group()
RanList = pygame.sprite.Group()
TroList = pygame.sprite.Group()
WormList = pygame.sprite.Group()
RootList = pygame.sprite.Group()

player_x_move, player_y_move = correct_speed(player_x_speed, player_y_speed)
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
    
    # Draws the barrier 
    pygame.draw.line(screen, ORANGE, (0, 400), (800, 400), 2)
    cooldown -= dt
    keys = pygame.key.get_pressed()
    
    # Player Shooting
    if keys[pygame.K_SPACE] and cooldown <= 0:
        bullet = player_bullet(player_x, player_y)
        player_bullet_list.add(bullet)
        cooldown = 250

    # Makes sure that the movement cannot go past the move speed (due to pressing both arrows and wasd at the same time)
    if player_x_move > player_x_speed:
        player_x_move = player_x_speed
    if player_x_move < -1*player_x_speed:
        player_x_move = -1*player_x_speed
    if player_y_move > player_y_speed:
        player_y_move = player_y_speed
    if player_y_move < -1*player_y_speed:
        player_y_move = -1*player_y_speed

    player_x += player_x_move
    player_y += player_y_move
    if player_x < 0:
        player_x = 0
    if player_x > 800:
        player_x = 800
    if player_y > 790:
        player_y = 790
    if player_y < 410:
        player_y = 410

    if virus_HP == 600 and virus == virus0:
        virus_x_move, virus_y_move = change_virus_speed(virus_x_move, virus_y_move, 6, 0)
        virus = virus1
    if virus_HP == 700 and AdSpawn == False:
        AdSpawn = True
        AdTimer = random.randint(1000, 2000)
    if virus_HP == 550 and RanSpawn == False:
        RanSpawn = True
        RanTimer = random.randint(1000, 2000)
    if virus_HP == 400 and virus == virus1:
        virus_x_move, virus_y_move = change_virus_speed(virus_x_move, virus_y_move, 2, 1)
        virus_binary_time = 0
        virus = virus2
        beybladebul = beyblade_bullet(virus_x, virus_y, player_x, player_y, 999, beyblade, 10)
        beyblade_list.add(beybladebul)
        WormSpawn = True
        WormTimer = random.randint(3000, 5000)
    if virus_HP == 300 and TroSpawn == False:
        TroSpawn = True
        TroTimer = random.randint(1000, 2000)
    if virus_HP == 100 and virus == virus2:
        RootSpawn = True
        RootTimer = random.randint(2000, 3000)
        virus = virus3
        virus_x_move, virus_y_move = change_virus_speed(virus_x_move, virus_y_move, 0, 1)
        virus_spasm = 2
        beybladebul = beyblade_bullet(virus_x, virus_y, player_x-100, player_y, 999, beyblade, 10)
        beyblade_list.add(beybladebul)
        beybladebul = beyblade_bullet(virus_x, virus_y, player_x+100, player_y, 999, beyblade, 10)
        beyblade_list.add(beybladebul)

    AdTimer -= (dt*enemy_mult)
    RanTimer -= (dt*enemy_mult)
    TroTimer -= (dt*enemy_mult)
    WormTimer -= (dt*enemy_mult)
    RootTimer -= (dt*enemy_mult)
    #Create smaller enemies
    if AdSpawn == True and AdTimer <= 0 and len(AdList.sprites())<5:
        if(AdFirst == True):
            AdHelp()
            AdFirst = False
            player_x_move, player_y_move = correct_speed(player_x_speed, player_y_speed)
        adware = advirus(random.randint(20, 780), random.randint(360, 400))
        enemies_list.add(adware)
        AdList.add(adware)
        adware = advirus(random.randint(20, 780), random.randint(360, 400))
        enemies_list.add(adware)
        AdList.add(adware)
        adware = advirus(random.randint(20, 780), random.randint(360, 400))
        enemies_list.add(adware)
        AdList.add(adware)
        AdTimer = random.randint(20000, 25000)
    
    if RanSpawn == True and RanTimer <=0 and len(RanList.sprites())<3:
        if(RanFirst == True):
            RanHelp()
            RanFirst = False
            player_x_move, player_y_move = correct_speed(player_x_speed, player_y_speed)
        ranware = ranvirus(random.randint(20, 780), 40)
        enemies_list.add(ranware)
        RanList.add(ranware)
        RanTimer = random.randint(10000, 15000)
    
    if TroSpawn == True and TroTimer <=0 and len(TroList.sprites())<1:
        if(TroFirst == True):
            TroHelp()
            TroFirst = False
            player_x_move, player_y_move = correct_speed(player_x_speed, player_y_speed)
        troware = trovirus(random.randint(40, 760))
        enemies_list.add(troware)
        TroList.add(troware)
        TroTimer = random.randint(15000, 20000)
    


    # Assign player, antivirus, and virus locations
    player_rect.center = (player_x, player_y)
    antivirus_rect = antivirus.get_rect(center = (player_x, player_y))
    virus_rect, virus_x, virus_y, virus_x_move, virus_y_move = virus_move(virus, virus_x, virus_y, virus_x_move, virus_y_move)
    
    # Draws antivirus first so that it doesn't overlap anything
    screen.blit(antivirus, antivirus_rect)

    # All the sub-enemies make their movements
    RanList.update(player_x, player_y, dt)
    TroList.update(dt)

    # Tick down all the timers for the enemies' shooting
    virus_light_time += dt
    virus_binary_time += dt
    #Checks what stage virus is in and make it use attacks accordingly
    if virus == virus0:
        if virus_light_time >= 1000:
            bullet = light_bullets(virus_x, virus_y, player_x, player_y)
            bullet_list.add(bullet)
            virus_light_time = 0
    
    
    if virus != virus0:
        if virus == virus3 and virus_spasm <=0 and virus_light_time >= 1000:
            temp_y_move = virus_y_move
            virus_x_move, virus_y_move = change_virus_speed(virus_x_move, virus_y_move, 50, -2)
            virus_spasm = 3
        if virus_light_time >= 1000 and virus_light_time <= 1400:
         bullet = light_bullets(virus_x, virus_y, player_x, player_y)
         bullet_list.add(bullet)
        if virus_light_time > 1400:
            if virus_spasm == 3:
                virus_x_move, virus_y_move = change_virus_speed(virus_x_move, virus_y_move, -50, 2)
                virus_y_move = temp_y_move
            if virus_x <= 0:
                virus_x = 50
            elif virus_x >=800:
                virus_x = 750
            virus_light_time = 0
            virus_spasm-=1 
    
    if virus == virus2:
        if virus_binary_time >= 3000 and virus_binary_time <= 4000:
            pygame.draw.rect(screen, YELLOW, (virus_rect.x, virus_rect.y+50, 80, 800), 2)
        if virus_binary_time >4000 and virus_binary_time <= 5000:
            pygame.draw.rect(screen, RED, (virus_rect.x, virus_rect.y+50, 80, 800), 2)
        if virus_binary_time >5000 and virus_binary_time <= 5100:
            screen.blit(binary_block, (virus_rect.x, virus_rect.y+50))
            binary_rect = pygame.Rect(virus_rect.x, virus_rect.y, 80, 800)
            if binary_rect.colliderect(player_rect) and player_immune <= 0:
                playerHP-=1
                pygame.time.delay(500)
                player_immune = 1000
        if virus_binary_time > 5100:
            virus_binary_time = 0



    #Check player collision with enemy bullet
    player_immune -= 40
    for bullet in bullet_list:
        if bullet.rect.colliderect(player_rect) and player_immune <= 0:
            playerHP -=1
            pygame.time.delay(500)
            player_immune = 1000
        if bullet.rect.x < -100 or bullet.rect.x > 900 or bullet.rect.y > 900:
            bullet.kill()
    
    for beybladecur in beyblade_list:
        offset = (beybladecur.rect.x - player_rect.x), (beybladecur.rect.y-player_rect.y)
        if player_mask.overlap(beybladecur.mask, offset) and player_immune <= 0:
            playerHP -= 1
            pygame.time.delay(500)
            player_immune = 1000

    if(playerHP <=0 and OS!= 2):
        pygame.time.delay(1000)
        Game_Over()
        pygame.quit()
        sys.exit()


    #Update and draw all enemy bullets
    bullet_list.update()
    beyblade_list.update()
    # for bullet in beyblade_list:
    #    pygame.draw.rect(screen, RED, bullet.rect)
    bullet_list.draw(screen)
    beyblade_list.draw(screen)
    enemies_list.draw(screen)
    for enemy in enemies_list:
        pygame.draw.rect(screen, GREEN, (enemy.rect.x, enemy.rect.y+50, enemy.HP*40/3, 3))
    

    #Update, draw, and check collision for player bullets
    player_bullet_list.update()
    for bullet in player_bullet_list:
        enemy = pygame.sprite.spritecollideany(bullet, enemies_list)
        if enemy:
            bullet.kill()
            enemy.HP-=1
            enemy.isAlive()
        elif bullet.rect.colliderect(virus_rect):
            virus_HP -= 50
            bullet.kill()
            if(virus_HP <=0):
                Victory()
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, RED, bullet.rect)
    virus_HP_bar = pygame.Rect(0, 0, virus_HP, 5)
    pygame.draw.rect(screen, GREEN, virus_HP_bar)
    
    #Draw player and virus
    pygame.draw.rect(screen, RED, player_rect)
    screen.blit(virus, virus_rect)

    center_text(str(playerHP), (pygame.font.SysFont('Georgia', 100, False, False)), RED, screen, 40, 720)

    pygame.display.update()
    dt = clock.tick(30)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit() 