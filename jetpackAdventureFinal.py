'''
----------------------------------------------------------------------------------------------------
Author:       Alden Shin-Culhane and Nathan Souphanthong
Created:      December 13, 2017
Title:        Jetpack Adventure Summative.py
----------------------------------------------------------------------------------------------------
--------------------------------------------------
        WELCOME TO JETPACK ADVENTURE 
--------------------------------------------------
'''
from random import randint
import math
import pygame
import time
pygame.init()

# Set screen
WIDTH = 1300
HEIGHT = 700
TOP = 0
BOTTOM = 700
gameWindow = pygame.display.set_mode((WIDTH,HEIGHT))

# Define colours & fonts
SKIN = (255,224,189)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (83,85,89)
RED = (255,0,0)
CYAN = (148,170,204)
GREEN = (0,255,0)
BLUE = (0,0,255)
ORANGE = (255,165,0)
BLOODORANGE = (255,50,0)
YELLOW = (255,255,0)
BROWN = (165,42,42)
GOLDENYELLOW = (255,223,0)
TURQUOISE = (29,135,129)
YELLOWORANGE = (236,176,34)
PINK = (255,192,203)
PURPLE = (160,32,240)

font = pygame.font.SysFont("Perpetua",36)
font2 = pygame.font.SysFont("Perpetua",150)
font3 = pygame.font.SysFont("Perpetua",72)
font4 = pygame.font.SysFont("Perpetua",56)
font5 = pygame.font.SysFont("Perpetua",110)

# Import photos
bg1 = pygame.image.load("jetpackAdventureBackground.png").convert()
bg2 = pygame.image.load("jetpackAdventureBackground.png").convert()
logo = pygame.image.load("Jet_Pack_Adventure_logo.png").convert_alpha()
shopIcon = pygame.image.load("ShopIcon.png").convert_alpha()
restartIcon = pygame.image.load("restartIcon.png").convert_alpha()
quitIcon = pygame.image.load("quitIcon.png").convert_alpha()
menuIcon = pygame.image.load("menuIcon.png").convert_alpha()
backButton = pygame.image.load("BackButton.png").convert_alpha()
coinIcon = pygame.image.load("CoinIcon.png").convert_alpha()
shirtIcon = pygame.image.load("shirtIcon.png").convert_alpha()
shoeIcon = pygame.image.load("shoeIcon.png").convert_alpha()
jetpackIcon = pygame.image.load("jetpackIcon.png").convert_alpha()
costIcon = pygame.image.load("costIcon.png").convert_alpha()

# Load music 
pygame.mixer.music.load("bankAccount.mp3")
pygame.mixer.music.set_volume(0.75)
pygame.mixer.music.play(-1)

# Load sound effects
gameOver = pygame.mixer.Sound("gameOver.wav")
gameOver.set_volume(0.5)
coinSound = pygame.mixer.Sound("coinSound.wav")
coinSound.set_volume(0.5)

'''
--------------------------------------------------
                    Functions
--------------------------------------------------
'''
def backButtons():
    # Edit global variables 
    global button
    
    # Draw back button
    pygame.draw.rect(gameWindow,TURQUOISE,(0,0,200,170))
    gameWindow.blit(backButton,(0,-20))
    pygame.draw.rect(gameWindow,BLACK,(5,0,200,170),10)
    
    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (cursorX,cursorY) = pygame.mouse.get_pos()
            if cursorX > 0 and cursorX < 200  and cursorY > -20 and cursorY < 180:
                button = False

def clothingPurchases():
    # Edit global variables
    global shirtClr
    global coinCount
    
    # Draw colour choices
    pygame.draw.rect(gameWindow,WHITE,(350,420,350,50))
    colourBlue = font.render("BLUE",1,BLUE)
    gameWindow.blit(colourBlue,(495,420))
    gameWindow.blit(costIcon,(650,425))
    cost1 = font.render("20",1,GOLDENYELLOW)
    gameWindow.blit(cost1,(615,425))

    pygame.draw.rect(gameWindow,WHITE,(350,490,350,50))
    colourBlack = font.render("BLACK",1,BLACK)
    gameWindow.blit(colourBlack,(485,490))
    gameWindow.blit(costIcon,(650,495))
    cost2 = font.render("25",1,GOLDENYELLOW)
    gameWindow.blit(cost2,(615,495))

    pygame.draw.rect(gameWindow,WHITE,(350,560,350,50))
    colourRed = font.render("RED",1,RED)
    gameWindow.blit(colourRed,(500,560))
    gameWindow.blit(costIcon,(650,565))
    cost3 = font.render("30",1,GOLDENYELLOW)
    gameWindow.blit(cost3,(615,565))

    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (cursorX,cursorY) = pygame.mouse.get_pos()

            # BLUE
            if cursorX > 350 and cursorX < 700 and cursorY > 420 and cursorY < 470:

                # If the user doesn't have enough coins, error message
                if coinCount < 20:
                    print ("Insufficent Funds")

                # If the user has enough coins, subtract coins purchase new colour
                if coinCount >= 20:
                    coinCount -= 20
                    shirtClr = BLUE
                    print ("Purchase Confirmed!")

            # BLACK
            if cursorX > 350 and cursorX < 700 and cursorY > 490 and cursorY < 540:

                # If the user doesn't have enough coins, error message
                if coinCount < 25:
                    print ("Insufficent Funds")

                # If the user has enough coins, subtract coins purchase new colour
                if coinCount >= 25:
                    coinCount -= 25
                    shirtClr = BLACK
                    print ("Purchase Confirmed!")
                    
            # RED                                   
            if cursorX > 350 and cursorX < 700 and cursorY > 560 and cursorY < 610:

                # If the user doesn't have enough coins, error message
                if coinCount < 30:
                    print ("Insufficent Funds")

                # If the user has enough coins, subtract coins purchase new colour
                if coinCount >= 30:
                    coinCount -= 30
                    shirtClr = RED
                    print ("Purchase Confirmed!")

def jetpackPurchases():
    # Edit global variables 
    global shirtClr
    global coinCount
    
    # Draw colour choices
    pygame.draw.rect(gameWindow,WHITE,(350,420,350,50))
    colourBlue = font.render("PINK",1,PINK)
    gameWindow.blit(colourBlue,(495,420))
    gameWindow.blit(costIcon,(650,425))
    cost1 = font.render("20",1,GOLDENYELLOW)
    gameWindow.blit(cost1,(615,425))

    pygame.draw.rect(gameWindow,WHITE,(350,490,350,50))
    colourBlack = font.render("ORANGE",1,ORANGE)
    gameWindow.blit(colourBlack,(470,490))
    gameWindow.blit(costIcon,(650,495))
    cost2 = font.render("25",1,GOLDENYELLOW)
    gameWindow.blit(cost2,(615,495))

    pygame.draw.rect(gameWindow,WHITE,(350,560,350,50))
    colourRed = font.render("PURPLE",1,PURPLE)
    gameWindow.blit(colourRed,(480,560))
    gameWindow.blit(costIcon,(650,565))
    cost3 = font.render("30",1,GOLDENYELLOW)
    gameWindow.blit(cost3,(615,565))

    # Check for user input
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (cursorX,cursorY) = pygame.mouse.get_pos()

            # PINK
            if cursorX > 350 and cursorX < 700 and cursorY > 420 and cursorY < 470:

                # If the user doesn't have enough coins, error message
                if coinCount < 20:
                    print ("Insufficent Funds")

                # If the user has enough coins, subtract coins purchase new colour
                if coinCount >= 20:
                    coinCount -= 20
                    jetpackClr = PINK
                    print ("Purchase Confirmed!")

            # ORANGE  
            if cursorX > 350 and cursorX < 700 and cursorY > 490 and cursorY < 540:

                # If the user doesn't have enough coins, error message
                if coinCount < 25:
                    print ("Insufficent Funds")

                # If the user has enough coins, subtract coins purchase new colour
                if coinCount >= 25:
                    coinCount -= 25
                    jetpackClr = ORANGE
                    print ("Purchase Confirmed!")
                    
            # PURPLE                   
            if cursorX > 350 and cursorX < 700 and cursorY > 560 and cursorY < 610:

                # If the user doesn't have enough coins, error message
                if coinCount < 30:
                    print ("Insufficent Funds")

                # If the user has enough coins, subtract coins purchase new colour
                if coinCount >= 30:
                    coinCount -= 30
                    jetpackClr = PURPLE
                    print ("Purchase Confirmed!")


                    
def coinCounters():
    # Edit global variables 
    global coinSpace
    
    # Draw counter
    pygame.draw.rect(gameWindow,TURQUOISE,(1100,0,200,170))
    pygame.draw.rect(gameWindow,BLACK,(1095,0,200,170),10)
    coinCounter = font3.render(" " + str(coinCount),1,GOLDENYELLOW) 
    
    # Create extra space if needed
    if coinCount >= 10:
        coinSpace = 25
    if coinCount >= 100:
        coinSpace = 60
        
    gameWindow.blit(coinCounter,(1150 - coinSpace,45))
    gameWindow.blit(coinIcon,(1185,30))

def clothingShop():
    # Draw clothing options 
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow,YELLOWORANGE,(0,0,1300,250))
    shopTitle = font5.render("CLOTHING SHOP",1,BLACK)
    gameWindow.blit(shopTitle,(260,45))

    pygame.draw.rect(gameWindow,GREY,(800,370,250,250))
    gameWindow.blit(shirtIcon,(825,395))

    pygame.draw.rect(gameWindow,WHITE,(300,350,450,50))
    colour = font.render("COLOURS",1,BLACK)
    gameWindow.blit(colour,(455,350))

    # Initizalize coin counter
    coinCounters()

    # Initialize back button
    backButtons()

    # Initialize colour buttons
    clothingPurchases()

    # Update display
    pygame.display.update()
    
def jetpackShop():
    # Draw the background
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow,YELLOWORANGE,(0,0,1300,250))
    shopTitle = font5.render("JETPACK SHOP",1,BLACK)
    gameWindow.blit(shopTitle,(310,45))
    pygame.draw.rect(gameWindow,GREY,(800,370,250,250))
    gameWindow.blit(jetpackIcon,(825,395))
    pygame.draw.rect(gameWindow,WHITE,(300,350,450,50))
    colour = font.render("COLOURS",1,BLACK)
    gameWindow.blit(colour,(455,350))

    # Initizalize coin counter
    coinCounters()

    # Initialize back button
    backButtons()

    # Function for transactions
    jetpackPurchases()

    # Update display
    pygame.display.update()
    
    
def shoeShop():
    global shoeClr
    global coinCount
    
    # Draw the background
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow,YELLOWORANGE,(0,0,1300,250))
    shopTitle = font5.render("SHOE SHOP",1,BLACK)
    gameWindow.blit(shopTitle,(370,45))
    pygame.draw.rect(gameWindow,GREY,(800,370,250,250))
    gameWindow.blit(shoeIcon,(825,395))
    pygame.draw.rect(gameWindow,WHITE,(300,350,450,50))
    colour = font.render("COLOURS",1,BLACK)
    gameWindow.blit(colour,(455,350))

    # Initizalize coin counter
    coinCounters()

    # Initialize back button
    backButtons()

    # Function for transaction
    # Draw colour choices
    pygame.draw.rect(gameWindow,WHITE,(350,420,350,50))
    colourBlue = font.render("WHITE",1,BLACK)
    gameWindow.blit(colourBlue,(480,420))
    gameWindow.blit(costIcon,(650,425))
    cost1 = font.render("20",1,GOLDENYELLOW)
    gameWindow.blit(cost1,(615,425))

    pygame.draw.rect(gameWindow,WHITE,(350,490,350,50))
    colourBlack = font.render("YELLOW",1,YELLOW)
    gameWindow.blit(colourBlack,(470,490))
    gameWindow.blit(costIcon,(650,495))
    cost2 = font.render("25",1,GOLDENYELLOW)
    gameWindow.blit(cost2,(615,495))

    pygame.draw.rect(gameWindow,WHITE,(350,560,350,50))
    colourRed = font.render("BLUE",1,BLUE)
    gameWindow.blit(colourRed,(490,560))
    gameWindow.blit(costIcon,(650,565))
    cost3 = font.render("30",1,GOLDENYELLOW)
    gameWindow.blit(cost3,(615,565))

    # Check for user input 
    for event in pygame.event.get():
        #if event.type == pygame.MOUSEBUTTONDOWN:
            (cursorX,cursorY) = pygame.mouse.get_pos()

            # WHITE
            if cursorX > 350 and cursorX < 700 and cursorY > 420 and cursorY < 470:
                
                # If the user doesn't have enough coins, error message
                if coinCount < 20:
                    print ("Insufficent Funds")
                    
                # If the user has enough coins, subtract coins purchase new colour
                if coinCount >= 20:
                    coinCount -= 20
                    shoeClr = WHITE
                    print ("Purchase Confirmed!")

            # YELLOW
            if cursorX > 350 and cursorX < 700 and cursorY > 490 and cursorY < 540:

                # If the user doesn't have enough coins, error message
                if coinCount < 25:
                    print ("Insufficent Funds")
    
                # If the user has enough coins, subtract coins purchase new colour
                if coinCount >= 25:
                    coinCount -= 25
                    shoeClr = YELLOW
                    print ("Purchase Confirmed!")
                    
            # BLUE                        
            if cursorX > 350 and cursorX < 700 and cursorY > 560 and cursorY < 610:

                # If the user doesn't have enough coins, error message
                if coinCount < 30:
                    print ("Insufficent Funds")

                # If the user has enough coins, subtract coins purchase new colour
                if coinCount >= 30:
                    coinCount -= 30
                    shoeClr = BLUE
                    print ("Purchase Confirmed!")

    # Update display
    pygame.display.update()

def shopWindow():
    # Edit global variables
    global button
    global buttonType
    global coinCount
    global shop 
    
    # Draw background
    gameWindow.fill(BLACK)
    pygame.draw.rect(gameWindow,WHITE,(150,300,1000,375),10)
    pygame.draw.rect(gameWindow,YELLOWORANGE,(0,0,1300,250))
    
    # Coin count
    coinCounters()
    
    # Shop Title
    shopTitle = font2.render("SHOP",1,BLACK)
    gameWindow.blit(shopTitle,(495,45))

    if button == False: 
        # Draw shop buttons
        pygame.draw.rect(gameWindow,GREY,(200,370,250,250))
        gameWindow.blit(shirtIcon,(225,395))
                        
        pygame.draw.rect(gameWindow,GREY,(500,370,300,250))
        gameWindow.blit(jetpackIcon,(550,390))
                        
        pygame.draw.rect(gameWindow,GREY,(850,370,250,250))
        gameWindow.blit(shoeIcon,(880,390))

        pygame.draw.rect(gameWindow,TURQUOISE,(0,0,200,170))           
        gameWindow.blit(backButton,(0,-20))
        pygame.draw.rect(gameWindow,BLACK,(5,0,200,170),10)
        pygame.display.update()
        
        # Check for button press
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (cursorX,cursorY) = pygame.mouse.get_pos()
                if cursorX > 200 and cursorX < 450 and cursorY > 370 and cursorY < 620:
                    gameWindow.fill(YELLOW)
                    button = True
                    buttonType = "Clothing"
                if cursorX > 500 and cursorX < 800 and cursorY > 370 and cursorY < 620:
                    gameWindow.fill(YELLOW)
                    button = True
                    buttonType = "Jetpack"
                if cursorX > 850 and cursorX < 1100  and cursorY > 370 and cursorY < 620:
                    gameWindow.fill(YELLOW)
                    button = True
                    buttonType = "Shoe"
                if cursorX > 0 and cursorX < 200  and cursorY > -20 and cursorY < 180:
                    shop = False

    # Determine shop type
    if button == True and buttonType == "Clothing":
        clothingShop()
        pygame.display.update()
        
    if button == True and buttonType == "Jetpack":
        jetpackShop()
        
    if button == True and buttonType == "Shoe":
        shoeShop()

def startGame():
    # Draw background
    gameWindow.blit(bg1,(0,0))

    # Draw Jetpack Adventure Logo
    gameWindow.blit(logo,(0,0))

    # Draw start message
    pygame.draw.rect(gameWindow,GREY,(795,600,300,45))
    startMessage = font.render("Press spacebar to start",1,WHITE)
    gameWindow.blit(startMessage,(800,600))

    # Draw shop icon
    gameWindow.blit(shopIcon,(-30,-20))

    # Update display
    pygame.display.update()

def restartScreen():
    # Edit global variables
    global inGame
    global restartCount
    global coinCount

    # Restart loop
    inRestart = True
    while inRestart == True:
        # Game summary
        if restartCount < 1:
            gameOver.play()
            print (" Game Over!")
            print (" Final score:",offScreen)
            print (" Total coins:",coinCount)
            print ("")
            restartCount += 1 
        
        # Draw background 
        gameWindow.blit(bg1,(0,0))

        # Game Over message
        pygame.draw.rect(gameWindow,GREY,(295,45,715,140))
        graphics = font2.render("Game Over!",1,WHITE)
        gameWindow.blit(graphics,(315,35))

        # End message
        graphics2 = font3.render("Final Score: "+str(offScreen),1,WHITE)
        gameWindow.blit(graphics2,(460,300))

        # Coin message
        coinCounter2 = font3.render("Total Coins: " + str(coinCount),1,WHITE)
        gameWindow.blit(coinCounter2,(455,375))

        # Draw restart button
        gameWindow.blit(restartIcon,(50,200))

        # Draw exit button
        gameWindow.blit(quitIcon,(950,200))

        # Restart or quit
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (cursorX,cursorY) = pygame.mouse.get_pos()
                
                # Restart game if restart button is pressed
                if cursorX > 50 and cursorX < 350 and cursorY > 200 and cursorY < 500:
                    inRestart = False
                    
                # Quit game if exit button is pressed
                if cursorX > 950 and cursorX < 1250 and cursorY > 200 and cursorY < 500:
                    inGame = False
                    inRestart = False

        # Update display, time delay 
        pygame.display.update()
     
def endScreen(messageY):
    while messageY > -500:
        # Draw background 
        gameWindow.blit(bg1,(0,0))

        # Thank you message
        graphics4 = font3.render("Thank you for playing!",1,WHITE)
        gameWindow.blit(graphics4,(350,messageY))
        
        # Authors 
        graphics5 = font4.render("Made by: Alden and Nathan",1,WHITE)
        gameWindow.blit(graphics5,(360,messageY+125))

        # Update display, time delay 
        pygame.display.update()
        pygame.time.delay(10)

        # Move text up
        messageY -= shift
    
def collision(x1,y1,w1,h1,x2,y2,w2,h2):
    # Check for collision
    if (x1+w1) >= x2 and x1 <= (x2+w2) and (y1+h1) >= y2 and y1 <= (y2+h2):
        return True
    else:
        return False

def drawMessages():
    # Render texts
    scoreGraphics = font.render("Score: "+str(offScreen),1,WHITE)
    coinGraphics = font.render("Coins: "+str(coinCount),1,WHITE)
    instructionGraphics = font3.render("Press Spacebar to use the Jetpack!",1,WHITE)

    # Draw instructional message before obstacles are cleared
    if loopCount < 150:
        gameWindow.blit(instructionGraphics,(225,150))

    # Draw timer and timer border
    gameWindow.blit(scoreGraphics,(10,10))
    gameWindow.blit(coinGraphics,(10,50))
    pygame.draw.rect(gameWindow,WHITE,(0,100,275,10))
    pygame.draw.rect(gameWindow,WHITE,(275,109,10,-150))

def drawBackground():
    gameWindow.blit(bg1,(bg1X,bg1Y))
    gameWindow.blit(bg2,(bg2X,bg2Y))

def drawPlayer():
    # Head
    pygame.draw.rect(gameWindow,SKIN,(playerX,playerY,playerW,playerH))
    pygame.draw.rect(gameWindow,BROWN,(playerX,playerY,playerW,playerH-15))
    pygame.draw.rect(gameWindow,BROWN,(playerX,playerY,playerW-15,playerH-5))
    pygame.draw.rect(gameWindow,BLACK,(playerX+12,playerY+6,playerW-15,playerH-15))
    
    # Shirt
    pygame.draw.rect(gameWindow,shirtClr,(playerX,playerY+20,playerW-5,playerH-3))

    # Arms
    pygame.draw.rect(gameWindow,BROWN,(playerX+4,playerY+20,playerW-15,playerH-10))
    pygame.draw.rect(gameWindow,BROWN,(playerX+4,playerY+27,playerW-6,playerH-15))
 
    # Pants
    pygame.draw.line(gameWindow,pantClr,(playerX+2,playerY+55),(playerX+5,playerY+37),10)

    # Shoes
    pygame.draw.rect(gameWindow,shoeClr,(playerX-2,playerY+50,playerW-7,playerH-14))

    # Jetpack
    pygame.draw.rect(gameWindow,jetpackClr,(playerX-8,playerY+25,playerW-12,playerH-14))
    pygame.draw.rect(gameWindow,jetpackClr,(playerX-22,playerY+18,playerW-5,playerH+5))

    # Draw jetpack "flame"
    if jetpackFlame == True:
        pygame.draw.polygon(gameWindow,ORANGE,((playerX-23,playerY+57),(playerX-10,playerY+57),(playerX-16,playerY+43)))

def redrawGameWindow():
    # Draw background 
    drawBackground()

    # Draw character
    drawPlayer()

    # Draw coins
    for i in range(numCoins):
        if coinVisible[i]:
            pygame.draw.ellipse(gameWindow,YELLOW,(coinX[i],coinY[i],coinW,coinH))

    # Draw obstacles
    for i in range(numObstacles):
        if obstacleVisible[i]:
            pygame.draw.rect(gameWindow,BLOODORANGE,(obstacleX[i],obstacleY[i],obstacleW,obstacleH))

    # Draw rocket
    pygame.draw.rect(gameWindow,ORANGE,(rocketX,rocketY,rocketW,rocketH))

    # Draw pause button
    if clickCount % 2 == 0:
        pygame.draw.polygon(gameWindow,BLACK,((1200,120),(1200,20),(1290,70)))
        gameWindow.blit(menuIcon,(1050,20))
    else:
        pygame.draw.rect(gameWindow,BLACK,(1200,20,20,100))
        pygame.draw.rect(gameWindow,BLACK,(1250,20,20,100))
    
    # Draw messages
    drawMessages()
    pygame.display.update()

'''
--------------------------------------------------
                    Main Program
--------------------------------------------------
'''
# Variables that save 
coinCount = 100
shirtClr = CYAN
pantClr = BLUE
shoeClr = CYAN
jetpackClr = RED

# Game loop
inGame = True
while inGame == True:
    # Declare variables
    inPlay = False
    inMenu = True
    gravity = True
    jetpack = True
    jetpackFlame = False
    shop = False
    button = False
    freeze = False
    insufficientFunds = False
    buttonType = " "
    colourChoice = " "
    offScreen = 0    
    elapsed = 0
    playerX = 320
    playerY = 642
    playerW = 20
    playerH = 20
    speedX = 10
    messageY = 600
    shift = 2.55
    loopCount = 0
    clickCount = 1
    restartCount = 0
    numObstacles = 3 # no more than 3 obstcales on the screen at once
    obstacleW = 75
    obstacleH = 325
    nextObstacle = 0
    rocketX = WIDTH + 1
    rocketY = 0
    rocketW = 50
    rocketH = 20
    rocketDelay = 100
    lastRocket = 0
    levelScore = 0 
    numCoins = 15
    nextCoin = 0
    coinW = 15
    coinH = 15
    coinSpace = 0 
    mouseX = 0
    mouseY = 0
    
    # Background properties
    bg1W = WIDTH
    bg1X = 0
    bg1Y = 0
    bg2W = WIDTH
    bg2X = WIDTH
    bg2Y = 0
    bgStep = 5
    reserveStep = 5

    # Set lists
    obstacleX = []
    obstacleY = []
    obstacleVisible = []
    coinX = []
    coinY =  []
    coinVisible = []

    # Set fps
    clock = pygame.time.Clock()
    FPS = 70

    # Generate static obstacles
    for i in range(numObstacles):           
        obstacleX.append(WIDTH)
        obstacleY.append(0)
        obstacleVisible.append(False)

    # Generate coins
    for i in range(numCoins):           
        coinX.append(WIDTH)
        coinY.append(0)
        coinVisible.append(False)

    # Menu loop
    while inMenu == True:
        
        # Prompt for start key
        pygame.event.get()
        keys = pygame.key.get_pressed()

        # Call menu function
        if shop == False:
            startGame()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (cursorX,cursorY) = pygame.mouse.get_pos()
                    if cursorX > -30 and cursorX < 170 and cursorY > -20 and cursorY < 180:
                        shop = True
                        
        # Draw shop if clicked
        if shop == True:
            shopWindow()

        # Start Game 
        if keys[pygame.K_SPACE]:
            inMenu = False 
            inPlay = True
            
        # Esc to quit    
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

    # Gameplay loop
    while inPlay == True:
     
        # Increment loop counter
        loopCount += 1 
        
        # Call function to draw game 
        redrawGameWindow()
                            
        # Set fps 
        clock.tick(FPS)

        # Pause button - freeze the game
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (cursorX,cursorY) = pygame.mouse.get_pos()
                if cursorX > 1200 and cursorX < 1290 and cursorY > 20 and cursorY < 120:
                    clickCount += 1
                if cursorX > 1050 and cursorX < 1150 and cursorY > 20 and cursorY < 120:
                    inMenu = True
                    inPlay = False
        # Pause game
        if clickCount % 2 == 0:
            bgStep = 0
            gravity = False
            jetpack = False

        # Play game 
        else:
            bgStep = reserveStep
            gravity = True
            jetpack = True
            
        # Get user input
        pygame.event.get()

        # Keyboard input          
        keys = pygame.key.get_pressed()

        # ESC to quit
        if keys[pygame.K_ESCAPE]:           
            inPlay = False

        # Jetpack
        if jetpack == True:

            # Press spacebar to use "jetpack"
            if keys[pygame.K_SPACE]:

                # Move player up 
                playerY -= 20
                
                # Draw jetpack flame
                jetpackFlame = True

                # Stops the character at the top of the screen 
                if playerY < -5:
                    playerY = -5

            # No flame when jetpack isn't in use
            else:
                jetpackFlame = False

        # Gravity
        if gravity == True:
            playerY += 8
        
        # Stops the character at the bottom of the screen
        if playerY > 642:
            playerY = 642

        # Scroll the background
        bg1X = bg1X - bgStep
        if bg1X - bgStep < 0 - bg1W: 
            bg1X += bg2W*2
        bg2X = bg2X - bgStep
        if bg2X - bgStep < 0 - bg2W:
            bg2X += bg1W*2

        # Update static obstacle positions
        obstaclePosition = 0
        for i in range(numObstacles):
            if obstacleVisible[i] == True:
                obstacleX[i] -= bgStep

                # Check for collision
                if collision(playerX,playerY,playerW,playerH+36,obstacleX[i],obstacleY[i],obstacleW,obstacleH):
                    inPlay = False

                # Add to score when obstacles go offscreen
                if obstacleX[i] < -75:
                    offScreen += 1
                    levelScore += 1
                    obstacleVisible[i] = False
                elif obstacleX[i] > obstaclePosition:
                    obstaclePosition = obstacleX[i]
            
        # Add new obstacle if needed
        if obstaclePosition < (WIDTH - randint(600,1000)):
            obstacleX[nextObstacle] = WIDTH
            obstacleY[nextObstacle] = randint(TOP,HEIGHT - obstacleH)
            obstacleVisible[nextObstacle] = True
            nextObstacle += 1
            nextObstacle = nextObstacle % 3

        # Detect when rocket is offscreen
        if rocketX <= -rocketW:
            rocketDelay = randint(50,200)

            # Add to score when rocket goes offscreen
            offScreen += 1
            levelScore += 1
            rocketX = WIDTH + 1

        # Move rocket if onscreen
        if rocketX > -rocketW and rocketX <= WIDTH:
            rocketX -= bgStep*3

            # Check for collision
            if collision(playerX,playerY,playerW,playerH+36,rocketX,rocketY,rocketW,rocketH):
                inPlay = False
        
        # Create new rocket when needed    
        elif loopCount - lastRocket > rocketDelay:
            rocketX = WIDTH
            rocketY = randint(200,500-rocketH)
            lastRocket = loopCount

        # Update coin positions
        coinPosition = 0
        for i in range(numCoins):
            if coinVisible[i] == True:
                coinX[i] -= bgStep

                # Check for collision
                if collision(playerX,playerY,playerW,playerH+36,coinX[i],coinY[i],coinW,coinH):
                    coinSound.play()
                    coinCount += 1
                    coinVisible [i] = False
                    
                # Offscreen coins
                if coinX[i] < -15:
                    coinVisible[i] = False
                elif coinX[i] > coinPosition:
                    coinPosition = coinX[i]
            
        # Add new coins if needed
        if coinPosition < (WIDTH - randint(200,400)):
            coinX[nextCoin] = WIDTH
            coinY[nextCoin] = randint(150,550)
            coinVisible[nextCoin] = True
            nextCoin += 1
            nextCoin = nextCoin % -15

        # Difficulty increase after intervals of 10 
        if levelScore >= 10:
            bgStep += 1
            reserveStep += 1
            levelScore = 0

    # Prompt for the user to restart or quit
    if inMenu == False:
        restartScreen()
    
# End messages
pygame.mixer.music.stop()
endScreen(messageY)
            
# Quit game when loop ends 
pygame.quit()

# Credits 
print (" Thank you for playing!")
print (" Made by: Alden and Nathan")

