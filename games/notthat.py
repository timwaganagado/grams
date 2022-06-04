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
WIDTH = 800
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

x = WIDTH/2
y = HEIGHT/2



right=False
left=False
jump = True

hasjump = True

ground = False
side = True

velocity = 0
acceleration = 0.5

speed = 4

jumpheight = 2

platforms = []

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                right = True 
            if event.key == pg.K_a:
                left = True
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit
            if event.key == pg.K_SPACE:
                if hasjump:
                    velocity = 10
                    jump = True
                    hasjump = False
            if event.key == pg.K_e:
                jumpheight += 1
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mpos = vec(pg.mouse.get_pos())
                new = pg.Rect(mpos.x, mpos.y, 50, 20)
                
                platforms.append(new)
        if event.type == pg.KEYUP:
            if event.key == pg.K_d:
                right = False 
            if event.key == pg.K_a:
                left = False
                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    
    xsave = x
    ysave = y
    
    if left:
        x -= speed
    if right:
        x += speed
    if jump:
        y -= velocity
        velocity -= acceleration
    else:
        y += velocity
        velocity += acceleration
    if velocity < jumpheight and jump:
        velocity = 0
        jump = False
    
    
    player = pg.Rect(x, y, 20, 20)
    if pg.Rect.collidelist(player, platforms) != -1:
        target = platforms[pg.Rect.collidelist(player, platforms)]
        if target.y > y+5 and target.x-20 < x < target.x+50 :
            if ground:
                x = xsave
                y = ysave
                
            else:    
                y = target.y - 20
                hasjump = True
            velocity = 0
            ground = True
        elif target.x-20 < x < target.x+50:
            x = xsave    
    else:
        ground = False
    if y > HEIGHT:
        y = 0
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    player = pg.Rect(x, y, 20, 20)
    pg.draw.rect(screen,BLACK,player)
    for new in platforms:
        pg.draw.rect(screen,BLACK,new)
    
    
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways