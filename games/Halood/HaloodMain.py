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
DARKBLUE = (0,0,139)
MOMENTUMCOLOR = (166, 138, 178)
check = 'working'

pg.init()
try:
    screen = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN,display = 1)
except:
    screen = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN,display = 0)
clock = pg.time.Clock()
cross = 'cross-1.png.png'

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
    class magee():
        def __init__(self):
            self.vec = 0
            self.health = 0
            self.combat_animation = 0    
            self.clickaura = []
            self.attacks = 0
    class swordguy():
        def __init__(self):
            self.vec = 0
    class lizard():
        def __init__(self):
            self.vec = 0
filename = os.path.dirname(sys.argv[0])
filename += '\Halood_images'


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
C.attacks = {'darkness':[5,5,[0,0,0],1],'conduction':[20,1,[1,0,1],1]}

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
mage.attacks = {'fire ball':[10,4,[0,0,1],1],'lightning':[15,1,[1,0,0],1],'ice shards':[5,2,[0,1,0],1],'miss':[0,2,[0,0,0],1]}

home_img = pg.image.load(os.path.join(filename,'swordguy_combat-1.png.png')).convert_alpha()
home_img = pg.transform.scale(home_img, (256, 256))

sword = enemy.swordguy()
sword.vec = vec(43,20)
sword.health = 30
sword.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
sword.clickaura = []
for aura in auras:
    sword.clickaura.append(vec(aura))
sword.attacks = {'slash':[4,4,[0,1,0],2],'miss':[0,2,[0,0,0],1]}

home_img = pg.image.load(os.path.join(filename,cross)).convert_alpha()
home_img = pg.transform.scale(home_img, (256, 256))

lizard = enemy.lizard()
lizard.vec = vec(43,20)
lizard.health = 25
lizard.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
lizard.clickaura = []
for aura in auras:
    lizard.clickaura.append(vec(aura))
lizard.attacks = {'pierce':[2,5,[0,1,0],3],'constrict':[5,1,[2,0,0],1],'miss':[0,2,[0,0,0],1]}

class boss():
    class courptbattlemage():
        def __init__(self):
            self.vec = 0
        def attack(self):
            if self.turncounter%3 == 0:
                for x in M.allies:
                    M.allies[x][1] - 5
                self.support([0])
            possible = []
            dead = []
            chance = []
            attacks = []
            for y in self.attacks:
                chance.append(self.attacks[y][1])
                attacks.append(y)
            for seesee in range(0,2):
                dead = []
                attacking = random.choices(attacks,chance)
                damage = self.attacks[attacking[0]]
                if damage[4]:
                    for x in M.spaces:
                        for l in M.spaces[x]:
                            if l[1] != 99:
                                possible.append(l[1])
                            else:
                                dead.append(l[1])
                else:
                    for x in M.spaces:
                        if x == 'front row':
                            for l in M.spaces[x]:
                                if l[1] != 99:
                                    possible.append(l[1])
                                else:
                                    dead.append(l[1])
                        if x == 'back row' and len(dead) == 2:
                            for j in M.spaces[x]:
                                possible.append(j[1])
                target = random.choice(possible)
                #print(attacking,damage[0])
                for x in range(0,damage[3]):
                    if M.allies[target][3] > 0:
                        M.allies[target][3] -= damage[0]
                        if M.allies[target][3] < 0:
                            M.allies[target][3] = 0
                    else:
                        M.allies[target][1] -= damage[0]
                        if damage[2][1] > 0:
                            print('bleed')
                            M.allies[target][4][1] += damage[2][1]
                    if damage[2][0] > 0:
                        print('stun')
                        M.allies[target][4][0] += damage[2][0]
                    if damage[2][2] > 0:
                        print('fire')
                        M.allies[target][4][2] += damage[2][2]
                    if target in M.damage:
                        M.damage[target].append(int(damage[0]))
                    else:
                        M.damage.update({target:[damage[0]]})
            self.turncounter += 1
        def support(self,target):
            if target[0] == 0:
                M.enemy[cbm][0][1] += M.enemy[cbm][0][1]*4/10
            print('heal')

cbm = boss.courptbattlemage()
cbm.vec = vec(43,20)
cbm.health = 100
cbm.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, -1), (1, -1), (2, -1), (2, -2), (1, -2), (0, -2), (0, -3), (1, -3), (2, -3)]
cbm.clickaura = []
cbm.turncounter = 0
for aura in auras:
    cbm.clickaura.append(vec(aura))
cbm.attacks = {'slash':[5,4,[0,0,0],2,False],'blast':[15,2,[0,0,1],1,False],'charging fire':[1,2,[0,0,3],1,True],'blinding light':[1,1,[1,0,0],1,True],'miss':[0,2,[0,0,0],1,True]}

class ally():
    def __init__(self):
        l = 0
    def profile(self,current,thing):
        current = current[1]
        l = vec(40,10)
        current = current.copy()
        rect = pg.Rect(0,100,0,150)
        current = pg.transform.chop(current,rect)
        current = pg.transform.scale(current,(300,128))
        goal_center = (int(l.x * TILESIZE + TILESIZE / 2), int(l.y * TILESIZE + TILESIZE / 2))
        screen.blit(current, current.get_rect(center=goal_center))
        draw_text(str(thing.lvl),50,BLACK,int(l.x * TILESIZE)-70,int(l.y * TILESIZE))
        draw_text(str(thing.exp)+'/'+str(thing.needtolvl),30,BLACK,int(l.x * TILESIZE)-90,int(l.y * TILESIZE+50))

    class heplane():
        def __init__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            blooddamage = int(M.allies[H][1])/int(self.health)+1+self.inc
            M.allies[self][1] -= self.attacks[attack][0][1]
            self.healdam.append(int((blooddamage * self.attacks[attack][0][0])/2))
            M.enemy[target][dup][1] -= blooddamage * self.attacks[attack][0][0]
            if self.attacks[attack][5][0] > 0:
                M.enemy[target][dup][4][0] += self.attacks[attack][5][0]
            if self.attacks[attack][5][1] > 0:
                M.enemy[target][dup][4][1] += self.attacks[attack][5][1]
            if self.attacks[attack][5][2] > 0:
                M.enemy[target][dup][4][2] += self.attacks[attack][5][2]
        def support(self,target):
            if 'self heal' in self.unlockedabilites:
                if target == H:
                    for x in self.healdam:
                        M.allies[M.selectedchar][1] += x
                    self.healdam = []
                    if M.allies[M.selectedchar][1] > 50:
                        M.allies[M.selectedchar][1] = 50
            else:
                M.actions.remove(H)
        def damage(self,taken):
            if M.allies[self][3] > 0:
                M.allies[self][3] -= taken[0]
                if M.allies[self][3] < 0:
                    M.allies[self][3] = 0
            else:
                M.allies[self][1] -= taken[0]
                if taken[2][1] > 0:
                    print('bleed')
                    M.allies[self][4][1] += taken[2][1]
        def draw_icons(self):

            text = str(round(int((M.allies[H][1]/self.health+1) * self.attacks[self.attack1][0][0])))

            text = str(round(int((M.allies[H][1]/self.health+1) * self.attacks[self.attack2][0][0])))
            
            
            icon = self.attacks[self.attack1][1]
            pos = self.attacks[self.attack1][2]
            rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 140)
            pg.draw.rect(screen,BLACK,rect)
            goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
            screen.blit(icon, icon.get_rect(center=goal_center))
            text = str(round(int((M.allies[H][1]/self.health+1+self.inc) * self.attacks[self.attack1][0][0])))
            draw_text(text, 20, RED, self.attacks[self.attack1][2].x*TILESIZE, self.attacks[self.attack1][2].y*TILESIZE + 65)
            
            icon = self.attacks[self.attack2][1]
            pos = self.attacks[self.attack2][2]
            rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 140)
            pg.draw.rect(screen,BLACK,rect)
            goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
            screen.blit(icon, icon.get_rect(center=goal_center))
            text = str(round(int((M.allies[H][1]/self.health+1+self.inc) * self.attacks[self.attack2][0][0])))
            draw_text(text, 20, RED, self.attacks[self.attack2][2].x*TILESIZE, self.attacks[self.attack2][2].y*TILESIZE + 65)

            
            if 'self heal' in self.unlockedabilites:
                if len(self.healdam) != 0:
                    l = 0
                    for x in self.healdam:
                        l += x
                        text = str(l)
                else:
                    text = str(0)
                icon = self.attacks[self.attack3][1]
                pos = self.attacks[self.attack3][2]
                rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 140)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                draw_text(text, 20, GREEN, self.attacks[self.attack3][2].x*TILESIZE, self.attacks[self.attack3][2].y*TILESIZE + 65)
        def draw_attack(self):
            pass
        def draw_skilltree(self):
            ally.profile(self.combat_animation,self)
            for z in self.abilities:
                pos = self.abilities[z][1]
                x = int(pos.x*TILESIZE-230)
                y = int(pos.y*TILESIZE-35)
                rect = pg.Rect(x, y, 50, 50)
                if self.abilities[z][2] == True:
                    self.abilities[z][0] = pg.draw.rect(screen,GREEN,rect)
                else:
                    self.abilities[z][0] = pg.draw.rect(screen,BLACK,rect)
        def skill(self,cur):
            if cur == 'self heal':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            if cur == 'increase':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.inc = 0.1
        def checklevel(self):
            if self.exp >= self.needtolvl:
                self.lvl += 1
                self.exp -= self.needtolvl
                self.needtolvl *= 2
    class cri():
        def __int__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            for x in M.enemy:
                if M.dup:
                    for y in M.enemy[x]:
                        y[1] -= self.attacks[self.attack1][0]
                else:
                    M.enemy[x][0][1] -= self.attacks[self.attack1][0]
            if self.attacks[attack][5][0] > 0:
                M.enemy[target][dup][4][0] += self.attacks[attack][5][0]
            if self.attacks[attack][5][1] > 0:
                M.enemy[target][dup][4][1] += self.attacks[attack][5][1]
            if self.attacks[attack][5][2] > 0:
                M.enemy[target][dup][4][2] += self.attacks[attack][5][2]
            self.passive(attack)
        def support(self,target):
            attack = M.selectedattack
            if attack == self.attack2:
                M.allies[target][3] += self.attacks[self.attack2][0]
                if M.allies[target][3] > target.health:
                    M.allies[target][3] = target.health
            elif attack == self.attack3:
                M.allies[target][1] += self.attacks[self.attack3][0]
                if M.allies[target][1] > target.health:
                    M.allies[target][1] = target.health
                stat = 0
                for x in M.allies[target][4]:
                    if stat != 0:
                        if x > 0:
                            M.allies[target][4][stat] = 0
                    stat += 1
            self.passive(attack)
        def passive(self,used):
            for x in self.attacks:
                if x == used:
                    self.attacks[x][0] += (1 + self.inc)
                else:
                    self.attacks[x][0] += (2 + self.inc)
                if x == self.attack1:
                    if self.attacks[x][0] >= self.stuncap:
                        self.attacks[x][5][0] = 1
                        print('stun')
                    if self.attacks[x][0] < self.stuncap:
                        self.attacks[x][5][0] = 0
                if self.attacks[x][0] > 10:
                    self.attacks[x][0] = 2
        def damage(self,taken):
            if M.allies[self][3] > 0:
                M.allies[self][3] -= taken[0]
                if M.allies[self][3] < 0:
                    M.allies[self][3] = 0
            else:
                M.allies[self][1] -= taken[0]
                if taken[2][1] > 0:
                    print('bleed')
                    M.allies[self][4][1] += taken[2][1]
        def draw_icons(self):
            for x in self.attacks:
                cur = cri_stunicon_img
                goal_center = (int(M.allies[self][0].x * TILESIZE + TILESIZE / 2 + 80), int(M.allies[self][0].y * TILESIZE + TILESIZE / 2 - 50))
                if self.attacks[self.attack1][0] < self.stuncap:
                    cur = cur.copy( )
                    cur.fill((105, 105, 105, 255),special_flags=pg.BLEND_RGB_MULT)            
                screen.blit(cur, cur.get_rect(center=goal_center))
                if S in M.allies: 
                    icon = self.attacks[x][1]
                    pos = self.attacks[x][2]
                    rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 150)
                    pg.draw.rect(screen,BLACK,rect)
                    goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                    screen.blit(icon, icon.get_rect(center=goal_center))
                    text = str(self.attacks[self.attack1][0])
                    draw_text(text, 20, RED, self.attacks[self.attack1][2].x*TILESIZE, self.attacks[self.attack1][2].y*TILESIZE + 75)
                    text = str(self.attacks[self.attack2][0])
                    draw_text(text, 20, BLUE, self.attacks[self.attack2][2].x*TILESIZE, self.attacks[self.attack2][2].y*TILESIZE + 75)
                    text = str(self.attacks[self.attack3][0])
                    draw_text(text, 20, GREEN, self.attacks[self.attack3][2].x*TILESIZE, self.attacks[self.attack3][2].y*TILESIZE + 75)
        def draw_attack(self):
            pass
        def draw_skilltree(self):
            ally.profile(self.combat_animation,self)
            for z in self.abilities:
                pos = self.abilities[z][1]
                x = int(pos.x*TILESIZE-230)
                y = int(pos.y*TILESIZE-35)
                rect = pg.Rect(x, y, 50, 50)
                if self.abilities[z][2] == True:
                    self.abilities[z][0] = pg.draw.rect(screen,GREEN,rect)
                else:
                    self.abilities[z][0] = pg.draw.rect(screen,BLACK,rect)
        def skill(self,cur):
            if cur == 'stun':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.stuncap = 6
            if cur == 'increase':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.inc = 1
        def checklevel(self):
            if self.exp >= self.needtolvl:
                self.lvl += 1
                self.exp -= self.needtolvl
                self.needtolvl *= 2
    class haptic():
        def __init__(self):
            attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            if self.momentum == 3:
                self.attacks[self.attack1][5][1] = 2
            else:
                self.attacks[self.attack1][5][1] = 0
            if attack == self.attack1:
                damage = (self.attacks[attack][0]+self.inc)*self.momentum
                
                self.momentum = 0
            else:
                damage = self.attacks[attack][0]+self.inc
                self.passive()
            
            M.enemy[target][dup][1] -= damage
            if self.attacktwice == True:
                M.enemy[target][dup][1] -= damage
                self.attacktwice = False
            if self.attacks[attack][5][0] > 0:
                M.enemy[target][dup][4][0] += self.attacks[attack][5][0]
            if self.attacks[attack][5][1] > 0:
                M.enemy[target][dup][4][1] += self.attacks[attack][5][1]
            if self.attacks[attack][5][2] > 0:
                M.enemy[target][dup][4][2] += self.attacks[attack][5][2]
            
        def support(self,target):
            if 'acceleration' in self.unlockedabilites:
                if target == Hap:
                    if  self.momentum > 0:
                        self.attacktwice = True
                        self.momentum -= 1
            else:
                M.actions.remove(Hap)
        def passive(self):
            self.momentum += 1
            if self.momentum >=3:
                self.momentum = 3
        def damage(self,taken):
            self.passive()
            chance = random.choices([1,0],[4,self.momentum*self.dodgec])
            print('yes')
            if chance[0] == 1:
                if M.allies[self][3] > 0:
                    M.allies[self][3] -= taken[0]
                    if M.allies[self][3] < 0:
                        M.allies[self][3] = 0
                else:
                    M.allies[self][1] -= taken[0]
                    if taken[2][1] > 0:
                        print('bleed')
                        M.allies[self][4][1] += taken[2][1]
        def draw_icons(self):
        
            rect = pg.Rect(int(M.allies[self][0].x*TILESIZE+80), int(M.allies[self][0].y*TILESIZE-50), 20, 135)
            pg.draw.rect(screen,MOMENTUMCOLOR,rect)
            for y in range(0,self.momentum):
                rect = pg.Rect(int(M.allies[self][0].x*TILESIZE+80), int(M.allies[self][0].y*TILESIZE+50-50*y), 20, 45)
                pg.draw.rect(screen,WHITE,rect)
            
                
            icon = self.attacks[self.attack1][1]
            pos = self.attacks[self.attack1][2]
            rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 150)
            pg.draw.rect(screen,BLACK,rect)
            goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
            screen.blit(icon, icon.get_rect(center=goal_center))
            text = str((self.attacks[self.attack1][0]+self.inc)*self.momentum)
            draw_text(text, 20, RED, self.attacks[self.attack1][2].x*TILESIZE, self.attacks[self.attack1][2].y*TILESIZE + 75)

            icon = self.attacks[self.attack2][1]
            pos = self.attacks[self.attack2][2]
            rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 150)
            pg.draw.rect(screen,BLACK,rect)
            goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
            screen.blit(icon, icon.get_rect(center=goal_center))
            text = str(self.attacks[self.attack2][0]+self.inc)
            draw_text(text, 20, RED, self.attacks[self.attack2][2].x*TILESIZE, self.attacks[self.attack2][2].y*TILESIZE + 75)

            if 'acceleration' in self.unlockedabilites:
                icon = self.attacks[self.attack3][1]
                pos = self.attacks[self.attack3][2]

                rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                text = str(self.attacks[self.attack3][0])
                draw_text(text, 20, BLACK, self.attacks[self.attack3][2].x*TILESIZE, self.attacks[self.attack3][2].y*TILESIZE + 75)
        def draw_skilltree(self):
            ally.profile(self.combat_animation,self)
            for z in self.abilities:
                pos = self.abilities[z][1]
                x = int(pos.x*TILESIZE-230)
                y = int(pos.y*TILESIZE-35)
                rect = pg.Rect(x, y, 50, 50)
                if self.abilities[z][2] == True:
                    self.abilities[z][0] = pg.draw.rect(screen,GREEN,rect)
                else:
                    self.abilities[z][0] = pg.draw.rect(screen,BLACK,rect)
        def skill(self,cur):
            if cur == 'acceleration':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            if cur == 'increase':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.inc = 1
            if cur == 'dodge':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.dodge = 1
        def checklevel(self):
            if self.exp >= self.needtolvl:
                self.lvl += 1
                self.exp -= self.needtolvl
                self.needtolvl *=2

