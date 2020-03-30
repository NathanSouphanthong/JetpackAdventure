#Arshia M and Zane Y
#Jan 15, 2018
#DDRGame.py
#A game mimicking Dance Dance Revolution on python where the user must match the arrows on the screen to the static arrow on top to the rythm of the music
from math import sqrt
from random import randint
import pygame
#Game Window Properties
WIDTH = 800
HEIGHT= 600
TOP = 0
pygame.init()
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.SysFont("COPPERPLATE GOTHIC",80)
font2 = pygame.font.SysFont("COPPERPLATE GOTHIC",150)
font3 = pygame.font.SysFont("COPPERPLATE GOTHIC",50)
font4 = pygame.font.SysFont("COPPERPLATE GOTHIC",40)
font5 = pygame.font.SysFont("Calibri", 45)
font6 = pygame.font.SysFont("Consolas",70)
font7 = pygame.font.SysFont("Consolas",25)
font8 = pygame.font.SysFont("Consolas",20)
font9 = pygame.font.SysFont("Lucida Console",70)
font10 = pygame.font.SysFont("Consolas",25)
font11 = pygame.font.SysFont("Consolas",20)


#---------------------------------------#
#               Colours                 #
#---------------------------------------#
RED  =(178, 17, 17)
GREEN=(0,255,0)
BLUE =(0,0,255)
CYAN =(0,255,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
GREY =(128,128,128)
GREYL = (0, 255, 246)
YELLOW = (238, 244, 66)
ORANGE = (234, 151, 7)
BROWN = (104, 73, 33)
PINK = (255,105,180)
PURPLE = (202, 101, 211)
LBLUE = (95, 151, 239)
DSBLUE=(30,144,255)
 
#---------------------------------------#
#              Properties               #
#---------------------------------------#
numPoints = 0
moderate = 0
insane = 0
ratingColour = WHITE
upArrowY = 800
downArrowY = 300
leftArrowY = 900
rightArrowY = 655
arrowSpeed = 0
numArrows = 0
rating = "Get Ready!"
readySpace = "Press Space to Start"
amatuer = 0
difficulty = 3
#difficulty = input("Enter difficulty:")
picture = pygame.image.load("dance.jpg")
spacebarPic = pygame.image.load("Spacbar.png")
numArrowsMissed = 0
if difficulty == 1:
    arrowSpeed = 4
elif difficulty == 2:
    arrowSpeed = 8
elif difficulty == 3:
    arrowSpeed = 13
#Arrow Coordinates
#Moving Arrows    
#Static Arrows
upStaticArrowY = -50
downStaticArrowY = 390
#Animation Timing
BEGIN = pygame.time.get_ticks()
clock = pygame.time.Clock()
FPS = 60
#---------------------------------------#
#              Functions                #
#---------------------------------------#
def mainScreen():
    mainMenuPic = pygame.image.load("something.png")
    gameWindow.blit(mainMenuPic,(0,0))
    width = mainMenuPic.get_width()
    height = mainMenuPic.get_height()
    
def arrowdown():    
    arrow = pygame.image.load("unnamed.png")
    gameWindow.blit(arrow,(80,139))
    width = arrow.get_width()
    height =arrow.get_height()
    
def arrowright():    
    arrow = pygame.image.load("unnamed2.png")
    gameWindow.blit(arrow,(150,80))
    width = arrow.get_width()
    height =arrow.get_height()
    
def arrowleft():    
    arrow = pygame.image.load("unnamed3.png")
    gameWindow.blit(arrow,(10,80))
    width = arrow.get_width()
    height =arrow.get_height()
    
def arrowup():    
    arrow = pygame.image.load("unnamed4.png")
    gameWindow.blit(arrow,(80,20))
    width = arrow.get_width()
    height = arrow.get_height()
    
def shape1():    
    shape = pygame.image.load("shapes1p.png")
    gameWindow.blit(shape,(10,450))
    width = shape.get_width()
    height = shape.get_height()
    
def shape2():    
    shape = pygame.image.load("shapes1p.png")
    gameWindow.blit(shape,(670,450))
    width = shape.get_width()
    height = shape.get_height()

def background():
    background = pygame.image.load("picb.png")
    gameWindow.blit(background,(0,0))
    width = background.get_width()
    height = background.get_height()
    
def shapes():
    shapes = pygame.image.load("dancing.png")
    gameWindow.blit(shapes,(530,300))
    width = shapes.get_width()
    height = shapes.get_height()
def keyboard():
    keyboard = pygame.image.load("keyboard.png")
    gameWindow.blit(keyboard,(25,180))
    width = keyboard.get_width()
    height = keyboard.get_height()
def pic123():
    pic123 = pygame.image.load("pic123.png")
    gameWindow.blit(pic123,(380,220))
    width = pic123.get_width()
    height = pic123.get_height()
    
def upArrowAnimation():
    pygame.draw.rect(gameWindow, GREYL,(500,upArrowY+300,40,70))
    pygame.draw.polygon(gameWindow, GREYL,((500,upArrowY+370),(510,upArrowY+380),(520,upArrowY+370)))
    pygame.draw.polygon(gameWindow, GREYL,((520,upArrowY+370),(530,upArrowY+380),(540,upArrowY+370)))
    pygame.draw.polygon(gameWindow, GREYL,((510,upArrowY+380),(520,upArrowY+370),(530,upArrowY+380)))
    pygame.draw.rect(gameWindow, GREYL, (480,upArrowY+300,80,10))
    pygame.draw.polygon(gameWindow, GREYL,((480,upArrowY+300),(520,upArrowY+250),(560,upArrowY+300)))
    pygame.draw.polygon(gameWindow, GREYL,((480,upArrowY+310),(490,upArrowY+320),(490,upArrowY+310)))
    pygame.draw.rect(gameWindow, GREYL,(490,upArrowY+310,10,10))
    pygame.draw.polygon(gameWindow, GREYL,((560,upArrowY+310),(550,upArrowY+320),(550,upArrowY+310)))
    pygame.draw.rect(gameWindow, GREYL,(540,upArrowY+310,10,10))
def downArrowAnimation():
    pygame.draw.rect(gameWindow,GREYL,(280,400+downArrowY,40,70))
    pygame.draw.rect(gameWindow,GREYL,(260,470+downArrowY,80,10))
    pygame.draw.rect(gameWindow,GREYL,(270,460+downArrowY,60,10))
    pygame.draw.polygon(gameWindow,GREYL,((260,480+downArrowY),(300,530+downArrowY),(340,480+downArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((260,470+downArrowY),(270,460+downArrowY),(270,470+downArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((340,470+downArrowY),(330,460+downArrowY),(330,470+downArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((280,400+downArrowY),(290,390+downArrowY),(300,400+downArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((300,400+downArrowY),(310,390+downArrowY),(320,400+downArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((290,390+downArrowY),(300,400+downArrowY),(310,390+downArrowY)))
def leftArrowAnimation():
    pygame.draw.rect(gameWindow, GREYL,(60,40+leftArrowY,70,40))
    pygame.draw.rect(gameWindow, GREYL,(50,20+leftArrowY,10,80))
    pygame.draw.rect(gameWindow, GREYL,(60,30+leftArrowY,10,60))
    pygame.draw.polygon(gameWindow, GREYL,((50,20+leftArrowY),(0,60+leftArrowY),(50,100+leftArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((60,20+leftArrowY),(70,30+leftArrowY),(60,30+leftArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((60,100+leftArrowY),(70,90+leftArrowY),(60,90+leftArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((130,40+leftArrowY),(140,50+leftArrowY),(130,60+leftArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((130,60+leftArrowY),(140,70+leftArrowY),(130,80+leftArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((140,50+leftArrowY),(130,60+leftArrowY),(140,70+leftArrowY)))
    
def rightArrowAnimation():
    pygame.draw.rect(gameWindow, GREYL,(660,40+rightArrowY,70,40))
    pygame.draw.rect(gameWindow, GREYL,(730,20+rightArrowY,10,80))
    pygame.draw.polygon(gameWindow, GREYL,((740,20+rightArrowY),(790,60+rightArrowY),(740,100+rightArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((730,20+rightArrowY),(720,30+rightArrowY),(730,30+rightArrowY)))
    pygame.draw.rect(gameWindow, GREYL,(720,30+rightArrowY,10,60))
    pygame.draw.polygon(gameWindow, GREYL,((720,90+rightArrowY),(730,100+rightArrowY),(730,90+rightArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((660,40+rightArrowY),(650,50+rightArrowY),(660,60+rightArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((660,60+rightArrowY),(650,70+rightArrowY),(660,80+rightArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((650,50+rightArrowY),(660,60+rightArrowY),(650,70+rightArrowY)))
    
def redrawGameWindow():
    upArrowAnimation()
    downArrowAnimation()
    leftArrowAnimation()
    rightArrowAnimation()
    
def distance(x1, y1, x2, y2):           
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def drawUpArrow():
    pygame.draw.rect(gameWindow, GREYL,(500,upStaticArrowY+100,40,70))
    pygame.draw.polygon(gameWindow, GREYL,((500,upStaticArrowY+170),(510,upStaticArrowY+180),(520,upStaticArrowY+170)))
    pygame.draw.polygon(gameWindow, GREYL,((520,upStaticArrowY+170),(530,upStaticArrowY+180),(540,upStaticArrowY+170)))
    pygame.draw.polygon(gameWindow, GREYL,((510,upStaticArrowY+180),(520,upStaticArrowY+170),(530,upStaticArrowY+180)))
    pygame.draw.rect(gameWindow, GREYL, (480,upStaticArrowY+100,80,10))
    pygame.draw.polygon(gameWindow, GREYL,((480,upStaticArrowY+100),(520,upStaticArrowY+50),(560,upStaticArrowY+100)))
    pygame.draw.polygon(gameWindow, GREYL,((480,upStaticArrowY+110),(490,upStaticArrowY+120),(490,upStaticArrowY+110)))
    pygame.draw.rect(gameWindow, GREYL,(490,upStaticArrowY+110,10,10))
    pygame.draw.polygon(gameWindow, GREYL,((560,upStaticArrowY+110),(550,upStaticArrowY+120),(550,upStaticArrowY+110)))
    pygame.draw.rect(gameWindow, GREYL,(540,upStaticArrowY+110,10,10))
def drawDownArrow():
    pygame.draw.rect(gameWindow,GREYL,(280,400-downStaticArrowY,40,70))
    pygame.draw.rect(gameWindow,GREYL,(260,470-downStaticArrowY,80,10))
    pygame.draw.rect(gameWindow,GREYL,(270,460-downStaticArrowY,60,10))
    pygame.draw.polygon(gameWindow,GREYL,((260,480-downStaticArrowY),(300,530-downStaticArrowY),(340,480-downStaticArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((260,470-downStaticArrowY),(270,460-downStaticArrowY),(270,470-downStaticArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((340,470-downStaticArrowY),(330,460-downStaticArrowY),(330,470-downStaticArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((280,400-downStaticArrowY),(290,390-downStaticArrowY),(300,400-downStaticArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((300,400-downStaticArrowY),(310,390-downStaticArrowY),(320,400-downStaticArrowY)))
    pygame.draw.polygon(gameWindow, GREYL,((290,390-downStaticArrowY),(300,400-downStaticArrowY),(310,390-downStaticArrowY)))
def drawLeftArrow():
    pygame.draw.rect(gameWindow, GREYL,(60,40,70,40))
    pygame.draw.rect(gameWindow, GREYL,(50,20,10,80))
    pygame.draw.rect(gameWindow, GREYL,(60,30,10,60))
    pygame.draw.polygon(gameWindow, GREYL,((50,20),(0,60),(50,100)))
    pygame.draw.polygon(gameWindow, GREYL,((60,20),(70,30),(60,30)))
    pygame.draw.polygon(gameWindow, GREYL,((60,100),(70,90),(60,90)))
    pygame.draw.polygon(gameWindow, GREYL,((130,40),(140,50),(130,60)))
    pygame.draw.polygon(gameWindow, GREYL,((130,60),(140,70),(130,80)))
    pygame.draw.polygon(gameWindow, GREYL,((140,50),(130,60),(140,70)))
def drawRightArrow():
    pygame.draw.rect(gameWindow, GREYL,(660,40,70,40))
    pygame.draw.rect(gameWindow, GREYL,(730,20,10,80))
    pygame.draw.polygon(gameWindow, GREYL,((740,20),(790,60),(740,100)))
    pygame.draw.polygon(gameWindow, GREYL,((730,20),(720,30),(730,30)))
    pygame.draw.rect(gameWindow, GREYL,(720,30,10,60))
    pygame.draw.polygon(gameWindow, GREYL,((720,90),(730,100),(730,90)))
    pygame.draw.polygon(gameWindow, GREYL,((660,40),(650,50),(660,60)))
    pygame.draw.polygon(gameWindow, GREYL,((660,60),(650,70),(660,80)))
    pygame.draw.polygon(gameWindow, GREYL,((650,50),(660,60),(650,70)))
def animation():
    gameWindow.blit(picture, (0,0))
    graphics = font5.render("Score: "+str(numPoints),150,WHITE)
    gameWindow.blit(graphics, (325,150))
    text = font5.render(rating,150,ratingColour)
    gameWindow.blit(text, (325,190))
    drawUpArrow()
    drawDownArrow()
    drawLeftArrow()
    drawRightArrow()
    redrawGameWindow()
    pygame.time.delay(1) 
    pygame.display.update()
    clock.tick(FPS)

def button(x,y,w,h,action):
    global mainMenu
    global controls
    global start
    
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            if click[0] == 1 and action == "Play":
                start = True
                mainMenu = False
            if click[0] == 1 and action == "Options":
                controls = True
                mainMenu = False
            if click[0] == 1 and action == "Back":
                mainMenu = True
                controls = False
                 
            

def flame():
    fire = pygame.image.load("fire.png")
    gameWindow.blit(fire ,(530,195))
    width = fire.get_width()
    height = fire.get_height()

def background2():
    background = pygame.image.load("picb2.png")
    gameWindow.blit(background,(0,0))
    width = background.get_width()
    height = background.get_height()

def arrowdown2():    
    arrow = pygame.image.load("unnamed.png")
    gameWindow.blit(arrow,(80,139))
    width = arrow.get_width()
    height =arrow.get_height()
def arrowright2():    
    arrow = pygame.image.load("unnamed2.png")
    gameWindow.blit(arrow,(150,80))
    width = arrow.get_width()
    height =arrow.get_height()
def arrowleft2():    
    arrow = pygame.image.load("unnamed3.png")
    gameWindow.blit(arrow,(10,80))
    width = arrow.get_width()
    height =arrow.get_height()
def arrowup2():    
    arrow = pygame.image.load("unnamed4.png")
    gameWindow.blit(arrow,(80,20))
    width = arrow.get_width()
    height = arrow.get_height()
            
            
                
     
#---------------------------------------#
#            Main Program
#---------------------------------------#
#Main Animations
numPerfects = 0
numGoods = 0
numOkays = 0
numBads = 0
endScreen = False
mainMenu = True
start = False
controls = False
inPlay = False
difficulty = False

while difficulty:
    background2()
    graphics = font9.render("DIFFICULTY",1,DSBLUE)
    gameWindow.blit(graphics,(280,40))
    graphics = font10.render("Select Your Difficulty...",1,BLACK)
    gameWindow.blit(graphics,(290,150))
    flame()
    pygame.draw.rect(gameWindow, ORANGE,(50,300,200,30))
    pygame.draw.rect(gameWindow, ORANGE,(60,290,80,50))
    pygame.draw.rect(gameWindow, LBLUE,(50,300,200,30),3)
    pygame.draw.rect(gameWindow, ORANGE,(60,290,180,50))
    pygame.draw.rect(gameWindow, ORANGE,(300,300,200,30))
    pygame.draw.rect(gameWindow, ORANGE,(310,290,80,50))
    pygame.draw.rect(gameWindow, LBLUE,(300,300,200,30),3)
    pygame.draw.rect(gameWindow, ORANGE,(310,290,180,50))
    pygame.draw.rect(gameWindow, ORANGE,(550,300,200,30))
    pygame.draw.rect(gameWindow, ORANGE,(560,290,80,50))
    pygame.draw.rect(gameWindow, LBLUE,(550,300,200,30),3)
    pygame.draw.rect(gameWindow, ORANGE,(560,290,180,50))
    graphics = font10.render("EASY",1,WHITE)
    gameWindow.blit(graphics,(120,305))
    graphics = font11.render("Soft, mainly for",1,BLACK)
    gameWindow.blit(graphics,(60,340))
    graphics = font11.render("begginners",1,BLACK)
    gameWindow.blit(graphics,(60,360))
    graphics = font10.render("MODERATE",1,WHITE)
    gameWindow.blit(graphics,(350,305))
    graphics = font11.render("A little harder",1,BLACK)
    gameWindow.blit(graphics,(300,340))
    graphics = font11.render("no biggie",1,BLACK)
    gameWindow.blit(graphics,(300,360))
    graphics = font10.render("INSANE",1,WHITE)
    gameWindow.blit(graphics,(610,305))
    graphics = font11.render("For the best",1,BLACK)
    gameWindow.blit(graphics,(550,340))
    graphics = font11.render("and only for the best",1,BLACK)
    gameWindow.blit(graphics,(550,360))
    arrowup()
    arrowleft()
    arrowright()
    arrowdown()
    flame()
    pygame.display.update()

while mainMenu:
    mainScreen()
    #Title (Dance Mania)
    graphics = font2.render("D",1,CYAN)
    gameWindow.blit(graphics,(250,50))
    graphics = font.render("ANCE",7,WHITE)
    gameWindow.blit(graphics,(370,65))
    graphics = font2.render("M",7,RED)
    gameWindow.blit(graphics,(450,140))
    graphics = font.render("ANIA",7,WHITE)
    gameWindow.blit(graphics,(580,155))
    #Outline for title
    pygame.draw.rect(gameWindow, WHITE,(370,140,250,5))
    pygame.draw.rect(gameWindow, WHITE,(580,230,250,5))
    #buttons
    pygame.draw.rect(gameWindow, LBLUE,(200,360,400,30))
    button(200,360,400,30,"Play")
    pygame.draw.rect(gameWindow, LBLUE,(210,350,80,50))
    button(210,350,80,50,"Play")
    pygame.draw.rect(gameWindow, PURPLE,(200,360,400,30),3)
    button(200,360,400,30,"Play")
    pygame.draw.rect(gameWindow, LBLUE,(210,350,380,50))
    button(210,350,380,50,"Play")
    graphics = font4.render("PLAY",7,WHITE)
    gameWindow.blit(graphics,(345,355))
    pygame.draw.rect(gameWindow, LBLUE,(200,450,400,30))
    button(200,450,400,30,"Options")
    pygame.draw.rect(gameWindow, LBLUE,(210,440,80,50))
    button(210,440,80,50,"Options")
    pygame.draw.rect(gameWindow, PURPLE,(200,450,400,30),3)
    button(200,450,420,30,"Options")
    pygame.draw.rect(gameWindow, LBLUE,(210,440,380,50))
    button(210,440,380,50,"Options")
    graphics = font4.render("OPTIONS",7,WHITE)
    gameWindow.blit(graphics,(300,445))
    arrowup()
    arrowleft()
    arrowright()
    arrowdown()
    shape1()
    shape2()
    pygame.display.update()


while controls:
    background()
    shapes()
    graphics = font6.render("INSTRUCTIONS",1,WHITE)
    gameWindow.blit(graphics,(20,40))
    graphics = font7.render("The main objective of this game is to match",1,WHITE)
    gameWindow.blit(graphics,(25,120))
    graphics = font7.render("the arrows with the static ones on screen",1,WHITE)
    gameWindow.blit(graphics,(25,145))
    graphics = font8.render("You can utilize the",1,BLACK)
    gameWindow.blit(graphics,(25,340))
    graphics = font8.render("arrow keys on your keyboard",1,BLACK)
    gameWindow.blit(graphics,(25,360))
    keyboard()
    pic123()
    graphics = font8.render("Example of the game",1,BLACK)
    gameWindow.blit(graphics,(355,355))
    graphics = font8.render("When you run the game, in the Python Shell",1,BLACK)
    gameWindow.blit(graphics,(10,460))
    graphics = font8.render("there is an option to choose your difficulty",1,BLACK)
    gameWindow.blit(graphics,(10,480))
    pygame.draw.rect(gameWindow, WHITE,(40,540,100,20))
    button(40,540,110,20,"Back")
    pygame.draw.rect(gameWindow, BLACK,(40,540,100,20),1)
    pygame.draw.rect(gameWindow, WHITE,(50,530,80,40))
    button(50,530,80,40,"Back")
    graphics = font8.render("BACK",1,BLACK)
    gameWindow.blit(graphics,(65,540))
    pygame.display.update()

    
while start:
    gameWindow.fill(WHITE) 
    gameWindow.blit(picture, (0,0))
    ready = font5.render(readySpace,100,ratingColour)
    gameWindow.blit(ready, (225,280))
    gameWindow.blit(spacebarPic, (245,325))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                inPlay = True
                start = False
            
while inPlay:
    animation()
    upArrowY =  upArrowY - arrowSpeed
    downArrowY = downArrowY - arrowSpeed
    leftArrowY = leftArrowY - arrowSpeed
    rightArrowY = rightArrowY - arrowSpeed
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if distance(70,upStaticArrowY+50,70,upArrowY+250) >= 0 and distance(70,upStaticArrowY+50,70,upArrowY+250) <= 5:
                    numPoints = numPoints + 5
                    rating = "Perfect!"
                    upArrowY = randint(600,700)
                    numArrows = numArrows + 1
                    ratingColour = YELLOW
                    numPerfects = numPerfects + 1
                if distance(70,upStaticArrowY+50,70,upArrowY+250) >= 6 and distance(70,upStaticArrowY+50,70,upArrowY+250) <= 15:
                    numPoints = numPoints + 3
                    rating = "Good!"
                    ratingColour = GREEN
                    upArrowY = randint(600,700)
                    numArrows = numArrows + 1
                    numGoods = numGoods + 1
                if distance(70,upStaticArrowY+50,70,upArrowY+250) >= 16 and distance(70,upStaticArrowY+50,70,upArrowY+250) <= 28:
                    numPoints = numPoints + 1
                    rating = "Okay"
                    upArrowY = randint(600,700)
                    ratingColour = ORANGE
                    numArrows = numArrows + 1
                    numOkays = numOkays + 1
                if distance(70,upStaticArrowY+50,70,upArrowY+250) >= 29 and distance(70,upStaticArrowY+50,70,upArrowY+250) <= 34:
                    rating = "Bad."
                    upArrowY = randint(600,700)
                    ratingColour = BROWN
                    numArrows = numArrows + 1
                    numBads = numBads + 1
                if distance(70,upStaticArrowY+50,70,upArrowY+250) > 35 and distance(70,upStaticArrowY+50,70,upArrowY+250) < 600:
                    numPoints = numPoints - 3
                    rating = "Miss"
                    upArrowY = randint(600,700)
                    ratingColour = RED
                    numArrows = numArrows + 1
                    numArrowsMissed = numArrowsMissed + 1
            if event.key == pygame.K_DOWN:
                if distance(300,530-downStaticArrowY,300,530+downArrowY) >= 0 and distance(300,530-downStaticArrowY,300,530+downArrowY) <= 5:
                    numPoints = numPoints + 5
                    rating = "Perfect!"
                    downArrowY = randint(600,700)
                    ratingColour = YELLOW
                    numArrows = numArrows + 1
                    numPerfects = numPerfects + 1
                if distance(300,530-downStaticArrowY,300,530+downArrowY) >= 6 and distance(300,530-downStaticArrowY,300,530+downArrowY) <= 15:
                    numPoints = numPoints + 3
                    rating = "Good!"
                    downArrowY = randint(600,700)
                    ratingColour = GREEN
                    numArrows = numArrows + 1
                    numGoods = numGoods + 1
                if distance(300,530-downStaticArrowY,300,530+downArrowY) >= 16 and distance(300,530-downStaticArrowY,300,530+downArrowY) <= 28:
                    numPoints = numPoints + 1
                    rating = "Okay"
                    downArrowY = randint(600,700)
                    ratingColour = ORANGE
                    numArrowsMissed = numArrowsMissed + 1
                    numOkays = numOkays + 1
                if distance(0,60,0,60+leftArrowY) >= 29 and distance(0,60,0,60+leftArrowY) <= 34:
                    rating = "Bad."
                    downArrowY = randint(600,700)
                    ratingColour = BROWN
                    numArrows = numArrows + 1
                    numBads = numBads + 1
                if distance(0,60,0,60+leftArrowY) > 35 and distance(0,60,0,60+leftArrowY) < 600:
                    numPoints = numPoints - 3
                    rating = "Miss"
                    downArrowY = randint(600,700)
                    ratingColour = RED
                    numArrows = numArrows + 1
                    numArrowsMissed = numArrowsMissed + 1
            if event.key == pygame.K_LEFT:
                if distance(0,60,0,60+leftArrowY) >= 0 and distance(0,60,0,60+leftArrowY) <= 5:
                    numPoints = numPoints + 5
                    rating = "Perfect!"
                    leftArrowY = randint(600,700)
                    ratingColour = YELLOW
                    numArrows = numArrows + 1
                    numPerfects = numPerfects + 1
                if distance(0,60,0,60+leftArrowY) >= 6 and distance(0,60,0,60+leftArrowY) <= 15:
                    numPoints = numPoints + 3
                    rating = "Good!"
                    leftArrowY = randint(600,700)
                    ratingColour = GREEN
                    numArrows = numArrows + 1
                    numGoods = numGoods + 1
                if distance(0,60,0,60+leftArrowY) >= 16 and distance(0,60,0,60+leftArrowY) <= 28:
                    numPoints = numPoints + 1
                    rating = "Okay"
                    leftArrowY = randint(600,700)
                    ratingColour = ORANGE
                    numArrows = numArrows + 1
                    numOkays = numOkays + 1
                if distance(0,60,0,60+leftArrowY) >= 29 and distance(0,60,0,60+leftArrowY) <= 34:
                    rating = "Bad."
                    leftArrowY = randint(600,700)
                    ratingColour = BROWN
                    numArrows = numArrows + 1
                    numBads = numBads + 1
                if distance(0,60,0,60+leftArrowY) > 35 and distance(0,60,0,60+leftArrowY) < 600:
                    numPoints = numPoints - 3
                    rating = "Miss"
                    leftArrowY = randint(600,700)
                    ratingColour = RED
                    numArrows = numArrows + 1
                    numArrowsMissed = numArrowsMissed + 1
            if event.key == pygame.K_RIGHT:
                if distance(790,60,790,60+rightArrowY) >= 0 and distance(790,60,790,60+rightArrowY) <= 5:
                    numPoints = numPoints + 5
                    rating = "Perfect!"
                    rightArrowY = randint(600,700)
                    ratingColour = YELLOW
                    numArrows = numArrows + 1
                    numPerfects = numPerfects + 1
                if distance(790,60,790,60+rightArrowY) >= 6 and distance(790,60,790,60+rightArrowY) <= 15:
                    numPoints = numPoints + 3
                    rating = "Good!"
                    rightArrowY = randint(600,700)
                    ratingColour = GREEN
                    numArrows = numArrows + 1
                    numGoods = numGoods + 1
                if distance(790,60,790,60+rightArrowY) >= 16 and distance(790,60,790,60+rightArrowY) <= 28:
                    numPoints = numPoints + 1
                    rating = "Okay"
                    rightArrowY = randint(600,700)
                    ratingColour = ORANGE
                    numArrows = numArrows + 1
                    numOkays = numOkays + 1
                if distance(790,60,790,60+rightArrowY) >= 29 and distance(790,60,790,60+rightArrowY) <= 34:
                    rating = "Bad."
                    rightArrowY = randint(600,700)
                    ratingColour = BROWN
                    numArrows = numArrows + 1
                    numBads = numBads + 1
                if distance(790,60,790,60+rightArrowY) > 35 and distance(790,60,790,60+rightArrowY) < 600:
                    numPoints = numPoints - 3
                    rating = "Miss"
                    rightArrowY = randint(600,700)
                    ratingColour = RED
                    numArrows = numArrows + 1
                    numArrowsMissed = numArrowsMissed + 1
                
    if upArrowY < -400:
        rating = "Miss"
        upArrowY = randint(600,700)
        numPoints = numPoints - 3
        ratingColour = RED
        numArrows = numArrows + 1
        numArrowsMissed = numArrowsMissed + 1
    if downArrowY < -550:
        rating = "Miss"
        downArrowY = randint(600,700)
        numPoints = numPoints - 3
        ratingColour = RED
        numArrows = numArrows + 1
        numArrowsMissed = numArrowsMissed + 1
    if leftArrowY < -450:
        leftArrowY = randint(600,700)
        rating = "Miss"
        numPoints = numPoints - 3
        ratingColour = RED
        numArrows = numArrows + 1
        numArrowsMissed = numArrowsMissed + 1
    if rightArrowY < -470:
        rightArrowY = randint(600,700)
        rating = "Miss"
        numPoints = numPoints - 3
        ratingColour = RED
        numArrows = numArrows + 1
        numArrowsMissed = numArrowsMissed + 1
    if numPoints < -20:
        inPlay = False
        endScreen  = True
        print "You Lost!"
        print "You missed too many arrows("+str(numArrowsMissed)+")"
        
    if numArrows == 200:
        inPlay = False
        endScreen = True
        print "Gameover!"
#while endScreen:
    
        
        
            
            
            
                
    
                
    
       
                
pygame.time.delay(1) 
pygame.display.update()
    
                      
pygame.quit()
#End Result
