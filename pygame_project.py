'''
Introductory to Programming Final Project : PyGame
Pong - Created by Steven Bai
ICS 207-02
Due date : Monday, May 13, 2019

'''

import pygame
import time

pygame.init()


#Dimensions of the game
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 800

#Colour codes
BLACK = 0,0,0
WHITE = 255, 255, 255
RED = 200, 0, 0
LIGHT_RED = 255, 0,0
GREEN = 0, 200, 0
LIGHT_GREEN = 0, 255, 0
BLUE = 0,0,200
LIGHT_BLUE = 0,0,255
GREY = 128, 128, 128
LIGHT_GREY = 128, 170, 128
#Dimensions of game objects
SP_PADDLE_HEIGHT= 17
SP_PADDLE_WIDTH= 165
MP_PADDLE_HEIGHT = 165
MP_PADDLE_WIDTH = 17
BALL_WIDTH = 25
BALL_HEIGHT = 26


#Display the window with dimensions, name it "Pong by Steven Bai"
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Pong by Steven Bai")

#Frame rate
clock = pygame.time.Clock()

#Obtain all sprites needed
SP_Paddle = pygame.image.load('SP_Paddle.png')
MP_Paddle1 = pygame.image.load('MP_Paddle1.png')     
MP_Paddle2 = pygame.image.load('MP_Paddle2.png')
option_Arrow = pygame.image.load('option_Arrow.png')
SPball = pygame.image.load('Ball.png')
MenuImage = pygame.image.load('MenuImage.png')

#Single player paddle
def paddle(x_sp, y_sp):
    gameDisplay.blit(SP_Paddle, (x_sp, y_sp))  #Display the single player paddle

#2 player paddle #1
def paddle1(x_mp1, y_mp1):
    gameDisplay.blit(MP_Paddle1, (x_mp1, y_mp1))  #Display the multi player paddle for P1
#2 player paddle #2   
def paddle2(x_mp2, y_mp2):
    gameDisplay.blit(MP_Paddle2, (x_mp2, y_mp2))  #Display the multi player paddle for P1

#Ball
def ball(x_ball, y_ball):
    gameDisplay.blit(SPball, (x_ball, y_ball))  #Display ball

#Displays the custom yellow/black background in the main menu
def background(x_menu, y_menu):
    gameDisplay.blit(MenuImage, (x_menu, y_menu))

#Create invisible text box (WHITE TEXT)    
def textObjects(text, font): 
    textSurface = font.render (text, True, WHITE)
    return textSurface, textSurface.get_rect()

#Create invisible text box (BLACK TEXT)
def textObjects1(text, font): 
    textSurface = font.render (text, True, BLACK)
    return textSurface, textSurface.get_rect()


#Quits the game
def quitPong():  
    pygame.quit()
    quit()

#Draws the buttons on the main menu WITH hovering black arrows 
def button(msg, x1, y1, w1, h1, inactive1, active1, action=None ):  #Obtain the message, coordinates, dimensions, 2 colours and the action
    #obtain the mouse information
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x1 + w1 > cursor[0] > x1 and y1 + h1 > cursor [1] > y1:  #Checks if cursor is within button
        pygame.draw.rect(gameDisplay, active1, (x1,y1,w1,h1)) #Shows the button lighting up
        if click[0] == 1 and action !=None:             
            action()
                          
        gameDisplay.blit(option_Arrow, ( x1-25, y1+15))  #arrow that hovers over option
            
    else:
        pygame.draw.rect(gameDisplay, inactive1, (x1,y1,w1,h1)) #Original place and colour of button
    
    singlePlayText = pygame.font.Font("freesansbold.ttf", 20)   #Displays the button
    textSurf, textRect = textObjects(msg, singlePlayText)
    textRect.center = ( (x1 + (w1/2)),(y1 + (h1/2) ))
    gameDisplay.blit(textSurf, textRect)
    
#Creates main menu button in the single/multi play without hovering black arrow
def menuButton(message, x2, y2, w2, h2, inactive2, active2, action = None ): #Displays button
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x2 + w2 > cursor[0] > x2 and y2 + h2 > cursor [1] > y2:   
        pygame.draw.rect(gameDisplay, active2, (x2, y2, w2, h2)) 
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive2, (x2, y2, w2, h2))

    menuText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = textObjects(message, menuText)
    textRect.center = ( (x2 + (w2/2)), (y2 + (h2/2)))
    gameDisplay.blit(textSurf, textRect)


def createText(message, x, y, size, colour):   #Shortcut for creating text
    controlsFont = pygame.font.Font('freesansbold.ttf', size)
    textSurf, textRect = colour(message, controlsFont)
    textRect.center = (x,y)
    gameDisplay.blit(textSurf, textRect)


def messageDisplay(text, x, y, size):
    largeText = pygame.font.Font('freesansbold.ttf', size) #Font, font size
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = (x, y) #Displays message in center
    gameDisplay.blit(textSurf, textRect)


    
#Update and display score for the single player
def SP_POINTS(points_added):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(points_added), True, WHITE)
    gameDisplay.blit(text, (25, 25))


#Victory message when P1 wins, give options to retry/main menu
def player1_win():
    messageDisplay('Player 1 wins!', DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3, 70)
    gameExit = False
    
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        menuButton("Retry", 250,400,125,50, GREEN, LIGHT_GREEN, gameLoopMP)
        menuButton("Main Menu", 625,400,125,50, RED, LIGHT_RED, mainMenu)
        pygame.display.update()
        clock.tick(60)
        
#Victory message when P2 wins, give options to retry/main menu
def player2_win():
    messageDisplay('Player 2 wins!', DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3, 70)
    gameExit = False
    
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        menuButton("Retry", 250,400,125,50, GREEN, LIGHT_GREEN, gameLoopMP)
        menuButton("Main Menu", 625,400,125,50, RED, LIGHT_RED, mainMenu)
        pygame.display.update()
        clock.tick(60)


#Game over message when single player drops ball, choose retry/main menu   
def SP_crash():
    pygame.mixer.music.pause()
    pygame.mixer.music.load("game_over.mp3")
    pygame.mixer.music.play(1)
    
    messageDisplay('You dropped the ball!', DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3, 70)
    gameExit = False
    
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        menuButton("Retry", 250,400,125,50, GREEN, LIGHT_GREEN, SP_Start)
        menuButton("Main Menu", 625,400,125,50, RED, LIGHT_RED, mainMenu)
        pygame.display.update()
        clock.tick(60)

#Display msg when P2 gets the point    
def MP_crash1():
    gameExit = False
    
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        messageDisplay('Player 2 scores!', DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3, 70) 
        pygame.display.update()
        clock.tick(60)
        return

#Display msg when P1 gets the point 
def MP_crash2():

    gameExit = False
    
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        messageDisplay('Player 1 scores!', DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3, 70) 
        pygame.display.update()
        clock.tick(60)
        return

#Starting screen for single player; give instructions/controls and options to return to main menu or play    
def SP_Start():  
    pygame.mixer.music.pause()
    pygame.mixer.music.load('delfino.mp3')
    pygame.mixer.music.play()
    
    gameExit = False
    
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(BLACK)
        messageDisplay('Endless Mode', DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3, 70)
        messageDisplay("Don't let the ball touch the bottom!", DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2.5, 30)
        messageDisplay('Use arrow keys to move left/right', DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2.25, 30)
        messageDisplay('Score a point every time the ball hits the top of the screen', DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2.05, 30)
        button("Go", 250,500,125,50, GREEN, LIGHT_GREEN, gameLoopSP)
        button("Main Menu", 625,500,125,50, RED, LIGHT_RED, mainMenu)
        pygame.display.update()
        clock.tick(60)

#Starting screen for multiplayer; give instructions/controls and options to return to main menu or play 
def MP_Start():  
    pygame.mixer.music.pause()
    pygame.mixer.music.load('final_dest.mp3')
    pygame.mixer.music.play()
    gameExit = False
    
    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(BLACK)
        messageDisplay('2 Player Mode', DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3, 60)
        messageDisplay('First to 5 points wins!', DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2.5, 50)
        
        createText("Player 2 controls:", 825 , 400, 30, textObjects)
        createText("Use arrow keys to", 825, 500, 30, textObjects)
        createText("move UP and DOWN", 825, 525, 30, textObjects)
                    

        createText("Player 1 controls:", 175, 400, 30, textObjects)
        createText("Use W to move up", 175, 500,30, textObjects)
        createText("and S to move down", 175, 525, 30,  textObjects)
        
        button("Play", 250,600,125,50, GREEN, LIGHT_GREEN, gameLoopMP)
        button("Main Menu", 625,600,125,50, RED, LIGHT_RED, mainMenu)
        pygame.display.update()
        clock.tick(60)


