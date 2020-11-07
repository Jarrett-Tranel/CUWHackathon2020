import pygame

pygame.init()   

size = [1400, 700]

screen = pygame.display.set_mode(size)

done = False 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True