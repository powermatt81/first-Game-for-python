# UTF-8
import pygame
import sys
import time
import random

pygame.init() # Initilize pygame

########################### Setting #######################################
## This is RGB ==> (Red,Green,Blue)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)

# Setting for EZ coding
screen_width = 800
screen_height = 600

# This is to setup a windows screen (x,y)
screen = pygame.display.set_mode((screen_width,screen_height))

# This is to name title bar
pygame.display.set_caption("SnakerEatBoss")

icon = pygame.image.load ("D:/VSC/python/apple2.png")
pygame.display.set_icon(icon)


img = pygame.image.load('D:/VSC/python/snakhead3.png')
appleimg = pygame.image.load('D:/VSC/python/apple2.png')

clock = pygame.time.Clock() # Using pygame function name to clock,renew fram
AppleThickness = 30
block_size = 20
eps = 18

direction = "right"

############################################################################

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause():
    paused = True

    while paused :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        screen.fill(white)
        message_to_screen("PAUSED",black,-100,size = "large")
        message_to_screen("Press C to Continue or Q to Quit.",black,25)
        pygame.display.update()
        clock.tick(15)            


def score(score):
    text = smallfont.render("Score: " + str (score), True, black)
    screen.blit (text, [0,0])

def randAppleGen():
    randAppleX = round (random.randrange(0, screen_width - AppleThickness)/10.0)*10.0
    randAppleY = round (random.randrange(0, screen_height - AppleThickness)/10.0)*10.0

    return randAppleX, randAppleY
randAppleX, randAppleY = randAppleGen()            


def game_intro() :
    
    intro = True
    while intro :
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit
                    quit() 


        screen.fill(white)
        message_to_screen("THE SnakeBoss",blue,-100,"large")
        message_to_screen("The objective of the game is to eat red apple",black,-30)
        message_to_screen("The more apple you eat, the longer you get",black,10)
        message_to_screen("If you run into youself, or the edges, you die",black,50)
        message_to_screen("Press C to Start, P to Pause or Q to Quite",black,150)
        pygame.display.update()
        clock.tick(15)


# Snake function
def snake (block_size, snakeList):
    
    if direction == "right":
        head = pygame.transform.rotate (img, 270)

    if direction == "left":
        head = pygame.transform.rotate (img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate (img, 180)

    screen.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    for XnY in snakeList [:-1] :
        pygame.draw.rect(screen, green, [XnY[0], XnY[1], block_size, block_size]) 

def text_objects(text,color, size):
    if size == "small" :
        textSurface = smallfont.render(text,True, color)
    elif size == "medium" :
        textSurface = medfont.render(text,True, color)
    elif size == "large" :
        textSurface = largefont.render(text,True, color)
    
    return textSurface, textSurface.get_rect()

# Message function for game
def message_to_screen (msg, color, y_displace = 0, size = "small" ):
    textSurf, textRect = text_objects(msg, color,size) 
    # screen_text = font.render(msg, True, color)
    # screen.blit(screen_text, [screen_width/2, screen_height/2])
    textRect.center = (screen_width/2),(screen_height/2) + y_displace
    screen.blit(textSurf, textRect)

####################### Game ##############################################
def game_loop() :
    global direction
    direction = "right"
    gameExit = False
    gameOver = False

    lead_x = screen_width / 2
    lead_y = screen_height / 2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    # AppleThickness = 30
#   Add random apple，range (start，stop)
    # randAppleX = round (random.randrange(0, screen_width - AppleThickness)/10.0)*10.0
    # randAppleY = round (random.randrange(0, screen_height - AppleThickness)/10.0)*10.0
    randAppleX, randAppleY = randAppleGen()  

    while not gameExit:
        
        while gameOver == True :
            screen.fill(white)
            message_to_screen("Gomer Over", red, -50, size = "large")
            message_to_screen( "Press C to try again or Q to quite", black, 50, "medium" )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0

                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0

                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y <0 :
            gameOver = True            
            #print(event)
            
    # The contorl could be stoped       
    #        if event.type == pygame.KEYUP:
    #           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #               lead_x_change =0
    
        lead_x += lead_x_change
        lead_y += lead_y_change 

        
        screen.fill(white) # fulfill the windows with select color
        
        #AppleThickness = 30
        #pygame.draw.rect(screen, red, [randAppleX,randAppleY,AppleThickness,AppleThickness])
        
        screen.blit (appleimg, (randAppleX,randAppleY))

        # [x-axis,Y-axis,height,width]
        # screen.fill(red, rect=[200,200,10,10])

        
        snakeHead = []
        snakeHead.append (lead_x)
        snakeHead.append (lead_y)
        snakeList.append (snakeHead)

        if len(snakeList) > snakeLength :
            del snakeList [0]

        for eachSegment in snakeList [:-1] :
            if eachSegment == snakeHead :
                gameOver = True

        snake( block_size, snakeList) 

        score((snakeLength - 1)*10)

        pygame.display.update() # renew display

        # if lead_x == randAppleX and lead_y == randAppleY :
        #     randAppleX = round (random.randrange(0, screen_width - block_size)/10.0)*10.0
        #     randAppleY = round (random.randrange(0, screen_height - block_size)/10.0)*10.0
        #     snakeLength += 1

        # if  lead_x >= randAppleX and lead_x <= randAppleX +AppleThickness :
        #     if  lead_y >= randAppleY and lead_y <= randAppleY +AppleThickness :
        #         randAppleX = round (random.randrange(0, screen_width - AppleThickness)/10.0)*10.0
        #         randAppleY = round (random.randrange(0, screen_height - AppleThickness)/10.0)*10.0
        #         snakeLength += 1
    
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness :
           
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness :
                # randAppleX = round (random.randrange(0, screen_width - AppleThickness)/10.0)*10.0
                # randAppleY = round (random.randrange(0, screen_height - AppleThickness)/10.0)*10.0
                randAppleX, randAppleY = randAppleGen()  
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness :
                # randAppleX = round (random.randrange(0, screen_width - AppleThickness)/10.0)*10.0
                # randAppleY = round (random.randrange(0, screen_height - AppleThickness)/10.0)*10.0
                randAppleX, randAppleY = randAppleGen()  
                snakeLength += 1
    



        clock.tick(eps) # moving speed


#    message_to_screen("YOU LOSE", red)
#    pygame.display.update()
#    time.sleep(2)
    pygame.quit()
    quit()

game_intro()

game_loop()