import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

TILESIZE = 30
GRIDWIDTH = 64
GRIDHEIGHT = 36
WIDTH = TILESIZE * GRIDWIDTH
HEIGHT = TILESIZE * GRIDHEIGHT
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

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN,display = 1)
clock = pg.time.Clock()

class enemy():
    class conrift():
        def __init__(self):
            self.vec = 0
            self.health = 0
            self.combat_animation = 0
            self.clickaura = []
    class magee():
        def __int__(self):
            self.vec = 0
            self.health = 0
            self.combat_animation = 0    
            self.clickaura = []

conrift_combat_img = pg.image.load('images/Layer 1_conrift_combat1.png').convert_alpha()
conrift_combat_img = pg.transform.scale(conrift_combat_img, (256, 256))
conrift_combat2_img = pg.image.load('images/Layer 1_conrift_combat2.png').convert_alpha()
conrift_combat2_img = pg.transform.scale(conrift_combat2_img, (256, 256))
conrift_combat3_img = pg.image.load('images/Layer 1_conrift_combat3.png').convert_alpha()
conrift_combat3_img = pg.transform.scale(conrift_combat3_img, (256, 256))

C = enemy.conrift()
C.vec = vec(43,20)
C.health = 50
C.combat_animation = {1:conrift_combat_img,2:conrift_combat2_img,3:conrift_combat3_img}
C.clickaura = [vec(-1,0),vec(-1,1),vec(-1,2),vec(-1,3),vec(-1,-1),vec(-1,-2),vec(-1,-3),vec(0,0),vec(0,1),vec(0,2),vec(0,3),vec(0,-1),vec(0,-2),vec(0,-3),vec(1,0),vec(1,1),vec(1,2),vec(1,3),vec(1,-1),vec(1,-2),vec(1,-3)]


home_img = pg.image.load('images/magee_combat.png').convert_alpha()
home_img = pg.transform.scale(home_img, (256, 256))

mage = enemy.magee()
mage.vec = vec(43,20)
mage.health = 30
mage.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, -1), (1, -1), (2, -1), (2, -2), (1, -2), (0, -2), (0, -3), (1, -3), (2, -3)]
mage.clickaura = []
for aura in auras:
    mage.clickaura.append(vec(aura))
#print(mage.clickaura)

def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))

class main():
    def __int__(self):
        self.heplanevec = 0
        self.current_animation = 0
        self.heplane_combat_animation = 0
        self.enemy = 0
        #self.clickaura = 0
    def draw_icons(self):
        ani = M.heplane_combat_animation
        goal_center = (self.heplanevec.x * TILESIZE + TILESIZE / 2, self.heplanevec.y * TILESIZE + TILESIZE / 2)
        screen.blit(ani[self.current_animation], ani[self.current_animation].get_rect(center=goal_center))
        
        for x in self.enemy:   
            ani = x.combat_animation 
            vec = self.enemy[x][0]    
            goal_center = (vec.x * TILESIZE + TILESIZE / 2, vec.y * TILESIZE + TILESIZE / 2)
            screen.blit(ani[self.current_animation], ani[self.current_animation].get_rect(center=goal_center))
            rect = pg.Rect(vec.x*TILESIZE, vec.y*TILESIZE, 30, 30)
            pg.draw.rect(screen,RED,rect)
    def draw_healthbar(self):
        for x in self.enemy:
            vec = self.enemy[x][0]
            heat = self.enemy[x][1] 
            #print(heat)
            rect = pg.Rect(vec.x*TILESIZE - 10, vec.y*TILESIZE - 120, heat, 20)
            pg.draw.rect(screen,RED,rect)
    def checkifdead(self):
        for x in self.enemy:
            if self.enemy[x][1] <=0 :
                self.enemy[x][0] = vec(-9,-9)
    def numberofenemy(self):
        if len(self.enemy) == 2:
            self.enemy[enemy1][0] = vec(43,10)
            self.enemy[enemy2][0] = vec(43,25)
            self.enemy[enemy1][2] = [self.enemy[enemy1][0]+ x for x in enemy1.clickaura]
            self.enemy[enemy2][2] = [self.enemy[enemy2][0]+ x for x in enemy2.clickaura]
    def getaura(self):
        y = []
        for x in self.enemy:
            y += self.enemy[x][2]
        return y

        

heplane_combat_img = pg.image.load('images/Layer 1_heplane_combat1.png').convert_alpha()
heplane_combat_img = pg.transform.scale(heplane_combat_img, (256, 256))
heplane_combat2_img = pg.image.load('images/Layer 1_heplane_combat2.png').convert_alpha()
heplane_combat2_img = pg.transform.scale(heplane_combat2_img, (256, 256))
heplane_combat3_img = pg.image.load('images/Layer 1_heplane_combat3.png').convert_alpha()
heplane_combat3_img = pg.transform.scale(heplane_combat3_img, (256, 256))

M = main()
M.heplanevec = vec(20,20)
M.heplane_combat_animation = {1:heplane_combat_img,2:heplane_combat2_img,3:heplane_combat3_img}
M.current_animation = 1
M.enemy = {}
for x in range(1,random.randint(2,3)):
    if x == 1:
        enemy1 = random.choice([mage])
        tout = enemy1.vec
        eat = enemy1.health
        M.enemy.update({enemy1:[tout,eat,[tout + x for x in enemy1.clickaura]]})
    if x == 2:
        enemy2 = random.choice([C])
        tout = enemy2.vec
        eat = enemy2.health
        M.enemy.update({enemy2:[tout,eat,[tout + x for x in enemy2.clickaura]]})
#M.clickaura = [vec(-1,-1)]


M.numberofenemy()

create = []

anim_timer = pg.time.get_ticks()
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mpos = vec(pg.mouse.get_pos()) // TILESIZE
                print(M.getaura())
                print(mpos)
                if mpos in M.getaura():
                    if mpos in M.enemy[enemy1][2]:
                        M.enemy[enemy1][1] -= 5
                    elif mpos in M.enemy[enemy2][2]:
                        M.enemy[enemy2][1] -= 5
                M.checkifdead()
                #create.append(mpos)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                M.enemy = random.choice([C,mage])
            if event.key == pg.K_a:
                print([(int(loc.x - M.enemy[enemy1][0].x), int(loc.y - M.enemy[enemy1][0].y)) for loc in create])
            if event.key == pg.K_m:
                print(M.conriftvec)
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit
            
                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    current_time = pg.time.get_ticks()
    if current_time - anim_timer > 1000:
        M.current_animation += 1
        if M.current_animation == 4:
            M.current_animation = 1
        anim_timer = pg.time.get_ticks()
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    # anything down here will be displayed ontop of anything above
    draw_grid()
    M.draw_icons()
    M.draw_healthbar()
    pg.display.flip() # dose the changes goto doccumentation for other ways