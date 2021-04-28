import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

TILESIZE = 60
GRIDWIDTH = 9
GRIDHEIGHT = 9
WIDTH = TILESIZE * GRIDWIDTH
HEIGHT = TILESIZE * GRIDHEIGHT
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
def draw_text(text, size, color, x, y):
    font = pg.font.Font(font_name, int(size/2))
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center = ((x+0.5)*TILESIZE,(y+0.5)*TILESIZE))
    screen.blit(text_surface, text_rect)
def drawboxs():
    for pos in stink:
        rect = pg.Rect(stink[pos].x*TILESIZE,stink[pos].y*TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen, BLACK, rect)
        draw_text(pos,TILESIZE,LIGHTGRAY,stink[pos].x,stink[pos].y)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

stink = {'GB':vec(0,0),'SM':vec(1,0),'TP':vec(2,0),'DD':vec(3,0),'3p':vec(0,1)}
wherestink = []
for l in stink:
    wherestink.append(stink[l])
changee = 0 
change = False
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pg.MOUSEBUTTONDOWN:
            mpos = vec(pg.mouse.get_pos()) // TILESIZE
            if event.button == 1:
                if change == False:
                    for l in stink:
                        if mpos == stink[l]:
                            change = True
                            changee = l
                elif change == True:
                    if mpos not in wherestink:
                        stink[changee] = mpos
                        change = False
                print(changee,change)
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_m:
                print(stink)
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit
        
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit()
    screen.fill(WHITE) # fills screnn with color
    # anything down here will be displayed ontop of anything above
    drawboxs()
    pg.display.flip() # dose the changes goto doccumentation for other ways