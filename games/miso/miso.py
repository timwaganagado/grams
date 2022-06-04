from ast import Pass
from cgi import test
from turtle import pos
from numpy import blackman
import pygame as pg
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
import copy


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

filename = os.path.dirname(sys.argv[0])
filename += '/misoimages'

font_name = pg.font.match_font('hack')
def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)
def draw_text_center(text, size, color, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x,y))
    screen.blit(text_surface, text_rect)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT),display = 0)

class player():
    def __init__(self):
        self.randomplayer()
        self.attacktimer = 0
        self.attacklimit = 0
        self.health = random.randint(6,12)
        self.curhealth = self.health
        self.currentattack = 2
        self.save = []
        self.kills = 0
    def draw(self):
        self.draw_char()
        self.draw_attackbar()
        self.draw_healthbar()
        self.draw_attacks()
    def randomplayer(self):
        picked = random.choice(prandomselect)
        self.image = pcollection[picked]
        self.attacks = []
        for x in range(0,2):
            pos = (1/15)
            rect = pg.Rect(WIDTH*pos+140*x, HEIGHT*(5/8), 60, 60)
            button = pg.draw.rect(screen,BLACK,rect)
            self.attacks.append([button,random.randint(3,7),random.randint(3,7)])
    def draw_char(self):
        cur = self.image[gloani]
        goal_center = (WIDTH*(3/8), HEIGHT/2)
        screen.blit(cur, cur.get_rect(center=(goal_center)))
    def draw_attackbar(self):
        if self.attacktimer != self.attacklimit:
            text = str(self.attacktimer)+'/'+str(self.attacklimit)
            draw_text_center(text,70,BLACK,WIDTH*(2/12), HEIGHT*(3/11))
            pos = (3/12)
            size = 250
            rect = pg.Rect(WIDTH*pos, HEIGHT*(1/4), size, 20)
            pg.draw.rect(screen,BLUE,rect)
            for y in range(0,self.attacklimit+1):
                rect = pg.Rect(WIDTH*pos+(size/self.attacklimit)*y-10, HEIGHT*(1/4), 10, 20)
                pg.draw.rect(screen,BLACK,rect)
            for y in range(0,self.attacktimer):
                rect = pg.Rect(int(WIDTH*pos+(size/self.attacklimit)*y), HEIGHT*(1/4), int(250/self.attacklimit)-5, 20)
                pg.draw.rect(screen,RED,rect)
    def draw_healthbar(self):
        text = str(self.curhealth)+'/'+str(self.health)
        draw_text_center(text,70,BLACK,WIDTH*(2/12), HEIGHT*(1/8))
        pos = (3/12)
        rect = pg.Rect(WIDTH*pos, HEIGHT*(1/8), 250, 20)
        pg.draw.rect(screen,GREY,rect)
        for y in range(0,self.health+1):
            rect = pg.Rect(WIDTH*pos+(250/self.health)*y-10, HEIGHT*(1/8), 10, 20)
            pg.draw.rect(screen,BLACK,rect)
        for y in range(0,self.curhealth):
            rect = pg.Rect(int(WIDTH*pos+(250/self.health)*y), HEIGHT*(1/8), int(250/self.health)-5, 20)
            pg.draw.rect(screen,GREEN,rect)
    def draw_attacks(self):
        for x in self.attacks:
            save = 0
            for y in self.save:
                if x[0] == y[0]:
                    save = y
            text = str(x[1])
            if save != 0:
                if save[1] < x[1]:
                    text=str(save[1])+'+1'
            
            rect = x[0]

            pg.draw.rect(screen,GREY,rect)
            draw_text_center(text,70,BLACK,rect[0]+rect[2]/2, rect[1]+rect[3]/2)
            
            text = str(x[2])
            if save != 0:
                if save[2] < x[2]:
                    text = str(save[2])+'+1'
            
            draw_text_center(text,70,BLACK,rect[0]+rect[2]/2, rect[1]+rect[3]/2-100)
            posx = rect[0]+rect[2]/2 - 60
            posy = rect[1]+rect[3]/2 - 70
            size = 120
            rect = pg.Rect(posx, posy, size, 20)
            pg.draw.rect(screen,BLUE,rect)
            for y in range(0,x[2]+1):
                rect = pg.Rect(posx+(size/x[2])*y-10, posy, 10, 20)
                pg.draw.rect(screen,BLACK,rect)
    def selectattack(self):
        self.attacklimit = self.attacks[self.currentattack][2]
    def attack(self):
        E.curhealth -= self.attacks[self.currentattack][1]
        self.attacklimit = 0
        self.currentattack = 2
        


pcollection={}
prandomselect =[]

heplane_combat_img = pg.image.load(os.path.join(filename,'Layer 1_heplane_combat1.png')).convert_alpha()
heplane_combat_img = pg.transform.scale(heplane_combat_img, (255, 255))
heplane_combat2_img = pg.image.load(os.path.join(filename,'Layer 1_heplane_combat2.png')).convert_alpha()
heplane_combat2_img = pg.transform.scale(heplane_combat2_img, (255, 255))
heplane_combat3_img = pg.image.load(os.path.join(filename,'Layer 1_heplane_combat3.png')).convert_alpha()
heplane_combat3_img = pg.transform.scale(heplane_combat3_img, (255, 255))
heplaneimages = {1:heplane_combat_img,2:heplane_combat2_img,3:heplane_combat3_img}

pcollection.update({'heplane':heplaneimages})
prandomselect.append('heplane')

P = player()

class enemy():
    def __init__(self):
        self.randomenemy()
        self.attacktimer = 0
        self.attacklimit = random.randint(3,7+P.kills)
        self.attackdamage = random.randint(1,5+P.kills)
        self.health = random.randint(6,12+P.kills)
        self.curhealth = self.health
    def draw(self):
        self.draw_enemy()
        self.draw_attackbar()
        self.draw_healthbar()
    def draw_enemy(self):
        cur = self.image[gloani]

        goal_center = (WIDTH*(5/6), HEIGHT/2)
        screen.blit(cur, cur.get_rect(center=(goal_center)))    
        text = str(self.attackdamage)
        draw_text_center(text,70,BLACK,WIDTH*(4/6), HEIGHT*(1/2))
    def randomenemy(self):
        picked = random.choice(randomselect)
        self.image = collection[picked]
        print(self.image)
    def draw_attackbar(self):
        text = str(self.attacktimer)+'/'+str(self.attacklimit)
        draw_text_center(text,70,BLACK,WIDTH*(12/20), HEIGHT*(3/11))
        
        rect = pg.Rect(WIDTH*(17/25), HEIGHT*(1/4), 250, 20)
        pg.draw.rect(screen,BLUE,rect)
        for y in range(0,self.attacklimit+1):
            rect = pg.Rect(WIDTH*(17/25)+(250/self.attacklimit)*y-10, HEIGHT*(1/4), 10, 20)
            pg.draw.rect(screen,BLACK,rect)
        for y in range(0,self.attacktimer):
            rect = pg.Rect(int(WIDTH*(17/25)+(250/self.attacklimit)*y), HEIGHT*(1/4), int(250/self.attacklimit)-5, 20)
            pg.draw.rect(screen,RED,rect)
    def draw_healthbar(self):
        text = str(self.curhealth)+'/'+str(self.health)
        draw_text_center(text,70,BLACK,WIDTH*(12/20), HEIGHT*(1/8))
        rect = pg.Rect(WIDTH*(17/25), HEIGHT*(1/8), 250, 20)
        pg.draw.rect(screen,GREY,rect)
        for y in range(0,self.health+1):
            rect = pg.Rect(WIDTH*(17/25)+(250/self.health)*y-10, HEIGHT*(1/8), 10, 20)
            pg.draw.rect(screen,BLACK,rect)
        for y in range(0,self.curhealth):
            rect = pg.Rect(int(WIDTH*(17/25)+(250/self.health)*y), HEIGHT*(1/8), int(250/self.health)-5, 20)
            pg.draw.rect(screen,GREEN,rect)
    def attack(self):
        P.curhealth -= self.attackdamage

collection = {}
randomselect = []


swordguy_img = pg.image.load(os.path.join(filename,'Layer 1_swordguy_combat1.png')).convert_alpha()
swordguy_img = pg.transform.scale(swordguy_img, (255, 255))
swordguy2_img = pg.image.load(os.path.join(filename,'Layer 1_swordguy_combat2.png')).convert_alpha()
swordguy2_img = pg.transform.scale(swordguy2_img, (255, 255))
swordguy3_img = pg.image.load(os.path.join(filename,'Layer 1_swordguy_combat3.png')).convert_alpha()
swordguy3_img = pg.transform.scale(swordguy3_img, (255, 255))
swordguyimages =  {1:swordguy_img,2:swordguy2_img,3:swordguy3_img}

collection.update({'swordguy':swordguyimages})
randomselect.append('swordguy')

E = enemy()

potenemy = ['enemy1']
enemies = {}
for x in potenemy:
    enemies.update({x:enemy()})
print(enemies[potenemy[0]].curhealth)


screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

gloani= 1
anim_timer = pg.time.get_ticks()
pausetime = 0
pausetimer = 0

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
            if event.key == pg.K_r:
                E = enemy()
            if event.key == pg.K_e:
                P = player()
            if event.key == pg.K_w:
                E.curhealth -=1
            if P.currentattack == 2:
                if event.key == pg.K_1:
                    P.currentattack = 0
                    P.selectattack()
                if event.key == pg.K_2:
                    P.currentattack = 1
                    P.selectattack()
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    if P.curhealth <= 0:
        P = player()
        E = enemy()
    if E.curhealth <= 0:
        E = enemy()
        P.kills += 1
        if P.kills % 2 == 0:
            P.health += 1
            P.curhealth += 5
            if P.curhealth > P.health:
                P.curhealth = P.health
            
        picked = random.randint(1,4)
        P.save = copy.deepcopy(P.attacks)
        print(P.save)
        if picked == 1:
            P.attacks[0][1] = P.attacks[0][1] + 1
        if picked == 2:
            P.attacks[0][2] = P.attacks[0][2] + 1
        if picked == 3:
            P.attacks[1][1] = P.attacks[1][1] + 1
        if picked == 4:
            P.attacks[1][2] = P.attacks[1][2] + 1
        print(P.save)
    current_time = pg.time.get_ticks()
    if P.attacktimer == P.attacklimit:
        if pausetimer == 0:
            pausetimer = pg.time.get_ticks()
        pausetime = pausetimer - pg.time.get_ticks()
        if P.currentattack != 2:
            P.attacktimer = 0
            P.attack()
    else:
        pausetimer= 0
        pausetime = 0
        P.save = []
    if current_time - anim_timer+pausetime > 750:
        gloani += 1
        if gloani == 4:
            gloani = 1
        anim_timer = pg.time.get_ticks()
        
        E.attacktimer += 1
        if E.attacktimer > E.attacklimit:
            E.attacktimer = 0
            E.attack()
        
        P.attacktimer += 1
        
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    E.draw()
    P.draw()
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways