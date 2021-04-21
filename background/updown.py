import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

# 517/116 = 4.45689655
#
#Red, Orange, Yellow, Green, Blue, Indigo and Violet.
TILESIZE = 2
SIZE = 8
WIDTH = TILESIZE ** SIZE
HEIGHT = TILESIZE ** SIZE
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
ORANGE = (255,69,0)
BLUE = (0,0,255)
INDIGO = (75,0,130)
VIOLET = (238,130,238)
check = 'working'

font_name = pg.font.match_font('hack')
def draw_text(text, size, color):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH/2,HEIGHT/2))
    screen.blit(text_surface, text_rect)

class numbers():
    def __int__(self):
        self.xyz = 0
        self.xyzchanged = 0
        self.rainbow = 0
    def changer(self):
        for num in self.xyz:
            value = self.xyz[num]
            if value == 0:
                self.xyz[num]+=random.choice([1,0])
            elif value == 255:
                self.xyz[num]+=random.choice([-1,0])
            else:
                self.xyz[num]+=random.choice([1,0,-1]) 
    def otherchanger(self):
        for num in self.xyz:
            if self.xyz[num] > self.xyzchanged[num]:
                self.xyz[num] += -1
            elif self.xyz[num] < self.xyzchanged[num]:
                self.xyz[num]+= 1
            else:
                self.xyzchanged[num] = random.randint(0,255)
    def background(self,back):
        current = self.rainbow[0]
        p,o,i = back
        if back == current:
            self.rainbow.remove(current)
            self.rainbow.append(current)
        else:
            if p != current[0]:
                if p > current[0]:
                    p -= 1
                else:
                    p += 1
            if o != current[1]:
                if o > current[1]:
                    o -= 1
                else:
                    o += 1
            if i != current[2]:
                if i > current[2]:
                    i -= 1
                else:
                    i += 1
        back=(p,o,i)
        return back

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

number = 2 #random.randint(0,100)
timer = 0
backgroundcolour = (WHITE[0],WHITE[1],WHITE[2])
color = BLACK
colours = [BROWN,BLACK,RED,GREEN,CYAN,MAGENTA,YELLOW,DARKGRAY,MEDGRAY,LIGHTGRAY,GREY]


A = numbers()

change = 1

A.xyz = {"x":random.randint(0,255),"y":random.randint(0,255),"z":random.randint(0,255)}
A.xyzchanged = {"x":random.randint(0,255),"y":random.randint(0,255),"z":random.randint(0,255)}
A.rainbow = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]


running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pg.MOUSEBUTTONDOWN:
            change += 1
            if change == 4:
                change = 1
                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            run = False
            pg.quit() 
    current_time = pg.time.get_ticks()
    if current_time - timer > 200:
        number += random.choice([1,-1])
        if number <= 0:
            number = random.randint(0,100)
        if number >= 100:
            number = random.randint(0,100)
        timer = pg.time.get_ticks()
        #color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if change == 1:
            color = random.choice(colours)
            A.xyz = {"x":color[0],"y":color[1],"z":color[2]}    
    if change == 2:
        A.changer()
    if change == 3:
        A.otherchanger()
    x = A.xyz['x']
    y = A.xyz['y']
    z = A.xyz['z']
    color = (x,y,z)
    #print((x,y,z))
    print(backgroundcolour)
    pg.display.set_caption('NUM') # changes the name of the application
    backgroundcolour = A.background(backgroundcolour)
    screen.fill(backgroundcolour) # fills screnn with color
    # anything down here will be displayed ontop of anything above

    text = str(number)
    
    draw_text(text,WIDTH,color)
    pg.display.flip() # dose the changes goto doccumentation for other ways