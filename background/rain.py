import pygame as pg
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
import pygame.gfxdraw

from pygame import color
vec = pg.math.Vector2

TILESIZE = 30
GRIDWIDTH = 9
GRIDHEIGHT = 9
WIDTH = 1920
HEIGHT = 1080
FPS = 144
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
ORANGE = (255, 165, 0)
check = 'working'

font_name = pg.font.match_font('hack')
def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN)
clock = pg.time.Clock()

direction = [-3,-2,-1,0,1,2,3]
number = 10
speed = 500
class raining():
    def __init__(self):
        self.vel=0
    def checkdrops(self):
        o = 0
        while o < number:
            o += 1
            #up = random.choices([True,False])[0]
            up = True
            if up:
                self.drops.update({o:[((random.choice(direction)*random.random()*10),(0)),(random.randint(0,255),random.randint(0,255),random.randint(0,255))]})
            else:
                self.drops.update({o:[(0*10,random.choice(direction)*10),(random.randint(0,255),random.randint(0,255),random.randint(0,255))]})
    def fall(self):
        test = dict(self.drops)
        for x in test:
            change = self.drops[x][0]
            colour = self.drops[x][1]
            del self.drops[x]
            check = vec(change)
            if type(x) == int:
                if check.y == 0:
                    x = (WIDTH,random.randint(0,HEIGHT))
                #else:
                #    x = (random.randint(0,WIDTH),HEIGHT/2)
                #x = vec(pg.mouse.get_pos())
                #x = (WIDTH,self.height)
                #self.height += self.add
                #if self.height > HEIGHT*2/3:
                #    self.add = -1
                #if self.height < HEIGHT/3:
                #    self.add = 1
                #x = (WIDTH/2,HEIGHT/2)
            new = vec(x)
            old = vec(x)
            new += change
            newchange = vec(change)
            newchange *= 1
            #drop = pg.Rect(new.x,new.y, 1, 1)
            #pg.draw.rect(screen,WHITE,drop)
            (255, 0, 0)
            (255, 165, 0)
            #show = random.choices([True,False],[50,50])[0]
            #if show:
            
            pg.gfxdraw.line(screen,int(new.x),int(new.y),int(old.x),int(old.y), colour)
            if (0 <= new.x < WIDTH and 0 <= new.y < HEIGHT) and not ( -0.09 < newchange.x < 0.09 and -0.09 < newchange.y < 0.09):
                self.drops.update({(new.x,new.y):[(newchange.x,newchange.y),colour]})
                
            
R = raining()
R.drops = {}
R.height = HEIGHT/3
R.add = 1
R.planets = {(int(WIDTH/2),int(HEIGHT/2)):10}
anim_timer = pg.time.get_ticks()

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
            
                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(BLACK) # fills screnn with color
    current_time = pg.time.get_ticks()
    if current_time - anim_timer > speed:
        R.checkdrops()
        anim_timer = pg.time.get_ticks()
    R.fall()
    pg.gfxdraw.filled_circle(screen, int(WIDTH/2), int(HEIGHT/2), 50, BLACK)
    pg.gfxdraw.aacircle(screen, int(WIDTH/2), int(HEIGHT/2), 50, WHITE)
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways