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
        gameDisplay.fill(white)
        gameDisplay.blit(image9, (x,y))
        pygame.display.update()
        time.sleep(1)
        intro = False
def game_over(): # load image while connecting controllers
    x = 300
    y = 250
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(image9, (x,y))
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

def Loser():
    gameDisplay.fill(white)
    gameDisplay.blit(image9, (0,0))

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
    

    if(left > 700 or left < -100): # player boundaries
        left_change = 0
    if(right > 700 or right < -100):
        right_change = 0

    if(ballx > 800): # inside screen
        ball_changex = -5
        game_over()
        time.sleep(1)
    if(ballx < 10):
        ball_changex = 5
        game_over()
        time.sleep(1)
    if(bally > 590):
        ball_changey = -5
    if(bally < 10):
        ball_changey = 5
        

    
    #left right = y 200 lengths
     #down up = x 200 lengths 500 10

    areaL = math.hypot(10 - ballx,200+left-bally) # MATH for collision
    areal = math.hypot(10 - ballx,100+left-bally) # CIRCLES
    # 2 collision masks since they are not that good
    if(areaL <= 50): 
        ball_changex = random.randint(5,10)
        ball_changey = random.randint(-10,5)
    if(areal <= 50):
        ball_changex = random.randint(5,10)
        ball_changey = random.randint(-10,5)

    areaR = math.hypot(690 - ballx,200+right-bally) 
    arear = math.hypot(690 - ballx,100+right-bally)
    
    if(areaR <= 50):
        ball_changex = random.randint(-10,-5)
        ball_changey = random.randint(-10,5)
    if(arear <= 50):
        ball_changex = random.randint(-10,-5)
        ball_changey = random.randint(-10,5)


    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()