ally = ally()
                    
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
H.healdam = []
H.inc = 0
H.abilities = {'self heal':[0,vec(47,17),True,'heal for half the damage dealt on enemies'],'increase':[0,vec(47,20),True,'Increases damage by 0.1']}
H.unlockedabilites = []
H.exp = 0
H.lvl = 0
H.needtolvl = 60
H.combat_animation = {1:heplane_combat_img,2:heplane_combat2_img,3:heplane_combat3_img}
H.attacks = {H.attack1:[[10,15],heplane_ability1_img,vec(18, 31),[vec(18,31) + a for a in iconaura],False,[1,0,0]],H.attack2:[[5,0],heplane_ability2_img,vec(23,31),[vec(23,31) + a for a in iconaura],False,[0,0,0]],H.attack3:[[0,0],heplane_ability3_img,vec(28,31),[vec(28,31)+ a for a in iconaura],True,[0,0,0]]}
aura = [(1, 3), (0, 3), (-1, 3), (-1, 2), (0, 2), (1, 2), (1, 1), (0, 1), (-1, 1), (-1, 0), (0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, -2), (0, -2), (1, -2), (1, -3), (0, -3), (-1, -3)]
H.clickaura = []
for x in aura:
    H.clickaura.append(vec(x))

S = ally.cri()
cri_combat_img = pg.image.load(os.path.join(filename,'Layer 1_cri_combat1.png')).convert_alpha()
cri_combat_img = pg.transform.scale(cri_combat_img, (256, 256))
cri_combat2_img = pg.image.load(os.path.join(filename,'Layer 1_cri_combat2.png')).convert_alpha()
cri_combat2_img = pg.transform.scale(cri_combat2_img, (256, 256))
cri_combat3_img = pg.image.load(os.path.join(filename,'Layer 1_cri_combat3.png')).convert_alpha()
cri_combat3_img = pg.transform.scale(cri_combat3_img, (256, 256))
cri_ability1_img = pg.image.load(os.path.join(filename,'crystal_icons-2.png.png'))
cri_ability1_img = pg.transform.scale(cri_ability1_img, (128, 128))
cri_ability2_img = pg.image.load(os.path.join(filename,'crystal_icons-3.png.png'))
cri_ability2_img = pg.transform.scale(cri_ability2_img, (128, 128))
cri_ability3_img = pg.image.load(os.path.join(filename,'crystal_icons-1.png.png'))
cri_ability3_img = pg.transform.scale(cri_ability3_img, (128, 128))
cri_stunicon_img = pg.image.load(os.path.join(filename,'sri_stun-1.png.png'))
cri_stunicon_img = pg.transform.scale(cri_stunicon_img, (128, 128))
S.attack1 = 'flash and crash'
S.attack2 = 'crystal glass'
S.attack3 = 'karen and her healing balony'
S.vec = vec(20,25)
S.health = 25
S.shield = 10
S.stuncap = 7
S.inc = 0
S.abilities = {'stun':[0,vec(47,17),True,'decreases the damage needed to stun from 7 to 6'],'increase':[0,vec(47,20),True,'increases the value that abilites increase to 2 rather then 1']}
S.unlockedabilites = []
S.exp = 0
S.lvl = 0
S.needtolvl = 60
S.combat_animation = {1:cri_combat_img,2:cri_combat2_img,3:cri_combat3_img}
S.attacks = {S.attack1:[5,cri_ability1_img,vec(18,31),[vec(18,31) + a for a in iconaura],False,[0,0,0]],S.attack2:[2,cri_ability3_img,vec(28,31),[vec(28,31)+a for a in iconaura],True,[0,0,0]],S.attack3:[2,cri_ability2_img,vec(23,31),[vec(23,31) + a for a in iconaura],True,[0,0,0]]}
S.clickaura = []
for x in aura:
    S.clickaura.append(vec(x))
    
Hap = ally.haptic()
haptic_combat_img = pg.image.load(os.path.join(filename,'Layer 1_haptic_combat1.png')).convert_alpha()
haptic_combat_img = pg.transform.scale(haptic_combat_img, (256, 256))
haptic_combat2_img = pg.image.load(os.path.join(filename,'Layer 1_haptic_combat2.png')).convert_alpha()
haptic_combat2_img = pg.transform.scale(haptic_combat2_img, (256, 256))
haptic_combat3_img = pg.image.load(os.path.join(filename,'Layer 1_haptic_combat3.png')).convert_alpha()
haptic_combat3_img = pg.transform.scale(haptic_combat3_img, (256, 256))
haptic_ability1_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
haptic_ability1_img = pg.transform.scale(haptic_ability1_img, (128, 128))
haptic_ability2_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
haptic_ability2_img = pg.transform.scale(haptic_ability2_img, (128, 128))
haptic_ability3_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
haptic_ability3_img = pg.transform.scale(haptic_ability3_img, (128, 128))
Hap.attack1 = 'accumulation'
Hap.attack2 = 'flailing'
Hap.attack3 = 'acceleration'
Hap.vec = vec(20,15)
Hap.health = 60
Hap.shield = 0
Hap.momentum = 0
Hap.inc = 0
Hap.dodgec = 0
Hap.attacktwice = False
Hap.abilities = {Hap.attack3:[0,vec(47,17),True,'An ability which when activated the next turns attack will happen twice'],'increase':[0,vec(47,20),True,'Increase all attacks by 1'],'dodge':[0,vec(47,23),True,'allows haptic to dodge attacks']}
Hap.unlockedabilites = []
Hap.exp = 0
Hap.lvl = 0
Hap.needtolvl = 60
Hap.combat_animation = {1:haptic_combat_img,2:haptic_combat2_img,3:haptic_combat3_img}
Hap.attacks = {Hap.attack1:[5,haptic_ability1_img,vec(18,31),[vec(18,31) + a for a in iconaura],False,[0,0,0]],Hap.attack2:[5,haptic_ability2_img,vec(23,31),[vec(23,31) + a for a in iconaura],False,[0,0,0]],Hap.attack3:[0,haptic_ability3_img,vec(28,31),[vec(28,31)+a for a in iconaura],True,[0,0,0]]}
Hap.clickaura = []
for x in aura:
    Hap.clickaura.append(vec(x))

class shopkeeper():
    class cleric():
        def action(self):
            if self.healparty.collidepoint(int(mpos.x*TILESIZE),int(mpos.y*TILESIZE)) and main.amountmoney >= 40:
                for x in M.allies:
                    M.allies[x][1] += 40
                    if M.allies[x][1] >= x.health:
                        M.allies[x][1] = x.health
                main.amountmoney -= 40
            if self.healone.collidepoint(int(mpos.x*TILESIZE),int(mpos.y*TILESIZE)) and main.amountmoney >= 15:
                self.heal = True
            elif self.heal == True and M.selectedchar != 0:
                M.allies[M.selectedchar][1] += 40
                if M.allies[M.selectedchar][1] >= M.selectedchar.health:
                    M.allies[M.selectedchar][1] = M.selectedchar.health
                self.heal = False
                main.amountmoney -= 15
            if self.resone.collidepoint(int(mpos.x*TILESIZE),int(mpos.y*TILESIZE)) and main.amountmoney >= 100:
                if M.ally1 not in M.allies:
                    pos = M.ally1.vec
                    eat = M.ally1.health
                    lean = M.ally1.shield
                    M.allies.update({M.ally1:[pos,eat,M.ally1.clickaura,lean,[0,0,0]]})
                    main.amountmoney -= 100
                if M.ally2 not in M.allies:
                    pos = M.ally2.vec
                    eat = M.ally2.health
                    lean = M.ally2.shield
                    M.allies.update({M.ally2:[pos,eat,M.ally2.clickaura,lean,[0,0,0]]})
                    main.amountmoney -= 100
                if M.ally3 not in M.allies:
                    pos = M.ally3.vec
                    eat = M.ally3.health
                    lean = M.ally3.shield
                    M.allies.update({M.ally3:[pos,eat,M.ally3.clickaura,lean,[0,0,0]]})
                    main.amountmoney -= 100
                
                M.numberofallies()
        def draw_actions(self):
            pos = M.clericvec
            x = int(pos.x*TILESIZE-250)
            y = int(pos.y*TILESIZE-70)
            rect = pg.Rect(x, y, 135, 45)
            self.healparty = pg.draw.rect(screen,BLACK,rect)
            draw_text('heal party',20,WHITE,x+5, y)
            x2 = int(pos.x*TILESIZE-300)
            y2 = int(pos.y*TILESIZE-70)
            rect = pg.Rect(x2, y2, 40, 45)
            pg.draw.rect(screen,BLACK,rect)
            draw_text('40',20,WHITE,x2+5, y2)
            
            y = int(pos.y*TILESIZE-20)
            rect = pg.Rect(x, y, 135, 45)
            self.healone = pg.draw.rect(screen,BLACK,rect)
            draw_text('heal individual',20,WHITE,x+5, y)
            y2 = int(pos.y*TILESIZE-20)
            rect = pg.Rect(x2, y2, 40, 45)
            pg.draw.rect(screen,BLACK,rect)
            draw_text('15',20,WHITE,x2+5, y2)

            y = int(pos.y*TILESIZE+30)
            rect = pg.Rect(x, y, 135, 45)
            self.resone = pg.draw.rect(screen,BLACK,rect)
            draw_text('res individual',20,WHITE,x+5, y)
            y2 = int(pos.y*TILESIZE+30)
            rect = pg.Rect(x2, y2, 40, 45)
            pg.draw.rect(screen,BLACK,rect)
            draw_text('100',20,WHITE,x2+5, y2)


skcleric = shopkeeper.cleric()
skcleric.heal = False

class main():
    def __init__(self):
        current_state = 0
    def draw_level(self):
        text = 'current level '+str(int(L.crossvec.x - 3))
        draw_text(text, 30, BLACK, 50, 10)
    def draw_money(self):
        text = 'coin '+str(self.amountmoney)
        draw_text(text, 30, BLACK, 50, 40)
    def states(self):
        if self.current_state == 'battle':
            pass
    def battletop(self):
        if self.current_state == 'battle':
            if mpos in M.getaura() and M.selectedchar != 0:
                if M.attackselect == True and M.enemycanattack == False :
                    if M.selectedchar.attacks[M.selectedattack][4] != False:
                        try:    
                            if mpos in M.allies[M.ally1][2]:
                                M.selectedchar.support(M.ally1)
                                self.attck_timer = pg.time.get_ticks()
                                M.actions.append(M.selectedchar)
                                M.attackselect = False
                                M.checkifdead()
                        except:
                            pass
                        try:
                            if mpos in M.allies[M.ally2][2]:
                                M.selectedchar.support(M.ally2)
                                M.actions.append(M.selectedchar)
                                M.attackselect = False
                                M.checkifdead()
                        except:
                            pass
                        try:
                            if mpos in M.allies[M.ally3][2]:
                                M.selectedchar.support(M.ally3)
                                M.actions.append(M.selectedchar)
                                M.attackselect = False
                                M.checkifdead()
                        except:
                            pass
                        M.attackselect = False
                    else:
                        try:
                            der,xxer = M.selectenemy()
                        
                            M.selectedchar.attack((der,xxer),M.selectedattack)
                            M.attackselect = False
                            M.actions.append(M.selectedchar)
                            M.checkifdead()
                        except:
                            M.attackselect = False         
                else:
                    pass 
            elif mpos not in M.getaura() and mpos not in M.selectingattack():
                M.selectedchar = 0
                M.attackselect = False
            if mpos in M.selectingattack():
                M.selectattack()
            if mpos in M.selectingchar() and M.attackselect == False:
                M.selectchar()
    def battlebottom(self):
        if current_time - self.anim_timer > 1000:
            M.current_animation += 1
            if M.current_animation == 4:
                M.current_animation = 1
            self.anim_timer = pg.time.get_ticks()
        if self.current_state == 'battle':
            

            if len(M.actions) >= len(M.allies) and M.enemycanattack == False:
                self.attck_timer = pg.time.get_ticks()
                M.enemycanattack = True
            M.draw_background()
            M.draw_allychar()
            M.draw_enemychar()
            M.draw_icons()
            M.draw_effects()
            if current_time - self.attck_timer > 1000 and M.enemycanattack == True:
                M.actions = []
                M.enemyattack()
                self.display_time = pg.time.get_ticks()   
                M.enemycanattack = False
                M.attackselect = False
            if M.click == True:
                M.draw_damage()
                if current_time - self.display_time > 1000:
                    
                    M.enemycanattack = False
                    M.display == False
                    M.checkifdead()
                    M.damage = {}
                    M.click = False
    def leveltop(self):
        if self.current_state == 'map':
            L.nextlevel()
            L.clickmenu()
    def levelbottom(self):
        if self.current_state == 'map':
            L.draw_currentposition()
            L.draw_linestoconnections()
            L.draw_icons()
    def shoptop(self):
        if self.current_state == 'shop':
            M.selectchar()
            M.selectingshopaction()
            M.selectingshop()      
    def shopbottom(self):
        if self.current_state == 'shop':
            M.draw_shopkeeps()   
            M.draw_shopinventory()
            M.draw_allychar()
    def switchtop(self):
        if self.current_state == 'switch':
            M.selectchar()
            M.switch()
    def switchbottom(self):
        if self.current_state == 'switch':
            M.draw_allychar()
            M.draw_switchbuttons()

