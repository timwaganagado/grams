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
    class magee():
        def __int__(self):
            self.vec = 0
            self.health = 0
            self.combat_animation = 0    
            self.clickaura = []
            self.attacks = 0
    class swordguy():
        def __int__(self):
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

home_img = pg.image.load(os.path.join(filename,'cross-1.png.png')).convert_alpha()
home_img = pg.transform.scale(home_img, (256, 256))

sword = enemy.swordguy()
sword.vec = vec(43,20)
sword.health = 30
sword.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, -1), (1, -1), (2, -1), (2, -2), (1, -2), (0, -2), (0, -3), (1, -3), (2, -3)]
sword.clickaura = []
for aura in auras:
    sword.clickaura.append(vec(aura))
sword.attacks = {'slash':[4,4,[0,1,0],2],'miss':[0,2,[0,0,0],1]}


class ally():
    class heplane():
        def __init__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            blooddamage = int(M.allies[H][1])/100 + 1
            M.allies[H][1] -= self.attacks[attack][0][1]
            self.healdam.append(int((blooddamage * self.attacks[attack][0][0])/2))
            M.enemy[target][dup][1] -= blooddamage * self.attacks[attack][0][0]
            if self.attacks[attack][5][0] > 0:
                M.enemy[target][dup][4][0] += self.attacks[attack][5][0]
                print(M.enemy[target][0][4],self.attacks[attack][5][0])
            if self.attacks[attack][5][1] > 0:
                M.enemy[target][dup][4][1] += self.attacks[attack][5][1]
            if self.attacks[attack][5][2] > 0:
                M.enemy[target][dup][4][2] += self.attacks[attack][5][2]
        def support(self,target):
            if target == H:
                for x in self.healdam:
                    M.allies[M.selectedchar][1] += x
                self.healdam = []
                if M.allies[M.selectedchar][1] > 50:
                    M.allies[M.selectedchar][1] = 50
        def draw_icons(self):
            for x in self.attacks:
                if H in M.allies: 
                    icon = self.attacks[x][1]
                    pos = self.attacks[x][2]
                    rect = pg.Rect(int(pos.x*TILESIZE-49), int(pos.y*TILESIZE-50), 128, 140)
                    pg.draw.rect(screen,BLACK,rect)
                    goal_center = (int(pos.x * TILESIZE + TILESIZE / 2), int(pos.y * TILESIZE + TILESIZE / 2))
                    screen.blit(icon, icon.get_rect(center=goal_center))
                    text = str(round(int((M.allies[M.ally1][1]/100 + 1) * self.attacks[self.attack1][0][0])))
                    draw_text(text, 20, RED, self.attacks[self.attack1][2].x*TILESIZE, self.attacks[self.attack1][2].y*TILESIZE + 65)
                    text = str(round(int((M.allies[M.ally1][1]/100 + 1) * self.attacks[self.attack2][0][0])))
                    draw_text(text, 20, RED, self.attacks[self.attack2][2].x*TILESIZE, self.attacks[self.attack2][2].y*TILESIZE + 65)
                    if len(M.ally1.healdam) != 0:
                        l = 0
                        for x in M.ally1.healdam:
                            l += x
                        text = str(l)
                    else:
                        text = str(0)
                    draw_text(text, 20, GREEN, self.attacks[self.attack3][2].x*TILESIZE, self.attacks[self.attack3][2].y*TILESIZE + 65)
        def draw_attack(self):
            pass
    class sri():
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
                    self.attacks[x][0] += 1
                else:
                    self.attacks[x][0] += 2
                if self.attacks[x][0] > 10:
                    self.attacks[x][0] = 2
        def draw_icons(self):
            for x in self.attacks:
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
H.attacks = {H.attack1:[[10,15],heplane_ability1_img,vec(18, 31),[vec(18,31) + a for a in iconaura],False,[1,0,0]],H.attack2:[[5,0],heplane_ability2_img,vec(23,31),[vec(23,31) + a for a in iconaura],False,[0,0,0]],H.attack3:[[0,0],heplane_ability3_img,vec(28,31),[vec(28,31)+ a for a in iconaura],True,[0,0,0]]}
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
sri_ability1_img = pg.image.load(os.path.join(filename,'crystal_icons-2.png.png'))
sri_ability1_img = pg.transform.scale(sri_ability1_img, (128, 128))
sri_ability2_img = pg.image.load(os.path.join(filename,'crystal_icons-1.png.png'))
sri_ability2_img = pg.transform.scale(sri_ability2_img, (128, 128))
sri_ability3_img = pg.image.load(os.path.join(filename,'crystal_icons-3.png.png'))
sri_ability3_img = pg.transform.scale(sri_ability3_img, (128, 128))
S.attack1 = 'flash and crash'
S.attack2 = 'crystal glass'
S.attack3 = 'karen and her healing balony'
S.vec = vec(20,25)
S.health = 25
S.shield = 10
S.combat_animation = {1:sri_combat_img,2:sri_combat2_img,3:sri_combat3_img}
S.attacks = {S.attack1:[5,sri_ability1_img,vec(18,31),[vec(18,31) + a for a in iconaura],False,[1,0,1]],S.attack2:[2,sri_ability2_img,vec(23,31),[vec(23,31) + a for a in iconaura],True,[0,0,0]],S.attack3:[2,sri_ability3_img,vec(28,31),[vec(28,31)+a for a in iconaura],True,[0,0,0]]}
S.clickaura = [S.vec + a for a in aura]