#Main menu screen
def mainMenu():
    pygame.mixer.music.pause()
    pygame.mixer.music.load('main_theme.mp3')
    pygame.mixer.music.play(-1) #Play music

    #Dimensions of the menu background    
    menu_x = 0
    menu_y = 0
    
    gameExit = False

    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        background(menu_x, menu_y) #Make the background 


        #Title
        largeText = pygame.font.Font('freesansbold.ttf', 130)
        textSurf, textRect = textObjects("Pong", largeText)
        textRect.center = ((DISPLAY_WIDTH/2), (DISPLAY_HEIGHT/3))
        gameDisplay.blit(textSurf, textRect)

        #Name at bottom of screen
        name = pygame.font.Font('freesansbold.ttf', 15)
        textSurf, textRect = textObjects1("Created by Steven Bai", name)
        textRect.center = ((DISPLAY_WIDTH/2),785)
        gameDisplay.blit(textSurf, textRect)

        #3 options: SP, MP or quit
        button("SINGLE PLAYER", 350,400,300,50, GREEN, LIGHT_GREEN,SP_Start)
        button("MULTIPLAYER", 350,500,300,50, BLUE, LIGHT_BLUE, MP_Start)
        button("QUIT", 350,600,300,50, RED, LIGHT_RED, quitPong)

        #update screen at 60 FPS
        pygame.display.update()
        clock.tick(60)

#Single player gameplay
def gameLoopSP():
    x_sp = (DISPLAY_WIDTH * .4175)   #coordinates of the single player paddle
    y_sp = (DISPLAY_HEIGHT *.8)

    #coordinates of ball
    x_ball = 487.5
    y_ball = 614

    #velocity of ball
    x_ball_v = -10
    y_ball_v =-10
    
    #velocity of paddle
    x_spVelocity = 0

    #Score
    points = 0
    
    gameExit = False


    while gameExit == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            #Player controlled movement for the paddle
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_sp > 0 :  #Moves to the left
                    x_spVelocity = -10
                elif event.key == pygame.K_RIGHT and  x_sp <835: #Moves to the right
                    x_spVelocity = 10

            #Stop moving if key is released        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_spVelocity = 0




        x_sp = x_sp + x_spVelocity   #Calulates position of paddle
        
        if x_sp < 0 :               #Stop ball if it goes up too far
            x_spVelocity = 0

        if x_sp >835:               #Stop ball if it goes down too far
            x_spVelocity = 0
            
        x_ball += x_ball_v   #Calculates position of ball
        y_ball += y_ball_v
        


        if x_ball <0 or x_ball>DISPLAY_WIDTH - 25:  #Bounce if ball hits left or right of screen
            x_ball_v = x_ball_v * -1


        if x_ball + BALL_WIDTH == x_sp or x_ball == (x_sp- BALL_WIDTH) + SP_PADDLE_WIDTH + BALL_WIDTH: #Bounce if ball hits corners of paddle
            x_ball_v = x_ball_v * -1

            
        if y_ball <0 :    #Bounce and add a point if ball hits top of screen
            y_ball_v = y_ball_v * -1
            points += 1


        if y_ball >DISPLAY_HEIGHT-26:  #Stop ball and display crash screen when ball hits bottom
            y_ball_v == 0
            x_ball_v ==0
            SP_crash()
                

        #Bounce if ball hits surface of paddle
        if y_sp == y_ball + BALL_HEIGHT : 
            if x_ball >= x_sp-40 and x_ball <= (x_sp-30) + 30 + SP_PADDLE_WIDTH + 30: 
                y_ball_v = y_ball_v * -1

            
        gameDisplay.fill(BLACK) #Makes the background black
        #Display points
        SP_POINTS(points)

        #Displaying position of ball and paddle
        paddle(x_sp, y_sp)  
        ball(x_ball, y_ball)

        #Main menu button on bottom left of screen
        menuButton("Main Menu", 10, 750, 100, 20, GREEN, LIGHT_GREEN, mainMenu) 

        #Update screen; 60 FPS
        pygame.display.update()
        clock.tick(60)


#Gameplay for multiplayer
        
