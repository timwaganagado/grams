import pygame as pg
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
vec = pg.math.Vector2

TILESIZE = 30
GRIDWIDTH = 9
GRIDHEIGHT = 9
WIDTH = 255
HEIGHT = 255
FPS = 30
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

font_name = pg.font.match_font('hack')
def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

hw,hh = WIDTH/2,HEIGHT/2
x,y = hw,hh
pmx,pmy = x,y
dx,dy = 0,0
distance = 0
speed = 3

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit
        if event.type == pg.MOUSEBUTTONDOWN:
            pmx,pmy = x,y
            if event.button == 1:
                mx,my = pg.mouse.get_pos()
        
                radians = math.atan2(my-pmy,mx-pmx)
                distance = int(math.hypot(mx-pmx,my-pmy)/speed)

                dx = math.cos(radians)*speed
                dy = math.sin(radians)*speed

                pmx,pmy = mx,my
                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    
    
    if distance:
        distance -=1
        x+=dx
        y+=dy
    screen.fill(WHITE)
    pg.draw.circle(screen,BLACK,(int(x),int(y)),25)
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
     # fills screnn with color
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways