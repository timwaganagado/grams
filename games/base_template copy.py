import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

TILESIZE = 30
GRIDWIDTH = 9
GRIDHEIGHT = 9
WIDTH = 255*3
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

x = 0
y = 0
c1 = random.randint(0,255)
c2 = random.randint(0,255)
c3 = random.randint(0,255)
nc1 = c1
nc2 = c2
nc3 = c3
done = True
running = True
while running:
    clock.tick(30)
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
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    #screen.fill(WHITE) # fills screnn with color

    #for ll in rectstodraw:
    #    rect = pg.Rect(rectstodraw[ll][3], rectstodraw[ll][4], 1, 1)
    #    pg.draw.rect(screen,(rectstodraw[ll][0],rectstodraw[ll][1],rectstodraw[ll][2]),rect)
    for ll in range(0,WIDTH*HEIGHT):
        #if x >= WIDTH/3*2:
        #    if nc1 == c1 or nc1 == 'done':
        #        nc1 = 'done'
        #    elif c1 > nc1:
        #        c1 -= 1
        #    elif c1 < nc1:
        #        c1 += 1
        #
        #    rect = pg.Rect(x, y, 1, 1)
        #    pg.draw.rect(screen,(x/3,c1,y),rect)
        #elif x >= WIDTH/3:
        #    if nc2 == c2 or nc2 == 'done':
        #        nc2 = 'done'
        #    elif c2 > nc2:
        #        c2 -= 1
        #    elif c2 < nc2:
        #        c2 += 1
#
        #    rect = pg.Rect(x, y, 1, 1)
        #    pg.draw.rect(screen,(c2,y,x/3),rect)

        if nc3 == c3 or nc3 == 'done':
            nc3 = 'done'
        elif c3 > nc3:
            c3 -= 1
        elif c3 < nc3:
            c3 += 1
        rect = pg.Rect(x, y, 1, 1)
        if x >= WIDTH/3*2:
            xx = 2
        elif x >= WIDTH/3:
            xx = 1
        else:
            xx = 0
        pg.draw.rect(screen,(y,x-255*xx,c3),rect)

        #print(x,y)
        x += 1
        if x >= WIDTH:
            x = 0
            y += 1
        if y >= HEIGHT:
            y= 0
        if nc3 == 'done':
            nc1 = random.randint(0,255)
            nc2 = random.randint(0,255)
            nc3 = random.randint(0,255)
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways