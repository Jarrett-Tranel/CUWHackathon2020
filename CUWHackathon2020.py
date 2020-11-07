#Project created by Jarrett Tranel, Trevor Krentz, Ross Jacobson, and Ishtiyaq Ahmed on 11/7/20
import pygame
from pygame import mixer 
mixer.init()
pygame.init()   

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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

size = [800, 500]

screen = pygame.display.set_mode(size)

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
    screen.fill(BLACK)

    for i in range(0, 10):
        pygame.draw.rect(screen, WHITE, [rect_x + (i * 50), rect_y, 40, 40])
        for j in range(0, 10):
            pygame.draw.rect(screen, WHITE, [rect_x + (i * 50), rect_y + (j * 50), 40, 40])


    pygame.display.flip()
    clock.tick(60)