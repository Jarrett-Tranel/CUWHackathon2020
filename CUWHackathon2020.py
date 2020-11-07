#Project created by Jarrett Tranel, Trevor Krentz, Ross Jacobson, and Ishtiyaq Ahmed on 11/7/20
import pygame

pygame.init()   

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = [800, 500]

screen = pygame.display.set_mode(size)

done = False 
#Music
#Controls
#Drawing shapes- 10/10 grid
#Array keeping track of each grid status
#Endings
rect_x = 50
rect_y = 50

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])

    pygame.display.flip()