import pygame
#set-up for song
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("Insert song file location here")
pygame.mixer.music.play(loops=-1)

#when closing program
pygame.mixer.music.stop()
pygame.mixer.quit