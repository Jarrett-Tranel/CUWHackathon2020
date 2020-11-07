import pygame
from pygame import mixer 
import time
import random 

mixer.init()
pygame.init()   

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 70, 0)
GREEN2 = (0, 200, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
LIGHTBLUE = (0, 0, 130)

twoDArray = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]]

# define the RGB value for white, 
# green, blue colour . 
scoreTextWhite = (255, 255, 255) 
scoreTextgreen = (0, 255, 0) 
scoreTextblue = (0, 0, 128) 

# set the pygame window name 
pygame.display.set_caption('Show Text') 



#random.seed(30)
for i in range(0, 10):
     for j in range(0, 10):
        ranNum = random.randint(0, 3)
        if ranNum == 0:
            twoDArray[i][j] = 1

#creating the door out
randx = random.randint(0, 1)
if randx == 1:
    randx = 9
randy = random.randint(0, 9)
twoDArray[randx][randy] = 2

#Creating the enemy
randx = random.randint(0, 9)
randy = random.randint(0, 9)
twoDArray[randx][randy] = 3
enemylocation = [randx, randy]


X = 700
Y = 500
size = [X, Y]



screen = pygame.display.set_mode(size)

font = pygame.font.Font('freesansbold.ttf', 32) 

titleText = font.render('MAZE', True, GREY, scoreTextblue) 
titleText2 = font.render('ESCAPE', True, GREY, scoreTextblue) 
text = font.render('Score', True, scoreTextgreen, scoreTextblue) 
scoreNumber = font.render("0",True,scoreTextgreen,scoreTextblue)

titleRect = titleText.get_rect()
titleRect2 = titleText2.get_rect() 
textRect = text.get_rect() 
scoreNumberTextRect = scoreNumber.get_rect()

# set the center of the rectangular object. 
titleRect.center = (X -70, Y -450)
titleRect2.center = (X -70, Y -410)
textRect.center = (X -70, Y // 3)
scoreNumberTextRect.center = (X - 70 , Y-250) 

#time.sleep(2)
#pygame.mixer.music.stop()

done = False 
#Music
#Controls
#Drawing shapes- 10/10 grid
#Array keeping track of each grid status
#Endings
rect_x = 50
rect_y = 5

x_speed = 0
y_speed = 0

clock = pygame.time.Clock()

while not done: 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -50
            elif event.key == pygame.K_RIGHT:
                x_speed = 50
            elif event.key == pygame.K_UP:
                y_speed = -50
            elif event.key == pygame.K_DOWN:
                y_speed = 50
            else:
                ranNum = random.randint(0, 1)
                if (ranNum == 0):
                    time.sleep(2)
                    twoDArray[enemylocation[0]][enemylocation[1]] = 0
                    twoDArray[enemylocation[0] - 1][enemylocation[1]] = 3
                    enemylocation[0] = enemylocation[0] - 1
                elif (ranNum == 1):
                    time.sleep(2)
                    twoDArray[enemylocation[0]][enemylocation[1]] = 0
                    twoDArray[enemylocation[0] + 1][enemylocation[1]] = 3
                    enemylocation[0] = enemylocation[0] + 1
                    

              
    
    rect_x = rect_x + x_speed
    rect_y = rect_y + y_speed
    x_speed = 0
    y_speed = 0
    screen.fill(GREEN)

    for i in range(0, 10):
        for j in range(0, 10):
            colorToDraw = GREEN2
            if twoDArray [i][j] == 1:
                colorToDraw = GREY
            elif twoDArray[i][j] == 2:
                colorToDraw = LIGHTBLUE
            pygame.draw.rect(screen, colorToDraw, [rect_x + (i * 50), rect_y + (j * 50), 40, 40])

  
    screen.blit(text, textRect) 
    screen.blit(scoreNumber, scoreNumberTextRect)
    screen.blit(titleText,titleRect)
    screen.blit(titleText2,titleRect2)
    
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)



		