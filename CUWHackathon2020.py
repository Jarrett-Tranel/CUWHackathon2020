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

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])
    pygame.draw.circle(screen, RED, [rect_x + 100, rect_y + 100], 30)


    pygame.display.flip()
    clock.tick(60)