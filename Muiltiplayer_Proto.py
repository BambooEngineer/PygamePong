import pygame # functions objects design
 # Cant USB sniff yet for controllers + Serial wouldnt work properly
import socket
import random
import math
import time # for now the pi is sending ball and player positions while running
             # the main pc recieves and gives control over
pygame.init() # next step is allowing pi to recieve the sameway main PC does
random.seed() # for one player and for the PC to run the way pi does for one  
             # player


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 5555)) # hosting server
sock.listen(5) # listens for connecting clients
clientsocket, address = sock.accept()# variables for connected clients
print(f"connection from {address} has been established!")
    
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
left = 100

right_change = 0
right = 100

up_change = 0 # movement
up = 300 # upPaddle pos

down_change = 0
down = 300

ball_changex = 5
ball_changey = 5 # pi sending with main PC recieving works perfect
ballx = 300      # but both sending and recieving for 1 player each doesnt
bally = 300

leftu = str.encode("L") # Byte States for Left 
leftd = str.encode("l")

game_intro()

def game_Two():
    global clientsocket # global socket
    
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
    global leftu
    global leftd
    
    while not crashed:
        
        for event in pygame.event.get(): # print events by how many times it occurs 
            if event.type == pygame.QUIT:
                crashed = True
        
        
            if event.type == pygame.KEYDOWN:# Keyboard Inputs
                if event.key == pygame.K_DOWN: # left
                    left_change = 5
                if event.key == pygame.K_UP:
                    left_change = -5
                #if event.key == pygame.K_z: # right
                    #right_change = 5
                #if event.key == pygame.K_c:
                    #right_change = -5

            if event.type == pygame.KEYUP: # Key let go
                if event.key == pygame.K_z or pygame.K_c or pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_a or pygame.K_d or pygame.K_UP or pygame.K_DOWN:
                    up_change = 0 # stop changing
                    down_change = 0
                    left_change = 0
                    #right_change = 0


    # down and up = 0 and 500
    # right and left = 10 and 300

        if(left_change == -5): # outgoing Bytes for Left 
            clientsocket.sendall(leftd)
        if(left_change == 5):
            clientsocket.sendall(leftu) # server side shouldnt have to 
        if(left_change == 0):       # specify client location if 
            clientsocket.sendall(b'0') # client already connected

        data = clientsocket.recv(1)
        values = data.decode("utf-8") # full pi socket control
        
        if(values == 'R'): # Incoming Data for right player across UDP
            right_change = 5
        if(values == 'r'):
            right_change = -5
        if(values == '0'):
            right_change = 0
        # Recieving code not working and reason for crashes so reposition maybe
        ballx += ball_changex
        bally += ball_changey
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
    
        if(areaL <= 50):
            ball_changex = 5
            ball_changey = -5

        areaR = math.hypot(690 - ballx,200+right-bally) # MATH for collision
   
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
