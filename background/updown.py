import pygame as pg
from os import path
from collections import deque
import random
import shelve
from pygame.draw import line

vec = pg.math.Vector2

# 517/116 = 4.45689655
#
#Red, Orange, Yellow, Green, Blue, Indigo and Violet.
TILESIZE = 2
SIZE = 9
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
check = [vec(-1,0),vec(1,0),vec(0,-1),vec(0,1)]

font_name = pg.font.match_font('hack')
def draw_number(text, size, color):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH/2,HEIGHT/2))
    screen.blit(text_surface, text_rect)

def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)

def draw_time(text, size, color):
    if text%60 <= 10:
        seconds = "{:0>2d}".format(text%60)
    else:
        seconds = str(text%60)
    text = str(str(int(text/60))+':'+seconds)
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH/2,HEIGHT*3/4))
    screen.blit(text_surface, text_rect)

def on_press(key):
    
    A.number= 0
    return False ,A.number# stop listener; remove this if want more keys

class block():
    def __int__(self):
        self.current = 0
        self.vel = 0 
        self.line = 0
    def move(self):
        keys = pg.key.get_pressed()
        movecheck = [self.current + l for l in check]
        move = random.randint(1,4)
        oldcurrent = vec(self.current)//TILESIZE
        loopcheck = 0
        if move == 1:
            oldcurrent.x -= self.vel
        if move == 2:
            oldcurrent.x += self.vel
        if move == 3:
            oldcurrent.y -= self.vel
        if move == 4:
            oldcurrent.y += self.vel
        #print(vec(self.current)//TILESIZE)
        while oldcurrent in self.line :
            if  loopcheck >= 8:
                self.line = []
                break
            oldcurrent = vec(self.current)//TILESIZE
            #print(self.line)
            move = random.randint(1,4)
            if move == 1:
                oldcurrent.x -= self.vel
            if move == 2:
                oldcurrent.x += self.vel
            if move == 3:
                oldcurrent.y -= self.vel
            if move == 4:
                oldcurrent.y += self.vel
            loopcheck += 1
        self.current = vec(oldcurrent.x*TILESIZE,oldcurrent.y*TILESIZE)
            
        
        self.line.append(vec(self.current.x,self.current.y)//TILESIZE)
    def draw(self,color):
        for i in self.line:
            rect = pg.Rect(i.x*TILESIZE, i.y*TILESIZE, TILESIZE, TILESIZE)
            pg.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), rect)

class numbers():
    def __int__(self):
        self.xyz = 0
        self.xyzchanged = 0
        self.rainbow = 0
        self.backorder = 0
        self.A.number= 0
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
        if current == self.backorder[-1]:
            #print(self.backorder)
            #print(self.rainbow)
            while len(self.rainbow) != 0:
                l = random.choice(self.rainbow)
                self.backorder.remove(l)
                self.rainbow.remove(l)
                self.backorder.append(l)
            self.rainbow = list(self.backorder)
            #print(self.backorder)
            #print(self.rainbow)
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
screen = pg.display.set_mode((WIDTH, HEIGHT),pg.NOFRAME)
clock = pg.time.Clock()


timer = 0
backgroundcolour = (WHITE[0],WHITE[1],WHITE[2])
color = BLACK
colours = [BROWN,BLACK,RED,GREEN,CYAN,MAGENTA,YELLOW,DARKGRAY,MEDGRAY,LIGHTGRAY,GREY]

speed = 1000

A = numbers()
B = block()

change = 1
changenum = 2

A.xyz = {"x":random.randint(0,255),"y":random.randint(0,255),"z":random.randint(0,255)}
A.xyzchanged = {"x":random.randint(0,255),"y":random.randint(0,255),"z":random.randint(0,255)}
A.rainbow = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]
A.backorder = list(A.rainbow)
A.number= 1 #random.randint(0,100)

B.current = vec((WIDTH/2),int(HEIGHT/2))
B.vel = 1
B.line = []

fade = 0
flip = True
screenflip = 1

pg.mouse.set_visible(False)

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                change += 1
                if change == 4:
                    change = 1
            if event.button == 3:
                speed += 500
                if speed > 2500:
                    speed = 200
        if event.type == pg.KEYDOWN:
            #print('g')
            #print(event.key)
            if event.key == pg.K_1:
                speed = 1000
            if event.key == pg.K_SPACE:
                if flip == True:
                    flip = False
                elif flip == False:
                    flip = True
            if event.key == pg.K_LSHIFT:
                changenum += 1
                if changenum == 3:
                    changenum = 1
            if event.key == pg.K_RETURN:
                screenflip += 1
                if screenflip == 2:
                    screen = pg.display.set_mode((WIDTH, HEIGHT))
                    screenflip = 0 
                else:
                    screen = pg.display.set_mode((WIDTH, HEIGHT),pg.NOFRAME)
            if event.key == pg.K_r:
                A.number= 0
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit() 
            
        
        #mpos = pg.mouse.get_pos()
        #n,m = mpos
        #print(mpos)
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    #listener = keyboard.Listener(on_press=on_press)
    #listener.start()  # start to listen on a separate thread

    current_time = pg.time.get_ticks()
    if current_time - timer > speed:
        B.move()
        if changenum == 1:
            A.number+= random.choice([1,-1])
            if A.number<= 0:
                A.number= random.randint(0,100)
            if A.number>= 100:
                A.number= random.randint(0,100)
            timer = pg.time.get_ticks()
            #color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        elif changenum == 2:
            A.number+= 1
            timer = pg.time.get_ticks()
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
    #print(backgroundcolour)
    #print(flip)
    pg.display.set_caption('NUM') # changes the name of the application
    if flip == True:
        backgroundcolour = A.background(backgroundcolour)
        screen.fill(backgroundcolour)
    # anything down here will be displayed ontop of anything above
    text = str(A.number)
    if changenum == 1:
        numbersize = WIDTH
    if changenum == 2:
        if  A.number >= 1000:
            numbersize = int(WIDTH/2)
        elif A.number>= 100:
            numbersize = int(WIDTH/1.3)
        else:
            numbersize = WIDTH
    #draw_text(text, 40,color,n,m,align='topleft')
    draw_time(A.number, 30, color)
    draw_number(text,numbersize,color)
    
    B.draw(color)
    pg.display.flip() # dose the changes goto doccumentation for other ways