class main():
    def __init__(self):
        current_state = 0
    def states(self):
        if self.current_state == 'battle':
            pass
    def battletop(self):
        if self.current_state == 'battle':
            if mpos in M.getaura() and M.selectedchar != 0:
                if M.attackselect == True and M.enemycanattack == False :
                    if M.selectedchar.attacks[M.selectedattack][4] != False:
                        if mpos in M.ally1.clickaura:
                            M.selectedchar.support(M.ally1)
                            attck_timer = pg.time.get_ticks()
                            M.actions.append(M.selectedchar)
                            M.attackselect = False
                            M.checkifdead()
                        elif mpos in M.ally2.clickaura:
                            M.selectedchar.support(M.ally2)
                            M.actions.append(M.selectedchar)
                            M.attackselect = False
                            M.checkifdead()
                        M.attackselect = False
                    else:
                        if M.dup:

                            if mpos in M.enemy[M.enemy1][0][2]:
                                    M.selectedchar.attack((M.enemy1,0),M.selectedattack)
                                    M.attackselect = False
                                    M.actions.append(M.selectedchar)
                                    M.checkifdead()

                            try:
                                if mpos in M.enemy[M.enemy1][1][2]:
                                        M.selectedchar.attack((M.enemy1,1),M.selectedattack)
                                        M.attackselect = False
                                        M.actions.append(M.selectedchar)
                                        M.checkifdead()
                            except:
                                pass
                        else:
                            try:
                                if mpos in M.enemy[M.enemy1][0][2]:
                                    M.selectedchar.attack((M.enemy1,0),M.selectedattack)
                                    M.attackselect = False
                                    M.actions.append(M.selectedchar)
                                    M.checkifdead()
                            except:
                                pass
                            try:
                                if mpos in M.enemy[M.enemy2][0][2]:
                                    M.selectedchar.attack((M.enemy2,0),M.selectedattack)
                                    M.attackselect = False
                                    M.actions.append(M.selectedchar)
                                    M.checkifdead()
                            except:
                                pass
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
        if self.current_state == 'battle':
            if current_time - self.anim_timer > 1000:
                M.current_animation += 1
                if M.current_animation == 4:
                    M.current_animation = 1
                self.anim_timer = pg.time.get_ticks()
            if current_time - self.attck_timer > 1000 and M.enemycanattack == True:
                M.actions = []
                M.enemyattack()
                self.display_time = pg.time.get_ticks()   
                M.enemycanattack = False
                M.attackselect = False
                M.checkifdead()
            if len(M.actions) >= len(M.allies) and M.enemycanattack == False:
                self.attck_timer = pg.time.get_ticks()
                M.enemycanattack = True

            if M.click == True:
                if current_time - self.display_time > 1000:
                    M.enemycanattack = False
                    M.display == False
                    M.damage = {}
                    M.click = False
            M.draw_background()
            M.draw_char()
            M.draw_icons()
            M.draw_healthbar()
            M.draw_damage()
            M.draw_effects()
    def leveltop(self):
        if self.current_state == 'map':
            L.nextlevel()
            M.numberofenemy()
    def levelbottom(self):
        if self.current_state == 'map':
            L.draw_currentposition()
            L.draw_linestoconnections()

