import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

TILESIZE = 30
GRIDWIDTH = 64
GRIDHEIGHT = 36
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

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN)
clock = pg.time.Clock()

def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))

class main():
    def __int__(self):
        self.p = 0
    def draw_icons(self):
        goal_center = (self.p.x * TILESIZE + TILESIZE / 2, self.p.y * TILESIZE + TILESIZE / 2)
        screen.blit(cross_img, cross_img.get_rect(center=goal_center))

cross_img = pg.image.load('images/cross-1.png.png').convert_alpha()
cross_img = pg.transform.scale(cross_img, (50, 50))
cross_img.fill((255, 0, 0, 255), special_flags=pg.BLEND_RGBA_MULT)

M = main()
M.p = vec(20,20)

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mpos = vec(pg.mouse.get_pos()) // TILESIZE
                M.p = mpos
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit
                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 

    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    # anything down here will be displayed ontop of anything above
    draw_grid()
    M.draw_icons()
    pg.display.flip() # dose the changes goto doccumentation for other ways