main = main()

main.current_state = 'shop'
main.amountmoney = 50

def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))
def draw_biggrid():
    for x in range(0, WIDTH, TILESIZE*2):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE*2 ):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))
        
class level():
    def __init__(self):
        self.level = 0
        self.crossvec = 0
    def clickmenu(self):
        if self.switchbutton.collidepoint(pos):
            main.current_state = 'switch'
    def draw_icons(self):
        pos = vec(20,30)
        x = int(pos.x*TILESIZE-230)
        y = int(pos.y*TILESIZE-35)
        rect = pg.Rect(x, y, 135, 30)
        self.switchbutton = pg.draw.rect(screen,BLACK,rect)
        draw_text('Party',20,WHITE,x+5, y)
    def draw_currentposition(self):
        vec = self.crossvec
        goal_center = (int(vec.x * TILESIZE*2 + TILESIZE*2 / 2), int(vec.y * TILESIZE*2 + TILESIZE*2 / 2))
        screen.blit(cross, cross.get_rect(center=goal_center))
        for x in self.levelindex:
            if self.levelid[x][1] == 'shop':
                pg.draw.circle(screen,BLUE,(int(self.levelindex[x].x*TILESIZE*2+TILESIZE*2/2),int(self.levelindex[x].y*TILESIZE*2+TILESIZE*2/2)),5)
            else:
                pg.draw.circle(screen,BLACK,(int(self.levelindex[x].x*TILESIZE*2+TILESIZE*2/2),int(self.levelindex[x].y*TILESIZE*2+TILESIZE*2/2)),5)
    def draw_linestoconnections(self):
        for x in self.connections:
            pg.draw.line(screen, BLUE, (int(self.crossvec.x*TILESIZE*2+TILESIZE*2/2),int(self.crossvec.y*TILESIZE*2+TILESIZE*2/2)), (int(x.x*TILESIZE*2+TILESIZE*2/2),int(x.y*TILESIZE*2+TILESIZE*2/2)))
    def create_map(self):
        self.levelid = {}
        line = 0
        for x in self.levels:
            tier = random.choices(['battle','shop'],[10,1])
            tier = tier[0]
            if tier == 'battle':
                if x.x == 4:
                        tier = 'battle'
                        cost = 2
                        enemies = []
                        while cost >= 1:
                            if len(enemies) == 5:
                                break
                            enemy = random.choices([sword,mage],[2,1])
                            remove = self.get_cost(enemy)
                            cost -= remove

                            enemies.append(enemy[0])
                        self.make(line,enemies,tier,x)
                if x.x == 5:
                    cost = 3
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage],[2,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 6:
                    cost = 4
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage],[1,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 7:
                    cost = 5
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage],[1,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 8:
                    cost = 5
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage],[1,2])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 9:
                    cost = 5
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage],[1,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 10:
                    cost = 5
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,lizard],[1,1,5])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 11:
                    cost = 6
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,lizard],[1,2,2])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 12:
                    cost = 7
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,lizard],[1,2,2])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 13:
                    cost = 8
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,lizard],[1,1,2])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 14:
                    cost = 8
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,lizard],[1,1,2])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 15:
                    cost = 9
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,lizard],[1,1,3])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 16:
                    cost = 10
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,lizard],[1,1,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 17:
                    cost = 11
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,C,lizard],[1,1,2,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 18:
                    cost = 11
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,C,lizard],[1,1,3,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 19:
                    cost = 12
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,C,lizard],[4,1,1,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 20:
                    cost = 12
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,C,lizard],[3,2,1,2])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 21:
                    cost = 13
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,C,lizard],[1,1,1,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 22:
                    cost = 13
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage],[1,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 23:
                    cost = 14
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,C,lizard],[1,1,1,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 24:
                    cost = 14
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,C,lizard],[1,1,1,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 25:
                    cost = 14
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,C,lizard],[1,2,2,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 26:
                    cost = 15
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([sword,mage,C,lizard],[1,5,3,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
                if x.x == 27:
                    cost = 15
                    enemies = []
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices([mage,C],[1,1])
                        remove = self.get_cost(enemy)
                        cost -= remove

                        enemies.append(enemy[0])
                    self.make(line,enemies,tier,x)
            else:
                self.make(line,[],tier,x)
            if x.x == 28:
                self.levelid.update({line:[[cbm],'battle']})
                self.levelindex.update({line:x})
            line += 1         
    def get_connections(self):
        self.connections = []
        possible = [vec(1,0),vec(1,-1),vec(1,1)]
        for x in possible:
            newcheck = self.crossvec + x
            if newcheck in self.levels:
                self.connections.append(newcheck)
    def get_cost(self,target):
        cost = 0
        
        if mage in target:
            cost = 5
        if sword in target:
            cost = 4
        if C in target:
            cost = 7
        if lizard in target:
            cost = 3
        return cost
    def make(self,line,enemies,tier,x):
        self.levelid.update({line:[enemies,tier]})
        self.levelindex.update({line:x}) 
    def nextlevel(self):
        if mpos2 in self.connections:
            if self.click == True:
                self.crossvec = mpos2
                self.level = mpos2.x - 3
                e,tier = self.getlevel()
                if self.level == 1:
                    M.restart()
                if 'battle' == tier:
                    M.start()
                else:
                    M.shopstart()
                L.get_connections()
                main.current_state = tier
                self.click = False
    def getlevel(self):
        for x in self.levelindex:
            if self.levelindex[x] == mpos2:
                e = self.levelid[x][0]
                tier = self.levelid[x][1]
        return e,tier


cross = pg.image.load(os.path.join(filename,'cross-1.png.png'))
cross = pg.transform.scale(cross, (TILESIZE*2, TILESIZE*2))

L = level()
L.level = 0
L.crossvec = vec(3,8)
L.connections =[]
L.levels = []
L.click = False
L.levelindex = {}
levels = [(4, 7), (4, 8), (4, 9), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (10, 14), (10, 13), (10, 12), (10, 11), (10, 10), (10, 9), (10, 8), (10, 7), (10, 6), (10, 5), (10, 4), (10, 3), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2), (21, 2), (22, 2), (27, 8), (27, 7), (27, 9), (26, 9), (26, 8), (26, 7), (26, 6), (26, 10), (25, 10), (25, 11), (25, 9), (25, 8), (25, 7), (25, 6), (25, 5), (24, 5), (24, 4), (23, 3), (23, 4), (11, 14), (12, 14), (13, 14), (14, 14), (15, 14), (24, 12), (24, 11), (23, 12), (23, 13), (22, 13), (22, 14), (21, 14), (20, 14), (18, 14), (19, 14), (17, 14), (16, 14), (16, 13), (15, 13), (13, 13), (14, 13), (12, 13), (11, 13), (11, 12), (12, 12), (13, 12), (14, 12), (15, 12), (16, 12), (17, 12), (17, 13), (18, 13), (18, 12), (19, 12), (19, 13), (20, 13), (20, 12), (21, 12), (21, 13), (22, 12), (22, 11), (23, 11), (23, 10), (24, 10), (24, 9), (23, 9), (24, 8), (23, 8), (24, 7), (23, 7), (24, 6), (23, 6), (23, 5), (22, 5), (22, 4), (22, 3), (21, 3), (21, 4), (20, 4), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (11, 4), (12, 4), (13, 4), (14, 4), (15, 4), (16, 4), (17, 4), (19, 4), (18, 4), (18, 5), (17, 5), (16, 5), (15, 5), (14, 5), (13, 5), (12, 5), (11, 5), (11, 6), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6), (19, 5), (20, 5), (20, 6), (21, 6), (21, 5), (22, 6), (22, 7), (22, 8), (22, 9), 
(22, 10), (21, 10), (21, 11), (21, 9), (21, 8), (21, 7), (20, 7), (20, 8), (20, 9), (20, 10), (20, 11), (19, 11), (19, 10), (19, 9), (19, 8), (19, 7), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11), (17, 11), (17, 10), (17, 
9), (17, 8), (17, 7), (16, 7), (16, 8), (16, 9), (16, 10), (16, 11), (15, 11), (15, 10), (15, 9), (15, 8), (15, 7), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (13, 11), (12, 11), (11, 11), (11, 10), (12, 10), (13, 10), 
(13, 9), (12, 9), (11, 9), (11, 8), (12, 8), (13, 8), (13, 7), (12, 7), (11, 7),[28, 8]]
for x in levels:
    if x not in L.levels:
        L.levels.append(vec(x))




class battle():
    def __init__(self):
        self.current_animation = 0
        self.allies = 0
        self.enemy = 0
        self.display = 0
        self.damage = 0
    def draw_switchbuttons(self):
        pos = vec(20,30)
        x = int(pos.x*TILESIZE-230)
        y = int(pos.y*TILESIZE-35)
        rect = pg.Rect(x, y, 135, 30)
        self.swapbutton = pg.draw.rect(screen,BLACK,rect)
        text = 'done'
        if self.swap == False:
            text = 'change order'
        draw_text(text,20,WHITE,x+5, y)

        if self.selectedchar != 0:
            self.selectedchar.draw_skilltree()
            if self.hov != False:
                draw_text(self.selectedchar.abilities[self.hov][3],20,BLACK,(self.selectedchar.abilities[self.hov][1].x-5)*TILESIZE,self.selectedchar.abilities[self.hov][1].y*TILESIZE)
    def switchhover(self):
        if self.selectedchar != 0:
            for k in self.selectedchar.abilities:
                if self.selectedchar.abilities[k][0].collidepoint(int(mpos.x*TILESIZE),int(mpos.y*TILESIZE)):
                    self.hov = k
                    self.hovertime = pg.time.get_ticks()
                elif current_time - self.hovertime > 1000:
                    self.hov = False
    def switch(self):
        if self.selectedchar != 0:
            for k in self.selectedchar.abilities:
                if self.selectedchar.abilities[k][0].collidepoint(int(mpos.x*TILESIZE),int(mpos.y*TILESIZE)) and self.selectedchar.abilities[k][2] and self.selectedchar.lvl > 0:
                    self.selectedchar.skill(k)
                    self.selectedchar.lvl -= 1
                else:
                    self.hov = False

        if self.swapbutton.collidepoint(int(mpos.x*TILESIZE),int(mpos.y*TILESIZE)):
            if self.swap == False:
                self.swap = True
            elif self.swap == True:
                self.swap = False
        if self.swap == True:
            if self.selected1 == 0:
                self.selected1 = self.selectedchar
            elif self.selected2 == 0:
                self.selected2 = self.selectedchar
            if self.selected1 != 0 and self.selected2 != 0:
                move = self.selected1
                if move in self.allies:
                    new = self.selected2
                    newl = {}
                    save = {}
                    for x in self.allies:
                        save.update({x:self.allies[x]})
                    for x in self.allies:
                        newl.update({x:x})
                    newl[move] = new
                    newl[new] = move
                    self.allies = {value:key for key, value in newl.items()}
                    for x in save:
                        self.allies[x] = save[x]
                self.selected1 = 0
                self.selected2 = 0
                self.numberofallies()

    def shopstart(self):
        self.selectedshop = 0
    def draw_shopkeeps(self):
        vec = self.clericvec
        img = self.cleric_img
        goal_center = (int(vec.x * TILESIZE + TILESIZE / 2), int(vec.y * TILESIZE + TILESIZE / 2))    
        self.b = screen.blit(img, img.get_rect(center=goal_center))
    def draw_shopinventory(self):
        if self.selectedshop == 'cleric':
            skcleric.draw_actions()
    def selectingshop(self):
        if self.b.collidepoint(int(mpos.x*TILESIZE),int(mpos.y*TILESIZE)):
            self.selectedshop = 'cleric'
    def selectingshopaction(self):
        if self.selectedshop == 'cleric':
            skcleric.action()
    def restart(self):
        ally1 = Hap
        ally2 = H
        ally3 = S
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
        self.allies.update({self.ally1:[pos,eat,self.ally1.clickaura,lean,[0,0,0]]})
        self.ally2 = ally2
        pos = self.ally2.vec
        eat = self.ally2.health
        lean = self.ally2.shield
        self.allies.update({self.ally2:[pos,eat,self.ally2.clickaura,lean,[0,0,0]]})
        self.ally3 = ally3
        pos = self.ally3.vec
        eat = self.ally3.health
        lean = self.ally3.shield
        self.allies.update({self.ally3:[pos,eat,self.ally3.clickaura,lean,[0,0,0]]})
        self.numberofallies()
        #for x in range(1,3):#range(1,random.randint(2,3))
        for x in self.allies:
            x.draw_skilltree()
    def start(self):
        enemy,tier = L.getlevel()
        self.savecost = enemy
        for x in enemy:
            if x in self.enemy:
                tout = x.vec
                eat = x.health
                attack = x.attacks
                self.enemy[x].append([tout,eat,x.clickaura,attack,[0,0,0]])
            else: 
                tout = x.vec
                eat = x.health
                attack = x.attacks
                self.enemy.update({x:[[tout,eat,x.clickaura,attack,[0,0,0]]]})
        self.numberofenemy()

    def draw_allychar(self):
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
                lol = pg.transform.scale(lol, (300, 275))
                lol.fill((0, 0, 0),special_flags=pg.BLEND_RGB_MULT)
                lel = lol.get_rect(center=goal_center)
                lel[1] -=2
                screen.blit(lol, lel)
            screen.blit(cur, cur.get_rect(center=goal_center))
            vec = self.allies[x][0]
            heat = self.allies[x][1]
            rect = pg.Rect(int(vec.x*TILESIZE - 10), int(vec.y*TILESIZE - 120), int(heat), 20)
            pg.draw.rect(screen,RED,rect)
            if self.allies[x][3] > 0:
                text = '+'+str(self.allies[x][3])
                draw_text(text, 20,BLUE , vec.x*TILESIZE + 40, vec.y*TILESIZE - 150)
                rect = pg.Rect(int(vec.x*TILESIZE - 10), int(vec.y*TILESIZE - 120), int(self.allies[x][3]   ), 20)
                pg.draw.rect(screen,BLUE,rect)
            
            text = str(heat)+'/'+str(x.health)
            draw_text(text, 20, BLACK, vec.x*TILESIZE - 10, vec.y*TILESIZE - 150)
    def draw_enemychar(self):
        for x in self.enemy:   
            if len(self.enemy[x]) > 1:
                for y in self.enemy[x]:
                    ani = x.combat_animation
                    vec = y[0]
                    goal_center = (int(vec.x * TILESIZE + TILESIZE / 2), int(vec.y * TILESIZE + TILESIZE / 2))
                    screen.blit(ani[self.current_animation], ani[self.current_animation].get_rect(center=goal_center))
                    vec = y[0]
                    heat = y[1] 
                    text = str(round(heat))+'/'+str(x.health)
                    draw_text(text, 20, BLACK, vec.x*TILESIZE - 10, vec.y*TILESIZE - 150)
                    rect = pg.Rect(int(vec.x*TILESIZE - 10), int(vec.y*TILESIZE - 120), int(heat), 20)
                    pg.draw.rect(screen,RED,rect)
            else:
                ani = x.combat_animation 
                vec = self.enemy[x][0][0]    
                goal_center = (int(vec.x * TILESIZE + TILESIZE / 2), int(vec.y * TILESIZE + TILESIZE / 2))
                screen.blit(ani[self.current_animation], ani[self.current_animation].get_rect(center=goal_center))
                vec = self.enemy[x][0][0]
                heat = self.enemy[x][0][1] 
                text = str(round(heat))+'/'+str(x.health)
                draw_text(text, 20, BLACK, vec.x*TILESIZE - 10, vec.y*TILESIZE - 150)
                rect = pg.Rect(int(vec.x*TILESIZE - 10), int(vec.y*TILESIZE - 120), int(heat), 20)
                pg.draw.rect(screen,RED,rect)

                
    def draw_icons(self):
        if M.selectedchar == self.ally1:
            self.ally1.draw_icons()
        if M.selectedchar == self.ally2:
            self.ally2.draw_icons()
        if M.selectedchar == self.ally3:
            self.ally3.draw_icons()
            
    def draw_damage(self):
        for x in self.damage:
            damage = 0
            for y in self.damage[x]:
                if y == 0:
                    draw_text('miss',30,RED,self.allies[x][0].x*TILESIZE, self.allies[x][0].y*TILESIZE-170,align="bottomright")  
                damage += y
            draw_text(str(damage),30,RED,self.allies[x][0].x*TILESIZE, self.allies[x][0].y*TILESIZE-150,align="bottomright")    
    def draw_background(self):
        goal_center = int(WIDTH / 2), int(HEIGHT/ 2)
        screen.blit(background_fall, background_fall.get_rect(center=goal_center))
    def draw_attack(self):
        self.selectedchar.draw_attack() #pffft over here you already made one
        pass
    def draw_effects(self):
        for x in self.allies:
            if self.allies[x][4][1] > 0:
                draw_text('bleed',10, RED, self.allies[x][0].x*TILESIZE + 25, self.allies[x][0].y*TILESIZE,align="bottomright")
            if self.allies[x][4][2] > 0:
                draw_text('fire',10, YELLOW, self.allies[x][0].x*TILESIZE + 25, self.allies[x][0].y*TILESIZE,align="bottomright")
    def checkifdead(self):
        test = dict(self.enemy)
        for x in test:
            if self.dup:
                for y in test[x]:
                    if y[1] <= 0:
                        self.enemy[x].remove(y)
                        self.killhistory.append(self.selectedchar)
                if len(test[x]) <= 0:
                    del self.enemy[x]
                    self.killhistory.append(self.selectedchar)
            else:
                if test[x][0][1] <=0 :
                    del self.enemy[x]
                    self.killhistory.append(self.selectedchar)
        test = dict(self.allies)
        for x in test:
            if test[x][1] <= 0:
                del self.allies[x]
                if x == self.selectedchar:
                    self.selectedchar = 0
                for w in self.spaces:
                    for a in self.spaces[w]:
                        if a[1] == x:
                            a[1] = 99
        if len(self.enemy) <= 0:
            #ally1 = H
            #ally2 = S
            main.current_state = 'map'
            self.selectedattack = 0
            self.selectedchar = 0
            self.current_animation = 1
            #self.allies = {}
            self.enemy = {}
            self.l = []
            self.actions = []
            coins = 0
            for x in self.savecost:
                e = L.get_cost([x])
                coins += e
            main.amountmoney += coins
            
            splitcoins = coins/len(self.allies)
            for x in self.killhistory:
                for z in self.allies:
                    if z == x:
                        z.exp += round(splitcoins*2)
                    else:
                        z.exp += round(splitcoins)
                    z.checklevel()
            thing = []
            for x in self.allies:
                thing.append(x)
            if len(self.killhistory) == 0:
                for l in range(len(self.savecost)):
                    x = random.choice(thing)
                    for z in self.allies:
                        if z == x:
                            z.exp += round(splitcoins*2)
                        else:
                            z.exp += round(splitcoins)
                        z.checklevel()
            self.savecost = []
        if len(self.allies) <= 0:
            self.restart()
            L.crossvec = vec(3,8)
            L.create_map()
            L.get_connections()
    def numberofenemy(self):
        spaces = {'space1':[vec(37,20),99],'space2':[vec(43,25),99],'space3':[vec(43,15),99],'space4':[vec(47,18),99],'space5':[vec(47,22),99]}
        taken = []
        self.dup = False
        number = 0
        for y in self.enemy:
            if len(self.enemy[y]) > 1:
                lel = 0
                for a in self.enemy[y]:  
                    for x in spaces:
                        for z in spaces:
                            taken.append(spaces[z][1])
                        
                        if spaces[x][1] == 99:
                            if number not in taken:
                                spaces[x][1] = number
                                self.enemy[y][lel][0] = spaces[x][0]
                                self.enemy[y][lel][2] = [self.enemy[y][lel][0]+ x for x in self.enemy[y][lel][2]]
                        taken = []
                    lel+=1
                    number += 1
                self.dup = True
            else:
                for x in spaces:
                    for z in spaces:
                        taken.append(spaces[z][1])
                    #print('enemy',taken)
                    if spaces[x][1] == 99:
                        if y not in taken:
                            spaces[x][1] = y
                            self.enemy[y][0][0] = spaces[x][0]
                            self.enemy[y][0][2] = [self.enemy[y][0][0]+ x for x in self.enemy[y][0][2]]
                    taken = []              
    def numberofallies(self):
        self.spaces = {'front row':[[vec(20,15), 99],[vec(20,25),99]],'back row':[[vec(13,20),99]]}
        taken = []
        self.dup = False
        for y in self.allies:
            for x in self.spaces:
                for a in self.spaces[x]:
                    for w in self.spaces:
                        for mom in self.spaces[w]:
                            taken.append(mom[1])
                    if a[1] == 99:
                        if y not in taken:
                            a[1] = y
                            self.allies[y][0] = a[0]
                            self.allies[y][2] = [self.allies[y][0]+ x for x in y.clickaura]
                    taken = []   
    def getaura(self):
        y = []
        for x in self.enemy:
            if len(self.enemy[x]) > 1:
                for z in self.enemy[x]:
                    y += z[2]
            else:
                y += self.enemy[x][0][2]
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
            for x in self.allies[z][2]:
                y.append(x)
        return y
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
        try:
            if mpos in self.allies[self.ally1][2]:
                M.selectedchar = self.ally1
                M.charselect = True
        except:
            pass
        try:
            if mpos in self.allies[self.ally2][2]:
                M.selectedchar = self.ally2
                M.charselect = True
        except:
            pass
        try:
            if mpos in self.allies[self.ally3][2]:
                M.selectedchar = self.ally3
                M.charselect = True
        except:
            pass
    def selectenemy(self):
        for x in self.enemy:
            if len(self.enemy[x]) > 1:
                lel = 0
                for z in self.enemy[x]:
                    if mpos in self.enemy[x][lel][2]:
                        cur_enemyspecific = lel
                        cur_enemyclass = x
                    lel += 1
            else:   
                if mpos in self.enemy[x][0][2]:
                    cur_enemyspecific = 0
                    cur_enemyclass = x
        return cur_enemyclass,cur_enemyspecific
    def enemyattack(self):
        self.statuseffects(False)
        for x in self.enemy:
            if x != cbm:
                if self.dup:
                    for z in self.enemy[x]:
                        if z[4][0] > 0:
                            z[4][0] -= 1
                            continue
                        attack = z[3]
                        self.workingattack(attack)
                else:
                    if self.enemy[x][0][4][0] > 0:
                        self.enemy[x][0][4][0] -= 1
                        continue
                    attack = self.enemy[x][0][3]
                    self.workingattack(attack)
            else:
                x.attack()
        self.click = True
        self.display = True
        self.statuseffects(True)
    def workingattack(self,attack):
        attacks = []
        chance = []
        possible = []
        dead = []
        for y in attack:
            chance.append(attack[y][1])
            attacks.append(y)
        for x in self.spaces:
            if x == 'front row':
                for l in self.spaces[x]:
                    if l[1] != 99:
                        possible.append(l[1])
                    else:
                        dead.append(l[1])
            if x == 'back row' and len(dead) == 2:
                for j in self.spaces[x]:
                    possible.append(j[1])
                        
        target = random.choice(possible)
        
        attacking = random.choices(attacks,chance)
        damage = attack[attacking[0]]
        print(attacking,damage[0])
        
        for x in range(0,damage[3]):
            target.damage(damage)

            if damage[2][0] > 0:
                print('stun')
                self.allies[target][4][0] += damage[2][0]
            if damage[2][2] > 0:
                print('fire')
                self.allies[target][4][2] += damage[2][2]
            if target in self.damage:
                self.damage[target].append(int(damage[0]))
            else:
                self.damage.update({target:[damage[0]]})
    def statuseffects(self,when):
        for x in self.allies:
            if when:
                if self.allies[x][4][0] > 0:
                    self.allies[x][4][0] -= 1
                    self.actions.append(x)
                    
            else:
                if self.allies[x][4][1] > 0:
                    self.allies[x][4][1] -= 0.5
                    self.allies[x][1] -= 2
                if self.allies[x][4][2] > 0:
                    self.allies[x][4][2] -= 1
                    self.allies[x][1] -= 5
        if not when:
            for x in self.enemy:
                if self.enemy[x][0][4][1] > 0:
                    self.enemy[x][0][4][1] -= 0.5
                    self.enemy[x][0][1] -= 2
                if self.enemy[x][0][4][2] > 0:
                    self.enemy[x][0][4][2] -= 1
                    self.enemy[x][0][1] -= 5
''' = progress + done ' ' in the works - later
Gameplay
multiple enemies that attack +
player character with multiple attacks that are selectable +
multiple characters whic requires an entire rework of how i implement characters +
heplane class +
cri class +
difficulty tweeks to make game harder === (everyone) or easeir (ava)
status effects to both enemies and allies +
programming bleed +
levels (rouge like) 
specific levels (a traditional rpg) that will require a class system +
boss enemies (trent)
more enemies (trent or daniel)
enemy with damage reduction
cri passive deals with increase in values the more you use them +
healing removes status effects except stun (cri) +
haptic class +
new enemy sowrd guy(medium) +
new enemy sword guy(actually easy) -
rework enemy selection so that its a list for multiple dupes +
and fixed resulting problems +
map system with levels +
maps have shops or camps
game over screen
placment order editable in a menu during map -
add more space for enemies +
changing enemy attack to one ata time and show damage=
apply current cahnges to boss class
shop mehanic 


Art
drawing heplane +
drawing conrift +
animate both +
drawing magee -
icons for heplane +
drawing cri +
animate cri +
icons for cri +
back ground (daniel) +
attack animations -
status effect through visual
drawing sword guy plus
map elements

In Class
highlight selected charcter more clear (jackson) ?
text health +
text enemy health +
draw health bars +
text damage from enemies +
text predicted damage +
text heal and shield +
text status effect damage -
delay when entering and exiting a fight


TRY
cool downs all
cool downs coilent

bonnied
evolution of a halood
affects bones
'''
M = battle()

M.restart()


M.clericvec = vec(37,20)
M.cleric_img = pg.image.load(os.path.join(filename,'cleric-1.png.png')).convert_alpha()
M.cleric_img = pg.transform.scale(M.cleric_img, (256, 256))
M.savecost = []
M.shopstart()

M.targetedenemy = 0
background_fall = pg.image.load(os.path.join(filename,'backgorunds-2.png.png'))
background_fall = pg.transform.scale(background_fall, (1920, 1080))


M.selected1 = 0
M.selected2 = 0
M.swap = False

M.hov = False
M.hovertime = 9999


M.killhistory = []

M.display = False
M.damage = {}
M.click = False
M.attackselect = False
#M.clickaura = [vec(-1,-1)]

main.attck_timer = 1000000
main.anim_timer = pg.time.get_ticks()
M.enemycanattack = False

L.create_map()

mpos = vec(0,0)
create = []

L.get_connections()
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if main.current_state == 'switch':
            mpos = vec(pg.mouse.get_pos()) // TILESIZE
            M.switchhover()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if main.current_state == 'battle' or main.current_state == 'shop' or main.current_state == 'switch':
                    mpos = vec(pg.mouse.get_pos()) // TILESIZE
                    create.append(mpos)
                if main.current_state == 'map':
                    mpos2 = vec(pg.mouse.get_pos()) // (TILESIZE*2)
                    pos = pg.mouse.get_pos()
                    L.click = True

                #L.crossvec =  mpos2
                main.switchtop()
                main.battletop()
                #L.levels.append(vec(mpos2))
                main.leveltop()
                main.shoptop()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                M.enemy = {}
                M.checkifdead()
                M.hov = False
            if event.key == pg.K_e:
                M.actions = [1,1,1]
            if event.key == pg.K_q:
                main.current_state = 'shop'


            if event.key == pg.K_a:
                print([(int(loc.x -  M.clericvec.x), int(loc.y - M.clericvec.y)) for loc in create])
            if event.key == pg.K_m:
                print([(int(loc.x),int(loc.y))for loc in L.levels])
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit
            
                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    current_time = pg.time.get_ticks()
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    # anything down here will be displayed ontop of anything above
    #draw_grid()
    
    draw_biggrid()
    main.switchbottom()
    main.levelbottom()
    main.battlebottom()
    main.shopbottom()
    main.draw_level()
    main.draw_money()
    pg.display.flip() # dose the changes goto doccumentation for other ways