#Project created by Jarrett Tranel, Trevor Krentz, Ross Jacobson, and Ishtiyaq Ahmed on 11/7/20
import pygame
from pygame import mixer 

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

#random.seed(30)
for i in range(0, 10):
     for j in range(0, 10):
        ranNum = random.randint(0, 3)
        if ranNum == 0:
            twoDArray[i][j] = 1

randx = random.randint(0, 1)
if randx == 1:
    randx = 9
randy = random.randint(0, 9)


twoDArray[randx][randy] = 2


size = [700, 500]

screen = pygame.display.set_mode(size)

person = pygame.image.load('/home/pi/Downloads/sprite.PNG')
def player():
    x=(size[0])
    y=(size[1])
    screen.blit(person, (x,y))
#music = pygame.mixer.music.load('Odd Time Signatures in Video Game Music.mp3')
#pygame.mixer.music.play(loops=-1)

#time.sleep(2)
#pygame.mixer.music.stop()

done = False 
#Music
#Controls
#Drawing shapes- 10/10 grid
#Array keeping track of each grid status
#Endings
rect_x = 50
rect_y = 10

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

    screen.blit(person, (0,0))
    pygame.display.flip()
    clock.tick(60)