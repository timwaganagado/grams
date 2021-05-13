import pygame as pg
from os import path
from collections import deque
import random
import copy
import shelve
import os , sys
vec = pg.math.Vector2

TILESIZE = 30
GRIDWIDTH = 64
GRIDHEIGHT = 36
WIDTH = TILESIZE * GRIDWIDTH
HEIGHT = TILESIZE * GRIDHEIGHT
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

pg.init()
try:
    screen = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN,display = 1)
except:
    screen = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN,display = 0)
clock = pg.time.Clock()


def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font("C:\Windows\Fonts\Arial.ttf",size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (int(x), int(y))})
    screen.blit(text_surface, text_rect)

class enemy():
    class conrift():
        def __init__(self):
            self.vec = 0
            self.health = 0
            self.combat_animation = 0
            self.clickaura = []
            self.attacks = 0
    class conrift2():
        def __init__(self):
            self.vec = 0
            self.health = 0
            self.combat_animation = 0
            self.clickaura = []
            self.attacks = 0
    class magee():
        def __int__(self):
            self.vec = 0
            self.health = 0
            self.combat_animation = 0    
            self.clickaura = []
            self.attacks = 0
    class magee2():
        def __int__(self):
            self.vec = 0
            self.health = 0
            self.combat_animation = 0    
            self.clickaura = []
            self.attacks = 0

filename = os.path.dirname(sys.argv[0])
filename += '\Halood_images'
print(filename)


conrift_combat_img = pg.image.load(os.path.join(filename,'Layer 1_conrift_combat1.png')).convert_alpha()
conrift_combat_img = pg.transform.scale(conrift_combat_img, (256, 256))
conrift_combat2_img = pg.image.load(os.path.join(filename,'Layer 1_conrift_combat2.png')).convert_alpha()
conrift_combat2_img = pg.transform.scale(conrift_combat2_img, (256, 256))
conrift_combat3_img = pg.image.load(os.path.join(filename,'Layer 1_conrift_combat3.png')).convert_alpha()
conrift_combat3_img = pg.transform.scale(conrift_combat3_img, (256, 256))

C = enemy.conrift()
C.vec = vec(43,20)
C.health = 50
C.combat_animation = {1:conrift_combat_img,2:conrift_combat2_img,3:conrift_combat3_img}
C.clickaura = [vec(-1,0),vec(-1,1),vec(-1,2),vec(-1,3),vec(-1,-1),vec(-1,-2),vec(-1,-3),vec(0,0),vec(0,1),vec(0,2),vec(0,3),vec(0,-1),vec(0,-2),vec(0,-3),vec(1,0),vec(1,1),vec(1,2),vec(1,3),vec(1,-1),vec(1,-2),vec(1,-3)]
C.attacks = {'darkness':[4,5],'conduction':[16,1]}


C2 = enemy.conrift2()
C2.vec = vec(43,20)
C2.health = 50
C2.combat_animation = {1:conrift_combat_img,2:conrift_combat2_img,3:conrift_combat3_img}
C2.clickaura = [vec(-1,0),vec(-1,1),vec(-1,2),vec(-1,3),vec(-1,-1),vec(-1,-2),vec(-1,-3),vec(0,0),vec(0,1),vec(0,2),vec(0,3),vec(0,-1),vec(0,-2),vec(0,-3),vec(1,0),vec(1,1),vec(1,2),vec(1,3),vec(1,-1),vec(1,-2),vec(1,-3)]
C2.attacks = {'darkness':[4,5],'conduction':[16,1]}



home_img = pg.image.load(os.path.join(filename,'magee_combat.png')).convert_alpha()
home_img = pg.transform.scale(home_img, (256, 256))

mage = enemy.magee()
mage.vec = vec(43,20)
mage.health = 30
mage.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, -1), (1, -1), (2, -1), (2, -2), (1, -2), (0, -2), (0, -3), (1, -3), (2, -3)]
mage.clickaura = []
for aura in auras:
    mage.clickaura.append(vec(aura))
mage.attacks = {'fire ball':[10,3],'miss':[0,1]}

mage2 = enemy.magee2()
mage2.vec = vec(43,20)
mage2.health = 30
mage2.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, -1), (1, -1), (2, -1), (2, -2), (1, -2), (0, -2), (0, -3), (1, -3), (2, -3)]
mage2.clickaura = []
for aura in auras:
    mage2.clickaura.append(vec(aura))
mage2.attacks = {'fire ball':[10,3],'miss':[0,1]}

def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))





class ally():
    class heplane():
        def __init__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            blooddamage = int(M.allies[H][1])/100 + 1
            M.allies[H][1] -= self.attacks[M.selectedattack][0][1]
            self.healdam.append(int((blooddamage * self.attacks[attack][0][0])/2))
            M.enemy[target][1] -= blooddamage * self.attacks[attack][0][0]
        def support(self,target):
            if target == H:
                for x in self.healdam:
                    M.allies[M.selectedchar][1] += x
                self.healdam = []
                if M.allies[M.selectedchar][1] > 50:
                    M.allies[M.selectedchar][1] = 50
        def draw_icons(self):
            for x in self.attacks:
                icon = self.attacks[x][1]
                pos = self.attacks[x][2]
                rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 128)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                text = str(round(int((M.allies[ally1][1]/100 + 1) * self.attacks[self.attack1][0][0])))
                draw_text(text, 20, RED, self.attacks[self.attack1][2].x*TILESIZE, self.attacks[self.attack1][2].y*TILESIZE - 50)
                text = str(round(int((M.allies[ally1][1]/100 + 1) * self.attacks[self.attack2][0][0])))
                draw_text(text, 20, RED, self.attacks[self.attack2][2].x*TILESIZE, self.attacks[self.attack2][2].y*TILESIZE - 50)
                if len(ally1.healdam) != 0:
                    l = 0
                    for x in ally1.healdam:
                        l += x
                    text = str(l)
                else:
                    text = str(0)
                draw_text(text, 20, GREEN, self.attacks[self.attack3][2].x*TILESIZE, self.attacks[self.attack3][2].y*TILESIZE - 50)
    class sri():
        def __int__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            for x in M.enemy:
                M.enemy[x][1] += -2
        def support(self,target):
            attack = M.selectedattack
            if attack == self.attack2:
                M.allies[target][3] += 10
                if M.allies[target][3] > target.health:
                    M.allies[target][3] = target.health
            elif attack == self.attack3:
                M.allies[target][1] += 10
                if M.allies[target][1] > target.health:
                    M.allies[target][1] = target.health
        def draw_icons(self):
            for x in self.attacks:
                icon = self.attacks[x][1]
                pos = self.attacks[x][2]
                rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 128)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                text = str(self.attacks[self.attack1][0])
                draw_text(text, 20, RED, self.attacks[self.attack1][2].x*TILESIZE, self.attacks[self.attack1][2].y*TILESIZE - 50)
                text = str(10)
                draw_text(text, 20, BLUE, self.attacks[self.attack2][2].x*TILESIZE, self.attacks[self.attack2][2].y*TILESIZE - 50)
                text = str(10)
                draw_text(text, 20, GREEN, self.attacks[self.attack3][2].x*TILESIZE, self.attacks[self.attack3][2].y*TILESIZE - 50)

