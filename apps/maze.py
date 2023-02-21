import pygame
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
vec = pygame.math.Vector2

TILESIZE = 30
GRIDWIDTH = 9
GRIDHEIGHT = 9
WIDTH = 255
HEIGHT = 255
FPS = 30
BLUE = (0,0,255)
BROWN = (165,42,42)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
DARKGRAY = (40, 40, 40)
MEDGRAY = (75, 75, 75)
LIGHTGRAY = (140, 140, 140)
GREY = (128,128,128)
check = 'working'

font_name = pygame.font.match_font('hack')
def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def draw():
    pass
    
def make_Square():
    pass





running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit
            
                    
                
        if event.type == pygame.QUIT: # allows for quit when clicking on the X 
            running = False
            pygame.quit() 
    pygame.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    draw()
    # anything down here will be displayed ontop of anything above
    pygame.display.flip() # dose the changes goto doccumentation for other ways