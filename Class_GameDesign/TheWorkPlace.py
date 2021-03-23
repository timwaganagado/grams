import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

TILESIZE = 48
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

def drawchar():   
    x,y = player
    rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
    pg.draw.rect(screen,WHITE,rect)
    x,y = ttest
    rect = pg.Rect(x,y,30,30)
    pg.draw.rect(screen,GREEN,rect)

def draw_icons():    
    start_center = (cursor.x , cursor.y)
    
    screen.blit(home_img, home_img.get_rect(center=start_center))

home_img = pg.image.load('images/Test pixel.png').convert_alpha()
home_img = pg.transform.scale(home_img, (1000, 1000))
home_img.set_alpha(200)
home_img.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)

player = vec(1,1)
cursor = vec(100,100)
ttest = vec(50,50)

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mpos = vec(pg.mouse.get_pos())
            ttest = mpos
        if event.type == pg.QUIT:
            run = False
            pg.quit() 
    screen.fill(WHITE)
    drawchar()
    draw_icons()
    pg.display.flip()