iconaura = [(2, 2), (2, 1), (2, 0), (2, -1), (2, -2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1), (0, 0), (0, -1), (0, -2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (-2, 2), (-2, 1), (-2, 0), (-2, -1), (-2, -2)]            
H = ally.heplane()
heplane_combat_img = pg.image.load(os.path.join(filename,'Layer 1_heplane_combat1.png')).convert_alpha()
heplane_combat_img = pg.transform.scale(heplane_combat_img, (256, 256))
heplane_combat2_img = pg.image.load(os.path.join(filename,'Layer 1_heplane_combat2.png')).convert_alpha()
heplane_combat2_img = pg.transform.scale(heplane_combat2_img, (256, 256))
heplane_combat3_img = pg.image.load(os.path.join(filename,'Layer 1_heplane_combat3.png')).convert_alpha()
heplane_combat3_img = pg.transform.scale(heplane_combat3_img, (256, 256))
heplane_ability1_img = pg.image.load(os.path.join(filename,'bloodcell-1.png'))
heplane_ability1_img = pg.transform.scale(heplane_ability1_img, (128, 128))
heplane_ability2_img = pg.image.load(os.path.join(filename,'fist-1.png'))
heplane_ability2_img = pg.transform.scale(heplane_ability2_img, (128, 128))
heplane_ability3_img = pg.image.load(os.path.join(filename,'blood heal-1.png'))
H.attack1 = 'coilent'
H.attack2 = 'punch'
H.attack3 = 'blood heal'
H.vec = vec(20,15)
H.health = 50
H.shield = 0
H.combat_animation = {1:heplane_combat_img,2:heplane_combat2_img,3:heplane_combat3_img}
H.attacks = {H.attack1:[[10,5],heplane_ability1_img,vec(18, 31),[vec(18,31) + a for a in iconaura],False],H.attack2:[[5,0],heplane_ability2_img,vec(23,31),[vec(23,31) + a for a in iconaura],False],H.attack3:[[0,0],heplane_ability3_img,vec(28,31),[vec(28,31)+ a for a in iconaura],True]}
H.healdam = []
aura = [(1, 3), (0, 3), (-1, 3), (-1, 2), (0, 2), (1, 2), (1, 1), (0, 1), (-1, 1), (-1, 0), (0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, -2), (0, -2), (1, -2), (1, -3), (0, -3), (-1, -3)]
H.clickaura = [H.vec + a for a in aura]

S = ally.sri()
sri_combat_img = pg.image.load(os.path.join(filename,'Layer 1_sri_combat1.png')).convert_alpha()
sri_combat_img = pg.transform.scale(sri_combat_img, (256, 256))
sri_combat2_img = pg.image.load(os.path.join(filename,'Layer 1_sri_combat2.png')).convert_alpha()
sri_combat2_img = pg.transform.scale(sri_combat2_img, (256, 256))
sri_combat3_img = pg.image.load(os.path.join(filename,'Layer 1_sri_combat3.png')).convert_alpha()
sri_combat3_img = pg.transform.scale(sri_combat3_img, (256, 256))
sri_ability1_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
sri_ability1_img = pg.transform.scale(sri_ability1_img, (128, 128))
sri_ability2_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
sri_ability2_img = pg.transform.scale(sri_ability2_img, (128, 128))
sri_ability3_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
sri_ability3_img = pg.transform.scale(sri_ability2_img, (128, 128))
S.attack1 = 'flash and crash'
S.attack2 = 'crystal glass'
S.attack3 = 'karen and her healing balony'
S.vec = vec(20,25)
S.health = 25
S.shield = 10
S.combat_animation = {1:sri_combat_img,2:sri_combat2_img,3:sri_combat3_img}
S.attacks = {S.attack1:[2,sri_ability1_img,vec(18,31),[vec(18,31) + a for a in iconaura],False],S.attack2:[0,sri_ability2_img,vec(23,31),[vec(23,31) + a for a in iconaura],True],S.attack3:[0,sri_ability3_img,vec(28,31),[vec(28,31)+a for a in iconaura],True]}
S.clickaura = [S.vec + a for a in aura]


class main():
    def __int__(self):
        self.current_animation = 0
        self.allies
        self.enemy = 0
        self.display = 0
        self.damage = 0
        #self.clickaura = 0
    def draw_char(self):
        for x in self.allies:
            ani = dict(x.combat_animation)
            vec = self.allies[x][0]
            cur = ani[self.current_animation]
            goal_center = (int(vec.x * TILESIZE + TILESIZE / 2), int(vec.y * TILESIZE + TILESIZE / 2))
            if x in self.actions:
                cur = cur.copy( )
                cur.fill((105, 105, 105, 255),special_flags=pg.BLEND_RGB_MULT)            
            if x == self.selectedchar:
                lol = cur.copy()
                lol = pg.transform.scale(lol, (285, 265))
                lol.fill((0, 0, 0),special_flags=pg.BLEND_RGB_MULT)
                lel = lol.get_rect(center=goal_center)
                lel[1] -=2
                screen.blit(lol, lel)
            screen.blit(cur, cur.get_rect(center=goal_center))
        
        for x in self.enemy:   
            ani = x.combat_animation 
            vec = self.enemy[x][0]    
            goal_center = (int(vec.x * TILESIZE + TILESIZE / 2), int(vec.y * TILESIZE + TILESIZE / 2))
            screen.blit(ani[self.current_animation], ani[self.current_animation].get_rect(center=goal_center))
    def draw_icons(self):
        if M.selectedchar == ally1:
            ally1.draw_icons()
        if M.selectedchar == ally2:
            ally2.draw_icons()
    def draw_healthbar(self):
        for x in self.allies:
            vec = self.allies[x][0]
            heat = self.allies[x][1]
            rect = pg.Rect(int(vec.x*TILESIZE - 10), int(vec.y*TILESIZE - 120), int(heat), 20)
            pg.draw.rect(screen,RED,rect)
            if self.allies[x][3] > 0:
                text = '/'+str(x.health)
                text2 = str(heat+self.allies[x][3])
                draw_text(text, 20,BLACK , vec.x*TILESIZE + 2, vec.y*TILESIZE - 150)
                draw_text(text2, 20, BLUE, vec.x*TILESIZE - 22, vec.y*TILESIZE - 150)
                rect = pg.Rect(int(vec.x*TILESIZE - 10), int(vec.y*TILESIZE - 120), int(self.allies[x][3]   ), 20)
                pg.draw.rect(screen,BLUE,rect)
            else:
                text = str(heat)+'/'+str(x.health)
                draw_text(text, 20, BLACK, vec.x*TILESIZE - 10, vec.y*TILESIZE - 150)
        for x in self.enemy:
            vec = self.enemy[x][0]
            heat = self.enemy[x][1] 
            text = str(round(heat))+'/'+str(x.health)
            draw_text(text, 20, BLACK, vec.x*TILESIZE - 10, vec.y*TILESIZE - 150)
            rect = pg.Rect(int(vec.x*TILESIZE - 10), int(vec.y*TILESIZE - 120), int(heat), 20)
            pg.draw.rect(screen,RED,rect)
    def draw_damage(self):
        if self.display == True:
            for x in self.damage:
                if len(self.damage[x]) == 2:
                    draw_text(str(self.damage[x][0]),30,RED,self.allies[x][0].x*TILESIZE-15, self.allies[x][0].y*TILESIZE-150,align="bottomright")
                    draw_text(str(self.damage[x][1]),30,RED,self.allies[x][0].x*TILESIZE+15, self.allies[x][0].y*TILESIZE-150,align="bottomright")
                else:
                    draw_text(str(self.damage[x][0]),30,RED,self.allies[x][0].x*TILESIZE, self.allies[x][0].y*TILESIZE-150,align="bottomright")    
    def draw_background(self):
        goal_center = int(WIDTH / 2), int(HEIGHT/ 2)
        screen.blit(background_fall, background_fall.get_rect(center=goal_center))
        
    def checkifdead(self):
        test = dict(self.enemy)
        for x in test:
            if test[x][1] <=0 :
                del self.enemy[x]
        test = dict(self.allies)
        for x in test:
            if test[x][1] <= 0:
                del self.allies[x]
        if len(self.allies) <= 0 or len(self.enemy) <= 0:
            ally1 = H
            ally2 = S

            self.selectedattack = 0
            self.selectedchar = 0
            self.current_animation = 1
            self.allies = {}
            self.enemy = {}
            self.l = []
            self.actions = []

            self.ally1 = ally1
            pos = self.ally1.vec
            eat = self.ally1.health
            lean = self.ally1.shield
            self.allies.update({self.ally1:[pos,eat,self.ally1.clickaura,lean]})

            self.ally2 = ally2
            pos = self.ally2.vec
            eat = self.ally2.health
            lean = self.ally2.shield
            self.allies.update({self.ally2:[pos,eat,self.ally2.clickaura,lean]})
            for x in range(1,3):#range(1,random.randint(2,3))
                if x == 1:
                    self.enemy1 = random.choice([C,mage])
                    tout = self.enemy1.vec
                    eat = self.enemy1.health
                    attack = self.enemy1.attacks
                    M.enemy.update({self.enemy1:[tout,eat,[tout + x for x in self.enemy1.clickaura],attack]})
                if x == 2:
                    self.enemy2 = random.choice([C,mage])
                    if self.enemy2 == self.enemy1:
                        if self.enemy2 == mage:
                            self.enemy2 = mage2
                        if self.enemy2 == C:
                            self.enemy2 = C2
                    tout = self.enemy2.vec
                    eat = self.enemy2.health
                    attack = self.enemy2.attacks
                    M.enemy.update({self.enemy2:[tout,eat,[tout + x for x in self.enemy2.clickaura],attack]})
            self.numberofenemy()
    def numberofenemy(self):
        if len(self.enemy) == 2:
            self.enemy[self.enemy1][0] = vec(43,10)
            self.enemy[self.enemy2][0] = vec(43,25)
            self.enemy[self.enemy1][2] = [self.enemy[self.enemy1][0]+ x for x in self.enemy1.clickaura]
            self.enemy[self.enemy2][2] = [self.enemy[self.enemy2][0]+ x for x in self.enemy2.clickaura]
    def getaura(self):
        y = []
        for x in self.enemy:
            y += self.enemy[x][2]
        for x in self.allies:
            y += self.allies[x][2]
        return y
    def selectingattack(self):
        y = []
        for z in self.allies:
            for x in z.attacks:
                y += z.attacks[x][3]
        return y
    def selectingchar(self):
        y = []
        for z in self.allies:
            for x in z.clickaura:
                y.append(x)
        return y
    def enemyattack(self):
        for x in self.enemy:
            attack = self.enemy[x][3]
            attacks = []
            chance = []
            possible = []
            for y in attack:
                chance.append(attack[y][1])
                attacks.append(attack[y][0])
            for x in self.allies:
                possible.append(x)
            target = random.choice(possible)
            damage = random.choices(attacks,chance)
            if self.allies[target][3] > 0:
                self.allies[target][3] -= damage[0]
                if self.allies[target][3] < 0:
                    self.allies[target][3] = 0
            else:
                self.allies[target][1] -= damage[0]
            if target in self.damage:
                self.damage[target].append(int(damage[0]))
            else:
                self.damage.update({target:[damage[0]]})
            self.click = True
            self.display = True
    def selectattack(self):
        if mpos in M.selectedchar.attacks[self.selectedchar.attack1][3]:
            M.selectedattack = self.selectedchar.attack1
            M.attackselect = True
        if mpos in M.selectedchar.attacks[self.selectedchar.attack2][3]:
            M.selectedattack = self.selectedchar.attack2
            M.attackselect = True
        if mpos in M.selectedchar.attacks[self.selectedchar.attack3][3]:
            M.selectedattack = self.selectedchar.attack3
            M.attackselect = True
        if self.selectedchar in self.actions:
            M.attackselect = False
    def selectchar(self):
        if mpos in ally1.clickaura:
            M.selectedchar = ally1
            M.charselect = True
        elif mpos in ally2.clickaura:
            M.selectedchar = ally2
            M.charselect = True
        
            

M = main()

ally1 = H
ally2 = S

M.selectedattack = 0
M.selectedchar = 0
M.current_animation = 1
M.allies = {}
M.enemy = {}
M.l = []
M.actions = []
background_fall = pg.image.load(os.path.join(filename,'backgorunds-2.png.png'))
background_fall = pg.transform.scale(background_fall, (1920, 1080))

M.ally1 = ally1
pos = M.ally1.vec
eat = M.ally1.health
lean = M.ally1.shield
M.allies.update({M.ally1:[pos,eat,M.ally1.clickaura,lean]}) #remeber to update list with clickaura with multiple characters

M.ally2 = ally2
pos = M.ally2.vec
eat = M.ally2.health
lean = M.ally2.shield
M.allies.update({M.ally2:[pos,eat,M.ally2.clickaura,lean]})


for x in range(1,random.randint(2,3)):
    if x == 1:
        M.enemy1 = random.choice([C,mage])
        tout = M.enemy1.vec
        eat = M.enemy1.health
        attack = M.enemy1.attacks
        M.enemy.update({M.enemy1:[tout,eat,[tout + x for x in M.enemy1.clickaura],attack]})
    if x == 2:
        M.enemy2 = random.choice([C,mage])
        if M.enemy2 == M.enemy1:
            if M.enemy2 == mage:
                M.enemy2 = mage2
            if M.enemy2 == C:
                M.enemy2 = C2
        tout = M.enemy2.vec
        eat = M.enemy2.health
        attack = M.enemy2.attacks
        M.enemy.update({M.enemy2:[tout,eat,[tout + x for x in M.enemy2.clickaura],attack]})
M.display = False
M.damage = {}
M.click = False
M.attackselect = False
#M.clickaura = [vec(-1,-1)]

attck_timer = 1000000
M.enemycanattack = False

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
                if mpos in M.getaura() and M.selectedchar != 0:
                    if M.attackselect == True and M.enemycanattack == False :
                        if M.selectedchar.attacks[M.selectedattack][4] != False:
                            if mpos in M.ally1.clickaura:
                                M.selectedchar.support(ally1)
                                attck_timer = pg.time.get_ticks()
                                M.actions.append(M.selectedchar)
                                M.attackselect = False
                                M.checkifdead()
                            elif mpos in M.ally2.clickaura:
                                M.selectedchar.support(ally2)
                                M.actions.append(M.selectedchar)
                                M.attackselect = False
                                M.checkifdead()
                            M.attackselect = False
                        else:
                            try:
                                if mpos in M.enemy[M.enemy1][2]:
                                    M.selectedchar.attack(M.enemy1,M.selectedattack)
                                    M.attackselect = False
                                    M.actions.append(M.selectedchar)
                                    M.checkifdead()
                            except:
                                pass
                            try:
                                if mpos in M.enemy[M.enemy2][2]:
                                    M.selectedchar.attack(M.enemy2,M.selectedattack)
                                    M.attackselect = False
                                    M.actions.append(M.selectedchar)
                                    M.checkifdead()
                            except:
                                pass
                            M.attackselect = False
                                
                        
                        
                            
                    else:
                        pass 
                if mpos in M.selectingattack():
                    M.selectattack()
                if mpos in M.selectingchar() and M.attackselect == False:
                    M.selectchar()
                if mpos not in M.getaura() and mpos not in M.selectingattack():
                    M.selectedchar = 0
                    M.attackselect = False
                create.append(mpos)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                M.enemy = random.choice([C,mage])
            if event.key == pg.K_a:
                print([(int(loc.x - M.heplanevec.x), int(loc.y - M.heplanevec.y)) for loc in create])
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
    if current_time - attck_timer > 1000 and M.enemycanattack == True:
        M.enemyattack()
        display_time = pg.time.get_ticks()   
        M.enemycanattack = False
        M.attackselect = False
        M.checkifdead()
    if len(M.actions) == len(M.allies) and M.enemycanattack == False:
        attck_timer = pg.time.get_ticks()
        M.enemycanattack = True
        M.actions = []
    if M.click == True:
        if current_time - display_time > 1000:
            M.enemycanattack = False
            M.display == False
            M.damage = {}
            M.click = False
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    # anything down here will be displayed ontop of anything above
    draw_grid()
    M.draw_background()
    M.draw_char()
    M.draw_icons()
    M.draw_healthbar()
    M.draw_damage()
    pg.display.flip() # dose the changes goto doccumentation for other ways