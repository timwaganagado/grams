import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

TILESIZE = 70
GRIDWIDTH = 35
GRIDHEIGHT = 15
WIDTH = 48 * 35
HEIGHT = 48 * 20
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
class enviroment():
    def __int__(self):
        self.player = 0
        self.cursor = 0
        self.ttest = 0
        self.pixels = 0
    def drawchar(self):   
        x,y = self.player
        rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen,BLACK,rect)
        x,y = self.ttest
        rect = pg.Rect(x,y,30,30)
        pg.draw.rect(screen,GREEN,rect)

    def draw_icons(self):
        for l in self.pixels:
            start_center = (self.pixels[l].x*TILESIZE + TILESIZE/2 , self.pixels[l].y*TILESIZE + TILESIZE/2)
    
            screen.blit(home_img, home_img.get_rect(center=start_center))

home_img = pg.image.load('images/bar_area-2.png').convert_alpha()
home_img = pg.transform.scale(home_img, (TILESIZE, TILESIZE))
#home_img.set_alpha(200)
#home_img.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)

E = enviroment()
E.player = vec(1,1)
E.cursor = vec(100,500)
E.ttest = vec(50,50)
E.pixels = {'sink': vec(16, 2)}
empt = {}
print(E.pixels)


 
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mpos = vec(pg.mouse.get_pos())//TILESIZE
            if event.button == 1:
                E.pixels['sink'] = mpos
            if event.button == 3:
                player = mpos
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_m:
                empt = {}
                for l in E.pixels:
                    empt.update({str(l):'vec('+str(E.pixels[l].x)+','+str(E.pixels[l].y)+')'})
                print(empt)
        if event.type == pg.QUIT:
            run = False
            pg.quit() 
    screen.fill(WHITE)
    E.drawchar()
    E.draw_icons()
    pg.display.flip()