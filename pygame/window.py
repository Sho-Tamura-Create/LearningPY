import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (800, 600) 

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("test")

while True:
 screen.fill((0, 0, 0)) 
 pygame.display.update() 

 for event in pygame.event.get():
     if event.type == QUIT: 
        sys.exit()