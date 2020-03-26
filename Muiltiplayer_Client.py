import pygame # variables to communicate = Ballx,Bally, Player 1 & 2
import socket
import random
import math
import time
pygame.init()
random.seed()

IP = "{}"
i = input("Enter UDP_IP\n")
IP = "{}".format(i)
i = input("Enter UDP_PORT\n")
B = int(i)
PORT = 0
PORT += B
print(IP +"\n"+str(PORT))
# recieving side 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP,PORT)) 

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600)) # resolution, xy
pygame.display.set_caption('Stephens Ping Pong Summer')
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
left = 100 # might not need change transmitted

right_change = 0
right = 100 # might not need change transmitted

up_change = 0 # movement
up = 300 # upPaddle pos

down_change = 0
down = 300

ball_changex = 5 #
ball_changey = 5 #
ballx = 300 # trans
bally = 300 # trans

game_intro()

def game_Two():
    global sock

    global crashed
    global left_change
    global left
    global right_change
    global right
    global up_change
    global up

    global down_change
    global down
    global ball_changex
    global ball_changey
    global ballx
    global bally
    rightu = str.encode("R")
    rightd = str.encode("r")

    while not crashed:
        data = sock.recv(1)
        values = data.decode("utf-8")

        if(values == 'L'):
            left_change = 5
        if(values == 'l'):
            left_change = -5
        if(values == '0'):
            left_change = 0

        for event in pygame.event.get(): # print events by how many times it oc$
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.KEYDOWN:# Keyboard Inputs
                #if event.key == pygame.K_DOWN: # left
                 #   left_change = 5
                #if event.key == pygame.K_UP:
               #     left_change = -5
                if event.key == pygame.K_z: # right
                    right_change = 5
                if event.key == pygame.K_c:
                    right_change = -5

            if event.type == pygame.KEYUP: # Key let go
                if event.key == pygame.K_z or pygame.K_c:
                    up_change = 0 # stop changing
                    down_change = 0
              #      left_change = 0
                    right_change = 0


        if(right_change == -5):
                sock.sendto(rightd,(IP,5554))
        if(right_change == 5):
                sock.sendto(rightu, (IP,5554))
        if(right_change == 0):
                sock.sendto(b'0',(IP, PORT))
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
        if(ballx < 10):
            ball_changex = 5
        if(bally > 590):
            ball_changey = -5
        if(bally < 10):
            ball_changey = 5

# collision is really complicated for no reason in pygame
    
    #left right = y 200 lengths
     #down up = x 200 lengths 500 10

        areaL = math.hypot(10 - ballx,200+left-bally) # MATH for collision
    #if(25 > ballx and (bally < left-200 or bally <= left)):
        if(areaL <= 50):
            ball_changex = 5
            ball_changey = -5

        areaR = math.hypot(690 - ballx,200+right-bally) # MATH for collision
    #if(25 > ballx and (bally < left-200 or bally <= left)):
        if(areaR <= 50):
            ball_changex = -5
            ball_changey = 5
        pygame.display.update()
        clock.tick(60)
        # x bound = 10 or 690 = paddle x positions, y variable = (-100,700)
        # ballx(10,800), bally(10,590), ball radius = 25
        # Area = hypot(x boundary - ballx, y variable - bally)
        # if Area <= ball radius: collision

    # Return the Euclidean norm, sqrt(x*x + y*y).
    #This is the length of the vector from the origin to point (x, y).


game_Two()
pygame.quit()
quit()



        
 