def gameLoopMP():
    #coordinates of paddle1; x_mp1 = x of multiplayer paddle #1
    x_mp1 = (20)   
    y_mp1 = (235)
    
    #coordinates of paddle2; x_mp2 = x of multiplayer paddle #2
    x_mp2 = (965)   
    y_mp2 = (235)

    #ball velocity
    x_ball_v = 7
    y_ball_v =7

    #ball coordinates 
    x_ball = 17 + 20
    y_ball = 235+ (MP_PADDLE_HEIGHT/2)

    #Default moving speed of paddles
    y_mp1Velocity = 0
    y_mp2Velocity = 0

    #Points; count1 = P1 count2 = P2
    count1 = 0
    count2 = 0
    
    
    gameExit = False

    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Give the 2 paddles when users press done the corresponding key
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_w and y_mp1>0:  #Moves up for P1
                    y_mp1Velocity = -6
                elif event.key == pygame.K_s and y_mp1<635: #Moves down for P1
                    y_mp1Velocity = 6
                elif event.key == pygame.K_UP and y_mp2>0:  #Moves up for P2
                    y_mp2Velocity = -6
                elif event.key == pygame.K_DOWN and y_mp2<635: #Moves down for P2
                    y_mp2Velocity = 6

                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s: #Stop moving when key is lifted
                    y_mp1Velocity = 0
    
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP: #Stop moving when key is lifted
                    y_mp2Velocity = 0

        y_mp1 += y_mp1Velocity   #Gives movement for paddle for P1
        y_mp2 += y_mp2Velocity   #Gives movement for paddle for P2


        #Gives movement for the ball on both axis
        x_ball += x_ball_v   
        y_ball += y_ball_v

        
        
        if y_mp1<0 :            #Stop if paddle leaves screen (top)
            y_mp1Velocity = 0

        if y_mp1>635 :            #Stop if paddle leaves screen (bottom)
            y_mp1Velocity = 0
            
        if y_mp2<0 :            #Stop if paddle leaves screen (top)
            y_mp2Velocity = 0

        if y_mp2>635 :            #Stop if paddle leaves screen (bottom)
            y_mp2Velocity = 0

        #Checking if player 1/2 has won, if so then skip the point counting process and display victory screen
        if count1 ==5:
            time.sleep(1.5)
            player1_win()

        if count2 ==5:
            time.sleep(1.5)
            player2_win()
            
        #If ball hits left of screen, P1 loses and P2 gets point    
        if x_ball <0:  
            x_ball_v = 0
            y_ball_v = 0
            count2 += 1
            
            if count2<5:
                MP_crash1()   #Display the message of P2 getting point
                
                time.sleep(1.5)  #Wait


            #Reset paddles and ball after P1 scores    
            x_mp1 = (20)   
            y_mp1 = (235)
            x_mp2 = (965)  
            y_mp2 = (235) 
            x_ball_v = -7
            y_ball_v = -7
            x_ball = 17 + 20
            y_ball = 235+ (MP_PADDLE_HEIGHT/2)             

        
        #If ball hits right of screen, P2 loses and P1 get point
        if x_ball>DISPLAY_WIDTH - 25:  
            x_ball_v = 0
            y_ball_v = 0
                
            count1 += 1
            
            if count1<5:
                MP_crash2()
                
                time.sleep(1.5)
            
            #Reset paddles and ball after P2 scores    
            x_mp1 = (20)   
            y_mp1 = (235)
            x_mp2 = (965)  
            y_mp2 = (235) 
            x_ball_v = -7
            y_ball_v = -7
            x_ball = 17 + 20
            y_ball = 235+ (MP_PADDLE_HEIGHT/2)      

            

        if y_ball <0 :   #bounce if ball hits top of screen
            y_ball_v = y_ball_v * -1

            
        if y_ball >DISPLAY_HEIGHT-26: #Gave over if ball hits bottom of screen
            y_ball_v = y_ball_v *-1


        #bouncing on P1 paddle
        if (x_mp1 + MP_PADDLE_WIDTH) == x_ball : #Bounce if ball is touching paddle 1 (horizontal )
            if y_ball + BALL_HEIGHT >= y_mp1 - 20 and y_ball <= (y_mp1 + MP_PADDLE_HEIGHT + 20) : #Bounce if ball is touching paddle 1(vertical)
                x_ball_v = x_ball_v * -1

        #bouncing on P2 paddle
        if x_mp2  == (x_ball + BALL_WIDTH): #Bounce if ball is touching paddle 2 (vertical)
            if y_ball + BALL_HEIGHT >= y_mp2 - 20 and y_ball <= (y_mp2 + MP_PADDLE_HEIGHT+20): #Bounce if ball is touching paddle 2(horizontal)
                x_ball_v = x_ball_v * -1
        


        gameDisplay.fill(BLUE) #Makes the background blue


        pygame.draw.rect(gameDisplay, WHITE, (0, 390, 1000, 7)) #White line that divides screen in half, like a ping pong table
        
        paddle1(x_mp1, y_mp1)  #draws P1 paddle; mp1 = multiplayer mode, player 1
        paddle2(x_mp2, y_mp2)  #draws P2 paddle; mp2 = multiplayer mode, player 1
        
        ball(x_ball, y_ball)   #draws the ball 

        #update and display the score count for both players
        font = pygame.font.SysFont(None, 50)
        text = font.render("P2: " + str(count2), True, WHITE)
        gameDisplay.blit(text, (530, 25))

        font = pygame.font.SysFont(None, 50)
        text = font.render("P1: " + str(count1), True, WHITE)
        gameDisplay.blit(text, (400, 25))

        

        menuButton("Main Menu", 10, 750, 100, 20, GREEN, LIGHT_GREEN, mainMenu) #Gives dimensions and colour for a main menu button on bottom left corner


        #Update screen at 60 FPS
        
        pygame.display.update()
        clock.tick(100)

#Start the game at the main menu
mainMenu()