main = main()

main.current_state = 'map'

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
    def draw_currentposition(self):
        vec = self.crossvec
        goal_center = (int(vec.x * TILESIZE*2 + TILESIZE*2 / 2), int(vec.y * TILESIZE*2 + TILESIZE*2 / 2))
        screen.blit(cross, cross.get_rect(center=goal_center))
        for x in self.levels:
            pg.draw.circle(screen,BLACK,(int(x.x*TILESIZE*2+TILESIZE*2/2),int(x.y*TILESIZE*2+TILESIZE*2/2)),5)
    def draw_linestoconnections(self):
        for x in self.connections:
            pg.draw.line(screen, BLUE, (self.crossvec.x*TILESIZE*2+TILESIZE*2/2,self.crossvec.y*TILESIZE*2+TILESIZE*2/2), (x.x*TILESIZE*2+TILESIZE*2/2,x.y*TILESIZE*2+TILESIZE*2/2))
            
    def get_connections(self):
        self.connections = []
        possible = [vec(1,0),vec(1,-1),vec(1,1)]
        for x in possible:
            newcheck = self.crossvec + x
            if newcheck in self.levels:
                self.connections.append(newcheck)
    def nextlevel(self):
        if mpos2 in self.connections:
            self.crossvec = mpos2
            self.level = mpos2.x - 3
            if self.level == 1:
                M.restart()
            else:
                M.start()
            L.get_connections()
            main.current_state = 'battle'
            main.states()
    def getlevelenemies(self):
        level = self.level
        if level == 1:
            e = [sword]
        if level == 2:
            e = [sword,sword]
        if level == 3:
            e = [mage]
        if level == 4:
            e = [mage,mage]
        if level == 5:
            e = [mage,sword]
        if level == 6:
            e = [C]
        if level == 7:
            e = [C,C]
        if level == 8:
            e = [sword,C]
        if level == 9:
            e = [mage,C]
        return e

cross = pg.image.load(os.path.join(filename,'cross-1.png.png'))
cross = pg.transform.scale(cross, (TILESIZE*2, TILESIZE*2))

L = level()
L.level = 0
L.crossvec = vec(3,8)
L.connections =[]
L.levels = []
levels = [(4, 7), (4, 8), (4, 9), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (10, 14), (10, 13), (10, 12), (10, 11), (10, 10), (10, 9), (10, 8), (10, 7), (10, 6), (10, 5), (10, 4), (10, 3), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2), (21, 2), (22, 2), (27, 8), (27, 7), (27, 9), (26, 9), (26, 8), (26, 7), (26, 6), (26, 10), (25, 10), (25, 11), (25, 9), (25, 8), (25, 7), (25, 6), (25, 5), (24, 5), (24, 4), (23, 3), (23, 4), (11, 14), (12, 14), (13, 14), (14, 14), (15, 14), (24, 12), (24, 11), (23, 12), (23, 13), (22, 13), (22, 14), (21, 14), (20, 14), (18, 14), (19, 14), (17, 14), (16, 14), (16, 13), (15, 13), (13, 13), (14, 13), (12, 13), (11, 13), (11, 12), (12, 12), (13, 12), (14, 12), (15, 12), (16, 12), (17, 12), (17, 13), (18, 13), (18, 12), (19, 12), (19, 13), (20, 13), (20, 12), (21, 12), (21, 13), (22, 12), (22, 11), (23, 11), (23, 10), (24, 10), (24, 9), (23, 9), (24, 8), (23, 8), (24, 7), (23, 7), (24, 6), (23, 6), (23, 5), (22, 5), (22, 4), (22, 3), (21, 3), (21, 4), (20, 4), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (11, 4), (12, 4), (13, 4), (14, 4), (15, 4), (16, 4), (17, 4), (19, 4), (18, 4), (18, 5), (17, 5), (16, 5), (15, 5), (14, 5), (13, 5), (12, 5), (11, 5), (11, 6), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6), (19, 5), (20, 5), (20, 6), (21, 6), (21, 5), (22, 6), (22, 7), (22, 8), (22, 9), 
(22, 10), (21, 10), (21, 11), (21, 9), (21, 8), (21, 7), (20, 7), (20, 8), (20, 9), (20, 10), (20, 11), (19, 11), (19, 10), (19, 9), (19, 8), (19, 7), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11), (17, 11), (17, 10), (17, 
9), (17, 8), (17, 7), (16, 7), (16, 8), (16, 9), (16, 10), (16, 11), (15, 11), (15, 10), (15, 9), (15, 8), (15, 7), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (13, 11), (12, 11), (11, 11), (11, 10), (12, 10), (13, 10), 
(13, 9), (12, 9), (11, 9), (11, 8), (12, 8), (13, 8), (13, 7), (12, 7), (11, 7)]
for x in levels:
    if x not in L.levels:
        L.levels.append(vec(x))

class battle():
    def __int__(self):
        self.current_animation = 0
        self.allies
        self.enemy = 0
        self.display = 0
        self.damage = 0
        #self.clickaura = 0
    def restart(self):
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
        self.allies.update({self.ally1:[pos,eat,self.ally1.clickaura,lean,[0,0,0]]})
        self.ally2 = ally2
        pos = self.ally2.vec
        eat = self.ally2.health
        lean = self.ally2.shield
        self.allies.update({self.ally2:[pos,eat,self.ally2.clickaura,lean,[0,0,0]]})
        enemy = L.getlevelenemies()
        #for x in range(1,3):#range(1,random.randint(2,3))
        if len(enemy) >= 1:
            self.enemy1 = enemy[0]
            tout = self.enemy1.vec
            eat = self.enemy1.health
            attack = self.enemy1.attacks
            M.enemy.update({self.enemy1:[[tout,eat,[tout + x for x in self.enemy1.clickaura],attack,[0,0,0]]]})
        if len(enemy) >= 2:
            self.enemy2 = enemy[1]
            if self.enemy2 in M.enemy:
                self.enemy[self.enemy2].append([tout,eat,[tout + x for x in self.enemy2.clickaura],attack,[0,0,0]])
            else: 
                tout = M.enemy2.vec
                eat = M.enemy2.health
                attack = M.enemy2.attacks
                self.enemy.update({M.enemy2:[[tout,eat,[tout + x for x in self.enemy2.clickaura],attack,[0,0,0]]]})
                self.numberofenemy()
    def start(self):
        enemy = L.getlevelenemies()
        #for x in range(1,random.randint(2,3)):
        if len(enemy) >= 1:
            self.enemy1 = enemy[0]
            tout = self.enemy1.vec
            eat = self.enemy1.health
            attack = self.enemy1.attacks
            M.enemy.update({self.enemy1:[[tout,eat,[tout + x for x in self.enemy1.clickaura],attack,[0,0,0]]]})
        if len(enemy) >= 2:
            M.enemy2 = enemy[1]
            if M.enemy2 in M.enemy:
                M.enemy[M.enemy1].append([tout,eat,[tout + x for x in M.enemy2.clickaura],attack,[0,0,0]])
            else: 
                tout = M.enemy2.vec
                eat = M.enemy2.health
                attack = M.enemy2.attacks
                M.enemy.update({M.enemy2:[[tout,eat,[tout + x for x in M.enemy2.clickaura],attack,[0,0,0]]]})
        self.numberofenemy()
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
                lol = pg.transform.scale(lol, (300, 275))
                lol.fill((0, 0, 0),special_flags=pg.BLEND_RGB_MULT)
                lel = lol.get_rect(center=goal_center)
                lel[1] -=2
                screen.blit(lol, lel)
            screen.blit(cur, cur.get_rect(center=goal_center))
        
        for x in self.enemy:   
            if len(self.enemy[x]) != 2:
                #print(self.enemy[x][0][0],'stink')
                ani = x.combat_animation 
                vec = self.enemy[x][0][0]    
                goal_center = (int(vec.x * TILESIZE + TILESIZE / 2), int(vec.y * TILESIZE + TILESIZE / 2))
                screen.blit(ani[self.current_animation], ani[self.current_animation].get_rect(center=goal_center))
            else:
                for y in self.enemy[x]:
                    ani = x.combat_animation
                    vec = y[0]
                    goal_center = (int(vec.x * TILESIZE + TILESIZE / 2), int(vec.y * TILESIZE + TILESIZE / 2))
                    screen.blit(ani[self.current_animation], ani[self.current_animation].get_rect(center=goal_center))
    def draw_icons(self):
        if M.selectedchar == self.ally1:
            self.ally1.draw_icons()
        if M.selectedchar == self.ally2:
            self.ally2.draw_icons()
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
            if len(self.enemy[x]) != 2:
                vec = self.enemy[x][0][0]
                heat = self.enemy[x][0][1] 
                text = str(round(heat))+'/'+str(x.health)
                draw_text(text, 20, BLACK, vec.x*TILESIZE - 10, vec.y*TILESIZE - 150)
                rect = pg.Rect(int(vec.x*TILESIZE - 10), int(vec.y*TILESIZE - 120), int(heat), 20)
                pg.draw.rect(screen,RED,rect)
            else:
                for y in self.enemy[x]:
                    vec = y[0]
                    heat = y[1] 
                    text = str(round(heat))+'/'+str(x.health)
                    draw_text(text, 20, BLACK, vec.x*TILESIZE - 10, vec.y*TILESIZE - 150)
                    rect = pg.Rect(int(vec.x*TILESIZE - 10), int(vec.y*TILESIZE - 120), int(heat), 20)
                    pg.draw.rect(screen,RED,rect)
    def draw_damage(self):
        if self.display == True:
            for x in self.damage:

                if x in self.allies:
                    if len(self.damage[x]) == 2:
                        draw_text(str(self.damage[x][0]),30,RED,self.allies[x][0].x*TILESIZE-15, self.allies[x][0].y*TILESIZE-150,align="bottomright")
                        draw_text(str(self.damage[x][1]),30,RED,self.allies[x][0].x*TILESIZE+15, self.allies[x][0].y*TILESIZE-150,align="bottomright")
                    else:
                        draw_text(str(self.damage[x][0]),30,RED,self.allies[x][0].x*TILESIZE, self.allies[x][0].y*TILESIZE-150,align="bottomright")    
    def draw_background(self):
        goal_center = int(WIDTH / 2), int(HEIGHT/ 2)
        screen.blit(background_fall, background_fall.get_rect(center=goal_center))
    def draw_attack(self):
        self.selectedchar.draw_attack() #pffft over here you already made one
        pass
    def draw_level(self):
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
                        #print(self.enemy)
                if len(test[x]) <= 0:
                    del self.enemy[x]
            else:
                if test[x][0][1] <=0 :
                    del self.enemy[x]
        test = dict(self.allies)
        for x in test:
            if test[x][1] <= 0:
                del self.allies[x]
        if len(self.enemy) <= 0:
            #ally1 = H
            #ally2 = S
            main.current_state = 'map'
            print(main.current_state)
            self.selectedattack = 0
            self.selectedchar = 0
            self.current_animation = 1
            #self.allies = {}
            self.enemy = {}
            self.l = []
            self.actions = []

            
        if len(self.allies) <= 0:
            print('i hope not')
            self.restart()
    def numberofenemy(self):
        self.dup = False
        if len(self.enemy) == 2:
            self.enemy[self.enemy1][0][0] = vec(43,10)
            self.enemy[self.enemy2][0][0] = vec(43,25)
            self.enemy[self.enemy1][0][2] = [self.enemy[self.enemy1][0][0]+ x for x in self.enemy1.clickaura]
            self.enemy[self.enemy2][0][2] = [self.enemy[self.enemy2][0][0]+ x for x in self.enemy2.clickaura]
            self.dup = False
        else:
            for x in self.enemy:
                if len(self.enemy[x]) == 2:
                    self.enemy[x][0][0] = vec(43,10)
                    self.enemy[x][1][0] = vec(43,25)
                    self.enemy[x][0][2] = [self.enemy[x][0][0]+ y for y in x.clickaura]
                    self.enemy[x][1][2] = [self.enemy[x][1][0]+ y for y in x.clickaura]
                    self.dup = True
                    
    def getaura(self):
        y = []
        for x in self.enemy:
            if self.dup:
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
            for x in z.clickaura:
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
        if mpos in self.ally1.clickaura:
            M.selectedchar = self.ally1
            M.charselect = True
        elif mpos in self.ally2.clickaura:
            M.selectedchar = self.ally2
            M.charselect = True
    def enemyattack(self):
        self.statuseffects(False)
        for x in self.enemy:
            if self.dup:
                for z in self.enemy[x]:
                    print(z[4])
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
        self.click = True
        self.display = True
        self.statuseffects(True)
        self.checkifdead()
    def workingattack(self,attack):
        attacks = []
        chance = []
        possible = []
        for y in attack:
            chance.append(attack[y][1])
            attacks.append(y)
        for x in self.allies:
            possible.append(x)
        target = random.choice(possible)
        attacking = random.choices(attacks,chance)
        damage = attack[attacking[0]]
        print(attacking,damage[0])
        for x in range(0,damage[3]):
            if self.allies[target][3] > 0:
                self.allies[target][3] -= damage[0]
                if self.allies[target][3] < 0:
                    self.allies[target][3] = 0
            else:
                self.allies[target][1] -= damage[0]
                if damage[2][1] > 0:
                    print('bleed')
                    self.allies[target][4][1] += damage[2][1]
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
                    print(self.actions)
                    
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
sri class +
difficulty tweeks to make game harder === (everyone) or easeir (ava)
status effects to both enemies and allies +
programming bleed +
levels (rouge like) 
specific levels (a traditional rpg) that will require a class system +
boss enemies (trent)
more enemies (trent or daniel)
enemy with damage reduction
sri passive deals with increase in values the more you use them +
healing removes status effects except stun (sri) +
haptic class -
new enemy sowrd guy(medium) +
new enemy sword guy(actually easy) -
rework enemy selection so that its a list for multiple dupes +
and fixed resulting problems +
map system with levels +
maps have shops or camps
game over screen
placment order editable in a menu during map

Art
drawing heplane +
drawing conrift +
animate both +
drawing magee -
icons for heplane +
drawing sri +
animate sri +
icons for sri +
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
'''
M = battle()






M.targetedenemy = 0
background_fall = pg.image.load(os.path.join(filename,'backgorunds-2.png.png'))
background_fall = pg.transform.scale(background_fall, (1920, 1080))




M.display = False
M.damage = {}
M.click = False
M.attackselect = False
#M.clickaura = [vec(-1,-1)]

main.attck_timer = 1000000
main.anim_timer = pg.time.get_ticks()
M.enemycanattack = False



create = []

L.get_connections()
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if main.current_state == 'battle':
                    mpos = vec(pg.mouse.get_pos()) // TILESIZE
                if main.current_state == 'map':
                    mpos2 = vec(pg.mouse.get_pos()) // (TILESIZE*2)
                #L.crossvec =  mpos2
                main.battletop()
                #L.levels.append(vec(mpos2))
                main.leveltop()
                #create.append(mpos)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                M.enemy = random.choice([C,mage])
            if event.key == pg.K_a:
                print([(int(loc.x - M.heplanevec.x), int(loc.y - M.heplanevec.y)) for loc in create])
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
    main.levelbottom()
    main.battlebottom()
    pg.display.flip() # dose the changes goto doccumentation for other ways