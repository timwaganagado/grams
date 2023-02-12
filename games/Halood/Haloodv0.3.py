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
WIDTH = 1920    
HEIGHT = 1080
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

class allycharacter:
    def __init__(self,pos):
        self.position = vec(pos)
        
        self.char_sprite = cross
        self.char_name = 'cross'
        self.colour = RED
        self.sizex = 500
        self.sizey = 128
        self.update_rectangle()
    def update_rectangle(self):
        self.rect = pg.Rect(int(self.position.x), int(self.position.y), self.sizex, self.sizey)
    def draw(self):
        pg.draw.rect(screen,BLACK,self.rect)
        goal_center = self.position.x+(self.sizey/2),self.position.y+(self.sizey/2)
        screen.blit(self.char_sprite,self.char_sprite.get_rect(center=goal_center))
        draw_text(self.char_name,50,self.colour,self.position.x+(self.sizex/2),self.position.y+(self.sizey /2),'center')

class enemycharacter:
    def __init__(self,pos):
        self.position = vec(pos)
        self.char_sprite = cross
        self.char_name = 'attackingcross'
        self.colour = RED
        self.sizex = 500
        self.sizey = 128
        self.update_rectangle()
    def update_rectangle(self):
        self.rect = pg.Rect(int(self.position.x), int(self.position.y-(self.sizey/2)), self.sizex , self.sizey)
    def draw(self):
        pg.draw.rect(screen,BLACK,self.rect)
        goal_center = self.position.x+self.sizex-(self.sizey/2),self.position.y
        screen.blit(self.char_sprite,self.char_sprite.get_rect(center=goal_center))
        draw_text(self.char_name,50,self.colour,self.position.x+(self.sizex/2),self.position.y,'center')

filename = os.path.dirname(sys.argv[0])
filename += '/Halood_images'

currentfileg =  filename +'/allies'  

cross = pg.image.load(os.path.join(filename,'cross-1.png.png')).convert_alpha()
cross = pg.transform.scale(cross, (50, 50))


class battlemanager:
    def __init__(self):
        self.selectedchar = 0
        self.player = [allycharacter((WIDTH/10,HEIGHT/5))]
        self.enemies = [enemycharacter((WIDTH*(7/10),HEIGHT/2))]
    def enemyturn(self):
        for x in self.enemies:
            x.selectattack()
    def draw(self):
        for x in self.player:
            x.draw()
        for x in self.enemies:
            x.draw()
    
    
bm = battlemanager()

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
    screen.fill(WHITE) # fills screnn with color
    bm.draw()
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways