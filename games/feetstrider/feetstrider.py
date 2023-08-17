from cmath import rect
from this import d
from tkinter import Y
from tkinter.messagebox import YES
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
WIDTH = 1920/2
HEIGHT = 1080/2
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
screen = pg.display.set_mode((int(WIDTH), int(HEIGHT)))
clock = pg.time.Clock()


class playmanager:
    def __init__(self):
        self.ground = ground()
        self.objects = [player()]

    def draw_objects(self):
        self.ground.draw()
        for x in self.objects:
            x.draw()
            x.update_pos()
    def moveobject(self,index,direction):
        if direction == 'left':
            if self.objects[index].left:
                self.objects[index].left = False
            else:
                self.objects[index].left = True
        if direction == 'right':
            if self.objects[index].right:
                self.objects[index].right = False
            else:
                self.objects[index].right = True
        if direction == 'jump':
            self.objects[index].jump = True
    def attackobject(self,index,attack):
        self.objects[index].attackchecks[attack] = True
    def move(self):
        for x in self.objects:
            x.move()
            x.attacks()
class ground:
    def __init__(self):
        l = WIDTH/2-WIDTH/2/2
        length = WIDTH/2
        self.rect = pg.Rect(l, HEIGHT*(2/3), length, 100)
    def draw(self):
        pg.draw.rect(screen,YELLOW,self.rect)

class player:
    def __init__(self):
        self.pos = vec(WIDTH*(2/5),HEIGHT/2)
        self.sizex = 15
        self.sizey = 20
        self.update_rect()
        self.left = False
        self.right = False
        self.jumpheight = 5
        self.jump = False
        self.jumpcurrent = 0
        self.influence = vec(0,0)
        self.attackchecks = {0:False,1:False,2:False}
        self.attacklock = False
        self.currentattack = 0
        self.duration = 0
    def update_rect(self):
        self.rect = pg.Rect(self.pos.x-(self.sizex/2), self.pos.y-(self.sizey/2), self.sizex, self.sizey)
    def test_rect(self):
        return pg.Rect(self.pos.x-(self.sizex/2), self.pos.y-(self.sizey/2), self.sizex, self.sizey)
    def update_pos(self):
        self.pos += vec(0,5)
        test = self.test_rect()
        if test.colliderect(pm.ground):
            self.pos = vec(self.pos.x,pm.ground.rect[1]-self.sizey/2)
        self.update_rect()
    def move(self):
        direction = vec(0,0)
        direction += self.influence
        if self.left:
            direction += vec(-5,0)
        if self.right:
            direction += vec(5,0)
        if self.jump:
            print(self.jumpcurrent < self.jumpheight)
            if self.jumpcurrent < self.jumpheight:
                direction += vec(0,-10)
                self.jumpcurrent+= 1
            else:
                self.jump =False
                self.jumpcurrent = 0
        self.pos += direction
        self.update_rect()
        if self.currentattack != 0:
            self.currentattack.update_rect()
    def attacks(self):
        if not self.attacklock:
            for x in self.attackchecks:
                if self.attackchecks[x]:
                    if x == 0 :
                        self.currentattack = baseattack1(self)
                        self.attacklock = True
                        self.attackchecks[x] = False
        else:
            self.duration += 1
            if self.duration == self.currentattack.duration:
                self.currentattack = 0
                self.attacklock = False
                self.duration = 0
    def draw(self):
        pg.draw.rect(screen,RED,self.rect)
        if self.currentattack != 0:
            self.currentattack.draw()
        

class baseattack1:
    def __init__(self,origin):
        self.pos = origin.pos
        self.parent = origin
        self.where = 0
        if self.parent.left:
            self.where = 'left'
            self.sizex = 10
        if self.parent.right:
            self.where = 'right'
            self.sizex = 10
        if self.where == 0:
            self.where = 'idle'
            self.sizex = 25
        self.sizey = 3
        self.duration = 20
        self.update_rect()
    def update_rect(self):
        print(self.where)
        if self.where == 'idle':
            self.rect = pg.Rect((self.parent.pos.x)-(self.sizex/2), self.parent.pos.y, self.sizex, self.sizey)
        if self.where == 'left':
            self.rect = pg.Rect(self.parent.pos.x-(self.parent.sizex/2)-self.sizex, self.parent.pos.y, self.sizex, self.sizey)
        if self.where == 'right':
            self.rect = pg.Rect(self.parent.pos.x-(self.parent.sizex/2)+self.parent.sizex, self.parent.pos.y, self.sizex, self.sizey)
    def draw(self):
        print(self.rect)
        pg.draw.rect(screen,YELLOW,self.rect)
        
pm = playmanager()

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
            if event.key == pg.K_a:
                pm.moveobject(0,'left')
            if event.key == pg.K_d:
                pm.moveobject(0,'right')
            if event.key == pg.K_w:
                pm.moveobject(0,'jump')
            if event.key == pg.K_f:
                pm.attackobject(0,0)
        if event.type == pg.KEYUP:
            if event.key == pg.K_a:
                pm.moveobject(0,'left')
            if event.key == pg.K_d:
                pm.moveobject(0,'right')
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    pm.draw_objects()
    pm.move()
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways