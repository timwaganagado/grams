import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

WIDTH = 900
HEIGHT = 500
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

def start():
    for x in range(0,10):
        dots.append([vec(WIDTH/2,HEIGHT/2),vec(WIDTH/2+random.randint(-2,2),HEIGHT/2+random.randint(-2,2))])

def draw_dots():
    for target in dots:
        rect = pg.Rect(target[0] , (10, 10))
        pg.draw.rect(screen, BROWN, rect)

def draw_average():
    x = 0
    y = 0
    while y != HEIGHT+1:
        if x+1 <= HEIGHT and x-1 >= 0 and y+1 <= WIDTH and y-1 >= 0:
            dc = screen.get_at((x+1, y))+screen.get_at((x-1, y))+screen.get_at((x, y+1))+screen.get_at((x, y-1))
            dc[0] = int(dc[0]/4)
            dc[1] = int(dc[1]/4)
            dc[2] = int(dc[2]/4)
            rect = pg.Rect((x,y) , (10, 10))
            pg.draw.rect(screen, dc, rect)
        x += 1
        if x > WIDTH:
            x = 0
            y += 1
        
def border(target):
    x,y = True
    if 0 > target.x > WIDTH:
        x = False
    if 0 > target.y > HEIGHT:
        y = False
    return x,y
dots = []
pdots = []

start()

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
            
                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    pg.display.set_caption("{:.2f}".format(clock.get_fps()))     # changes the name of the application
    screen.fill(WHITE)
    draw_dots()
    draw_average()
    # fills screnn with color
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways