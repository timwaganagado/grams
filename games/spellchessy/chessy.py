#spell auto battler
from email.policy import default
from re import X
from matplotlib.pyplot import text
import pygame as pg
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
vec = pg.math.Vector2

WIDTH = 960
HEIGHT = 540
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

filename = os.path.dirname(sys.argv[0])
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))

fireorb = pg.image.load(os.path.join(filename,'01.png')).convert_alpha()
fireorb = pg.transform.scale(fireorb, (50, 50))

coldorb = pg.image.load(os.path.join(filename,'06.png')).convert_alpha()
coldorb = pg.transform.scale(coldorb, (50, 50))

filename += '/primarys'



blackorb = pg.image.load(os.path.join(filename,'0.png')).convert_alpha()
blackorb = pg.transform.scale(blackorb, (50, 50))


class defualtpower:
    def attack(self,target,amount = 0):
        print(self)
        self.atk += amount
        target.damage(self.type,self,self.atk)
    def damage(self,cametype,came,amount):
        if cametype in self.weakness:
            if random.choices([True,False],[8,2])[0]:
                amount *= 2
        if self.type in came.weakness:
            amount/=2
        if amount <= 1:
            amount = 1
        self.health_current -= amount
    def health(self):
        print(self.health_current)
    def draw_orb(self):
        pos = self.vec
        screen.blit(self.look, self.look.get_rect(center=pos))
        draw_text(str(self.health_current),20,RED,pos.x,pos.y)
    
class fire():
    def __init__(self):
        self.type = fire
        self.weakness = [cold]
        self.speed = 5
        self.look = fireorb
    def attack(self,target):
        amount = self.atk
        print(self)
        super().attack(target,amount = amount)
    def __repr__(self):
        return ('fire')


class cold():
    def __init__(self):
        self.type = cold
        self.weakness = [random.randint(1,2)]
        self.speed = 2
        self.look = coldorb

        
def getorb(x,vec):
    class orb(x,defualtpower): 
        def __init__(self):
            super().__init__()
            self.atk = 1
            self.health_current = 50
            self.vec = vec

    return orb()

print(WIDTH/2+100)
positionally = [380,320,260,200,140]

allyorbs = []

ll = getorb(fire,vec(380,HEIGHT/2))
ww = getorb(cold,vec(260,HEIGHT/2))




ww.health()
ll.health()


clock = pg.time.Clock()


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
                ll.attack(ww)
                ww.attack(ll)
            
                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(BLACK) # fills screnn with color
    ww.draw_orb()
    ll.draw_orb()
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways