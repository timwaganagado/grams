from cmath import rect
from turtle import width
from numpy import size
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
WIDTH = 1000
HEIGHT = 1000
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

class ball():
    def __init__(self,x,y,size):
        self.y = y
        self.yvelocity = 0
        self.yacceleration = 2
        self.x = x
        self.xvelocity = 0
        self.xacceleration = 0.9
        self.size = size
        self.xforce = 0
        self.yforce = 0
        
    def movement(self):
        global balls
        self.movement_horizontal()
        self.movement_vertical()
        print(750 < self.y < 800)
        if N.position-10 < self.x < N.position + 20 and self.y > HEIGHT-N.height:
            balls.remove(self)
            balls.append(ball(random.randint(0,1000),10,random.randint(10,20)))
    def movement_change(self,horchange,verchange):
        if 750 < self.y < 850 :
            print('true')
            horchange *= 2
            verchange *= 2
        self.xforce = horchange
        self.yforce = verchange
    def movement_horizontal(self):
        #print(0 < self.x + self.xvelocity < WIDTH)
        if not 0 < self.x + self.xvelocity < WIDTH :
            self.xvelocity *= -1
        self.x += self.xvelocity 
        self.xvelocity += self.xforce
        self.xforce = 0
        self.xvelocity *= self.xacceleration
    def movement_vertical(self):
        global balls
        if not 0 < self.y+5 + self.yvelocity < HEIGHT:
            balls.remove(self)
            balls.append(ball(random.randint(0,1000),10,random.randint(10,20)))

        self.y += self.yvelocity
        totalvelocity = 0
        if self.yvelocity > 0:
            totalvelocity += self.yvelocity * 0.1*-1
        if self.yvelocity < 0:
            totalvelocity += self.yvelocity *0.1*-1
        totalvelocity += self.yacceleration
        if self.yforce != 0:
            totalvelocity += self.yforce
            self.yforce *= 0.1
        self.yvelocity += totalvelocity

    def draw_ball(self):
        pg.draw.circle(screen,GREY,(self.x,self.y),self.size)


def getballs(balltype):
    if balltype == 1:
        return ball(random.randint(10,WIDTH-20), 0,10)
    if balltype == 2:
        return ball(WIDTH*((random.randint(1,4))/4), 0,20)


balls = []  
for x in range(1,2):
    balls.append(getballs(1))
print(balls)


class net():
    def __init__(self):
        self.height = 200
        self.position = 500
    def draw_net(self):
        rect = pg.Rect(self.position, HEIGHT-self.height, 10, self.height)
        pg.draw.rect(screen,GREY,rect)

N = net()

anim_timer = pg.time.get_ticks()
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pg.mouse.get_pos()
                for x in balls:
                    x.movement_change((x.x-pos[0])*0.1*-1,(x.y-pos[1])*0.1*-1)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit
            if event.key == pg.K_d:
                for x in balls:
                    x.movement_change(100,-50)
            if event.key == pg.K_a:
                for x in balls:
                    x.movement_change(-100,-50)

                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    #current_time = pg.time.get_ticks()
    #if current_time - anim_timer > 200:
    screen.fill(WHITE) 
    pg.draw.line(screen,RED,(0,800),(WIDTH,800),50)
    for x in balls:
        x.movement()
        x.draw_ball()
    #anim_timer = pg.time.get_ticks()
    N.draw_net()
    
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    # fills screnn with color
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways