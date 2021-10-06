import pygame as pg
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
vec = pg.math.Vector2

TILESIZE = 30
GRIDWIDTH = 30
GRIDHEIGHT = 20
WIDTH = TILESIZE*GRIDWIDTH
HEIGHT = TILESIZE*GRIDHEIGHT
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

def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

filename = os.path.dirname(sys.argv[0])
filename += '\images'

builder0 = pg.image.load(os.path.join(filename,'testput00.png')).convert_alpha()
builder0 = pg.transform.scale(builder0, (30, 30))

builderup = pg.image.load(os.path.join(filename,'testput01.png')).convert_alpha()
builderup = pg.transform.scale(builderup, (30, 30))

builderright = pg.image.load(os.path.join(filename,'testput02.png')).convert_alpha()
builderright = pg.transform.scale(builderright, (30, 30))

builderdown = pg.image.load(os.path.join(filename,'testput03.png')).convert_alpha()
builderdown = pg.transform.scale(builderdown, (30, 30))

builderleft = pg.image.load(os.path.join(filename,'testput04.png')).convert_alpha()
builderleft = pg.transform.scale(builderleft, (30, 30))

builderupright = pg.image.load(os.path.join(filename,'testput05.png')).convert_alpha()
builderupright = pg.transform.scale(builderupright, (30, 30))

builderupdown = pg.image.load(os.path.join(filename,'testput06.png')).convert_alpha()
builderupdown = pg.transform.scale(builderupdown, (30, 30))

builderupleft = pg.image.load(os.path.join(filename,'testput07.png')).convert_alpha()
builderupleft = pg.transform.scale(builderupleft, (30, 30))

builderdownright = pg.image.load(os.path.join(filename,'testput08.png')).convert_alpha()
builderdownright = pg.transform.scale(builderdownright, (30, 30))

builderleftright = pg.image.load(os.path.join(filename,'testput09.png')).convert_alpha()
builderleftright = pg.transform.scale(builderleftright, (30, 30))

builderdownleft = pg.image.load(os.path.join(filename,'testput10.png')).convert_alpha()
builderdownleft = pg.transform.scale(builderdownleft, (30, 30))

builderupdownright = pg.image.load(os.path.join(filename,'testput11.png')).convert_alpha()
builderupdownright = pg.transform.scale(builderupdownright, (30, 30))

builderupdownleft = pg.image.load(os.path.join(filename,'testput12.png')).convert_alpha()
builderupdownleft = pg.transform.scale(builderupdownleft, (30, 30))

builderuprightleft = pg.image.load(os.path.join(filename,'testput13.png')).convert_alpha()
builderuprightleft = pg.transform.scale(builderuprightleft, (30, 30))

builderdownrightleft = pg.image.load(os.path.join(filename,'testput14.png')).convert_alpha()
builderdownrightleft = pg.transform.scale(builderdownrightleft, (30, 30))

builderall = pg.image.load(os.path.join(filename,'testput15.png')).convert_alpha()
builderall = pg.transform.scale(builderall, (30, 30))

pipe0 = pg.image.load(os.path.join(filename,'pipetest00.png')).convert_alpha()
pipe0 = pg.transform.scale(pipe0, (30, 30))

pipeup = pg.image.load(os.path.join(filename,'pipetest07.png')).convert_alpha()
pipeup = pg.transform.scale(pipeup, (30, 30))

pipeleft = pg.image.load(os.path.join(filename,'pipetest08.png')).convert_alpha()
pipeleft = pg.transform.scale(pipeleft, (30, 30))

pipedown = pg.image.load(os.path.join(filename,'pipetest09.png')).convert_alpha()
pipedown = pg.transform.scale(pipedown, (30, 30))

piperight = pg.image.load(os.path.join(filename,'pipetest10.png')).convert_alpha()
piperight = pg.transform.scale(piperight, (30, 30))

pipeupdown = pg.image.load(os.path.join(filename,'pipetest01.png')).convert_alpha()
pipeupdown = pg.transform.scale(pipeupdown, (30, 30))

pipeleftright = pg.image.load(os.path.join(filename,'pipetest02.png')).convert_alpha()
pipeleftright = pg.transform.scale(pipeleftright, (30, 30))

pipeupleft = pg.image.load(os.path.join(filename,'pipetest03.png')).convert_alpha()
pipeupleft = pg.transform.scale(pipeupleft, (30, 30))

pipeleftdown = pg.image.load(os.path.join(filename,'pipetest06.png')).convert_alpha()
pipeleftdown = pg.transform.scale(pipeleftdown, (30, 30))

pipeupright = pg.image.load(os.path.join(filename,'pipetest04.png')).convert_alpha()
pipeupright = pg.transform.scale(pipeupright, (30, 30))

pipedownright = pg.image.load(os.path.join(filename,'pipetest05.png')).convert_alpha()
pipedownright = pg.transform.scale(pipedownright, (30, 30))




class combiner():
    def __init__(self):
        self.vlaues = 0
    def draw_structre(self):
        for pos in self.locs:
            up = False
            left = False
            down = False
            right = False
            cur = builder0
            if (pos.x-1,pos.y) in pipes.locs:
                left = True
            if (pos.x+1,pos.y) in pipes.locs:
                right = True
            if (pos.x,pos.y-1) in pipes.locs:
                up = True
            if (pos.x,pos.y+1) in pipes.locs:
                down = True
            if up and left and down and right:
                cur = builderall
            elif right and left and down:
                cur = builderdownrightleft
            elif up and left and right:
                cur = builderuprightleft
            elif up and down and right:
                cur = builderupdownright
            elif up and left and down:
                cur = builderupdownleft
            elif down and right:
                cur = builderdownright
            elif left and right:
                cur = builderleftright
            elif left and down:
                cur = builderdownleft
            elif up and left:
                cur = builderupleft
            elif up and down:
                cur = builderupdown
            elif up and right:
                cur = builderupright
            elif up:
                cur = builderup
            elif left:
                cur = builderleft
            elif right:
                cur = builderright
            elif down:
                cur = builderdown
            goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
            screen.blit(cur, cur.get_rect(center=goal_center))
            draw_text(str(self.values[(pos.x,pos.y)]),20,RED,pos.x*TILESIZE,pos.y*TILESIZE)
    def add(self,mpos):
        self.locs.append(mpos)
        self.values.update({(mpos.x,mpos.y):0})

combiner = combiner()
combiner.locs = []
combiner.values = {}

class pipes():
    def __init__(self):
        self.locs = 0
    def draw_pipe(self):
        for pos in self.locs:
            up = False
            left = False
            down = False
            right = False
            cur = pipe0
            if (pos.x-1,pos.y) in pipes.locs or (pos.x-1,pos.y) in combiner.locs:
                left = True
            if (pos.x+1,pos.y) in pipes.locs or (pos.x+1,pos.y) in combiner.locs:
                right = True
            if (pos.x,pos.y-1) in pipes.locs or (pos.x,pos.y-1) in combiner.locs:
                up = True
            if (pos.x,pos.y+1) in pipes.locs or (pos.x,pos.y+1) in combiner.locs:
                down = True
            if down and right:
                cur = pipedownright
            elif left and right:
                cur = pipeleftright
            elif left and down:
                cur = pipeleftdown
            elif up and left:
                cur = pipeupleft
            elif up and down:
                cur = pipeupdown
            elif up and right:
                cur = pipeupright
            elif up:
                cur = pipeup
            elif left:
                cur = pipeleft
            elif right:
                cur = piperight
            elif down:
                cur = pipedown
            goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
            screen.blit(cur, cur.get_rect(center=goal_center))
    def add(self,mpos):
        self.locs.append(mpos)
pipes = pipes()
pipes.locs = []

everything = []

class extractor():
    def __init__(self):
        self.locs = 0
    def add(self,mpos):
        self.locs.append(mpos)
extractor = extractor()
extractor.locs = []

connections = {}



checkaround = [vec(0,-1),vec(-1,0),vec(0,1),vec(1,0)]

def checkconnections(pos,x):
    e = [pos+k for k in checkaround]
    fell = True
    isac = False
    for ww in e:
        if ww in everything:
            if ww not in combiner.locs:
                fell = False
                for ll in connections:
                    for ee in connections[ll]:
                        if ww == ee:
                            connections[ll].append(pos)
            else:
                fell = False
                isac = True
                save = ww
                
    if fell:
        noc = 0
        for ll in connections:
            noc += 1
        connections.update({noc:[pos]})
        innouts.update({noc:[]})
    if isac:
        noc = 0
        for ll in connections:
            noc += 1
        connections.update({noc:[pos]})
        connections[noc].append(save)
        innouts.update({noc:[]})
    checker = []
    x.add(mpos)
    everything.append(mpos)
    #if x != combiner:
    print(connections)
    for jj in everything:
        for ll in connections:
            for ee in connections[ll]:
                if jj == ee and ee not in combiner.locs:
                    checker.append(ll)
                    print(checker)
        if len(checker) > 1:
            save = ll
            for qq in checker:
                if qq < save:
                    save = qq
            #test = dict(connections)
            for ll in checker:
                if ll != save:
                    for ee in connections[ll]:
                        if ee != mpos:
                            connections[save].append(ee)
                    del connections[ll]
                    del innouts[ll]
        checker = []
    checker = []
    #for qq in combiner:
    #    for ll in connections:
    #        for ee in connections[ll]:
    #            if ee == qq and len(connections[ll]) == 1:
    #                checker.append(ll)
    #    if len(checker) > 1:
    #        save = ll
    #        for qq in checker:
    #            if qq < save:
    #                save = qq
    #        #test = dict(connections)
    #        for ll in checker:
    #            if ll != save:
    #                for ee in connections[ll]:
    #                    if ee != mpos:
    #                        connections[save].append(ee)
    #                del connections[ll]
    #                del innouts[ll]
innouts = {}

def checkputs():
    check = []
    for ww in innouts:
        for ee in innouts[ww]:
            check.append(ee[0])
    for ll in connections:
        for x in connections[ll]:
            if x not in check:
                if x in extractor.locs:
                    innouts[ll].append((x,False))
            if x in combiner.locs:
                check = []
                for ee in innouts[ll]:
                    check.append(ee[0])
                if x not in check:
                        innouts[ll].append((x,True))
    

def checkifconnedted():
    
    for qq in innouts:
        out = []
        inpu = []
        for ww in innouts[qq]:
            if ww[1] == False:
                out.append(ww[0])
            if ww[1] == True:
                inpu.append(ww[0])
        if len(out) > 0 and len(inpu) > 0:
            x = 0
            for ee in out:
                x += get_structreamount(ee)
            x = x/int(len(inpu))
            for ww in inpu:
                if ww in combiner.locs:
                    combiner.values[(ww.x,ww.y)] += x 
def get_structreamount(cur):
    if cur in extractor.locs:
        ret = random.randint(10,20)
    if cur in combiner.locs:
        ret = combiner.values[cur]
    return ret

def draw_structre():
    combiner.draw_structre()
    pipes.draw_pipe()

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
        if event.type == pg.MOUSEBUTTONDOWN:
            mpos = vec(pg.mouse.get_pos()) // TILESIZE
            if event.button == 1:
                checkconnections(mpos,combiner)
            if event.button == 2:
                checkconnections(mpos,extractor)
            if event.button == 3:
                checkconnections(mpos,pipes)
                
                
                
            print('pipes',pipes)
            print('combiner',combiner)
            print('connections',connections)
            checkputs()
            print('innouts',innouts)
            
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    draw_grid()
    draw_structre()
    checkifconnedted()
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways