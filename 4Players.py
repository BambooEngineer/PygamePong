import pygame # functions objects design
 # Cant USB sniff yet for controllers + Serial wouldnt work properly
 # maybe UDP Sockets 
import random
import math
import time
import serial
pygame.init()
random.seed()


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600)) # resolution, xy
pygame.display.set_caption('Tutorial')
clock = pygame.time.Clock() 

image1 = pygame.image.load('right.jpg') # image file
image2 = pygame.image.load('left.jpg') # image file
image3 = pygame.image.load('down.jpg') # image file
image4 = pygame.image.load('up.jpg') # image file
image5 = pygame.image.load('SOS.jpg')
image6 = pygame.image.load('Flipped.jpg')
image7 = pygame.image.load('Turned.jpg')
image8 = pygame.image.load('Away.jpg')
image9 = pygame.image.load('Loser.jpg')

players = False

def game_intro(): # load image while connecting controllers
    x = 300
    y = 250
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(image5, (x,y))
        pygame.display.update()
        clock.tick(60)
        time.sleep(1)
        gameDisplay.fill(white)
        gameDisplay.blit(image6, (x,y))
        pygame.display.update()
        time.sleep(1)
        gameDisplay.fill(white)
        gameDisplay.blit(image7, (x,y))
        pygame.display.update()
        time.sleep(1)
        gameDisplay.fill(white)
        gameDisplay.blit(image8, (x,y))
        pygame.display.update()
        time.sleep(1)
        gameDisplay.fill(white)
        gameDisplay.blit(image5, (x,y))
        pygame.display.update()
        time.sleep(1)
        intro = False
    
def things(thingx, thingy, radiusw, color):
    pygame.draw.circle(gameDisplay,color,[thingx,thingy],(radiusw))

def leftPaddle(x,y): # displaying image function
    gameDisplay.blit(image1, (x,y))

def rightPaddle(x,y): # displaying image function
    gameDisplay.blit(image2, (x,y))

def downPaddle(x,y): # displaying image function
    gameDisplay.blit(image4, (x,y))

def upPaddle(x,y): # displaying image function
    gameDisplay.blit(image3, (x,y))

crashed = False

left_change = 0
left = 100

right_change = 0
right = 100

up_change = 0 # movement
up = 300 # upPaddle pos

down_change = 0
down = 300

ball_changex = random.randint(-5,5)
ball_changey = random.randint(-5,5)
ballx = 300
bally = 300

game_intro()
while not crashed:
    
    for event in pygame.event.get(): # print events by how many times it occurs 
        if event.type == pygame.QUIT:
            crashed = True
        
        
        if event.type == pygame.KEYDOWN:# Keyboard Inputs
            if event.key == pygame.K_LEFT: # which keypad
                up_change = -5 # change dir
            if event.key == pygame.K_RIGHT:
                up_change = 5 # change dir
            if event.key == pygame.K_a:# down
                down_change = -5
            if event.key == pygame.K_d:
                down_change = 5
            if event.key == pygame.K_DOWN: # left
                left_change = 5
            if event.key == pygame.K_UP:
                left_change = -5
            if event.key == pygame.K_z: # right
                right_change = 5
            if event.key == pygame.K_c:
                right_change = -5

        if event.type == pygame.KEYUP: # Key let go
            if event.key == pygame.K_z or pygame.K_c or pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_a or pygame.K_d or pygame.K_UP or pygame.K_DOWN:
                up_change = 0 # stop changing
                down_change = 0
                left_change = 0
                right_change = 0


    # down and up = 0 and 500
    # right and left = 10 and 300


    ballx += ball_changex
    bally += ball_changey
    up += up_change # pos turned variable
    down += down_change
    left += left_change
    right += right_change
    gameDisplay.fill(white) # color ref uptop
    things(ballx,bally,25,red)
    leftPaddle(10,left) 
    rightPaddle(690,right) 
    downPaddle(down, 500) 
    upPaddle(up, 10)

    if(down > 500 or down < 10): # boundaries 
        down_change = 0
    if(up > 500 or up < 10):
        up_change = 0
    if(left > 300 or left < 10):
        left_change = 0
    if(right > 300 or right < 10):
        right_change = 0

    if(ballx > 800): # inside screen
        ball_changex = -5
    if(ballx < 10):
        ball_changex = 5
    if(bally > 590):
        ball_changey = -5
    if(bally < 10):
        ball_changey = 5
        
        
 # collision is really complicated for no reason in pygame
    
    #left right = y 200 lengths
     #down up = x 200 lengths 500 10

    areaL = math.hypot(10 - ballx,left-bally) # MATH for collision
    #if(25 > ballx and (bally < left-200 or bally <= left)):
    if(areaL <= 80+25):
        ball_changex = 5
        ball_changey = random.randint(-5,5)

    areaR = math.hypot(690 - ballx,right-bally) # MATH for collision
    #if(25 > ballx and (bally < left-200 or bally <= left)):
    if(areaR <= 80+25):
        ball_changex = -5
        ball_changey = random.randint(-5,5)

    areaD = math.hypot(down - ballx,500-bally) # MATH for collision
    #if(25 > ballx and (bally < left-azc200 or bally <= left)):
    if(areaD <= 80+25):
        ball_changey = -5
        ball_changex = random.randint(-5,5)
        
    areaU = math.hypot(up - ballx,10-bally) # MATH for collision
    #if(25 > ballx and (bally < left-200 or bally <= left)):
    if(areaU <= 80+25):
        ball_changey = 5
        ball_changex = random.randint(-5,5)

    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
