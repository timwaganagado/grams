
import pygame as pg
from os import path
from collections import deque
import random
import copy
import shelve
import os , sys
import math
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
PURPLE = (149, 53, 83)
VIOLET = (127,0,255)
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

filename = os.path.dirname(sys.argv[0])
filename += '\Halood_images'

fire = 'fire'
bleed = 'bleed'
stun = 'stun'
weakness = 'weakness'
dodge = 'dodge'

class testenemy():
    class stun():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self)
            enemy.defaultattack(self,damage)
        def damage(self,dup,damage):
            M.enemy[self][dup][1] -= damage
    class bleed():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self)
            enemy.defaultattack(self,damage)
        def damage(self,dup,damage):
            M.enemy[self][dup][1] -= damage

home_img = pg.image.load(os.path.join(filename,cross)).convert_alpha()
home_img = pg.transform.scale(home_img, (256, 256))

testenemy = testenemy()

stunte = testenemy.stun()
stunte.vec = vec(43,20)
stunte.health = 25
stunte.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
stunte.clickaura = []
for aura in auras:
    stunte.clickaura.append(vec(aura))
stunte.attacks = {'constrict':[0,[{stun:1}],False,1,1]}

bleedte = testenemy.bleed()
bleedte.vec = vec(43,20)
bleedte.health = 25
bleedte.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
bleedte.clickaura = []
for aura in auras:
    bleedte.clickaura.append(vec(aura))
bleedte.attacks = {'constrict':[0,[{bleed:1}],False,1,1]}

class enemy():
    def decision(target):
        attack = M.enemy[target][0][3]
        chance = []
        attacks = []
        for y in attack:
            chance.append(attack[y][4])
            attacks.append(y)

        attacking = random.choices(attacks,chance)
        damage = attack[attacking[0]]
        return damage
    def defaultattack(target,damage):
        possible = []
        dead = []
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
        for x in range(0,damage[3]):
            target.damage(damage)
            for x in damage[1]:
                if x == 0:
                    break
                if fire in x:
                    if fire in M.allies[target][4]:
                        M.allies[target][4][fire] += x[fire]
                    else:
                        M.allies[target][4].update({fire:x[fire]})
                if bleed in x:
                    if bleed in M.allies[target][4]:
                        M.allies[target][4][bleed] += x[bleed]
                    else:
                        M.allies[target][4].update({bleed:x[bleed]})
                if stun in x:
                    if stun in M.allies[target][4]:
                        M.allies[target][4][stun] += x[stun]
                    else:
                        M.allies[target][4].update({stun:x[stun]})
            if target in M.damage:
                M.damage[target].append(int(damage[0]))
            else:
                M.damage.update({target:[damage[0]]})
        pass
    class conrift():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self)
            enemy.defaultattack(self,damage)
        def damage(self,dup,damage):
            M.enemy[self][dup][1] -= damage
    class magee():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            if M.enemy[self][ll][1] < 15:
                damage = enemy.decision(self)
            else:
                damage = self.attacks['heal']
            if damage[2]:
                self.support(damage)
            else:
                enemy.defaultattack(self,damage)
        def support(self,damage):
            lowest = 10000000
            if damage[3] == 0:
                print('eeeee')
                for x in M.enemy:
                    if len(M.enemy[x]) > 1:
                        lel = 0
                        for ww in M.enemy[x]:
                            if M.enemy[x][lel][1] < lowest:
                                healb = x
                                heals = lel
                                lowest = M.enemy[x][lel][1]
                            lel += 1
                    else:
                        if M.enemy[x][0][1] < lowest:
                            healb = x
                            heals = 0
                            lowest = M.enemy[x][0][1]
                M.enemy[healb][heals][1] += damage[0]
                if M.enemy[healb][heals][1] > healb.health:
                    M.enemy[healb][heals][1] = healb.health
        def damage(self,dup,damage):
            M.enemy[self][dup][1] -= damage
    class swordguy():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self)
            enemy.defaultattack(self,damage)
        def damage(self,dup,damage):
            M.enemy[self][dup][1] -= damage
    class lizard():
        def __init__(self):
            self.vec = 0 
        def thunk(self,ll):
            damage = enemy.decision(self)
            enemy.defaultattack(self,damage)
        def damage(self,dup,damage):
            M.enemy[self][dup][1] -= damage
    class boulderine():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self)
            if damage[2]:
                self.support(damage,ll)
            else:
                enemy.defaultattack(self,damage)
        def support(self,damage,ll):
            M.enemy[self][ll][4].update({dodge:1})
        def damage(self,dup,damage):
            if dodge in M.enemy[self][dup][4]: 
                M.selectedchar.damage([10])
            else:
                M.enemy[self][dup][1] -= damage
            





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
C.attacks = {'darkness':[5,[0],False,1,5],'conduction':[20,[{fire:1,stun:1}],False,1,1]}

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
mage.attacks = {'fire ball':[10,[{fire:1}],False,1,4],'lightning':[15,[{stun:1}],False,1,1],'ice shards':[5,[{bleed:1}],False,1,4],'heal':[15,[0],True,0,2],'miss':[0,[0],False,1,2]}

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
sword.attacks = {'slash':[4,[{bleed:1}],False,2,4],'miss':[0,[0],False,1,2]}

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
lizard.attacks = {'pierce':[2,[{bleed:1}],False,3,5],'constrict':[5,[{stun:2}],False,1,1],'miss':[0,[0],False,1,2]}

boulderine = enemy.boulderine()
boulderine.vec = vec(43,20)
boulderine.health = 25
boulderine.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
boulderine.clickaura = []
for aura in auras:
    boulderine.clickaura.append(vec(aura))
boulderine.attacks = {'weak smoke':[5,[{weakness:1}],False,1,2],'reposte':[0,[{0}],True,0,2],'miss':[0,[0],False,1,1]}

'''
0 is dmg
1 is effects
2 is support
3 is amount of hits
'''

''' 
4 is hit chance 
'''
#
'''
4 is sprite
5 is click aura
'''


kcross = pg.image.load(os.path.join(filename,cross)).convert_alpha()
kcross = pg.transform.scale(kcross, (128, 128))

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
                for x in range(0,damage[3]):
                    target.damage(self.attacks[attacking[0]])
                    for x in damage[2]:
                        if x == 0:
                            break
                        if fire in x:
                            M.allies[target][4][2] += x[fire]
                        if bleed in x:
                            M.allies[target][4][1] += x[bleed]
                        if stun in x:
                            M.allies[target][4][0] += x[stun]
                    if target in M.damage:
                        M.damage[target].append(int(damage[0]))
                    else:
                        M.damage.update({target:[damage[0]]})
            self.turncounter += 1
        def support(self,target):
            if target[0] == 0:
                M.enemy[cbm][0][1] += M.enemy[cbm][0][1]*4/10
    class selloquie():
        def __init__(self):
            self.vec = 0
        def attack(self):
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
                ##print(attacking,damage[0])
                for x in range(0,damage[3]):
                    
                    if M.allies[target][3] > 0:
                        M.allies[target][3] -= damage[0]
                        if M.allies[target][3] < 0:
                            M.allies[target][3] = 0
                    else:
                        M.allies[target][1] -= damage[0]
                        if damage[2][1] > 0:
                            #print('bleed')
                            M.allies[target][4][1] += damage[2][1]
                    if damage[2][0] > 0:
                        #print('stun')
                        M.allies[target][4][0] += damage[2][0]
                    if damage[2][2] > 0:
                        #print('fire')
                        M.allies[target][4][2] += damage[2][2]
                    if target in M.damage:
                        M.damage[target].append(int(damage[0]))
                    else:
                        M.damage.update({target:[damage[0]]})
            self.turncounter += 1
        def support(self,target):
            if target[0] == 0:
                M.enemy[cbm][0][1] += M.enemy[cbm][0][1]*4/10
            #print('heal')
            
cbm = boss.courptbattlemage()
cbm.vec = vec(43,20)
cbm.health = 100
cbm.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, -1), (1, -1), (2, -1), (2, -2), (1, -2), (0, -2), (0, -3), (1, -3), (2, -3)]
cbm.clickaura = []
cbm.turncounter = 0
for aura in auras:
    cbm.clickaura.append(vec(aura))
cbm.attacks = {'slash':[5,4,[0],2,False],'blast':[15,2,[{fire:1}],1,False],'charging fire':[1,2,[{fire:3}],1,True],'blinding light':[1,1,[{stun:1}],1,True],'miss':[0,2,[0],1,True]}




class ally():
    def __init__(self):
        l = 0
    def create_clickaura(self):
        pass
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
    def applyeffects(self,target,dup,attack,ally):
        for x in ally.attacks[attack][1]:
                if x == 0:
                        break
                if fire in x:
                    if fire in M.enemy[target][dup][4]:
                        M.enemy[target][dup][4][fire] += x[fire]
                    else:
                        M.enemy[target][dup][4].update({fire:x[fire]})
                if bleed in x:
                    if bleed in M.enemy[target][dup][4]:
                        M.enemy[target][dup][4][bleed] += x[bleed]
                    else:
                        M.enemy[target][dup][4].update({bleed:x[bleed]})
                if stun in x:
                    if stun in M.enemy[target][dup][4]:
                        M.enemy[target][dup][4][stun] += x[stun]
                    else:
                        M.enemy[target][dup][4].update({stun:x[stun]})
    def damage(self,target,taken):
        if M.allies[target][3] > 0:
                M.allies[target][3] -= taken[0]
                if M.allies[target][3] < 0:
                    M.allies[target][3] = 0
        else:
                M.allies[target][1] -= taken[0]
    def fixclick(self,target):
        pos = vec(18,31)
        for attack in target.attacks:
            pass
            if attack in target.abilities:
                if attack in target.unlockedabilites:
                    target.attacks[attack][5] = [pos + a for a in iconaura]
                    pos += vec(5,0)
            else:
                target.attacks[attack][5] = [pos + a for a in iconaura]
                pos += vec(5,0)
    class heplane():
        def __init__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            blooddamage = int(M.allies[H][1])/int(self.health)+1+self.inc
            M.allies[self][1] -= self.attacks[attack][0][1]
            self.healdam.append(int((blooddamage * self.attacks[attack][0][0])/2))
            damage = blooddamage * self.attacks[attack][0][0]
            target.damage(dup,damage)
            ally.applyeffects(target,dup,attack,self)
        def support(self,target):
            if M.selectedattack == self.attack3:
                if self.attack3 in self.unlockedabilites:
                    for x in self.healdam:
                        M.allies[M.selectedchar][1] += x
                    self.healdam = []
                    if M.allies[M.selectedchar][1] > 50:
                        M.allies[M.selectedchar][1] = 50
                else:
                    M.actions.remove(H)
            if M.selectedattack == self.attack4:
                if self.attack4 in self.unlockedabilites:
                    M.allies[M.selectedchar][3] += self.attacks[self.attack4][0][0]
                    M.allies[M.selectedchar][1] -= 10
                    if M.allies[M.selectedchar][3] > 50:
                        M.allies[M.selectedchar][3] = 50
                else:
                    M.actions.remove(H)
        def damage(self,taken):
            ally.damage(self,taken)
        def draw_icons(self):

            text = str(round(int((M.allies[H][1]/self.health+1) * self.attacks[self.attack1][0][0])))

            text = str(round(int((M.allies[H][1]/self.health+1) * self.attacks[self.attack2][0][0])))
            
            
            pos = vec(18,31)
            for attack in self.attacks:
                
                if self.attack3 not in self.unlockedabilites:
                    if attack == self.attack3:
                        continue
                if self.attack4 not in self.unlockedabilites:
                    if attack == self.attack4:
                        continue
                icon = self.attacks[attack][4]
                rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                if attack == self.attack1 or attack == self.attack2:
                    text = str(round(int((M.allies[H][1]/self.health+1) * self.attacks[attack][0][0])))
                    draw_text(text, 20, RED, pos.x*TILESIZE, pos.y*TILESIZE + 75)
                if attack == self.attack3:
                    text = 0
                    for a in self.healdam:
                        text += a 
                    text = str(text)
                    draw_text(text, 20, GREEN, pos.x*TILESIZE, pos.y*TILESIZE + 75)
                if attack == self.attack4:
                    text = str(self.attacks[attack][0][0])
                    draw_text(text, 20, BLUE, pos.x*TILESIZE, pos.y*TILESIZE + 75)
                pos += vec(5,0)

                
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
            if cur == self.attack3:
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            if cur == 'increase':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.inc = 0.1
            if cur == self.attack4:
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            ally.fixclick(self)
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
            self.passive(attack)
            ally.applyeffects(target,dup,attack,self)
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
                if stun in M.allies[target][4]:
                    M.allies[target][4] = {stun:M.allies[target][4][stun]}
                else:
                    M.allies[target][4] = {}
            self.passive(attack)
        def passive(self,used):
            for x in self.attacks:
                if x == used:
                    self.attacks[x][0] += (1 + self.inc)
                else:
                    self.attacks[x][0] += (2 + self.inc)
                if x == self.attack1:
                    if self.attacks[x][0] >= self.stuncap:
                        self.attacks[x][1][0][stun] = 1
                    if self.attacks[x][0] < self.stuncap:
                        self.attacks[x][1][0][stun] = 0
                if self.attacks[x][0] > 10:
                    self.attacks[x][0] = 2
        def damage(self,taken):
            ally.damage(self,taken)
        def draw_icons(self):
            cur = cri_stunicon_img
            goal_center = (int(M.allies[self][0].x * TILESIZE + TILESIZE / 2 + 80), int(M.allies[self][0].y * TILESIZE + TILESIZE / 2 - 50))
            if self.attacks[self.attack1][0] < self.stuncap:
                cur = cur.copy( )
                cur.fill((105, 105, 105, 255),special_flags=pg.BLEND_RGB_MULT)            
            screen.blit(cur, cur.get_rect(center=goal_center))

            pos = vec(18,31)
            for attack in self.attacks:
                icon = self.attacks[attack][4]
                rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                text = str(self.attacks[attack][0])
                if attack == self.attack1:
                    draw_text(text, 20, RED, pos.x*TILESIZE, pos.y*TILESIZE + 75)
                if attack == self.attack2:
                    draw_text(text, 20, BLUE, pos.x*TILESIZE, pos.y*TILESIZE + 75)
                if attack == self.attack3:
                    draw_text(text, 20, GREEN, pos.x*TILESIZE, pos.y*TILESIZE + 75)
                pos += vec(5,0)
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
                self.attacks[self.attack1][1][0][bleed] = 2
            else:
                self.attacks[self.attack1][1][0][bleed] = 0
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
            ally.applyeffects(target,dup,attack,self)
            
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
            if chance[0] == 1:
                ally.damage(self,taken)
        def draw_icons(self):
            rect = pg.Rect(int(M.allies[self][0].x*TILESIZE+80), int(M.allies[self][0].y*TILESIZE-50), 20, 135)
            pg.draw.rect(screen,MOMENTUMCOLOR,rect)
            for y in range(0,self.momentum):
                rect = pg.Rect(int(M.allies[self][0].x*TILESIZE+80), int(M.allies[self][0].y*TILESIZE+50-50*y), 20, 45)
                pg.draw.rect(screen,WHITE,rect)

            pos = vec(18,31)
            for attack in self.attacks:
                if self.attack3 not in self.unlockedabilites:
                    if attack == self.attack3:
                        continue
                icon = self.attacks[attack][4]
                rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                if attack != self.attack3:
                    text = str(self.attacks[attack][0])
                    if attack == self.attack1:
                        text = str((self.attacks[attack][0]+self.inc)*self.momentum)
                    draw_text(text, 20, RED, pos.x*TILESIZE, pos.y*TILESIZE + 75)

                pos += vec(5,0)
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
                self.dodgec = 1
        def checklevel(self):
            if self.exp >= self.needtolvl:
                self.lvl += 1
                self.exp -= self.needtolvl
                self.needtolvl *=2    
    class sillid():
        def __int__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            if self.attacks[attack][0][1] != 0:
                damage = (self.attacks[attack][0][0]+self.inc)*int(random.choices([1,2],[int(100-self.chance),int(0+self.chance)])[0])
                
                self.passive(attack)
                if attack == self.attack4:
                    for x in M.enemy:
                        for y in M.enemy[x]:
                            y[1] -= self.attacks[self.attack4][0][0]

                            ally.applyeffects(target,dup,attack,self)
                else:
                    ally.applyeffects(target,dup,attack,self)
                M.enemy[target][dup][1] -= damage
            else:
                M.actions.remove(self)
            
        def support(self,target):
            if self.acts != 0:
                for x in range(self.acts):
                    if self.attack4 in self.unlockedabilites:
                        cur = random.choices([self.attack1,self.attack2,self.attack4],[35,45,20])[0]
                    else:
                        cur = random.choices([self.attack1,self.attack2],[30,70])[0]
                    self.attacks[cur][0][1] += 1
                self.acts = 0
            else:
                M.actions.remove(self)
        def passive(self,used):
            self.attacks[used][0][1] -= 1
            self.acts += 1
        def damage(self,taken):
            ally.damage(self,taken)
        def draw_icons(self):
            pos = vec(18,31)
            for attack in self.attacks:
                if self.attack4 not in self.unlockedabilites:
                    if attack == self.attack4:
                        continue
                icon = self.attacks[attack][4]
                rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                text = str(self.attacks[attack][0][1])
                draw_text(text, 50, VIOLET, pos.x*TILESIZE + 40, pos.y*TILESIZE - 50)
                text = str(self.attacks[attack][0][0]+self.inc)
                if attack != self.attack3:
                    draw_text(text, 20, RED, pos.x*TILESIZE, pos.y*TILESIZE + 75)
                pos += vec(5,0)
                
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
            if cur == self.attack4:
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            if cur == 'increase':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.inc = 1
            if cur == 'critical':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.chance = 20
        def checklevel(self):
            if self.exp >= self.needtolvl:
                self.lvl += 1
                self.exp -= self.needtolvl
                self.needtolvl *= 2
    class noverence():
        def __int__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            if self.block:
                self.block = False
                self.combat_animation = {1:nover_combat_img,2:nover_combat2_img,3:nover_combat3_img}
            target,dup = target
            damage = 0
            if self.transformed:
                for x in M.allies:
                    M.allies[x][1] -= 5
                M.allies[self][1] += 5
                damage = self.attacks[attack][0][1]
                if M.enemy[target][dup][4][1] > 0:
                    damage *= 1.5
            else:
                damage = self.attacks[attack][0][0]
            ally.applyeffects(target,dup,attack,self)
            M.enemy[target][dup][1] -= damage
            self.passive(attack)
            
        def support(self,target):
            if self.block:
                self.block = False
                self.combat_animation = {1:nover_combat_img,2:nover_combat2_img,3:nover_combat3_img}
            if M.selectedattack == self.attack3:
                if self.acts == 0:
                    if self.transformed:
                        self.combat_animation = {1:nover_combat_img,2:nover_combat2_img,3:nover_combat3_img}
                        self.transformed = False
                    else:
                        self.combat_animation = {1:nover_transformed_img,2:nover_transformed_img,3:nover_transformed_img}
                        self.transformed = True
                else:
                    M.actions.remove(self)
            elif M.selectedattack == self.attack1:
                if self.transformed:
                    M.allies[self][3] += self.attacks[self.attack1][0][1]
                    self.block = True
                    
                else:
                    M.allies[self][3] += self.attacks[self.attack1][0][0]
                    self.block = True
                    self.combat_animation = {1:nover_block_img,2:nover_block_img,3:nover_block_img}
                pass
        def passive(self,used):           
            self.acts -= 1
            if self.acts < 0:
                self.acts = 0 
        def damage(self,taken):
            if self.block:
                taken[0] = int(taken[0]/2)
            ally.damage(self,taken)
        def draw_icons(self):
            #cur = cri_stunicon_img
            #goal_center = (int(M.allies[self][0].x * TILESIZE + TILESIZE / 2 + 80), int(M.allies[self][0].y * TILESIZE + TILESIZE / 2 - 50))
            #if self.attacks[self.attack1][0] < self.stuncap:
            #    cur = cur.copy( )
            #    cur.fill((105, 105, 105, 255),special_flags=pg.BLEND_RGB_MULT)            
            #screen.blit(cur, cur.get_rect(center=goal_center))
            pos = vec(18,31)
            for attack in self.attacks:
                if attack != self.attack4:
                    icon = self.attacks[attack][4]
                    rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 150)
                    pg.draw.rect(screen,BLACK,rect)
                    goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                    screen.blit(icon, icon.get_rect(center=goal_center))
                    if self.transformed:
                        text = str(self.attacks[attack][0][1])
                    else:
                        text = str(self.attacks[attack][0][0]+self.inc)
                    if attack == self.attack1:
                        draw_text(text, 20, BLUE, pos.x*TILESIZE, pos.y*TILESIZE + 75)
                    elif attack == self.attack2:
                        draw_text(text, 20, RED, pos.x*TILESIZE, pos.y*TILESIZE + 75)    
                pos += vec(5,0)
            #attack = self.attack2
            #    icon = self.attacks[attack][1]
            #    pos = self.attacks[attack][2]
            #    rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 150)
            #    pg.draw.rect(screen,BLACK,rect)
            #    goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
            #    screen.blit(icon, icon.get_rect(center=goal_center))
            #    if self.transformed:
            #        text = str(self.attacks[attack][0][1])
            #    else:
            #        text = str(self.attacks[attack][0][0]+self.inc)
            #    draw_text(text, 20, RED, pos.x*TILESIZE, pos.y*TILESIZE + 75)

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
            if cur == self.attack4:
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            if cur == 'increase':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.inc = 1
            if cur == 'critical':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.chance = 20
        def checklevel(self):
            if self.exp >= self.needtolvl:
                self.lvl += 1
                self.exp -= self.needtolvl
                self.needtolvl *= 2
ally = ally()
                    
iconaura = [(2, 2), (2, 1), (2, 0), (2, -1), (2, -2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1), (0, 0), (0, -1), (0, -2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (-2, 2), (-2, 1), (-2, 0), (-2, -1), (-2, -2)]            

nover = ally.noverence()
nover_combat_img = pg.image.load(os.path.join(filename,cross)).convert_alpha()
nover_combat_img = pg.transform.scale(nover_combat_img, (256, 256))
nover_combat2_img = pg.image.load(os.path.join(filename,cross)).convert_alpha()
nover_combat2_img = pg.transform.scale(nover_combat2_img, (256, 256))
nover_combat3_img = pg.image.load(os.path.join(filename,cross)).convert_alpha()
nover_combat3_img = pg.transform.scale(nover_combat3_img, (256, 256))

nover_transformed_img = pg.image.load(os.path.join(filename,'nover_transformed.png')).convert_alpha()
nover_transformed_img = pg.transform.scale(nover_transformed_img, (256, 256))

nover_block_img = pg.image.load(os.path.join(filename,'house-1.png.png')).convert_alpha()
nover_block_img = pg.transform.scale(nover_block_img, (256, 256))

nover_ability1_img = pg.image.load(os.path.join(filename,cross))
nover_ability1_img = pg.transform.scale(nover_ability1_img, (128, 128))
nover_ability2_img = pg.image.load(os.path.join(filename,cross))
nover_ability2_img = pg.transform.scale(nover_ability2_img, (128, 128))
nover_ability3_img = pg.image.load(os.path.join(filename,cross))
nover_ability3_img = pg.transform.scale(nover_ability3_img, (128, 128))
nover_ability4_img = pg.image.load(os.path.join(filename,cross))
nover_ability4_img = pg.transform.scale(nover_ability3_img, (128, 128))
nover.attack1 = 'block'
nover.attack2 = 'leech'
nover.attack3 = 'transform'
nover.attack4 = 'mimic'
nover.vec = vec(20,15)
nover.health = 50
nover.shield = 0
nover.acts = 2
nover.transformed = False
nover.block = False
nover.inc = 0
nover.abilities = {'self heal':[0,vec(47,17),True,'heal for half the damage dealt on enemies'],'increase':[0,vec(47,20),True,'Increases damage by 0.1'],'static blood':[0,vec(47,23),True,'allows heplane to trade health for shields']}
nover.unlockedabilites = []
nover.exp = 0
nover.lvl = 0
nover.needtolvl = 10
nover.combat_animation = {1:nover_combat_img,2:nover_combat2_img,3:nover_combat3_img}
nover.attacks = {nover.attack1:[[0,10],[{stun:1}],True,1,nover_ability1_img,[vec(18,31) + a for a in iconaura]],nover.attack2:[[5,10],[{bleed:1}],False,1,nover_ability2_img,[vec(23,31) + a for a in iconaura]],nover.attack3:[[0,0],[0],True,1,nover_ability3_img,[vec(28,31)+ a for a in iconaura]],nover.attack4:[[0,0],[0],True,1,cross,[vec(33,31)+ a for a in iconaura]]}
aura = [(1, 3), (0, 3), (-1, 3), (-1, 2), (0, 2), (1, 2), (1, 1), (0, 1), (-1, 1), (-1, 0), (0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, -2), (0, -2), (1, -2), (1, -3), (0, -3), (-1, -3)]
nover.clickaura = []
print([vec(18,31) + a for a in iconaura])
for x in aura:
    nover.clickaura.append(vec(x))

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
heplane_ability4_img = pg.image.load(os.path.join(filename,cross)).convert_alpha()
heplane_ability4_img = pg.transform.scale(heplane_ability4_img, (128, 128))
H.attack1 = 'coilent'
H.attack2 = 'punch'
H.attack3 = 'blood heal'
H.attack4 = 'static blood'
H.vec = vec(20,15)
H.health = 50
H.shield = 0
H.healdam = []
H.inc = 0
H.abilities = {H.attack3:[0,vec(47,17),True,'heal for half the damage dealt on enemies'],'increase':[0,vec(47,20),True,'Increases damage by 0.1'],H.attack4:[0,vec(47,23),True,'allows heplane to trade health for shields']}
H.unlockedabilites = []
H.exp = 0
H.lvl = 0
H.needtolvl = 10
H.combat_animation = {1:heplane_combat_img,2:heplane_combat2_img,3:heplane_combat3_img}
H.attacks = {H.attack1:[[10,15],[{fire:1}],False,1,heplane_ability1_img,[vec(18,31) + a for a in iconaura]],H.attack2:[[5,0],[0],False,1,heplane_ability2_img,[vec(23,31) + a for a in iconaura]],H.attack3:[[0,0],[0],True,1,heplane_ability3_img,[vec(28,31)+ a for a in iconaura]],H.attack4:[[20,0],[0],True,1,heplane_ability4_img,[vec(33,31)+ a for a in iconaura]]}
aura = [(1, 3), (0, 3), (-1, 3), (-1, 2), (0, 2), (1, 2), (1, 1), (0, 1), (-1, 1), (-1, 0), (0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, -2), (0, -2), (1, -2), (1, -3), (0, -3), (-1, -3)]
H.clickaura = []
for x in aura:
    H.clickaura.append(vec(x))

Cri = ally.cri()
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
Cri.attack1 = 'flash and crash'
Cri.attack2 = 'crystal glass'
Cri.attack3 = 'karen and her healing balony'
Cri.vec = vec(20,25)
Cri.health = 25
Cri.shield = 10
Cri.stuncap = 7
Cri.inc = 0
Cri.abilities = {'stun':[0,vec(47,17),True,'decreases the damage needed to stun from 7 to 6'],'increase':[0,vec(47,20),True,'increases the value that abilites increase to 2 rather then 1']}
Cri.unlockedabilites = []
Cri.exp = 0
Cri.lvl = 0
Cri.needtolvl = 10
Cri.combat_animation = {1:cri_combat_img,2:cri_combat2_img,3:cri_combat3_img}
Cri.attacks = {Cri.attack1:[5,[{stun:0}],False,1,cri_ability1_img,[vec(18,31) + a for a in iconaura]],Cri.attack2:[2,[0],True,1,cri_ability3_img,[vec(23,31)+a for a in iconaura]],Cri.attack3:[2,True,[0],1,cri_ability2_img,[vec(28,31) + a for a in iconaura]]}
Cri.clickaura = []
for x in aura:
    Cri.clickaura.append(vec(x))
    
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
Hap.needtolvl = 10
Hap.combat_animation = {1:haptic_combat_img,2:haptic_combat2_img,3:haptic_combat3_img}
Hap.attacks = {Hap.attack1:[5,[{bleed:0}],False,1,haptic_ability1_img,[vec(18,31) + a for a in iconaura]],Hap.attack2:[5,[0],False,1,haptic_ability2_img,[vec(23,31) + a for a in iconaura]],Hap.attack3:[0,[0],True,1,haptic_ability3_img,[vec(28,31)+a for a in iconaura]]}
Hap.clickaura = []
for x in aura:
    Hap.clickaura.append(vec(x))

sillid = ally.sillid()
sillid_combat_img = pg.image.load(os.path.join(filename,'sillid_temp.png')).convert_alpha()
sillid_combat_img = pg.transform.scale(sillid_combat_img, (256, 256))
sillid_combat2_img = pg.image.load(os.path.join(filename,'sillid_temp.png')).convert_alpha()
sillid_combat2_img = pg.transform.scale(sillid_combat2_img, (256, 256))
sillid_combat3_img = pg.image.load(os.path.join(filename,'sillid_temp.png')).convert_alpha()
sillid_combat3_img = pg.transform.scale(sillid_combat3_img, (256, 256))
sillid_ability1_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
sillid_ability1_img = pg.transform.scale(sillid_ability1_img, (128, 128))
sillid_ability2_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
sillid_ability2_img = pg.transform.scale(sillid_ability2_img, (128, 128))
sillid_ability3_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
sillid_ability3_img = pg.transform.scale(sillid_ability3_img, (128, 128))
sillid_ability4_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
sillid_ability4_img = pg.transform.scale(sillid_ability4_img, (128, 128))
sillid.attack1 = 'iron arrow'
sillid.attack2 = 'dirt arrow'
sillid.attack3 = 'restock'
sillid.attack4 = 'uranium arrow'
sillid.vec = vec(20,15)
sillid.health = 35
sillid.shield = 0
sillid.acts = 0
sillid.inc = 0
sillid.chance = 0
sillid.abilities = {sillid.attack4:[0,vec(47,17),True,'access to uranium arrows appears sometimes when restocking'],'increase':[0,vec(47,20),True,'Increase all attacks by 1'],'critical':[0,vec(47,23),True,'allows haptic to dodge attacks']}
sillid.unlockedabilites = []
sillid.exp = 0
sillid.lvl = 0
sillid.needtolvl = 10
sillid.combat_animation = {1:sillid_combat_img,2:sillid_combat2_img,3:sillid_combat3_img}
sillid.attacks = {sillid.attack1:[[10,1],[{bleed:1}],False,1,sillid_ability1_img,[vec(18,31) + a for a in iconaura]],sillid.attack2:[[5,3],[0],False,1,sillid_ability2_img,[vec(23,31) + a for a in iconaura]],sillid.attack3:[[0,0],[0],True,1,sillid_ability3_img,[vec(28,31)+a for a in iconaura]],sillid.attack4:[[10,1],[{fire:1,stun:1}],False,1,sillid_ability4_img,[vec(33,31) + a for a in iconaura]]}
sillid.clickaura = []
for x in aura:
    sillid.clickaura.append(vec(x))

class shopkeeper():
    class cleric():
        def action(self):
            if self.healone.collidepoint(int(mpos.x*TILESIZE),int(mpos.y*TILESIZE)) and main.amountmoney >= 15:
                self.heal = True
            elif self.heal == True and M.selectedchar != 0:
                M.allies[M.selectedchar][1] += 40
                if M.allies[M.selectedchar][1] >= M.selectedchar.health:
                    M.allies[M.selectedchar][1] = M.selectedchar.health
                self.heal = False
                main.amountmoney -= 15
            if self.healparty.collidepoint(int(mpos.x*TILESIZE),int(mpos.y*TILESIZE)) and main.amountmoney >= 40:
                for x in M.allies:
                    M.allies[x][1] += 40
                    if M.allies[x][1] >= x.health:
                        M.allies[x][1] = x.health
                main.amountmoney -= 40
            
            if self.resone.collidepoint(int(mpos.x*TILESIZE),int(mpos.y*TILESIZE)) and main.amountmoney >= 100:
                if M.ally1 not in M.allies:
                    pos = M.ally1.vec
                    eat = M.ally1.health
                    lean = M.ally1.shield
                    M.allies.update({M.ally1:[pos,eat,M.ally1.clickaura,lean,[]]})
                    main.amountmoney -= 100
                if M.ally2 not in M.allies:
                    pos = M.ally2.vec
                    eat = M.ally2.health
                    lean = M.ally2.shield
                    M.allies.update({M.ally2:[pos,eat,M.ally2.clickaura,lean,[]]})
                    main.amountmoney -= 100
                if M.ally3 not in M.allies:
                    pos = M.ally3.vec
                    eat = M.ally3.health
                    lean = M.ally3.shield
                    M.allies.update({M.ally3:[pos,eat,M.ally3.clickaura,lean,[]]})
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
            
            y = int(pos.y*TILESIZE-10)
            rect = pg.Rect(x, y, 135, 45)
            self.healone = pg.draw.rect(screen,BLACK,rect)
            draw_text('heal individual',20,WHITE,x+5, y)
            y2 = int(pos.y*TILESIZE-10)
            rect = pg.Rect(x2, y2, 40, 45)
            pg.draw.rect(screen,BLACK,rect)
            draw_text('15',20,WHITE,x2+5, y2)

            y = int(pos.y*TILESIZE+50)
            rect = pg.Rect(x, y, 135, 45)
            self.resone = pg.draw.rect(screen,BLACK,rect)
            draw_text('res individual',20,WHITE,x+5, y)
            y2 = int(pos.y*TILESIZE+50)
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
                    if M.selectedchar.attacks[M.selectedattack][2] != False:
                           
                        if mpos in M.allies[M.ally1][2]:
                                M.actions.append(M.selectedchar)
                                M.selectedchar.support(M.ally1)
                                M.attackselect = False
                                M.checkifdead()
                        
                        try:
                            if mpos in M.allies[M.ally2][2]:
                                M.actions.append(M.selectedchar)
                                M.selectedchar.support(M.ally2)
                                M.attackselect = False
                                M.checkifdead()
                        except:
                            pass
                        try:
                            if mpos in M.allies[M.ally3][2]:
                                M.actions.append(M.selectedchar)
                                M.selectedchar.support(M.ally3)                              
                                M.attackselect = False
                                M.checkifdead()
                        except:
                            pass
                        try:
                            if mpos in M.allies[M.ally4][2]:
                                M.actions.append(M.selectedchar)
                                M.selectedchar.support(M.ally4)                              
                                M.attackselect = False
                                M.checkifdead()
                        except:
                            pass
                        M.attackselect = False
                    else:
                        
                            der,xxer = M.selectenemy()
                            if der != 'pass':
                                M.actions.append(M.selectedchar)
                                M.selectedchar.attack((der,xxer),M.selectedattack)
                                M.attackselect = False

                                M.checkifdead()

                                M.attackselect = False         
                else:
                    pass 
            elif mpos not in M.getaura() and mpos not in M.selectingattack():
                M.selectedchar = 0
                M.attackselect = False
            if mpos in M.selectingchar() :#and M.attackselect == False:
                M.selectchar()
            if mpos in M.selectingattack():
                M.selectattack()
                print(M.selectedattack)
    def battlebottom(self):
        if current_time - self.anim_timer > 1000:
            M.current_animation += 1
            if M.current_animation == 4:
                M.current_animation = 1
            self.anim_timer = pg.time.get_ticks()
        if self.current_state == 'battle':
            

            if len(M.actions) >= len(M.allies) and self.playertrunover == False:
                M.statuseffects(False)
                self.playertrunover = True
                self.little = {}
                self.k = 0
                self.enemy_attck_time = pg.time.get_ticks()
                for x in M.enemy:
                    if len(M.enemy[x]) > 1:
                        for y in range(len(M.enemy[x])):
                            self.little.update({self.k:[x,y]})
                            self.k += 1
                    else:
                        self.little.update({self.k:[x,0]})
                        self.k += 1 
                self.k = 0
                self.enemycanattack = True
                M.checkifdead()
            M.draw_background()
            M.draw_allychar()
            M.draw_enemychar()
            M.draw_icons()
            M.draw_effects()
            if current_time - self.enemy_attck_time > 1000 and self.enemycanattack:
                self.display_time = pg.time.get_ticks()  
                self.enemy_attck_time = pg.time.get_ticks()
                M.enemyattack(self.k,self.little[self.k][1])
                self.k += 1
                if self.k >= len(self.little):
                    self.enemycanattack = False
                    self.playertrunover = False
                    M.actions = []
                    M.statuseffects(True)
                

            M.draw_damage()
            
            if current_time - self.display_time > 1000:
                
                M.enemycanattack = False
                M.checkifdead()
                M.damage = {}
                
                
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
    def overmaptop(self):
        if self.current_state == 'overmap':
            O.selectmap()
    def overmapbottom(self):
        if self.current_state == 'overmap':
            O.draw_overmap()

main = main()

main.current_state = 'overmap'
main.amountmoney = 50
main.enemy_attck_time = 0
main.enemycanattack = False
main.playertrunover = False
main.display_time = 0
main.k = 0
main.little = {}

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
        

class overmap():
    def __init__(self):
        self.over = 0
    def selectmap(self):
        if mpos2 == vec(0,0):
            main.current_state = 'map'
            main.test = True
            self.get_levelcontents()
            T.create_map()
        if mpos2 in self.connections:
            self.crossvec = mpos2
            self.get_connections()
            main.current_state = 'map'
            self.get_levelcontents()
            L.create_map()
    def get_levelcontents(self):
        vec = self.crossvec.x
        L.levelmaster = self.mapmaster[int((vec-2)/2)]
    def draw_overmap(self):
        vec = self.crossvec
        goal_center = (int(vec.x * TILESIZE*2 + TILESIZE*2 / 2), int(vec.y * TILESIZE*2 + TILESIZE*2 / 2))
        screen.blit(cross, cross.get_rect(center=goal_center))
        for x in self.maps:
            pg.draw.circle(screen,BLACK,(int(x.x*TILESIZE*2+TILESIZE*2/2),int(x.y*TILESIZE*2+TILESIZE*2/2)),5)
        for x in self.connections:
            pg.draw.line(screen, BLUE, (int(self.crossvec.x*TILESIZE*2+TILESIZE*2/2),int(self.crossvec.y*TILESIZE*2+TILESIZE*2/2)), (int(x.x*TILESIZE*2+TILESIZE*2/2),int(x.y*TILESIZE*2+TILESIZE*2/2)))
    def get_connections(self):
        self.connections = []
        possible = [vec(2,2),vec(2,-2)]
        for x in possible:
            newcheck = self.crossvec + x
            if newcheck in self.maps:
                self.connections.append(newcheck)
O = overmap()
O.over = 1
O.crossvec = vec(3,8)
O.maps = []
maps = [(5, 6), (5, 10), (7, 8), (9, 6), (9, 10), (7, 12), (7, 4), (7, 4), (9, 2), (9, 2), (9, 14), (11, 12), (11, 8), (11, 4), (13, 2), (13, 6), (13, 10), (13, 14), (15, 4), (15, 8), (15, 12), (17, 14), (17, 10), (17, 6), (17, 2), (19, 4), (19, 8), (19, 12), (21, 14), (21, 10), (21, 6), (21, 2), (23, 4), (25, 6), (27, 8), (25, 10), (23, 12), (23, 8)]
for x in maps:
    O.maps.append(vec(x))
O.mapmaster = {1:{0:[2,[sword,mage],[2,1]],1:[2,[sword,mage],[2,1]],2:[2,[sword,mage],[2,1]],3:[2,[sword,mage],[2,1]],4:[2,[sword,mage],[2,1]],5:[3,[sword,mage],[2,1]],6:[4,[sword,mage],[1,1]],7:[5,[sword,mage],[1,1]],8:[5,[sword,mage],[1,2]],9:[5,[sword,mage],[1,1]],10:[5,[sword,mage,lizard],[1,1,5]]
,11:[6,[sword,mage,lizard],[1,2,2]],12:[7,[sword,mage,lizard],[1,2,2]],13:[8,[sword,mage,lizard],[1,1,2]],14:[8,[sword,mage,lizard],[1,1,2]],15:[9,[sword,mage,lizard],[1,1,3]]
,16:[10,[sword,mage,lizard],[1,1,1]],17:[11,[sword,mage,C,lizard],[1,1,2,1]],18:[11,[sword,mage,C,lizard],[1,1,3,1]],19:[12,[sword,mage,C,lizard],[4,1,1,1]],20:[12,[sword,mage,C,lizard],[3,2,1,2]]
,21:[13,[sword,mage,C,lizard],[1,1,1,1]],22:[13,[sword,mage],[1,1]],23:[14,[sword,mage,C,lizard],[1,1,1,1]],24:[14,[sword,mage,C,lizard],[1,1,1,1]],25:[14,[sword,mage,C,lizard],[1,2,2,1]]
,26:[15,[sword,mage,C,lizard],[1,5,3,1]],27:[15,[mage,C],[1,1]],28:[15,[mage,C],[1,1]],29:[15,[mage,C],[1,1]],30:[15,[mage,C],[1,1]],31:[15,[mage,C],[1,1]],32:[15,[mage,C],[1,1]],33:[15,[mage,C],[1,1]],34:[15,[mage,C],[1,1]]
,35:[15,[mage,C],[1,1]],36:[15,[mage,C],[1,1]],37:[15,[mage,C],[1,1]],38:[15,[mage,C],[1,1]],39:[15,[mage,C],[1,1]],40:[15,[mage,C],[1,1]],41:[15,[mage,C],[1,1]],42:[15,[mage,C],[1,1]]},
2:{4:[2,[sword,mage],[2,1]],5:[3,[sword,mage],[2,1]]},
0:{0:[2,[stunte],[1]],4:[2,[stunte],[1]],5:[2,[bleedte],[1]],6:[2,[stunte,bleedte],[1,1]],7:[100,[mage,stunte],[1,2]],8:[5,[boulderine],[1]]}}

O.get_connections()

class test():
    def create_map(self):
        L.levelid = {}
        L.levelindex = {}
        L.drawdis = {}
        L.levelstatus = []
        L.path = {}
        L.pathloc = []
        tier = {}
        L.tierasi = {}
        line = 0
        L.closest = {}
        L.levelid = {}
        line = 0
        print(L.levels)
        tier = 'battle'
        for x in L.levels:
            if tier == 'battle':
                if x.x in L.levelmaster:
                    enemies = []
                    cost = L.levelmaster[x.x][0]
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices(L.levelmaster[x.x][1],L.levelmaster[x.x][2])
                        remove = L.get_cost(enemy)
                        cost -= remove
                        enemies.append(enemy[0])
                    L.make(line,enemies,tier,x)
            else:
                L.make(line,[],tier,x)
            if x.x == 28:
                L.levelid.update({line:[[cbm],'battle']})
                L.levelindex.update({line:x})
            line += 1         
                
T = test()


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
        #for x in self.connections:
        #    pg.draw.line(screen, BLUE, (int(self.crossvec.x*TILESIZE*2+TILESIZE*2/2),int(self.crossvec.y*TILESIZE*2+TILESIZE*2/2)), (int(x.x*TILESIZE*2+TILESIZE*2/2),int(x.y*TILESIZE*2+TILESIZE*2/2)))
        #a,b = self.finddis(self.crossvec)
        ##print(a ** random.choice([1.5,1.55,1.6]))
        #pg.draw.line(screen, BLUE, (int(self.crossvec.x*TILESIZE*2+TILESIZE*2/2),int(self.crossvec.y*TILESIZE*2+TILESIZE*2/2)), (int(b.x*TILESIZE*2+TILESIZE*2/2),int(b.y*TILESIZE*2+TILESIZE*2/2)))
        for x in self.drawdis:
            x2 = int(x)
            y = self.tierasi[x]
            dis = self.drawdis[x]
            dis2 = int(dis)
            once = True
            while dis > 0:
                if dis <= dis2/2 and once:
                    pg.draw.line(screen, BLUE, (int(x*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)), (int((x+2)*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)))
                    x += 2
                    once = False
                pg.draw.line(screen, BLUE, (int(x*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)), (int(x*TILESIZE*2+TILESIZE*2/2),int((y-1)*TILESIZE*2+TILESIZE*2/2)))
                y -= 1
                dis -= 1
                
            while dis < 0:
                if dis >= dis2/2 and once:
                    pg.draw.line(screen, BLUE, (int(x*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)), (int((x+2)*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)))
                    x += 2
                    once = False
                pg.draw.line(screen, BLUE, (int(x*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)), (int(x*TILESIZE*2+TILESIZE*2/2),int((y+1)*TILESIZE*2+TILESIZE*2/2)))
                y += 1
                dis += 1
            while x != x2 + 4:
                pg.draw.line(screen, BLUE, (int(x*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)), (int((x+1)*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)))
                x += 1
    def create_map(self):
        self.levelid = {}
        self.levelindex = {}
        self.drawdis = {}
        self.levelstatus = []
        self.path = {}
        self.pathloc = []
        tier = {}
        self.tierasi = {}
        line = 0
        self.closest = {}
        for x in self.levels:
            if x.x % 4 == 1:
                if x.x not in tier:
                    tier.update({x.x:[x.y]})
                else:
                    tier[x.x].append(x.y)
        
        for x in tier:
            l = random.choice(tier[x])
            self.tierasi.update({x:l})
        for x in self.tierasi:
            if x != 25:
                x2 = x + 4
                dis = self.tierasi[x] - self.tierasi[x2] 
                self.drawdis.update({x:dis})

        for x in self.drawdis:
            x2 = int(x)
            y = self.tierasi[x]
            dis = self.drawdis[x]
            dis2 = int(dis)
            once = True
            while dis > 0:
                if dis <= dis2/2 and once:
                    pg.draw.line(screen, BLUE, (int(x*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)), (int((x+1)*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)))
                    x += 2
                    once = False
                    self.pathloc.append(vec(x,y))
                pg.draw.line(screen, BLUE, (int(x*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)), (int(x*TILESIZE*2+TILESIZE*2/2),int((y-1)*TILESIZE*2+TILESIZE*2/2)))
                y -= 1
                dis -= 1
                self.pathloc.append(vec(x,y))
            while dis < 0:
                if dis >= dis2/2 and once:
                    pg.draw.line(screen, BLUE, (int(x*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)), (int((x+1)*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)))
                    x += 2
                    once = False
                    self.pathloc.append(vec(x,y))
                pg.draw.line(screen, BLUE, (int(x*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)), (int(x*TILESIZE*2+TILESIZE*2/2),int((y+1)*TILESIZE*2+TILESIZE*2/2)))
                y += 1
                dis += 1
                self.pathloc.append(vec(x,y))
            while x != x2 + 4:
                pg.draw.line(screen, BLUE, (int(x*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)), (int((x+1)*TILESIZE*2+TILESIZE*2/2),int(y*TILESIZE*2+TILESIZE*2/2)))
                x += 1
                self.pathloc.append(vec(x,y))

        for x in self.levels:
            tier = 'battle'
            if x.x in self.tierasi:
                if x.y == self.tierasi[x.x]:
                    tier = 'shop'
            if tier == 'battle':
                if x.x in self.levelmaster:
                    level,b = self.finddis(x)
                    
                    enemies = []
                    level **= random.choice([1.4,1.41,1.42,1.43,1.45,1.46,1.47,1.48,1.49,1.5])
                    level += x.x**0.85
                    level = int(round(level))
                    cost = self.levelmaster[level][0]
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices(self.levelmaster[level][1],self.levelmaster[level][2])
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
        possible = [vec(1,0),vec(1,-1),vec(1,1),vec(0,1),vec(0,-1)]
        for x in possible:
            newcheck = self.crossvec + x
            if newcheck in self.levels:
                self.connections.append(newcheck)
    def finddis(self,a):
        dis = 100
        newb = 100
        for b in self.pathloc:
            
            newdis = math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
            if newdis < dis:
                dis = newdis
                newb = b
        
        return int(dis),newb
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
        if boulderine in target:
            cost = 5
        return cost
    def make(self,line,enemies,tier,x):
        self.levelid.update({line:[enemies,tier]})
        self.levelindex.update({line:x}) 
    def nextlevel(self):
        if lock == True:
            if mpos2 in self.connections:
                if self.click == True:
                    self.crossvec = mpos2
                    self.level = mpos2.x - 3
                    e,tier = self.getlevel()
                    if self.level == 1:
                        M.restart()
                    if 'battle' == tier:
                        M.start()
                    elif 'shop' == tier:
                        M.shopstart()
                    L.get_connections()
                    main.current_state = tier
                    self.click = False
        else:
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
        if mpos2 in self.levelstatus:
            main.current_state = 'map'
            e = 0
            tier = 'map'
        else:
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
        ally1 = H
        ally2 = nover
        ally3 = sillid
        ally4 = Cri
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
        self.allies.update({self.ally1:[pos,eat,self.ally1.clickaura,lean,{}]})
        self.ally2 = ally2
        pos = self.ally2.vec
        eat = self.ally2.health
        lean = self.ally2.shield
        self.allies.update({self.ally2:[pos,eat,self.ally2.clickaura,lean,{}]})
        self.ally3 = ally3
        pos = self.ally3.vec
        eat = self.ally3.health
        lean = self.ally3.shield
        self.allies.update({self.ally3:[pos,eat,self.ally3.clickaura,lean,{}]})
        self.ally4 = ally4
        pos = self.ally4.vec
        eat = self.ally4.health
        lean = self.ally4.shield
        self.allies.update({self.ally4:[pos,eat,self.ally4.clickaura,lean,{}]})
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
                self.enemy[x].append([tout,eat,x.clickaura,attack,{}])
            else: 
                tout = x.vec
                eat = x.health
                attack = x.attacks
                self.enemy.update({x:[[tout,eat,x.clickaura,attack,{}]]})
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
        for x in self.allies:
            if self.selectedchar == x:
                x.draw_icons()
            
    def draw_damage(self):
        for x in self.damage:
            damage = 0
            for y in self.damage[x]:
                if y == 0:
                    draw_text('miss',30,RED,self.allies[x][0].x*TILESIZE, self.allies[x][0].y*TILESIZE-170,align="bottomright")  
                damage += y
            if x in self.allies:
                draw_text(str(damage),30,RED,self.allies[x][0].x*TILESIZE, self.allies[x][0].y*TILESIZE-150,align="bottomright")    
    def draw_background(self):
        goal_center = int(WIDTH / 2), int(HEIGHT/ 2)
        screen.blit(background_fall, background_fall.get_rect(center=goal_center))
    def draw_attack(self):
        self.selectedchar.draw_attack() #pffft over here you already made one
        pass
    def draw_effects(self):
        for x in self.allies:
            if bleed in self.allies[x][4]:
                draw_text('bleed',10, RED, self.allies[x][0].x*TILESIZE + 25, self.allies[x][0].y*TILESIZE,align="bottomright")
            if fire in self.allies[x][4]:
                draw_text('fire',10, YELLOW, self.allies[x][0].x*TILESIZE + 25, self.allies[x][0].y*TILESIZE,align="bottomright")
            if stun in self.allies[x][4]:
                draw_text('stun',10, YELLOW, self.allies[x][0].x*TILESIZE + 25, self.allies[x][0].y*TILESIZE,align="bottomright")
    def checkifdead(self):
        test = dict(self.enemy)
        for x in test:
            if self.dup:
                for y in test[x]:
                    if int(y[1]) <= 0:
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
            #ally2 = Cri
            if main.current_state == 'battle':
                L.levelstatus.append(mpos2)
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
            if len(self.killhistory) != 0:
                if len(self.allies)-len(self.killhistory) != 0:
                    tsplitcoins = coins - (splitcoins*1.2)*len(self.killhistory)
                    tsplitcoins = tsplitcoins/(len(self.allies)-len(self.killhistory))
                    for x in self.killhistory:
                        x.exp += round(splitcoins*1.2)

                        x.checklevel()
                    for z in self.allies:
                        if z not in self.killhistory:
                            z.exp += round(tsplitcoins)
                            z.checklevel()
                else:
                    for x in self.killhistory:
                        x.exp += round(splitcoins*1.2)

                        x.checklevel()
            else:
                thing = []
                blah = []
                for x in self.allies:
                    thing.append(x)
                for l in range(len(self.savecost)):
                    x = random.choice(thing)
                    blah.append(x)
                if len(self.allies)-len(self.savecost) != 0:
                    tsplitcoins = coins - (splitcoins*1.2)*len(self.savecost)
                    tsplitcoins = tsplitcoins/(len(self.allies)-len(self.savecost))


                    for x in blah:
                        x.exp += round(splitcoins*1.2)
                        x.checklevel()
                    for z in self.allies:
                        if z not in blah:
                            z.exp += round(tsplitcoins)
                            z.checklevel()
                else:
                    for x in blah:
                        x.exp += round(splitcoins*1.2)
                        x.checklevel()
            self.savecost = []
            self.killhistory = []
            if len(L.connections) == 0:
                main.current_state = 'overmap'
                L.crossvec = vec(3,8)
                L.get_connections()
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
                    if spaces[x][1] == 99:
                        if y not in taken:
                            spaces[x][1] = y
                            self.enemy[y][0][0] = spaces[x][0]
                            self.enemy[y][0][2] = [self.enemy[y][0][0]+ x for x in self.enemy[y][0][2]]
                    taken = []              
    def numberofallies(self):
        self.spaces = {'front row':[[vec(20,15), 99],[vec(20,25),99]],'back row':[[vec(13,15),99],[vec(13,25),99]]}
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
        if self.selectedchar != 0:
            for x in self.selectedchar.attacks:
                y += self.selectedchar.attacks[x][5]
        return y
    def selectingchar(self):
        y = []
        for z in self.allies:
            for x in self.allies[z][2]:
                y.append(x)
        return y
    def selectattack(self):
        
        try:
            if mpos in M.selectedchar.attacks[self.selectedchar.attack1][5]:
                M.selectedattack = self.selectedchar.attack1
                M.attackselect = True
            if mpos in M.selectedchar.attacks[self.selectedchar.attack2][5]:
                M.selectedattack = self.selectedchar.attack2
                M.attackselect = True
            if mpos in M.selectedchar.attacks[self.selectedchar.attack3][5]:
                M.selectedattack = self.selectedchar.attack3
                M.attackselect = True
            if mpos in M.selectedchar.attacks[self.selectedchar.attack4][5]:
                M.selectedattack = self.selectedchar.attack4
                M.attackselect = True
        except:
            pass
        if self.selectedchar in self.actions:
            M.attackselect = False
    def selectchar(self):
        for x in self.allies:
            if mpos in self.allies[x][2]:
                M.selectedchar = x
                M.charselect = True
    def selectenemy(self):
        cur_enemyspecific = 'pass'
        cur_enemyclass = 'pass'
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
    def enemyattack(self,cur,spec):
        x = main.little[cur][0]
        ll = int(spec)
        if x != cbm:
            if stun in self.enemy[x][ll][2]:
                if self.enemy[x][ll][2][stun] > 1:
                    self.enemy[x][ll][2][stun] -= 1
                else:
                    del self.enemy[x][ll][2][stun]
            else: 

                x.thunk(ll)
        else:
            x.attack()
        
    def workingattack(self,attack,effect):
        pass
    def statuseffects(self,when):
        if when:
            for x in self.allies:
                if stun in self.allies[x][4]:
                    self.allies[x][4][stun] -= 1
                    self.actions.append(x)
                if bleed in self.allies[x][4]:
                    self.allies[x][4][bleed] -= 0.5
                    self.allies[x][1] -= 2
                if fire in self.allies[x][4]:
                    self.allies[x][4][fire] -= 1
                    self.allies[x][1] -= 5
        if not when:
            # for x in self.allies:
            #     if self.allies[x][4][0] > 0:
            #         self.allies[x][4][0] -= 1
            #         self.actions.append(x)
            for x in self.enemy:
                lel = 0
                for y in self.enemy[x]:
                    if bleed in self.enemy[x][lel][4]:
                        self.enemy[x][lel][4][bleed] -= 0.5
                        self.enemy[x][lel][1] -= 2
                    if fire in self.enemy[x][lel][4]:
                        self.enemy[x][lel][4][fire] -= 1
                        self.enemy[x][lel][1] -= 5
                    lel += 1
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
changing enemy attack to one at a time and show damage+
apply current changes to boss class
shop mehanic +


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



NAMES 
zither
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

M.damage = {}
M.attackselect = False
#M.clickaura = [vec(-1,-1)]


main.anim_timer = pg.time.get_ticks()
M.enemycanattack = False

M.draw_shopkeeps()

mpos = vec(0,0)
create = []
lock = True

L.get_connections()
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does #print: event
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
                if main.current_state == 'map' or main.current_state == 'overmap':
                    mpos2 = vec(pg.mouse.get_pos()) // (TILESIZE*2)
                    pos = pg.mouse.get_pos()
                    L.click = True

                #L.crossvec =  mpos2
                #O.maps.append(vec(mpos2))
                main.switchtop()
                main.battletop()
                
                main.leveltop()
                main.shoptop()
                main.overmaptop()

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_r:
                M.enemy = {}
                M.checkifdead()
                M.hov = False
            if event.key == pg.K_e:
                M.actions = [1,1,1,1]
            if event.key == pg.K_q:
                main.current_state = 'overmap'
            if event.key == pg.K_c:
                M.selectedchar.lvl += 1
            if event.key == pg.K_h:
                M.allies[M.selectedchar] += 100
            if event.key == pg.K_n:
                M.allies[M.selectedchar][1] = 0
            if event.key == pg.K_l:
                if lock == True:
                    lock = False
                else:
                    lock = True
            if event.key == pg.K_k:
                for x in M.allies:
                    x.exp = 0
            print(lock)
            #if event.key == pg.K_a:
            #    print([(int(loc.x -  M.clericvec.x), int(loc.y - M.clericvec.y)) for loc in create])
            if event.key == pg.K_m:
                print([(int(loc.x),int(loc.y))for loc in O.maps])
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
    main.overmapbottom()
    main.draw_level()
    main.draw_money()
    pg.display.flip() # dose the changes goto doccumentation for other ways