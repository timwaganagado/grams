import pygame as pg
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
vec = pg.math.Vector2

TILESIZE = 30
WIDTH = 1920
HEIGHT = 1080
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

font_name = pg.font.match_font('hack')
def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


check_tile_connections = ((0,-0.5),(0.5,0),(0,0.5),(-0.5,0))

class tile():
    def __init__(self,x,y,con):
        self.x = x
        self.y = y
        self.connections = con

class wall():
    def __init__(self,x,y,ori) -> None:
        self.x = x
        self.y = y
        self.ori = ori



class Grid():
    def __init__(self) -> None:
        #self.pot_wall = []
        #self.pot_wall_pos = []
        #for x in range(0, WIDTH, TILESIZE):
        #    for y in range(0, HEIGHT, TILESIZE):
        #        self.pot_wall.append(wall((x+(TILESIZE/2))/TILESIZE,y/TILESIZE,"hor"))
        #        self.pot_wall.append(wall(x/TILESIZE,(y+(TILESIZE/2))/TILESIZE,"ver"))
#
        #for x in self.pot_wall:
        #    self.pot_wall_pos.append((x.x,x.y))
#
#
        #self.tiles = []
        #for x in range(0, WIDTH, TILESIZE):
        #    for y in range(0, HEIGHT, TILESIZE):
        #        tartile = (x+(TILESIZE/2))/TILESIZE,(y+(TILESIZE/2))/TILESIZE
        #        print(tartile)
        #        cons = self.checkcon(tartile)
        #        self.tiles.append(tile(tartile[0],tartile[1],cons))
        #print(self.tiles)  
        self.close = False  

        self.update_grid()

    def translate_gridtopos(self):
        pass

    def update_grid(self):
        self.cell_size = 50 

        self.grid_size_x = self.cell_size * 20
        self.grid_size_x = round(self.grid_size_x/self.cell_size) * self.cell_size

        self.grid_size_y = self.cell_size * 8
        self.grid_size_y = round(self.grid_size_y/self.cell_size) * self.cell_size

        self.grid_pos_x = WIDTH/2 - self.grid_size_x/2
        self.grid_pos_y = 50

    def checkcon(self,tartile):
        cons = []
        for x in check_tile_connections:
            targetwall = tartile[0] + x[0] , tartile[1] + x[1]
            if targetwall in self.pot_wall_pos:
                cons.append((targetwall))
        return cons
    
    def shows_places(self): 
        return
        for x in self.pot_wall:
            pg.draw.circle(screen,BLUE,(x.x*TILESIZE,x.y*TILESIZE),5)

        for x in self.tiles:
            pg.draw.circle(screen,BLACK,(x.x*TILESIZE,x.y*TILESIZE),5)
    #def draw_grid(self):
    #    for x in range(0, WIDTH, TILESIZE):
    #        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    #    for y in range(0, HEIGHT, TILESIZE):
    #        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))
    def draw_grid(self):
        #vertical lines
        for x in range(int(self.grid_pos_x), int(self.grid_pos_x+self.grid_size_x+1), self.cell_size):
            pg.draw.line(screen, BLACK, (x, int(self.grid_pos_y)), (x, int(self.grid_pos_y+self.grid_size_y-1)))
        #horizontal lines
        for y in range(int(self.grid_pos_y), int(self.grid_pos_y+self.grid_size_y+1), self.cell_size):
            pg.draw.line(screen, BLACK, (int(self.grid_pos_x), y), (int(self.grid_pos_x+self.grid_size_x-1), y))
    def find_closest(self):
        m = mpos
        m = (m[0])/TILESIZE,(m[1])/TILESIZE

        target = 0
        shortest = float("inf")
        for x in self.tiles:
            length = math.sqrt((m[0] - x.x) ** 2 + (m[1] - x.y) ** 2)
            if length < shortest:
                shortest = length
                target = x
        self.close = target
    def show_connections(self):
        if self.close:
            m = mpos
            m = (m[0])/TILESIZE,(m[1])/TILESIZE
            pg.draw.circle(screen,GREEN,(m[0]*TILESIZE,m[1]*TILESIZE),5)
            for y in self.close.connections:
                pg.draw.line(screen,RED, (self.close.x*TILESIZE,self.close.y*TILESIZE), (y[0]*TILESIZE,y[1]*TILESIZE))


T = Grid()

mpos = False

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
            if event.key == pg.K_w:
                T.gridsize +=1
            
        if event.type == pg.MOUSEBUTTONDOWN:  
            mpos = pg.mouse.get_pos()      
            T.find_closest()     
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    T.draw_grid()
    T.shows_places()
    T.show_connections()
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways