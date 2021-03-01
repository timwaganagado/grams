import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

TILESIZE = 48
GRIDWIDTH = 28
GRIDHEIGHT = 15
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
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


moving = False

checkmove = [vec(0,1),vec(1,0),vec(0,-1),vec(-1,0)]
checkmove += [vec(1, 1), vec(-1, 1), vec(1, -1), vec(-1, -1),vec(0,2),vec(2,0),vec(0,-2),vec(-2,0)]

class map():
    def __int__():
        self.moveable = []
        self.player = []
    def draw(self):
        for move in self.moveable:
            rect = pg.Rect(move * TILESIZE, (TILESIZE, TILESIZE))
            pg.draw.rect(screen, LIGHTGRAY, rect)
    def drawplayer(self):   
        x,y = self.player
        rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen,WHITE,rect)


    
    

M = map()
M.player = vec(0,0)

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
                    mpos = vec(pg.mouse.get_pos()) // TILESIZE
                    
                    if event.button == 1:
                        
                        M.moveable = [movement + M.player for movement in checkmove]
                        if moving == False:
                            moving = True
                        else:
                            if mpos in M.moveable:
                                M.player = mpos 
                                moving = False  
                            else:
                                moving = False   
                    elif event.button == 3:
                        
                        M.player = mpos 
                        
                    #if event.button == 3:
                        
                        
                    
                    
        if event.type == pg.QUIT:
            running = False
        
        screen.fill(DARKGRAY)
        
        if moving:
            M.draw()
        M.drawplayer()
    pg.display.flip()