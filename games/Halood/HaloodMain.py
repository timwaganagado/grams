
from turtle import width
import pygame as pg
from os import path
from collections import deque
import random
import copy
import shelve
import os , sys
import math

from pygame import display
vec = pg.math.Vector2

#HEIGHTTILESIZE = 30



#ipad 832 computer 1080
HEIGHT = 1080
#ipad 23/16 computer 16/9
WIDTH = int(HEIGHT*(16/9))
print(WIDTH)
GRIDWIDTH = WIDTH/30
GRIDHEIGHT = HEIGHT/30
imagescaledheight = int(HEIGHT/(4+(7/32)))
imagescaledwidth = int(WIDTH/7.5) 
obstaclesscaledheight = int(HEIGHT/(27/5))
obstaclesscaledwidth = int(WIDTH/(48/5))
abilityscaledheight = int(HEIGHT/(135/16))
abilityscaledwidth = int(WIDTH/(15/1))
WIDTHTILESIZE = int(WIDTH/(64/1))
HEIGHTTILESIZE = int(HEIGHT/(36/1))
print(WIDTHTILESIZE,HEIGHTTILESIZE)
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
ORANGE = (255, 165, 0)
check = 'working'

pg.init()
displayspec = 0
#displayspec = input('')
#if displayspec == '':
#    displayspec = 0
#else:
#    displayspec = int(displayspec)

try:
    screen = pg.display.set_mode((WIDTH, HEIGHT),display = displayspec)
except:
    screen = pg.display.set_mode((WIDTH, HEIGHT),pg.WINDOWED,display = 0)
clock = pg.time.Clock()
cross = 'cross-1.png.png'
filename = os.path.dirname(sys.argv[0])
filename += '/Halood_images'

def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font("C:/Windows/Fonts/Arial.ttf",size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (int(x), int(y))})
    screen.blit(text_surface, text_rect)

def draw_text_center(text, size, color, x, y):
    font = pg.font.Font(filename+'/scout-font-family/Scout Font Family/Scout-Bold.otf', size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x,y))
    screen.blit(text_surface, text_rect)


secondrow = [vec(4,2),vec(4,3),vec(4,4),vec(4,5)]                
firstrow = [vec(5,2),vec(5,3),vec(5,4),vec(5,5)]

topcollumenemy = [vec(6,2),vec(7,2),vec(8,2),vec(9,2)]
secondcollumenemy = [vec(6,3),vec(7,3),vec(8,3),vec(9,3)]
thirdcollumenemy = [vec(6,4),vec(7,4),vec(8,4),vec(9,4)]
bottomcollumenemy = [vec(6,5),vec(7,5),vec(8,5),vec(9,5)]

collumcheck = {2:topcollumenemy,3:secondcollumenemy,4:thirdcollumenemy,5:bottomcollumenemy}

twobthree = [vec(-1,0),vec(-1,-1,),vec(-1,1),vec(0,-1),vec(0,1)]
threebthree = [vec(-1,0),vec(-1,-1,),vec(-1,1),vec(0,-1),vec(0,1),vec(1,0),vec(1,-1),vec(1,1)]

enemytwobthree = [vec(-1,0),vec(-1,-1,),vec(-1,1),vec(0,-1),vec(0,1),vec(0,0)]
#general effects
fire = 'fire'
bleed = 'bleed'
stun = 'stun'
weakness = 'weakness'
dodge = 'dodge'
charge = 'charge'
pierce = 'pierce'
erosion = 'erosion'

#char spec effects
needle = 'needle'

class testenemy():
    class stunte():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self,ll)
            enemy.defaultattack(self,ll,damage)
        def damage(self,dup,damage,inin):
            M.enemy[self][dup][1] -= damage
    class bleedte():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self,ll)
            enemy.defaultattack(self,ll,damage)
        def damage(self,dup,damage,inin):
            M.enemy[self][dup][1] -= damage
    class spsword():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self,ll)
            enemy.defaultattack(self,ll,damage)
        def damage(self,dup,damage,inin):
            M.enemy[self][dup][1] -= damage

home_img = pg.image.load(os.path.join(filename,cross)).convert_alpha()
home_img = pg.transform.scale(home_img, (imagescaledwidth, imagescaledheight))

testenemy = testenemy()

stunte = testenemy.stunte()

currentfileg =  filename +'/enemies'

currentfiles = currentfileg + '/swordguy'
swordguy_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat1.png')).convert_alpha()
swordguy_img = pg.transform.scale(swordguy_img, (imagescaledwidth, imagescaledheight))
swordguy2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat2.png')).convert_alpha()
swordguy2_img = pg.transform.scale(swordguy2_img, (imagescaledwidth, imagescaledheight))
swordguy3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat3.png')).convert_alpha()
swordguy3_img = pg.transform.scale(swordguy3_img, (imagescaledwidth, imagescaledheight))

stunte.vec = vec(43,20)
stunte.health = 25
stunte.immunities = []
stunte.combat_animation = {1:home_img,2:home_img,3:home_img}
stunte.attack_animation = {1:home_img,2:home_img,3:home_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
stunte.clickaura = []
for aura in auras:
    stunte.clickaura.append(vec(aura))
stunte.attacks = {'constrict':[0,{stun:1},False,1,1]}

bleedte = testenemy.bleedte()

bleedte.vec = vec(43,20)
bleedte.health = 25
bleedte.immunities = []
bleedte.combat_animation = {1:home_img,2:home_img,3:home_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
bleedte.clickaura = []
for aura in auras:
    bleedte.clickaura.append(vec(aura))
bleedte.attacks = {'constrict':[0,{bleed:1},False,1,1]}

swordguy_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat1.png')).convert_alpha()
swordguy_img = pg.transform.scale(swordguy_img, (imagescaledwidth, imagescaledheight))
swordguy2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat2.png')).convert_alpha()
swordguy2_img = pg.transform.scale(swordguy2_img, (imagescaledwidth, imagescaledheight))
swordguy3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat3.png')).convert_alpha()
swordguy3_img = pg.transform.scale(swordguy3_img, (imagescaledwidth, imagescaledheight))

swordguy_attacking_img = pg.image.load(os.path.join(currentfiles,'swordguy_attacking0.png')).convert_alpha()
swordguy_attacking_img = pg.transform.scale(swordguy_attacking_img, (imagescaledwidth, imagescaledheight))
swordguy_attacking2_img = pg.image.load(os.path.join(currentfiles,'swordguy_attacking1.png')).convert_alpha()
swordguy_attacking2_img = pg.transform.scale(swordguy_attacking2_img, (imagescaledwidth, imagescaledheight))
swordguy_attacking3_img = pg.image.load(os.path.join(currentfiles,'swordguy_attacking2.png')).convert_alpha()
swordguy_attacking3_img = pg.transform.scale(swordguy_attacking3_img, (imagescaledwidth, imagescaledheight))

spsword = testenemy.spsword()

spsword.vec = vec(43,20)
spsword.health = 30
spsword.immunities = []
spsword.combat_animation = {1:swordguy_img,2:swordguy2_img,3:swordguy3_img}
spsword.attack_animation = {1:swordguy_attacking_img,2:swordguy_attacking2_img,3:swordguy_attacking3_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
spsword.clickaura = []
for aura in auras:
    spsword.clickaura.append(vec(aura))
spsword.attacks = {'miss':[0,{},False,1,1]}

class enemy():
    def decision(target,ll):
        attack = target.attacks
        chance = []
        attacks = []
        for y in attack:
            chance.append(attack[y][4])
            attacks.append(y)

        attacking = random.choices(attacks,chance)[0] #selects attack
        
        damage = attack[attacking] #damage number
        
        able = damage[5][0] #type of attack eg straight
        pospos = damage[6] #vec where the enemy can attack from
        poopee = M.unconversion[(M.enemy[target][ll][0].x,M.enemy[target][ll][0].y)] #current vec
        checker = [vec(1,0),vec(0,1),vec(-1,0),vec(0,-1)] #vec check
        checked = [] #possible places the enemy can move to
        movement = target.movement +1 #gets movement 
        checked.append(vec(poopee)) #adds the enemy's current position to places it can move to
        
        for x in range(0,movement): # checks the where the enemy can move 
            #print(x)
            if x == 1: # first check around the enemy
                for x in checker:
                    new = poopee+ x
                    if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0: # restricts movements to the grid
                        checked.append(new)
            else: # second and more checks and if the movement is more
                oldchecked = list(checked)
                for y in oldchecked: #grabs the already checked positions and checks around them
                    for x in checker:
                        new = y+ x 
                        if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0:
                            if new not in checked: #prevents already checked vecs to be added to the list
                                checked.append(new)
        
        pot = [] # the potential positions the enemy can attack from
        possible = [] # is a simplified list 
        agros = [] #list of the agros of player characters which help the selection of attack
        hitmult = {} 
        potpos = {}
        for x in checked:
            if x in pospos:
                pot.append(x)
        if able == 'straight':
            at = 0
            for x in pot:
                x = vec(x)
                start = vec(5,x.y)
                while start.x > 1:
                    start = (start.x,start.y)
                    if M.allyspaces[start] != 0:
                        hitmult.update({at:[M.allyspaces[start],start]})
                        possible.append(at)
                        agros.append(M.allyspaces[start].agro)
                        at += 1
                        if M.allyspaces[start] in potpos:
                            potpos[start].append(x)
                        else:
                            potpos.update({start:[x]})
                        break
                    start = vec(start)
                    start.x -= 1
                    
        
        #for x in M.spaces:
        #    if x == 'front row':
        #        for l in M.spaces[x]:
        #            if l[1] != 99:
        #                possible.append(l[1])
        #                agros.append(l[1].agro)
        #            else:
        #                dead.append(l[1])
        #    if x == 'back row' and len(dead) == 2:
        #        for j in M.spaces[x]:
        #            if j[1] != 99:
        #                possible.append(j[1])
        #                agros.append(j[1].agro)
        #            else:
        #                dead.append(j[1])
        char = target
        if len(possible) != 0:
            M.enemy[target][ll][6] = True
            M.enemy[target][ll][3] = attacking
            target = random.choices(possible,agros)[0]
            target = hitmult[target]
            newpos = random.choice(potpos[target[1]])
            M.enemyspaces[M.unconversion[(M.enemy[char][ll][0].x,M.enemy[char][ll][0].y)]] = 0
            M.enemy[char][ll][0] = vec(M.conversion[newpos.x,newpos.y])
            M.enemyspaces[M.unconversion[(M.enemy[char][ll][0].x,M.enemy[char][ll][0].y)]] = char
            M.enemy[char][ll][2] = [M.enemy[char][ll][0]+ x for x in char.clickaura] 
        else:
            target = 0
            newpos = vec(random.choice(checked))
            M.enemyspaces[M.unconversion[(M.enemy[char][ll][0].x,M.enemy[char][ll][0].y)]] = 0
            M.enemy[char][ll][0] = vec(M.conversion[newpos.x,newpos.y])
            M.enemyspaces[M.unconversion[(M.enemy[char][ll][0].x,M.enemy[char][ll][0].y)]] = char
            M.enemy[char][ll][2] = [M.enemy[char][ll][0]+ x for x in char.clickaura] 
        return damage,target
    def defaultattack(initiated,dup,damage,target):
        if target != 0:
            pot = []
            for x in M.obstacles:
                for y in M.obstacles[x]:
                    pot.append(M.unconversion[y[0].x,y[0].y])
            if target[1] in pot:
                for x in M.obstacles:
                    lel = 0
                    for y in M.obstacles[x]:
                        if target[1] == M.unconversion[y[0].x,y[0].y]:
                            target[0].damage(lel,initiated,dup) #obstacle damage
                        lel += 1
                        
            else:
                for x in range(0,damage[3]):
                    target[0].damage(damage,initiated,dup)
    def defaultheavyattack(initiated,dup):
        pos = M.enemy[initiated][dup][0]
        pos = vec(M.unconversion[pos.x,pos.y])
        attack = M.enemy[initiated][dup][4]['heavy']
        attpos = M.enemy[initiated][dup][4]['heavy'][1]
        attack = initiated.heavyattacks[attack[0]]
        

        
        newpos = attpos
        save = M.enemyspaces[M.unconversion[(M.enemy[initiated][dup][0].x,M.enemy[initiated][dup][0].y)]]
        M.enemyspaces[M.unconversion[(M.enemy[initiated][dup][0].x,M.enemy[initiated][dup][0].y)]] = 0
        if M.enemyspaces[newpos.x,newpos.y] == 0: # movement
            M.enemy[initiated][dup][6] = True #attack animation
            M.enemy[initiated][dup][3] = M.enemy[initiated][dup][4]['heavy'][0] #draws the text of the attack
            M.enemyspaces[M.unconversion[(M.enemy[initiated][dup][0].x,M.enemy[initiated][dup][0].y)]] = 0
            M.enemy[initiated][dup][0] = vec(M.conversion[newpos.x,newpos.y])
            M.enemyspaces[M.unconversion[(M.enemy[initiated][dup][0].x,M.enemy[initiated][dup][0].y)]] = initiated#movement
            M.enemy[initiated][dup][2] = [M.enemy[initiated][dup][0]+ x for x in initiated.clickaura] #updating other movement things
            if attack[5][0] == 'spec 1st column': #damage
                targetpos = (5,attpos.y)
                for ll in attack[5][1]:
                    new = targetpos+ ll
                    if M.allyspaces[new.x,new.y] != 0:
                        for q in range(0,attack[3]):
                            if M.allyspaces[new.x,new.y] in obstacles.allothem:
                                lel = 0
                                for y in M.obstacles[M.allyspaces[new.x,new.y]]:
                                    if (new.x,new.y) == M.unconversion[y[0].x,y[0].y]:
                                        M.allyspaces[new.x,new.y].damage(lel,initiated,dup)
                                    lel += 1
                            else:  
                                if M.allyspaces[new.x,new.y] != 0:      
                                    M.allyspaces[new.x,new.y].damage(attack,initiated,dup) #ally damage
        else:
            M.enemyspaces[M.unconversion[(M.enemy[initiated][dup][0].x,M.enemy[initiated][dup][0].y)]] = save
    def damage(target,dup,damage,inin):
        if pierce in M.enemy[target][dup][4]:
            damage *= 1.5
        damage = ally.checkblessing('attacking',inin,damage,target,dup)
        M.enemy[target][dup][1] -= damage 
        M.enemy[target][dup][5].append(damage)
        total = 0
        amount = 0
        done = True
        for ll in M.enemy[target][dup][5]:
            if ll == 'done':
                done = False
            else:    
                total += ll
            if ll != 'done':
                if ll >= 5:
                    amount += 1
        if done:
            if total >= target.stagger and amount >= 2 and stun not in target.immunities and 'ps' not in M.enemy[target][dup][4]:
                M.enemy[target][dup][5].append('done')
                if stun in M.enemy[target][dup][4]:
                    M.enemy[target][dup][4][stun] += 1
                else:
                    M.enemy[target][dup][4].update({stun:1})
                M.enemy[target][dup][4].update({'ps':1})
    class conrift():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self,ll)
            enemy.defaultattack(self,ll,damage)
        def damage(self,dup,damage,inin):
            enemy.damage(self,dup,damage,inin)
    class magee():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            if M.enemy[self][ll][1] < 15:
                damage = self.attacks['heal']
            else:
                damage = enemy.decision(self,ll)
            if damage[2]:
                self.support(damage)
            else:
                enemy.defaultattack(self,ll,damage)
        def support(self,damage):
            lowest = 10000000
            if damage[3] == 0:
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
        def damage(self,dup,damage,inin):
            enemy.damage(self,dup,damage,inin)
    class swordguy():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage,target = enemy.decision(self,ll)
            enemy.defaultattack(self,ll,damage,target)
        def heavythunk(self,ll):
            enemy.defaultheavyattack(self,ll)
        def damage(self,dup,damage,inin):
            enemy.damage(self,dup,damage,inin)
    class archer():
        def __init__(self):
            self.vec = 0 
        def thunk(self,ll):
            damage = enemy.decision(self,ll)
            enemy.defaultattack(self,ll,damage)
        def damage(self,dup,damage,inin):
            enemy.damage(self,dup,damage,inin)
    class boulderine():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self,ll)
            if damage[2]:
                self.support(damage,ll)
            else:
                enemy.defaultattack(self,ll,damage)
        def support(self,damage,ll):
            M.enemy[self][ll][4].update({dodge:1})
        def damage(self,dup,damage,inin):
            if dodge in M.enemy[self][dup][4]: 
                if M.allies[M.selectedchar][3] > 0:
                    enemy.damage(self,dup,damage,inin)
                    M.selectedchar.damage([10,{},False,2,4],self,dup)
                else:
                    M.selectedchar.damage([10,{},False,2,4],self,dup)
            else:
                enemy.damage(self,dup,damage,inin)
    class hardboulderine():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self,ll)
            if damage[2]:
                self.support(damage,ll)
            else:
                enemy.defaultattack(self,ll,damage)
        def support(self,damage,ll):
            M.enemy[self][ll][4].update({dodge:1})
        def damage(self,dup,damage,inin):
            if dodge in M.enemy[self][dup][4]: 
                if M.allies[M.selectedchar][3] > 0:
                    enemy.damage(self,dup,damage,inin)
                    M.selectedchar.damage([10])
                else:
                    M.selectedchar.damage([10])
            else:
                enemy.damage(self,dup,damage,inin)
    class rentoron():
        def __init__(self):
            self.vec = 0 
        def thunk(self,ll):
            damage = enemy.decision(self,ll)
            if damage[2] or charge in M.enemy[self][ll][4]:
                self.support(damage,ll)
            else:
                enemy.defaultattack(self,ll,damage)
        def support(self,damage,ll):
            if charge in M.enemy[self][ll][4]:
                for x in M.allies:
                    x.damage([10,{}],self,ll)
            else:
                M.enemy[self][ll][4].update({charge:1})
        def damage(self,dup,damage,inin):
            enemy.damage(self,dup,damage,inin)
    class grosehound():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self,ll)
            enemy.defaultattack(self,ll,damage)
        def damage(self,dup,damage,inin):
            enemy.damage(self,dup,damage,inin)
    class barrier():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            damage = enemy.decision(self,ll)
            if damage[2]:
                damage[3] = random.choice([1,2,3,4,5,6,7,8])
            enemy.defaultattack(self,ll,damage)
        def damage(self,dup,damage,inin):
            enemy.damage(self,dup,damage,inin)
    class dva():
        def __init__(self):
            self.vec = 0
        def thunk(self,ll):
            if 'weapon' not in M.enemy[self][ll][4]:
                cweapons = []
                for x in self.weapons:
                    cweapons.append(x)
                M.enemy[self][ll][4].update({'weapon':random.choice(cweapons)})
            selectedweapon = M.enemy[self][ll][4]['weapon']
            self.attacks.update(self.weapons[selectedweapon])
            damage = enemy.decision(self,ll)
            for x in self.weapons[selectedweapon]:
                del self.attacks[x]
            if damage[2]:
                cweapons = []
                for x in self.weapons:  
                    if x != selectedweapon:
                        cweapons.append(x)
                M.enemy[self][ll][4].update({'weapon':random.choice(cweapons)})
            else:
                enemy.defaultattack(self,ll,damage)
        def damage(self,dup,damage,inin):
            enemy.damage(self,dup,damage,inin)



    
    

enemy.list = []
enemy.list.append(bleedte)
enemy.list.append(spsword)
enemy.list.append(stunte)

currentfiles = currentfileg + '/conrift'

conrift_combat_img = pg.image.load(os.path.join(currentfiles,'conrift_combat0.png')).convert_alpha()
conrift_combat_img = pg.transform.scale(conrift_combat_img, (imagescaledwidth, imagescaledheight))
conrift_combat2_img = pg.image.load(os.path.join(currentfiles,'conrift_combat1.png')).convert_alpha()
conrift_combat2_img = pg.transform.scale(conrift_combat2_img, (imagescaledwidth, imagescaledheight))
conrift_combat3_img = pg.image.load(os.path.join(currentfiles,'conrift_combat2.png')).convert_alpha()
conrift_combat3_img = pg.transform.scale(conrift_combat3_img, (imagescaledwidth, imagescaledheight))

magee_attacking_img = pg.image.load(os.path.join(currentfiles,'conrift_attacking0.png')).convert_alpha()
magee_attacking_img = pg.transform.scale(magee_attacking_img, (imagescaledwidth, imagescaledheight))
magee_attacking2_img = pg.image.load(os.path.join(currentfiles,'conrift_attacking1.png')).convert_alpha()
magee_attacking2_img = pg.transform.scale(magee_attacking2_img, (imagescaledwidth, imagescaledheight))
magee_attacking3_img = pg.image.load(os.path.join(currentfiles,'conrift_attacking2.png')).convert_alpha()
magee_attacking3_img = pg.transform.scale(magee_attacking3_img, (imagescaledwidth, imagescaledheight))

conrift = enemy.conrift()
enemy.list.append(conrift)
conrift.vec = vec(43,20)
conrift.health = 40
conrift.immunities = [bleed,fire]
conrift.combat_animation = {1:conrift_combat_img,2:conrift_combat2_img,3:conrift_combat3_img}
conrift.attack_animation = {1:magee_attacking_img,2:magee_attacking2_img,3:magee_attacking3_img}
conrift.clickaura = [vec(-1,0),vec(-1,1),vec(-1,2),vec(-1,3),vec(-1,-1),vec(-1,-2),vec(-1,-3),vec(0,0),vec(0,1),vec(0,2),vec(0,3),vec(0,-1),vec(0,-2),vec(0,-3),vec(1,0),vec(1,1),vec(1,2),vec(1,3),vec(1,-1),vec(1,-2),vec(1,-3)]
conrift.attacks = {'darkness':[5,{},False,1,5],'conduction':[20,{fire:1,stun:1},False,1,1]}
conrift.stagger = 15

currentfiles = currentfileg + '/magee'

magee_combat_img = pg.image.load(os.path.join(currentfiles,'magee_combat0.png')).convert_alpha()
magee_combat_img = pg.transform.scale(magee_combat_img, (imagescaledwidth, imagescaledheight))
magee_combat2_img = pg.image.load(os.path.join(currentfiles,'magee_combat1.png')).convert_alpha()
magee_combat2_img = pg.transform.scale(magee_combat2_img, (imagescaledwidth, imagescaledheight))
magee_combat3_img = pg.image.load(os.path.join(currentfiles,'magee_combat2.png')).convert_alpha()
magee_combat3_img = pg.transform.scale(magee_combat3_img, (imagescaledwidth, imagescaledheight))

magee_attacking_img = pg.image.load(os.path.join(currentfiles,'magee_attacking0.png')).convert_alpha()
magee_attacking_img = pg.transform.scale(magee_attacking_img, (imagescaledwidth, imagescaledheight))
magee_attacking2_img = pg.image.load(os.path.join(currentfiles,'magee_attacking1.png')).convert_alpha()
magee_attacking2_img = pg.transform.scale(magee_attacking2_img, (imagescaledwidth, imagescaledheight))
magee_attacking3_img = pg.image.load(os.path.join(currentfiles,'magee_attacking2.png')).convert_alpha()
magee_attacking3_img = pg.transform.scale(magee_attacking3_img, (imagescaledwidth, imagescaledheight))

magee = enemy.magee()
enemy.list.append(magee)
magee.vec = vec(43,20)
magee.health = 30
magee.immunities = [bleed]
magee.combat_animation = {1:magee_combat_img,2:magee_combat2_img,3:magee_combat3_img}
magee.attack_animation = {1:magee_attacking_img,2:magee_attacking2_img,3:magee_attacking3_img}
auras = [(0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, -1), (1, -1), (2, -1), (2, -2), (1, -2), (0, -2), (0, -3), (1, -3), (2, -3)]
magee.clickaura = []
for aura in auras:
    magee.clickaura.append(vec(aura))
magee.attacks = {'fire ball':[10,{fire:1},False,1,4],'lightning':[15,{stun:1},False,1,1],'ice shards':[5,{pierce:1},False,1,4],'heal':[5,{},True,0,2],'miss':[0,{},False,1,1]}
magee.stagger = 15

currentfiles = currentfileg + '/swordguy'

swordguy_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat1.png')).convert_alpha()
swordguy_img = pg.transform.scale(swordguy_img, (imagescaledwidth, imagescaledheight))
swordguy2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat2.png')).convert_alpha()
swordguy2_img = pg.transform.scale(swordguy2_img, (imagescaledwidth, imagescaledheight))
swordguy3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat3.png')).convert_alpha()
swordguy3_img = pg.transform.scale(swordguy3_img, (imagescaledwidth, imagescaledheight))

swordguy_attacking_img = pg.image.load(os.path.join(currentfiles,'swordguy_attacking0.png')).convert_alpha()
swordguy_attacking_img = pg.transform.scale(swordguy_attacking_img, (imagescaledwidth, imagescaledheight))
swordguy_attacking2_img = pg.image.load(os.path.join(currentfiles,'swordguy_attacking1.png')).convert_alpha()
swordguy_attacking2_img = pg.transform.scale(swordguy_attacking2_img, (imagescaledwidth, imagescaledheight))
swordguy_attacking3_img = pg.image.load(os.path.join(currentfiles,'swordguy_attacking2.png')).convert_alpha()
swordguy_attacking3_img = pg.transform.scale(swordguy_attacking3_img, (imagescaledwidth, imagescaledheight))

swordguy = enemy.swordguy()
enemy.list.append(swordguy)
swordguy.vec = vec(43,20)
swordguy.health = 30
swordguy.immunities = []
swordguy.movement = 2
swordguy.speed = 50
swordguy.combat_animation = {1:swordguy_img,2:swordguy2_img,3:swordguy3_img}
swordguy.attack_animation = {1:swordguy_attacking_img,2:swordguy_attacking2_img,3:swordguy_attacking3_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
swordguy.clickaura = []
for aura in auras:
    swordguy.clickaura.append(vec(aura))
swordguy.attacks = {'blunt slash':[3,{},False,2,4,['straight',False],[vec(6,2),vec(6,3),vec(6,4),vec(6,5),vec(7,2),vec(7,3),vec(7,4),vec(7,5)]],'slash':[3,{pierce:1},False,2,2,['straight',False],[vec(6,2),vec(6,3),vec(6,4),vec(6,5),vec(7,2),vec(7,3),vec(7,4),vec(7,5)]],'miss':[0,{},False,1,1,['straight',False],[vec(6,2),vec(6,3),vec(6,4),vec(6,5),vec(7,2),vec(7,3),vec(7,4),vec(7,5)]]}
swordguy.heavyattacks = {'wild flailing':[10,{bleed:1},False,2,1,['spec 1st column',enemytwobthree],[vec(6,3),vec(6,4)]]}
swordguy.stagger = 10

home_img = pg.image.load(os.path.join(filename,cross)).convert_alpha()
home_img = pg.transform.scale(home_img, (imagescaledwidth, imagescaledheight))

currentfiles = currentfileg + "/archer"

archer_img = pg.image.load(os.path.join(currentfiles,'archer_combat0.png')).convert_alpha()
archer_img = pg.transform.scale(archer_img, (imagescaledwidth, imagescaledheight))
archer2_img = pg.image.load(os.path.join(currentfiles,'archer_combat1.png')).convert_alpha()
archer2_img = pg.transform.scale(archer2_img, (imagescaledwidth, imagescaledheight))
archer3_img = pg.image.load(os.path.join(currentfiles,'archer_combat2.png')).convert_alpha()
archer3_img = pg.transform.scale(archer3_img, (imagescaledwidth, imagescaledheight))

archer_attacking_img = pg.image.load(os.path.join(currentfiles,'archer_attacking0.png')).convert_alpha()
archer_attacking_img = pg.transform.scale(archer_attacking_img, (imagescaledwidth, imagescaledheight))
archer_attacking2_img = pg.image.load(os.path.join(currentfiles,'archer_attacking1.png')).convert_alpha()
archer_attacking2_img = pg.transform.scale(archer_attacking2_img, (imagescaledwidth, imagescaledheight))
archer_attacking3_img = pg.image.load(os.path.join(currentfiles,'archer_attacking2.png')).convert_alpha()
archer_attacking3_img = pg.transform.scale(archer_attacking3_img, (imagescaledwidth, imagescaledheight))

archer = enemy.archer()
enemy.list.append(archer)
archer.vec = vec(43,20)
archer.health = 20
archer.immunities = []
archer.combat_animation = {1:archer_img,2:archer2_img,3:archer3_img}
archer.attack_animation = {1:archer_attacking_img,2:archer_attacking2_img,3:archer_attacking3_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
archer.clickaura = []
for aura in auras:
    archer.clickaura.append(vec(aura))
archer.attacks = {'piercing arrow':[5,{pierce:1},False,1,5],'blunt arrow':[5,{},False,1,1],'miss':[0,{},False,1,1]}
archer.stagger = 10

currentfiles = currentfileg + '/boulderine'

boulderine = enemy.boulderine()
enemy.list.append(boulderine)
boulderine.vec = vec(43,20)
boulderine.health = 35
boulderine.immunities = []
boulderine.combat_animation = {1:home_img,2:home_img,3:home_img}
boulderine.attack_animation = {1:magee_attacking_img,2:magee_attacking2_img,3:magee_attacking3_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
boulderine.clickaura = []
for aura in auras:
    boulderine.clickaura.append(vec(aura))
boulderine.attacks = {'weak smoke':[5,{weakness:1},False,1,2],'reposte':[0,{},True,0,2],'miss':[0,{},False,1,1]}
boulderine.stagger = 15

currentfiles = currentfileg + '/hardboulderine'

hardboulderine = enemy.hardboulderine()
enemy.list.append(hardboulderine)
hardboulderine.vec = vec(43,20)
hardboulderine.health = 40
hardboulderine.immunities = []
hardboulderine.combat_animation = {1:home_img,2:home_img,3:home_img}
hardboulderine.attack_animation = {1:magee_attacking_img,2:magee_attacking2_img,3:magee_attacking3_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
hardboulderine.clickaura = []
for aura in auras:
    hardboulderine.clickaura.append(vec(aura))
hardboulderine.attacks = {'hard smoke':[10,{},False,1,2],'reposte':[0,{},True,0,2],'miss':[0,{},False,1,1]}
hardboulderine.stagger = 20

currentfiles = currentfileg + '/rentoron'

rentoron_combat_img = pg.image.load(os.path.join(currentfiles,'rentoron_combat0.png')).convert_alpha()
rentoron_combat_img = pg.transform.scale(rentoron_combat_img, (imagescaledwidth, imagescaledheight))
rentoron_combat2_img = pg.image.load(os.path.join(currentfiles,'rentoron_combat1.png')).convert_alpha()
rentoron_combat2_img = pg.transform.scale(rentoron_combat2_img, (imagescaledwidth, imagescaledheight))
rentoron_combat3_img = pg.image.load(os.path.join(currentfiles,'rentoron_combat2.png')).convert_alpha()
rentoron_combat3_img = pg.transform.scale(rentoron_combat3_img, (imagescaledwidth, imagescaledheight))

rentoron_attacking_img = pg.image.load(os.path.join(currentfiles,'rentoron_attacking0.png')).convert_alpha()
rentoron_attacking_img = pg.transform.scale(rentoron_attacking_img, (imagescaledwidth, imagescaledheight))
rentoron_attacking2_img = pg.image.load(os.path.join(currentfiles,'rentoron_attacking1.png')).convert_alpha()
rentoron_attacking2_img = pg.transform.scale(rentoron_attacking2_img, (imagescaledwidth, imagescaledheight))
rentoron_attacking3_img = pg.image.load(os.path.join(currentfiles,'rentoron_attacking2.png')).convert_alpha()
rentoron_attacking3_img = pg.transform.scale(rentoron_attacking3_img, (imagescaledwidth, imagescaledheight))

rentoron = enemy.rentoron()
enemy.list.append(rentoron)
rentoron.vec = vec(43,20)
rentoron.health = 30
rentoron.immunities = []
rentoron.combat_animation = {1:rentoron_combat_img,2:rentoron_combat2_img,3:rentoron_combat3_img}
rentoron.attack_animation = {1:rentoron_attacking_img,2:rentoron_attacking2_img,3:rentoron_attacking3_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
rentoron.clickaura = []
for aura in auras:
    rentoron.clickaura.append(vec(aura))
rentoron.attacks = {'jump':[2,{charge:1},True,1,2],'smack':[5,{},False,1,4],'miss':[0,{},False,1,1]}
rentoron.stagger = 13

currentfiles = currentfileg + '/grosehund'

grosehund_combat_img = pg.image.load(os.path.join(currentfiles,'grosehund_combat0.png')).convert_alpha()
grosehund_combat_img = pg.transform.scale(grosehund_combat_img, (imagescaledwidth, imagescaledheight))
grosehund_combat2_img = pg.image.load(os.path.join(currentfiles,'grosehund_combat1.png')).convert_alpha()
grosehund_combat2_img = pg.transform.scale(grosehund_combat2_img, (imagescaledwidth, imagescaledheight))
grosehund_combat3_img = pg.image.load(os.path.join(currentfiles,'grosehund_combat2.png')).convert_alpha()
grosehund_combat3_img = pg.transform.scale(grosehund_combat3_img, (imagescaledwidth, imagescaledheight))

grosehund_attacking_img = pg.image.load(os.path.join(currentfiles,'grosehund_attacking0.png')).convert_alpha()
grosehund_attacking_img = pg.transform.scale(grosehund_attacking_img, (imagescaledwidth, imagescaledheight))
grosehund_attacking2_img = pg.image.load(os.path.join(currentfiles,'grosehund_attacking1.png')).convert_alpha()
grosehund_attacking2_img = pg.transform.scale(grosehund_attacking2_img, (imagescaledwidth, imagescaledheight))
grosehund_attacking3_img = pg.image.load(os.path.join(currentfiles,'grosehund_attacking2.png')).convert_alpha()
grosehund_attacking3_img = pg.transform.scale(grosehund_attacking3_img, (imagescaledwidth, imagescaledheight))

grosehound = enemy.grosehound()
enemy.list.append(grosehound)
grosehound.vec = vec(43,20)
grosehound.health = 15
grosehound.immunities = []
grosehound.combat_animation = {1:grosehund_combat_img,2:grosehund_combat2_img,3:grosehund_combat3_img}
grosehound.attack_animation = {1:grosehund_attacking_img,2:grosehund_attacking2_img,3:grosehund_attacking3_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
grosehound.clickaura = []
for aura in auras:
    grosehound.clickaura.append(vec(aura))
grosehound.attacks = {'scratch':[3,{},False,1,4],'deep bite':[3,{bleed:1},False,1,2],'miss':[0,{},False,1,1]}
grosehound.stagger = 5

currentfiles = currentfileg + '/barrier'

barrier = enemy.barrier()
enemy.list.append(archer)
barrier.vec = vec(43,20)
barrier.health = 77
barrier.immunities = [stun,bleed]
barrier.combat_animation = {1:home_img,2:home_img,3:home_img}
barrier.attack_animation = {1:magee_attacking_img,2:magee_attacking2_img,3:magee_attacking3_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
barrier.clickaura = []
for aura in auras:
    barrier.clickaura.append(vec(aura))
barrier.attacks = {'decimating energy':[5,{},False,5,5],'chaos energy':[5,{},False,1,1],'misalignment':[5,{},False,1,2]}
barrier.stagger = 10

currentfiles = currentfileg + '/dva'

dva = enemy.dva()
enemy.list.append(dva)
dva.vec = vec(43,20)
dva.health = 45
dva.immunities = [stun,bleed]
dva.combat_animation = {1:home_img,2:home_img,3:home_img}
dva.attack_animation = {1:magee_attacking_img,2:magee_attacking2_img,3:magee_attacking3_img}
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
dva.clickaura = []
for aura in auras:
    dva.clickaura.append(vec(aura))
dva.weapons = {'shard gun':{'direct fire':[2,{pierce:1},False,5,5],'spray fire':[1,{},False,5,1]},'shrapnel cannon':{'cannon fire':[5,{erosion:1},False,2,2],'cannon malfunction':[5,{},False,1,2]},'silicer cannon':{'sclicer fire':[5,{},False,1,2],'sclicer malfunction':[5,{},False,1,2]}}
dva.attacks = {'leg slash':[5,{bleed:1},False,1,5],'change weapon':[0,{},True,1,2],'malfunction':[0,{},False,1,3]}
dva.stagger = 20

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
kcross = pg.transform.scale(kcross, (128, abilityscaledheight))

class boss():
    class courptbattlemage():
        def __init__(self):
            self.vec = 0
        def decision(self,ll):
            attack = self.attacks
            chance = []
            attacks = []
            for y in attack:
                chance.append(attack[y][4])
                attacks.append(y)
            return attacks,chance
        def thunk(self,ll):
            if self.turncounter%3 == 0:
                for x in M.allies:
                    M.allies[x][1] - 5
                self.support([0])
            attacks,chance = self.decision(ll)
            self.attack(ll,attacks,chance)
        def damage(self,dup,damage,inin):
            M.enemy[self][dup][1] -= damage
        def attack(self,ll,attacks,chance):
            if self.attackone == 1:
                self.turncounter += 1
                M.enemy[self][ll][3] = []
                self.attackone += 1
            else:
                self.attackone = 1
            dead = []
            possible = []
            attacking = random.choices(attacks,chance)[0]
            if attacking == 'slash' or attacking == 'heavy swing':
                self.attack_animation = {1:cbm_attackingblunt_img,2:cbm_attackingblunt2_img,3:cbm_attackingblunt3_img}
            else:
                self.attack_animation = {1:cbm_attackingmagic_img,2:cbm_attackingmagic2_img,3:cbm_attackingmagic3_img}
            M.enemy[self][ll][3].append(attacking)
            damage = self.attacks[attacking]
            if damage[5]:
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
                target.damage(damage,self,ll)
        def support(self,target):
            if target[0] == 0:
                M.enemy[self][0][1] += M.enemy[self][0][1]*4/10
        def damage(self,dup,damage,inin):
            M.enemy[self][dup][1] -= damage
    class selloquie():
        def __init__(self):
            self.vec = 0
        def decision(self,ll):
            attack = self.attacks
            chance = []
            attacks = []
            for y in attack:
                chance.append(attack[y][4])
                attacks.append(y)
            return attacks,chance
        def thunk(self,ll):
            if self.turncounter%3 == 0:
                for x in M.allies:
                    M.allies[x][1] - 5
                self.support([0])
            attacks,chance = self.decision(ll)
            self.attack(ll,attacks,chance)
        def damage(self,dup,damage,inin):
            M.enemy[self][dup][1] -= damage
        def attack(self,ll,attacks,chance):
            if self.attackone == 1:
                self.turncounter += 1
                M.enemy[self][ll][3] = []
                self.attackone += 1
            else:
                self.attackone = 1
            dead = []
            possible = []
            attacking = random.choices(attacks,chance)[0]
            if attacking == 'slash' or attacking == 'heavy swing':
                self.attack_animation = {1:cbm_attackingblunt_img,2:cbm_attackingblunt2_img,3:cbm_attackingblunt3_img}
            else:
                self.attack_animation = {1:cbm_attackingmagic_img,2:cbm_attackingmagic2_img,3:cbm_attackingmagic3_img}
            M.enemy[self][ll][3].append(attacking)
            damage = self.attacks[attacking]
            if damage[5]:
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
                target.damage(damage,self,ll)
        def support(self,target):
            if target[0] == 0:
                M.enemy[self][0][1] += M.enemy[self][0][1]*4/10
        def damage(self,dup,damage,inin):
            M.enemy[self][dup][1] -= damage
            
boss = boss()
boss.bosses = []

currentfiles = currentfileg + '/cbm'

cbm_combat_img = pg.image.load(os.path.join(currentfiles,'cbm_combat0.png')).convert_alpha()
cbm_combat_img = pg.transform.scale(cbm_combat_img, (300, 300))
cbm_combat1_img = pg.image.load(os.path.join(currentfiles,'cbm_combat1.png')).convert_alpha()
cbm_combat1_img = pg.transform.scale(cbm_combat1_img, (300, 300))
cbm_combat2_img = pg.image.load(os.path.join(currentfiles,'cbm_combat2.png')).convert_alpha()
cbm_combat2_img = pg.transform.scale(cbm_combat2_img, (300, 300))

cbm_attackingmagic_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingmagic0.png')).convert_alpha()
cbm_attackingmagic_img = pg.transform.scale(cbm_attackingmagic_img, (300, 300))
cbm_attackingmagic2_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingmagic1.png')).convert_alpha()
cbm_attackingmagic2_img = pg.transform.scale(cbm_attackingmagic2_img, (300, 300))
cbm_attackingmagic3_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingmagic2.png')).convert_alpha()
cbm_attackingmagic3_img = pg.transform.scale(cbm_attackingmagic3_img, (300, 300))

cbm_attackingblunt_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingblunt0.png')).convert_alpha()
cbm_attackingblunt_img = pg.transform.scale(cbm_attackingblunt_img, (300, 300))
cbm_attackingblunt2_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingblunt1.png')).convert_alpha()
cbm_attackingblunt2_img = pg.transform.scale(cbm_attackingblunt2_img, (300, 300))
cbm_attackingblunt3_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingblunt2.png')).convert_alpha()
cbm_attackingblunt3_img = pg.transform.scale(cbm_attackingblunt3_img, (300, 300))

cbm = boss.courptbattlemage()
boss.bosses.append(cbm)
cbm.vec = vec(43,20)
cbm.health = 200
cbm.immunities = []
cbm.attackone = 1
cbm.combat_animation = {1:cbm_combat_img,2:cbm_combat1_img,3:cbm_combat2_img}
cbm.attack_animation = {1:magee_attacking_img,2:magee_attacking2_img,3:magee_attacking3_img}
auras = [(0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, -1), (1, -1), (2, -1), (2, -2), (1, -2), (0, -2), (0, -3), (1, -3), (2, -3)]
cbm.clickaura = []
cbm.turncounter = 0
for aura in auras:
    cbm.clickaura.append(vec(aura))
cbm.attacks = {'slash':[5,{},False,2,4,False],'heavy swing':[15,{},False,1,3,False],'charging fire':[1,{fire:3},False,1,3,True],'blinding light':[1,{stun:1},False,1,2,True],'miss':[0,{},False,1,1,True]}

cbm_combat_img = pg.image.load(os.path.join(currentfiles,'cbm_combat0.png')).convert_alpha()
cbm_combat_img = pg.transform.scale(cbm_combat_img, (300, 300))
cbm_combat1_img = pg.image.load(os.path.join(currentfiles,'cbm_combat1.png')).convert_alpha()
cbm_combat1_img = pg.transform.scale(cbm_combat1_img, (300, 300))
cbm_combat2_img = pg.image.load(os.path.join(currentfiles,'cbm_combat2.png')).convert_alpha()
cbm_combat2_img = pg.transform.scale(cbm_combat2_img, (300, 300))

cbm_attackingmagic_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingmagic0.png')).convert_alpha()
cbm_attackingmagic_img = pg.transform.scale(cbm_attackingmagic_img, (300, 300))
cbm_attackingmagic2_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingmagic1.png')).convert_alpha()
cbm_attackingmagic2_img = pg.transform.scale(cbm_attackingmagic2_img, (300, 300))
cbm_attackingmagic3_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingmagic2.png')).convert_alpha()
cbm_attackingmagic3_img = pg.transform.scale(cbm_attackingmagic3_img, (300, 300))

cbm_attackingblunt_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingblunt0.png')).convert_alpha()
cbm_attackingblunt_img = pg.transform.scale(cbm_attackingblunt_img, (300, 300))
cbm_attackingblunt2_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingblunt1.png')).convert_alpha()
cbm_attackingblunt2_img = pg.transform.scale(cbm_attackingblunt2_img, (300, 300))
cbm_attackingblunt3_img = pg.image.load(os.path.join(currentfiles,'cbm_attackingblunt2.png')).convert_alpha()
cbm_attackingblunt3_img = pg.transform.scale(cbm_attackingblunt3_img, (300, 300))

selloquie = boss.selloquie()
boss.bosses.append(selloquie)
selloquie.vec = vec(43,20)
selloquie.health = 200
selloquie.immunities = []
selloquie.attackone = 1
selloquie.combat_animation = {1:cbm_combat_img,2:cbm_combat1_img,3:cbm_combat2_img}
selloquie.attack_animation = {1:magee_attacking_img,2:magee_attacking2_img,3:magee_attacking3_img}
auras = [(0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0), (0, 0), (0, -1), (1, -1), (2, -1), (2, -2), (1, -2), (0, -2), (0, -3), (1, -3), (2, -3)]
selloquie.clickaura = []
selloquie.turncounter = 0
for aura in auras:
    cbm.clickaura.append(vec(aura))
selloquie.attacks = {'Water Slash':[5,{},False,2,4,False],'Ice Slash':[15,{},False,1,3,False],'Steam Jet':[1,{fire:3},False,1,3,True],'Flooding Rain':[1,{stun:1},False,1,2,True],'Mystical Typhoon':[0,{},True,1,1,False],'miss':[0,{},False,1,1,True]}





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
        current = pg.transform.scale(current,(300,abilityscaledheight))
        goal_center = (int(l.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(l.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
        screen.blit(current, current.get_rect(center=goal_center))
        draw_text(str(thing.lvl),50,BLACK,int(l.x * WIDTHTILESIZE)-70,int(l.y * HEIGHTTILESIZE))
        draw_text(str(thing.exp)+'/'+str(thing.needtolvl),30,BLACK,int(l.x * WIDTHTILESIZE)-90,int(l.y * HEIGHTTILESIZE+50))
    def applyeffects(self,target,dup,attack,ally):
        M.allies[ally][6] = False
        for x in ally.attacks[attack][0][effects]:
            if x == 0:
                break
            for y in x:
                if target in obstacles.allothem:
                    pass
                else:
                    if y not in target.immunities:
                        if needle == y:
                            if needle in M.enemy[target][dup][4]:
                                if M.enemy[target][dup][4][needle][0] != 3:
                                    M.enemy[target][dup][4][needle][0] += x[needle]
                                M.enemy[target][dup][4][needle][1] = 2
                            else:
                                M.enemy[target][dup][4].update({needle:[x[needle],2]})
                        else:
                            if y in M.enemy[target][dup][4]:
                                M.enemy[target][dup][4][y] += ally.attacks[attack][0][effects][x]
                            else:
                                M.enemy[target][dup][4].update({x:ally.attacks[attack][0][effects][x]})
    def damage(self,target,taken,initiated,ll):
        if taken == 'dodged':
            if target in M.damage:
                M.damage[target].append('dodged')
            else:
                M.damage.update({target:['dodged']})
        else:
            if "deflect" in M.allies[target][4]:
                target = M.allies[target][4]["deflect"]
                target.damage(taken,initiated,ll)
            else:
                x = taken[1]
                damage = int(taken[0])
                damage = ally.checkblessing('defending',target,damage,initiated,ll)
                if M.allies[target][3] > 0:
                    M.allies[target][3] -= damage
                    if pierce in M.allies[target][4]:
                        M.allies[target][3] -= damage
                    if M.allies[target][3] < 0:
                        M.allies[target][3] = 0
                else:
                    M.allies[target][1] -= damage
                    if pierce in M.allies[target][4]:
                        M.allies[target][1] -= damage
                    if bleed in x:
                        if bleed in M.allies[target][4]:
                            M.allies[target][4][bleed] += x[bleed]
                        else:
                            M.allies[target][4].update({bleed:x[bleed]})
                for y in x:
                    if pierce == y:
                        ll = random.choices([1,2],[80,20])[0]
                        if ll == 2:
                            M.allies[target][4].update({pierce:1})
                            if M.allies[target][3] == 0:
                                if bleed in M.allies[target][4]:
                                    M.allies[target][4][bleed] += 1
                                else:
                                    M.allies[target][4].update({bleed:1})
                    else:
                        if bleed != y:
                            if y in M.allies[target][4]:
                                M.allies[target][4][y] += x[y]
                            else:
                                M.allies[target][4].update({y:x[y]})
                
                
                if target in M.damage:
                    M.damage[target].append(damage)
                else:
                    M.damage.update({target:[damage]})
    def defaultheavyattack(self,target):
        where = M.allies[target][4][heavy][0]
        what = M.allies[target][4][heavy][1]
        del M.allies[target][4][heavy]
        M.allyspaces[M.unconversion[where.x,where.y]] = target
        if target.attacks[what][0][typeofattack][0] == sttatck: #straight attack
            #print(M.unconversion[M.allies[M.selectedchar][0].x,M.allies[M.selectedchar][0].y][1])
            ccc = []
            
            for x in collumcheck[M.unconversion[where.x,where.y][1]]:#check postions along column
                if M.enemyspaces[x.x,x.y] != 0:
                    ccc = [x]
                    break
        if len(ccc) != 0:
            pos = ccc[0]
            new = M.conversion[pos[0],pos[1]]
            der, xxer = M.areaselectenemy(new)
            target.attack((der,xxer),what)
            if target.attacks[what][0][typeofattack][1] != 0:
                for x in target.attacks[what][0][typeofattack][1]:
                    new = pos + x
                    new = (new.x,new.y)
                    if new in M.enemyspaces:
                        if M.enemyspaces[new] != 0:
                            new = M.conversion[new[0],new[1]]
                            der, xxer = M.areaselectenemy(new)
                            M.selectedchar.attack((der,xxer),what)
    def fixclick(self,target):
        pos = vec(18,31)
        for attack in target.attacks:
            pass
            if attack in target.abilities:
                if attack in target.unlockedabilites:
                    target.attacks[attack][2] = [pos + a for a in iconaura]
                    pos += vec(5,0)
            else:
                target.attacks[attack][2] = [pos + a for a in iconaura]
                pos += vec(5,0)
    def checkattack(self,damage,target):
        if weakness in M.allies[target][4]:
            damage /= 2
        return damage
    def draw_skilltree(self,target):
        ally.profile(target.combat_animation,target)
        for z in target.abilities:
            pos = target.abilities[z][1]
            x = int(pos.x*WIDTHTILESIZE-230)
            y = int(pos.y*HEIGHTTILESIZE-35)
            rect = pg.Rect(x, y, 50, 50)
            if z not in target.unlockedabilites:
                pg.draw.rect(screen,GREEN,target.abilities[z][0])
            else:
                pg.draw.rect(screen,BLACK,target.abilities[z][0])
    def init_skilltree(self,target):
        for z in target.abilities:
            pos = target.abilities[z][1]
            x = int(pos.x*WIDTHTILESIZE-230)
            y = int(pos.y*HEIGHTTILESIZE-35)
            rect = pg.Rect(x, y, 50, 50)
            target.abilities[z][0] = rect
    def checkblessing(self,when,target,damage,aimed,dup):
        if target.blessing != -1:
            damage = B.checkblessing(B.inventory[target.blessing][1],when,damage,target,aimed,dup)
        return damage
    class heplane():
        def __init__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            blooddamage = int(M.allies[self][1])/int(self.health)+1
            if attack == self.attack1:
                M.allies[self][1] -= 10
            if self.attack3 in self.unlockedabilites:
                self.healdam += int((blooddamage * self.attacks[attack][0]['damage'])/2)
            damage = blooddamage * self.attacks[attack][0]['damage'] *(1+self.inc)
            damage = ally.checkattack(damage,self)
            self.passive()
            target.damage(dup,damage,self)
            ally.applyeffects(target,dup,attack,self)
        def heavythunk(self):
            ally.defaultheavyattack(self)
        def support(self,target):
            if M.selectedattack == self.attack3:
                if self.attack3 in self.unlockedabilites:
                    self.passive()
                    M.allies[self][1] += self.healdam
                    self.healdam = 0
                    if M.allies[self][1] > 50:
                        M.allies[self][1] = 50
                else:
                    M.actions.remove(self)
            if M.selectedattack == self.attack4:
                if self.attack4 in self.unlockedabilites:
                    self.passive()
                    M.allies[self][3] += self.attacks[self.attack4][0][dealtdamage]
                    M.allies[self][1] -= 10
                    if M.allies[self][3] > 50:
                        M.allies[self][3] = 50
                else:
                    M.actions.remove(self)
        def passive(self):
            damage = ally.checkblessing('passive',self,0,0,0)
        def passive_endturn(self):
            damage = ally.checkblessing('endpassive',self,0,0,0)
            M.allies[self][1] += 10
            if M.allies[self][1] > 50:
                M.allies[self][1] = 50
        def damage(self,taken,initiated,ll):
            ally.damage(self,taken,initiated,ll)
        def draw_icons(self):
            pos = vec(18,31)
            for attack in self.attacks:
                
                if self.attack3 not in self.unlockedabilites:
                    if attack == self.attack3:
                        continue
                if self.attack4 not in self.unlockedabilites:
                    if attack == self.attack4:
                        continue
                icon = self.attacks[attack][1]
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE-49), int(pos.y*HEIGHTTILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                if attack == self.attack1 or attack == self.attack2:
                    text = str(round(int((M.allies[self][1]/self.health+1) * self.attacks[attack][0][dealtdamage])))
                    draw_text(text, 20, RED, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)
                if attack == self.attack3:
                    text = str(self.healdam)
                    draw_text(text, 20, GREEN, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)
                if attack == self.attack4:
                    text = str(self.attacks[attack][0][dealtdamage])
                    draw_text(text, 20, BLUE, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)
                pos += vec(5,0)
        def draw_attack(self):
            pass
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
            damage = self.attacks[self.attack1][0][dealtdamage]
            damage = ally.checkattack(damage,self)
            target.damage(dup,damage,self)
            ally.applyeffects(target,dup,attack,self)
            self.passive(attack)
        def support(self,target):
            attack = M.selectedattack
            if attack == self.attack2:
                M.allies[target][3] += self.attacks[self.attack2][0][dealtdamage]
                if M.allies[target][3] > target.health:
                    M.allies[target][3] = target.health
            elif attack == self.attack3:
                M.allies[target][1] += self.attacks[self.attack3][0][dealtdamage]
                if M.allies[target][1] > target.health:
                    M.allies[target][1] = target.health
                if stun in M.allies[target][4]:
                    M.allies[target][4] = {stun:M.allies[target][4][stun]}
                else:
                    M.allies[target][4] = {}
            self.passive(attack)
        def passive(self,used):
            damage = ally.checkblessing('passive',self,0,0,0)
            for x in self.attacks:
                if x == used:
                    self.attacks[x][0]['damage'] += (1 + self.inc)
                else:
                    self.attacks[x][0]['damage'] += (2 + self.inc)
                if x == self.attack1:
                    if self.attacks[x][0]['damage'] >= self.stuncap:
                        self.attacks[self.attack1][0][effects].update({stun:1}) 
                    if self.attacks[x][0]['damage'] < self.stuncap:
                        if stun in self.attacks[self.attack1][0][effects]:
                            del self.attacks[self.attack1][0][effects][stun]
                if self.attacks[x][0]['damage'] > 10:
                    self.attacks[x][0]['damage'] = 2
        def passive_endturn(self):
            damage = ally.checkblessing('endpassive',self,0,0,0)
        def damage(self,taken,initiated,ll):
            ally.damage(self,taken,initiated,ll)
        def draw_icons(self):
            cur = cri_stunicon_img
            goal_center = (int(M.allies[self][0].x * WIDTHTILESIZE + WIDTHTILESIZE / 2 + 80), int(M.allies[self][0].y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2 - 50))
            if self.attacks[self.attack1][0][dealtdamage] < self.stuncap:
                cur = cur.copy( )
                cur.fill((105, 105, 105, 255),special_flags=pg.BLEND_RGB_MULT)            
            screen.blit(cur, cur.get_rect(center=goal_center))

            pos = vec(18,31)
            for attack in self.attacks:
                icon = self.attacks[attack][1]
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE-49), int(pos.y*HEIGHTTILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                text = str(self.attacks[attack][0][dealtdamage])
                if attack == self.attack1:
                    draw_text(text, 20, RED, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)
                if attack == self.attack2:
                    draw_text(text, 20, BLUE, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)
                if attack == self.attack3:
                    draw_text(text, 20, GREEN, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)
                pos += vec(5,0)
        def draw_attack(self):
            pass
        def skill(self,cur):
            if cur == 'stun':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.stuncap = 6
            if cur == 'increase':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.inc = 1
            ally.fixclick(self)
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
            if attack == self.attack1:
                damage = (self.attacks[attack][0]+self.inc)*self.momentum
                self.momentum = 0
            else:
                damage = self.attacks[attack][0]+self.inc
            damage = ally.checkattack(damage,self)
            target.damage(dup,damage,self)
            if self.attacktwice == True:
                target.damage(dup,damage,self)
                self.attacktwice = False
            ally.applyeffects(target,dup,attack,self)
            self.passive(attack)
        def support(self,target):
            if 'acceleration' in self.unlockedabilites:
                if target == Hap:
                    if  self.momentum > 0:
                        self.attacktwice = True
                        self.momentum -= 1
            else:
                M.actions.remove(Hap)
        def passive(self,used):
            if used != self.attack1:
                damage = ally.checkblessing('passive',self,0,0,0)
                self.momentum += 1
                if self.momentum >=3:
                    self.momentum = 3
                if self.momentum == 3:
                    self.attacks[self.attack1][1][0].update({bleed:2}) 
                else:
                    if bleed in self.attacks[self.attack1][1][0]:
                        del self.attacks[self.attack1][1][0][bleed]
        def passive_endturn(self):
            damage = ally.checkblessing('endpassive',self,0,0,0)
            if bleed in self.attacks[self.attack1][1][0]:
                del self.attacks[self.attack1][1][0][bleed]
            self.momentum = 0
        def damage(self,taken,initiated,ll):
            self.passive(0)
            hit = random.choices([True,False],[4,self.momentum*self.dodgec])[0]
            if hit:
                ally.damage(self,taken,initiated,ll)
            else:
                ally.damage(self,"dodged",initiated,ll)
        def draw_icons(self):
            rect = pg.Rect(int(M.allies[self][0].x*WIDTHTILESIZE+80), int(M.allies[self][0].y*HEIGHTTILESIZE-50), 20, 135)
            pg.draw.rect(screen,MOMENTUMCOLOR,rect)
            for y in range(0,self.momentum):
                rect = pg.Rect(int(M.allies[self][0].x*WIDTHTILESIZE+80), int(M.allies[self][0].y*HEIGHTTILESIZE+50-50*y), 20, 45)
                pg.draw.rect(screen,WHITE,rect)

            pos = vec(18,31)
            for attack in self.attacks:
                if self.attack3 not in self.unlockedabilites:
                    if attack == self.attack3:
                        continue
                icon = self.attacks[attack][4]
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE-49), int(pos.y*HEIGHTTILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                if attack != self.attack3:
                    text = str(self.attacks[attack][0])
                    if attack == self.attack1:
                        text = str((self.attacks[attack][0]+self.inc)*self.momentum)
                    draw_text(text, 20, RED, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)

                pos += vec(5,0)
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
        def __init__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            if self.attacks[attack][0][1] != 0:
                damage = (self.attacks[attack][0][0]+self.inc)*int(random.choices([1,2],[int(100-self.chance),int(0+self.chance)])[0])
                
                self.passive(attack)
                if attack == self.attack4:
                    for x in M.enemy:
                        lel = 0
                        for y in M.enemy[x]:
                            ally.applyeffects(x,lel,attack,self)
                            M.enemy[x][lel][1] -= self.attacks[self.attack4][0][0]
                            lel += 1
                else:
                    ally.applyeffects(target,dup,attack,self)
                target.damage(dup,damage,self)
            else:
                M.actions.remove(self)

        def support(self,target):
            if self.acts != 0:
                for x in range(self.acts):
                    if self.attack4 in self.unlockedabilites:
                        cur = random.choices([self.attack1,self.attack2,self.attack4],[35,55,10])[0]
                    else:
                        cur = random.choices([self.attack1,self.attack2],[30,70])[0]
                    self.attacks[cur][0][1] += 1
                self.acts = 0
            else:
                M.actions.remove(self)
        def passive(self,used):
            damage = ally.checkblessing('passive',self,0,0,0)
            self.attacks[used][0][1] -= 1
            self.acts += 1
        def passive_endturn(self):
            damage = ally.checkblessing('endpassive',self,0,0,0)
            for x in range(self.acts):
                if self.attack4 in self.unlockedabilites:
                    cur = random.choices([self.attack1,self.attack2,self.attack4],[35,55,10])[0]
                else:
                    cur = random.choices([self.attack1,self.attack2],[30,70])[0]
                self.attacks[cur][0][1] += 1
            self.acts = 0
        def damage(self,taken,initiated,ll):
            ally.damage(self,taken,initiated,ll)
        def draw_icons(self):
            pos = vec(18,31)
            for attack in self.attacks:
                if self.attack4 not in self.unlockedabilites:
                    if attack == self.attack4:
                        continue
                icon = self.attacks[attack][4]
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE-49), int(pos.y*HEIGHTTILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                text = str(self.attacks[attack][0][0]+self.inc)
                if attack != self.attack3:
                    draw_text(text, 20, RED, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)
                    text = str(self.attacks[attack][0][1])
                    draw_text(text, 50, VIOLET, pos.x*WIDTHTILESIZE + 40, pos.y*HEIGHTTILESIZE - 50)
                else:
                    text = str(self.acts)
                    draw_text(text, 50, VIOLET, pos.x*WIDTHTILESIZE + 40, pos.y*HEIGHTTILESIZE - 50)

                pos += vec(5,0)
                
        def draw_attack(self):
            pass
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
        def __init__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            if self.block:
                self.block = False
                if self.transformed:
                    M.allies[self][3] -= self.saveblock 
                    self.combat_animation = {1:nover_transformed_img,2:nover_transformed_img,3:nover_transformed_img}
                else:
                    self.combat_animation = {1:nover_combat_img,2:nover_combat2_img,3:nover_combat3_img}
            
            if self.mimicing:
                self.savemimic.attack(target,attack)
                self.passive(attack)
            else:
                target,dup = target
                damage = 0
                if self.transformed:
                    for x in M.allies:
                        M.allies[x][1] += 5
                    M.allies[self][1] -= 5 * (3 - self.acts)
                    damage = self.attacks[attack][0] * 3
                    if bleed in M.enemy[target][dup][4]:
                        damage *= 1.5
                else:
                    damage = self.attacks[attack][0]
                ally.applyeffects(target,dup,attack,self)
                damage = ally.checkattack(damage,self)
                target.damage(dup,damage,self)
                self.passive(attack)
        def support(self,target):
            if self.block:
                self.block = False
                if self.transformed:
                    M.allies[self][3] -= self.saveblock 
                    self.combat_animation = {1:nover_transformed_img,2:nover_transformed_img,3:nover_transformed_img}
                else:
                    self.combat_animation = {1:nover_combat_img,2:nover_combat2_img,3:nover_combat3_img}
            if self.mimicing:
                self.savemimic.support(target)
                self.passive(0)
            else:
                if M.selectedattack == self.attack4:
                    if self.actsmimic == 0 and target != self:
                        self.actsmimic = 2
                        self.mimicing = True
                        self.attacks = target.attacks
                        self.savemimic = target
                        self.combat_animation = {1:nover_mimic_img,2:nover_mimic2_img,3:nover_mimic3_img}
                        if target in M.allies:
                            self.allymimic = True
                        else:
                            self.allymimic = False
                    else:
                        M.actions.remove(self)
                elif M.selectedattack == self.attack3:
                    if self.acts == 0:
                        if self.transformed:
                            self.acts = 2
                            self.combat_animation = {1:nover_combat_img,2:nover_combat2_img,3:nover_combat3_img}
                            self.transformed = False
                        else:
                            self.combat_animation = {1:nover_transformed_img,2:nover_transformed_img,3:nover_transformed_img}
                            self.transformed = True
                            self.acts = 2
                    else:
                        M.actions.remove(self)
                elif M.selectedattack == self.attack1:
                    self.passive(0)
                    if self.transformed:
                        M.allies[self][3] += self.attacks[self.attack1][0] + 10
                        self.saveblock = self.attacks[self.attack1][0] + 10
                        self.block = True

                    else:
                        M.allies[self][3] += self.attacks[self.attack1][0]
                        self.block = True
                        self.combat_animation = {1:nover_block_img,2:nover_block_img,3:nover_block_img}

        def passive(self,used):     
            damage = ally.checkblessing('passive',self,0,0,0)
            self.acts -= 1
            if self.acts < 0:
                self.acts = 0 
            self.actsmimic -= 1
            if self.actsmimic < 0:
                self.actsmimic = 0 
                if self.mimicing:
                    self.actsmimic = 3
                    self.combat_animation = {1:nover_combat_img,2:nover_combat2_img,3:nover_combat3_img}
                    self.attacks = self.saveattacks
                    self.mimicing = False
        def passive_endturn(self):
            damage = ally.checkblessing('endpassive',self,0,0,0)
        def damage(self,taken,initiated,ll):
            if self.block:
                taken[0] = int(taken[0]/2)
                self.saveblock -= taken[0]
            ally.damage(self,taken,initiated,ll)
        def draw_icons(self):
            if self.mimicing:
                if self.allymimic:
                    self.savemimic.draw_icons()
            else:
                pos = vec(18,31)
                for attack in self.attacks:
                    if self.attack4 not in self.unlockedabilites:
                        if attack == self.attack4:
                            continue
                    icon = self.attacks[attack][4]
                    rect = pg.Rect(int(pos.x*WIDTHTILESIZE-49), int(pos.y*HEIGHTTILESIZE-50), 128, 150)
                    pg.draw.rect(screen,BLACK,rect)
                    goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                    screen.blit(icon, icon.get_rect(center=goal_center))
                    if self.transformed:
                        text = str(self.attacks[attack][0]*3)
                    else:
                        text = str(self.attacks[attack][0]+self.inc)
                    if attack == self.attack1:
                        draw_text(text, 20, BLUE, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)
                    elif attack == self.attack2:
                        draw_text(text, 20, RED, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)   
                    elif attack == self.attack3:
                        text = str(self.acts)
                        draw_text(text, 50, VIOLET, pos.x*WIDTHTILESIZE + 40, pos.y*HEIGHTTILESIZE - 50) 
                    elif attack == self.attack4:
                        text = str(self.actsmimic)
                        draw_text(text, 50, VIOLET, pos.x*WIDTHTILESIZE + 40, pos.y*HEIGHTTILESIZE - 50) 
                    pos += vec(5,0)
        def draw_attack(self):
            pass
        
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
    class fairum():
        def __init__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            damage = 0
            if self.plates > 2:
                if attack == self.attack1:
                    M.enemy[target][dup][1] += 5
                    damage = 5
                    if bigmpos.x != 9:
                        M.enemyspaces[bigmpos.x,bigmpos.y] = 0
                        M.enemyspaces[bigmpos.x+1,bigmpos.y] = target
                        M.enemy[target][dup][0] = vec(M.conversion[bigmpos.x+1,bigmpos.y])
                if attack == self.attack4:
                    damage += random.randint(3,self.attacks[self.attack4][0][0])
                target.damage(dup,damage,self)
                ally.applyeffects(target,dup,attack,self)
                self.passive(attack)
            else:
                M.actions.remove(self)
        def support(self,target):
            if M.selectedattack == self.attack2:
                self.plates += 6
                self.passive(self.attack2)
            elif M.selectedattack == self.attack3:
                if self.plates != 0 and target != self:
                    M.allies[target][4].update({'deflect':self})
                    self.passive(self.attack3)
                else:
                    M.actions.remove(self)
            else:
                M.actions.remove(self)
        def passive(self,used):
            damage = ally.checkblessing('passive',self,0,0,0)
            self.plates -= self.attacks[used][0][1]
            self.plates += 2
            if self.plates > self.plateslimit:
                self.plates = self.plateslimit
        def passive_endturn(self):
            damage = ally.checkblessing('endpassive',self,0,0,0)
            self.plates += 10
            if self.plates > self.plateslimit:
                self.plates = self.plateslimit
        def damage(self,taken,initiated,ll):
            newtaken = list(taken)
            newtaken[0] -= self.plates
            if newtaken[0] <= 0:
                newtaken[0] = 0
            self.plates -= 1
            ally.damage(self,newtaken,initiated,ll)
        def draw_icons(self):
            xdif = 0
            ydif = 0
            for y in range(0,self.plates):
                ydif += 1
                if y%5 == 0:
                    xdif += 1
                    ydif = 0
                rect = pg.Rect(int(M.allies[self][0].x*WIDTHTILESIZE+80+(20*xdif)), int(M.allies[self][0].y*HEIGHTTILESIZE+30-30*ydif), 10, 20)
                pg.draw.rect(screen,WHITE,rect)
            pos = vec(18,31)
            for attack in self.attacks:
                if self.attack3 not in self.unlockedabilites:
                    if attack == self.attack3:
                        continue
                if self.attack4 not in self.unlockedabilites:
                    if attack == self.attack4:
                        continue
                icon = self.attacks[attack][4]
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE-49), int(pos.y*HEIGHTTILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                text = str(self.attacks[attack][0][0])
                if attack != self.attack1 or attack != self.attack4:
                    draw_text(text, 20, RED, pos.x*WIDTHTILESIZE, pos.y*HEIGHTTILESIZE + 75)
                pos += vec(5,0)
        def draw_attack(self):
            pass
        def skill(self,cur):
            if cur == self.attack4:
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            if cur == 'increase':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.plateslimit = 15
            if cur == self.attack3:
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            ally.fixclick(self)
        def checklevel(self):
            if self.exp >= self.needtolvl:
                self.lvl += 1
                self.exp -= self.needtolvl
                self.needtolvl *= 2
    class zither():
        def __init__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            damage = 0
            self.passive(0)
            if attack == self.attack1:
                damage = self.attacks[self.attack1][0]
            if attack == self.attack2:
                if needle in M.enemy[target][dup][4]:
                    del M.enemy[target][dup][4][needle]
                    damage = self.attacks[self.attack2][0]
            if needle in M.enemy[target][dup][4]:
                stacks = M.enemy[target][dup][4][needle][0]
                damage *= -0.25*stacks*stacks+1.75*stacks-0.5
            ally.applyeffects(target,dup,attack,self)
            
            target.damage(dup,damage,self)
            self.passive(attack)
            #M.actions.remove(self)
        def support(self,target):
            self.passive(0)
            if M.selectedattack == self.attack3:
                self.agro = 10
            if M.selectedattack == self.attack4:
                stacks = 0
                for ww in M.enemy:
                    lel = 0
                    for x in M.enemy[ww]:
                        if needle in x[4]:
                            if needle in M.enemy[ww][lel][4]:
                                stacks += M.enemy[ww][lel][4][needle][0]
                                del M.enemy[ww][lel][4][needle]
                        lel += 1
                stacks *= 5
                M.allies[self][3] += stacks
        def passive(self,used):
            damage = ally.checkblessing('passive',self,0,0,0)
            if self.agro >= 1:
                self.agro = 1
        def passive_endturn(self):
            damage = ally.checkblessing('endpassive',self,0,0,0)
        def damage(self,taken,initiated,ll):
            if needle in M.enemy[initiated][ll][4]:
                stacks = M.enemy[initiated][ll][4][needle][0]
                chance = 100/stacks
                otherchance = 100-chance
                hit = random.choices([True,False],[otherchance,chance])[0]
            else:
                chance = 0.3*self.dodgeskill
                otherchance = 100-chance
                hit = random.choices([True,False],[otherchance,chance])[0]
            if hit:
                ally.damage(self,taken,initiated,ll)
            else:
                ally.damage(self,"dodged",initiated,ll)
        def draw_icons(self):
            pos = vec(18,31)
            for attack in self.attacks:
                if self.attack3 not in self.unlockedabilites:
                    if attack == self.attack3:
                        continue
                if self.attack4 not in self.unlockedabilites:
                    if attack == self.attack4:
                        continue
                icon = self.attacks[attack][4]
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE-49), int(pos.y*HEIGHTTILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                text = str(self.attacks[attack][0])
                if attack != self.attack3:
                    draw_text(text, 20, RED, pos.x*WIDTHTILESIZE, pos.y*WIDTHTILESIZE + 75)
                pos += vec(5,0)
        def draw_attack(self):
            pass
        def skill(self,cur):
            if cur == self.attack4:
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            if cur == 'annihilation':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.attacks[self.attack2][0] += 2
            if cur == self.attack3:
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            if cur == 'light feet':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.dodgeskill += 1
            ally.fixclick(self)
        def checklevel(self):
            if self.exp >= self.needtolvl:
                self.lvl += 1
                self.exp -= self.needtolvl
                self.needtolvl *= 2
    class maxine():
        def __init__(self):
            self.attack1 = 0
        def attack(self,target,attack):
            target,dup = target
            damage = 0
            self.passive(0)
            if attack == self.attack1:
                damage = self.attacks[self.attack1][0]
            if attack == self.attack2:
                if needle in M.enemy[target][dup][4]:
                    del M.enemy[target][dup][4][needle]
                    damage = self.attacks[self.attack2][0]
            if needle in M.enemy[target][dup][4]:
                stacks = M.enemy[target][dup][4][needle][0]
                damage *= -0.25*stacks*stacks+1.75*stacks-0.5
            ally.applyeffects(target,dup,attack,self)
            
            target.damage(dup,damage,self)
            self.passive(attack)
            #M.actions.remove(self)
        def support(self,target):
            self.passive(0)
            if M.selectedattack == self.attack3:
                self.agro = 10
            if M.selectedattack == self.attack4:
                stacks = 0
                for ww in M.enemy:
                    lel = 0
                    for x in M.enemy[ww]:
                        if needle in x[4]:
                            if needle in M.enemy[ww][lel][4]:
                                stacks += M.enemy[ww][lel][4][needle][0]
                                del M.enemy[ww][lel][4][needle]
                        lel += 1
                stacks *= 5
                M.allies[self][3] += stacks
        def passive(self,used):
            damage = ally.checkblessing('passive',self,0,0,0)
            if self.agro >= 1:
                self.agro = 1
        def passive_endturn(self):
            damage = ally.checkblessing('endpassive',self,0,0,0)
        def damage(self,taken,initiated,ll):
            if needle in M.enemy[initiated][ll][4]:
                stacks = M.enemy[initiated][ll][4][needle][0]
                chance = 100/stacks
                otherchance = 100-chance
                hit = random.choices([True,False],[otherchance,chance])[0]
            else:
                chance = 0.3*self.dodgeskill
                otherchance = 100-chance
                hit = random.choices([True,False],[otherchance,chance])[0]
            if hit:
                ally.damage(self,taken,initiated,ll)
            else:
                ally.damage(self,"dodged",initiated,ll)
        def draw_icons(self):
            pos = vec(18,31)
            for attack in self.attacks:
                if self.attack3 not in self.unlockedabilites:
                    if attack == self.attack3:
                        continue
                if self.attack4 not in self.unlockedabilites:
                    if attack == self.attack4:
                        continue
                icon = self.attacks[attack][4]
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE-49), int(pos.y*HEIGHTTILESIZE-50), 128, 150)
                pg.draw.rect(screen,BLACK,rect)
                goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                screen.blit(icon, icon.get_rect(center=goal_center))
                text = str(self.attacks[attack][0])
                if attack != self.attack3:
                    draw_text(text, 20, RED, pos.x*WIDTHTILESIZE, pos.y*WIDTHTILESIZE + 75)
                pos += vec(5,0)
        def draw_attack(self):
            pass
        def skill(self,cur):
            if cur == self.attack4:
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            if cur == 'annihilation':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.attacks[self.attack2][0] += 2
            if cur == self.attack3:
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
            if cur == 'light feet':
                self.abilities[cur][2] = False
                self.unlockedabilites.append(cur)
                self.dodgeskill += 1
            ally.fixclick(self)
        def checklevel(self):
            if self.exp >= self.needtolvl:
                self.lvl += 1
                self.exp -= self.needtolvl
                self.needtolvl *= 2
                

currentfileg =  filename +'/allies'                
                
sttatck = 'sttatck'
anywhere = 'anywhere'
dealtdamage = 'damage'
effects = 'effects'
support = 'support'
hits = 'hits'
typeofattack = 'typofattck'
whereattack = 'where can attack'
heavy = 'is the attack heavy'

ally = ally()
                    
iconaura = [(2, 2), (2, 1), (2, 0), (2, -1), (2, -2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1), (0, 0), (0, -1), (0, -2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (-2, 2), (-2, 1), (-2, 0), (-2, -1), (-2, -2)]            

currentfiles = currentfileg + '/zither'

maxine = ally.maxine()
maxine_combat_img = pg.image.load(os.path.join(currentfiles,'zither_combat0.png')).convert_alpha()
maxine_combat_img = pg.transform.scale(maxine_combat_img, (imagescaledwidth, imagescaledheight))
maxine_combat2_img = pg.image.load(os.path.join(currentfiles,'zither_combat1.png')).convert_alpha()
maxine_combat2_img = pg.transform.scale(maxine_combat2_img, (imagescaledwidth, imagescaledheight))
maxine_combat3_img = pg.image.load(os.path.join(currentfiles,'zither_combat2.png')).convert_alpha()
maxine_combat3_img = pg.transform.scale(maxine_combat3_img, (imagescaledwidth, imagescaledheight))
maxine_ability1_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
maxine_ability1_img = pg.transform.scale(maxine_ability1_img, (128, abilityscaledheight))
maxine_ability2_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
maxine_ability2_img = pg.transform.scale(maxine_ability2_img, (128, abilityscaledheight))
maxine_ability3_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
maxine_ability3_img = pg.transform.scale(maxine_ability3_img, (128, abilityscaledheight))
maxine_ability4_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
maxine_ability4_img = pg.transform.scale(maxine_ability4_img, (128, abilityscaledheight))
maxine.attack1 = 'naradait'
maxine.attack2 = 'annihilate'
maxine.attack3 = 'fanning'
maxine.attack4 = 'rein it in'
maxine.vec = vec(20,15)
maxine.health = 50
maxine.shield = 0
maxine.agro = 1
maxine.movement = 3
maxine.immunities = []
maxine.abilities = {maxine.attack3:[0,vec(47,17),'Intemidate the enemies making it more likely to attack zither'],maxine.attack4:[0,vec(47,20),'zither will retract her needles and convert them to shield'],'annihilation':[0,vec(47,23),'Annihilate will deal more damage'],'light feet':[0,vec(47,26),"Zither can dodge attacks even when enemies don't have needles"]}
maxine.unlockedabilites = []
maxine.blessing = -1
maxine.dodgeskill = 0
maxine.exp = 0
maxine.lvl = 0
maxine.needtolvl = 10
maxine.combat_animation = {1:maxine_combat_img,2:maxine_combat2_img,3:maxine_combat3_img}
maxine.attacks = {maxine.attack1:[10,[{needle:1}],False,1,maxine_ability1_img,[vec(18,31) + a for a in iconaura],[sttatck,0],secondrow+firstrow],maxine.attack2:[14,[0],False,1,maxine_ability2_img,[vec(23,31) + a for a in iconaura],[sttatck,0],firstrow],maxine.attack3:[0,[0],True,1,maxine_ability3_img,[vec(28,31)+a for a in iconaura],[vec(0,0),0],False],maxine.attack4:[0,[0],True,1,maxine_ability4_img,[vec(33,31) + a for a in iconaura],[vec(0,0),0],False]}
maxine.clickaura = []
aura = [(1, 3), (0, 3), (-1, 3), (-1, 2), (0, 2), (1, 2), (1, 1), (0, 1), (-1, 1), (-1, 0), (0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, -2), (0, -2), (1, -2), (1, -3), (0, -3), (-1, -3)]
for x in aura:
    maxine.clickaura.append(vec(x))

currentfiles = currentfileg + '/zither'

zither = ally.zither()
zither_combat_img = pg.image.load(os.path.join(currentfiles,'zither_combat0.png')).convert_alpha()
zither_combat_img = pg.transform.scale(zither_combat_img, (imagescaledwidth, imagescaledheight))
zither_combat2_img = pg.image.load(os.path.join(currentfiles,'zither_combat1.png')).convert_alpha()
zither_combat2_img = pg.transform.scale(zither_combat2_img, (imagescaledwidth, imagescaledheight))
zither_combat3_img = pg.image.load(os.path.join(currentfiles,'zither_combat2.png')).convert_alpha()
zither_combat3_img = pg.transform.scale(zither_combat3_img, (imagescaledwidth, imagescaledheight))
zither_ability1_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
zither_ability1_img = pg.transform.scale(zither_ability1_img, (128, abilityscaledheight))
zither_ability2_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
zither_ability2_img = pg.transform.scale(zither_ability2_img, (128, abilityscaledheight))
zither_ability3_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
zither_ability3_img = pg.transform.scale(zither_ability3_img, (128, abilityscaledheight))
zither_ability4_img = pg.image.load(os.path.join(filename,'cross-1.png.png'))
zither_ability4_img = pg.transform.scale(zither_ability4_img, (128, abilityscaledheight))
zither.attack1 = 'contort'
zither.attack2 = 'annihilate'
zither.attack3 = 'fanning'
zither.attack4 = 'rein it in'
zither.vec = vec(20,15)
zither.health = 50
zither.shield = 0
zither.agro = 1
zither.movement = 3
zither.immunities = []
zither.abilities = {zither.attack3:[0,vec(47,17),'Intemidate the enemies making it more likely to attack zither'],zither.attack4:[0,vec(47,20),'zither will retract her needles and convert them to shield'],'annihilation':[0,vec(47,23),'Annihilate will deal more damage'],'light feet':[0,vec(47,26),"Zither can dodge attacks even when enemies don't have needles"]}
zither.unlockedabilites = []
zither.blessing = -1
zither.dodgeskill = 0
zither.exp = 0
zither.lvl = 0
zither.needtolvl = 10
zither.combat_animation = {1:zither_combat_img,2:zither_combat2_img,3:zither_combat3_img}
zither.attacks = {zither.attack1:[10,[{needle:1}],False,1,zither_ability1_img,[vec(18,31) + a for a in iconaura],[sttatck,0],secondrow+firstrow],zither.attack2:[14,[0],False,1,zither_ability2_img,[vec(23,31) + a for a in iconaura],[sttatck,0],firstrow],zither.attack3:[0,[0],True,1,zither_ability3_img,[vec(28,31)+a for a in iconaura],[vec(0,0),0],False],zither.attack4:[0,[0],True,1,zither_ability4_img,[vec(33,31) + a for a in iconaura],[vec(0,0),0],False]}
zither.clickaura = []
aura = [(1, 3), (0, 3), (-1, 3), (-1, 2), (0, 2), (1, 2), (1, 1), (0, 1), (-1, 1), (-1, 0), (0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, -2), (0, -2), (1, -2), (1, -3), (0, -3), (-1, -3)]
for x in aura:
    zither.clickaura.append(vec(x))

currentfiles = currentfileg + '/fairum'

fairum = ally.fairum()
fairum_combat_img = pg.image.load(os.path.join(currentfiles,"fairum_combat0.png")).convert_alpha()
fairum_combat_img = pg.transform.scale(fairum_combat_img, (imagescaledwidth, imagescaledheight))
fairum_combat2_img = pg.image.load(os.path.join(currentfiles,"fairum_combat1.png")).convert_alpha()
fairum_combat2_img = pg.transform.scale(fairum_combat2_img, (imagescaledwidth, imagescaledheight))
fairum_combat3_img = pg.image.load(os.path.join(currentfiles,"fairum_combat2.png")).convert_alpha()
fairum_combat3_img = pg.transform.scale(fairum_combat3_img, (imagescaledwidth, imagescaledheight))
fairum_ability1_img = pg.image.load(os.path.join(currentfiles,'fairum_abilites0.png'))
fairum_ability1_img = pg.transform.scale(fairum_ability1_img, (128, abilityscaledheight))
fairum_ability2_img = pg.image.load(os.path.join(currentfiles,'fairum_abilites1.png'))
fairum_ability2_img = pg.transform.scale(fairum_ability2_img, (128, abilityscaledheight))
fairum_ability3_img = pg.image.load(os.path.join(currentfiles,'fairum_abilites2.png'))
fairum_ability3_img = pg.transform.scale(fairum_ability3_img, (128, abilityscaledheight))
fairum_ability4_img = pg.image.load(os.path.join(currentfiles,'fairum_abilites3.png'))
fairum_ability4_img = pg.transform.scale(fairum_ability4_img, (128, abilityscaledheight))
fairum.attack1 = 'plate push'
fairum.attack2 = 'construct'
fairum.attack3 = 'project'
fairum.attack4 = 'steel rain'
fairum.vec = vec(20,15)
fairum.health = 50
fairum.shield = 0
fairum.agro = 1
fairum.movement = 2
fairum.immunities = []
fairum.plates = 10
fairum.plateslimit = 10
fairum.abilities = {fairum.attack4:[0,vec(47,17),'Use plates to deal AOE damage'],'increase':[0,vec(47,20),'Increase plate limit up to 15'],fairum.attack3:[0,vec(47,23),'Project plates to protect allies']}
fairum.unlockedabilites = []
fairum.blessing = -1
fairum.exp = 0
fairum.lvl = 0
fairum.needtolvl = 10
fairum.combat_animation = {1:fairum_combat_img,2:fairum_combat2_img,3:fairum_combat3_img}
fairum.attacks = {fairum.attack1:[[0,4],[{bleed:1}],False,1,fairum_ability1_img,[vec(18,31) + a for a in iconaura],[sttatck,0],False],fairum.attack2:[[0,0],[0],True,1,fairum_ability2_img,[vec(23,31) + a for a in iconaura],[vec(0,0),0],False],fairum.attack3:[[0,0],[0],True,1,fairum_ability3_img,[vec(28,31)+a for a in iconaura],[vec(0,0),0],False],fairum.attack4:[[5,7],[],False,1,fairum_ability4_img,[vec(33,31) + a for a in iconaura],[sttatck,twobthree],secondrow+firstrow]}
fairum.clickaura = []
aura = [(1, 3), (0, 3), (-1, 3), (-1, 2), (0, 2), (1, 2), (1, 1), (0, 1), (-1, 1), (-1, 0), (0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, -2), (0, -2), (1, -2), (1, -3), (0, -3), (-1, -3)]
for x in aura:
    fairum.clickaura.append(vec(x))

currentfiles = currentfileg + '/nover'

nover = ally.noverence()
nover_combat_img = pg.image.load(os.path.join(currentfiles,'Layer 1_nover_combat1.png')).convert_alpha()
nover_combat_img = pg.transform.scale(nover_combat_img, (imagescaledwidth, imagescaledheight))
nover_combat2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_nover_combat2.png')).convert_alpha()
nover_combat2_img = pg.transform.scale(nover_combat2_img, (imagescaledwidth, imagescaledheight))
nover_combat3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_nover_combat3.png')).convert_alpha()
nover_combat3_img = pg.transform.scale(nover_combat3_img, (imagescaledwidth, imagescaledheight))

nover_transformed_img = pg.image.load(os.path.join(currentfiles,'nover_transformed.png')).convert_alpha()
nover_transformed_img = pg.transform.scale(nover_transformed_img, (imagescaledwidth, imagescaledheight))

nover_mimic_img = pg.image.load(os.path.join(currentfiles,'Layer 1_nover_mimic1.png')).convert_alpha()
nover_mimic_img = pg.transform.scale(nover_mimic_img, (imagescaledwidth, imagescaledheight))
nover_mimic2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_nover_mimic2.png')).convert_alpha()
nover_mimic2_img = pg.transform.scale(nover_mimic2_img, (imagescaledwidth, imagescaledheight))
nover_mimic3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_nover_mimic3.png')).convert_alpha()
nover_mimic3_img = pg.transform.scale(nover_mimic3_img, (imagescaledwidth, imagescaledheight))

nover_block_img = pg.image.load(os.path.join(currentfiles,'nover_combat_alternate.png')).convert_alpha()
nover_block_img = pg.transform.scale(nover_block_img, (imagescaledwidth, imagescaledheight))

nover_ability1_img = pg.image.load(os.path.join(currentfiles,"nover_abilites0.png"))
nover_ability1_img = pg.transform.scale(nover_ability1_img, (128, abilityscaledheight))
nover_ability2_img = pg.image.load(os.path.join(currentfiles,"nover_abilites1.png"))
nover_ability2_img = pg.transform.scale(nover_ability2_img, (128, abilityscaledheight))
nover_ability3_img = pg.image.load(os.path.join(currentfiles,"nover_abilites2.png"))
nover_ability3_img = pg.transform.scale(nover_ability3_img, (128, abilityscaledheight))
nover_ability4_img = pg.image.load(os.path.join(currentfiles,"nover_abilites3.png"))
nover_ability4_img = pg.transform.scale(nover_ability4_img, (128, abilityscaledheight))
nover.attack1 = 'block'
nover.attack2 = 'leech'
nover.attack3 = 'transform'
nover.attack4 = 'mimic'
nover.vec = vec(20,15)
nover.health = 50
nover.shield = 0
nover.agro = 1
nover.movement = 2
nover.immunities = []
nover.acts = 2
nover.actsmimic = 3
nover.transformed = False
nover.block = False
nover.mimicing = False
nover.saveblock = 0
nover.inc = 0
nover.abilities = {nover.attack4:[0,vec(47,17),'mimic allies actions'],'increase':[0,vec(47,20),'Increases damage by 0.1'],'static blood':[0,vec(47,23),'allows  to trade health for shields']}
nover.unlockedabilites = []
nover.blessing = -1
nover.exp = 0
nover.lvl = 0
nover.needtolvl = 10
nover.combat_animation = {1:nover_combat_img,2:nover_combat2_img,3:nover_combat3_img}
nover.saveattacks = {nover.attack1:[0,[{stun:1}],True,1,nover_ability1_img,[vec(18,31) + a for a in iconaura],[sttatck,0],secondrow+firstrow],nover.attack2:[5,[{bleed:1}],False,1,nover_ability2_img,[vec(23,31) + a for a in iconaura],[sttatck,0],secondrow+firstrow],nover.attack3:[0,[0],True,1,nover_ability3_img,[vec(28,31)+ a for a in iconaura]],nover.attack4:[0,[0],True,1,nover_ability4_img,[vec(33,31)+ a for a in iconaura]]}
nover.attacks = {nover.attack1:[0,[{stun:1}],True,1,nover_ability1_img,[vec(18,31) + a for a in iconaura],[sttatck,0],secondrow+firstrow],nover.attack2:[5,[{bleed:1}],False,1,nover_ability2_img,[vec(23,31) + a for a in iconaura],[sttatck,0],secondrow+firstrow],nover.attack3:[0,[0],True,1,nover_ability3_img,[vec(28,31)+ a for a in iconaura],[vec(0,0),0],False],nover.attack4:[0,[0],True,1,nover_ability4_img,[vec(33,31)+ a for a in iconaura],[vec(0,0),0],False]}
aura = [(1, 3), (0, 3), (-1, 3), (-1, 2), (0, 2), (1, 2), (1, 1), (0, 1), (-1, 1), (-1, 0), (0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, -2), (0, -2), (1, -2), (1, -3), (0, -3), (-1, -3)]
nover.clickaura = []
#print([vec(18,31) + a for a in iconaura])
for x in aura:
    nover.clickaura.append(vec(x))

currentfiles = currentfileg + '/heplane'

H = ally.heplane()
heplane_combat_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat1.png')).convert_alpha()
heplane_combat_img = pg.transform.scale(heplane_combat_img, (imagescaledwidth, imagescaledheight))
heplane_combat2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat2.png')).convert_alpha()
heplane_combat2_img = pg.transform.scale(heplane_combat2_img, (imagescaledwidth, imagescaledheight))
heplane_combat3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat3.png')).convert_alpha()
heplane_combat3_img = pg.transform.scale(heplane_combat3_img, (imagescaledwidth, imagescaledheight))
heplane_ability1_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites0.png'))
heplane_ability1_img = pg.transform.scale(heplane_ability1_img, (abilityscaledwidth, abilityscaledheight))
heplane_ability2_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites1.png'))
heplane_ability2_img = pg.transform.scale(heplane_ability2_img, (128, abilityscaledheight))
heplane_ability3_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites2.png'))
heplane_ability3_img = pg.transform.scale(heplane_ability3_img, (128, abilityscaledheight))
heplane_ability4_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites3.png')).convert_alpha()
heplane_ability4_img = pg.transform.scale(heplane_ability4_img, (128, abilityscaledheight))
H.attack1 = 'coilent'
H.attack2 = 'punch'
H.attack3 = 'blood heal'
H.attack4 = 'static blood'
H.vec = vec(20,15)
H.health = 50
H.shield = 0
H.agro = 1
H.movement = 2
H.speed = 30
H.immunities = []
H.healdam = 0
H.inc = 0
H.abilities = {H.attack3:[0,vec(47,17),'heal for half the damage dealt on enemies'],'increase':[0,vec(47,20),'Increases damage by 0.1'],H.attack4:[0,vec(47,23),'allows heplane to trade health for shields']}
H.unlockedabilites = []
H.blessing = -1
H.exp = 0
H.lvl = 0
H.needtolvl = 10
H.combat_animation = {1:heplane_combat_img,2:heplane_combat2_img,3:heplane_combat3_img}
H.attacks = {H.attack1:[{dealtdamage:10,effects:{fire:1},support:False,hits:1,typeofattack:[sttatck,0],whereattack:secondrow+firstrow,heavy:True},heplane_ability1_img,[vec(18,31) + a for a in iconaura]],H.attack2:[{dealtdamage:5,effects:{},support:False,hits:1,typeofattack:[sttatck,0],whereattack:secondrow+firstrow,heavy:False},heplane_ability2_img,[vec(18,31) + a for a in iconaura]],H.attack3:[{dealtdamage:0,effects:{},support:True,hits:1,typeofattack:[anywhere,0],whereattack:False,heavy:False},heplane_ability3_img,[vec(18,31) + a for a in iconaura]],H.attack4:[{dealtdamage:20,effects:{},support:True,hits:1,typeofattack:[anywhere,0],whereattack:False,heavy:False},heplane_ability4_img,[vec(18,31) + a for a in iconaura]]}
aura = [(1, 3), (0, 3), (-1, 3), (-1, 2), (0, 2), (1, 2), (1, 1), (0, 1), (-1, 1), (-1, 0), (0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, -2), (0, -2), (1, -2), (1, -3), (0, -3), (-1, -3)]
H.clickaura = []
for x in aura:
    H.clickaura.append(vec(x))



currentfiles = currentfileg + '/cri'

Cri = ally.cri()
cri_combat_img = pg.image.load(os.path.join(currentfiles,'cri_combat0.png')).convert_alpha()
cri_combat_img = pg.transform.scale(cri_combat_img, (imagescaledwidth, imagescaledheight))
cri_combat2_img = pg.image.load(os.path.join(currentfiles,'cri_combat1.png')).convert_alpha()
cri_combat2_img = pg.transform.scale(cri_combat2_img, (imagescaledwidth, imagescaledheight))
cri_combat3_img = pg.image.load(os.path.join(currentfiles,'cri_combat2.png')).convert_alpha()
cri_combat3_img = pg.transform.scale(cri_combat3_img, (imagescaledwidth, imagescaledheight))
cri_ability1_img = pg.image.load(os.path.join(currentfiles,'crystal_icons-2.png.png'))
cri_ability1_img = pg.transform.scale(cri_ability1_img, (128, abilityscaledheight))
cri_ability2_img = pg.image.load(os.path.join(currentfiles,'crystal_icons-3.png.png'))
cri_ability2_img = pg.transform.scale(cri_ability2_img, (128, abilityscaledheight))
cri_ability3_img = pg.image.load(os.path.join(currentfiles,'crystal_icons-1.png.png'))
cri_ability3_img = pg.transform.scale(cri_ability3_img, (128, abilityscaledheight))
cri_stunicon_img = pg.image.load(os.path.join(currentfiles,'sri_stun-1.png.png'))
cri_stunicon_img = pg.transform.scale(cri_stunicon_img, (128, abilityscaledheight))
Cri.attack1 = 'flash and crash'
Cri.attack2 = 'crystal glass'
Cri.attack3 = 'karen and her healing balony'
Cri.vec = vec(20,25)
Cri.health = 25
Cri.shield = 10
Cri.agro = 1
Cri.immunities = []
Cri.movement = 2
Cri.stuncap = 7
Cri.inc = 0
Cri.abilities = {'stun':[0,vec(47,17),'decreases the damage needed to stun from 7 to 6'],'increase':[0,vec(47,20),'increases the value that abilites increase to 2 rather then 1']}
Cri.unlockedabilites = []
Cri.blessing = -1
Cri.exp = 0
Cri.lvl = 0
Cri.needtolvl = 10
Cri.combat_animation = {1:cri_combat_img,2:cri_combat2_img,3:cri_combat3_img}
Cri.attacks = {Cri.attack1:[{dealtdamage:5,effects:{},support:False,hits:1,typeofattack:[sttatck,threebthree],whereattack:secondrow+firstrow,heavy:False},cri_ability1_img,[vec(18,31) + a for a in iconaura]],Cri.attack2:[{dealtdamage:2,effects:{},support:True,hits:1,typeofattack:[anywhere,0],whereattack:False,heavy:False},cri_ability3_img,[vec(18,31) + a for a in iconaura]],Cri.attack3:[{dealtdamage:2,effects:{},support:True,hits:1,typeofattack:[anywhere,0],whereattack:False,heavy:False},cri_ability2_img,[vec(18,31) + a for a in iconaura]]}
Cri.clickaura = []
for x in aura:
    Cri.clickaura.append(vec(x))

2,True,[0],1,cri_ability2_img,[vec(28,31) + a for a in iconaura],[anywhere,0],False


currentfiles = currentfileg + '/haptic'    
    
Hap = ally.haptic()
haptic_combat_img = pg.image.load(os.path.join(currentfiles,'Layer 1_haptic_combat1.png')).convert_alpha()
haptic_combat_img = pg.transform.scale(haptic_combat_img, (imagescaledwidth, imagescaledheight))
haptic_combat2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_haptic_combat2.png')).convert_alpha()
haptic_combat2_img = pg.transform.scale(haptic_combat2_img, (imagescaledwidth, imagescaledheight))
haptic_combat3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_haptic_combat3.png')).convert_alpha()
haptic_combat3_img = pg.transform.scale(haptic_combat3_img, (imagescaledwidth, imagescaledheight))
haptic_ability1_img = pg.image.load(os.path.join(currentfiles,'haptic_abilites1.png'))
haptic_ability1_img = pg.transform.scale(haptic_ability1_img, (128, abilityscaledheight))
haptic_ability2_img = pg.image.load(os.path.join(currentfiles,'haptic_abilites0.png'))
haptic_ability2_img = pg.transform.scale(haptic_ability2_img, (128, abilityscaledheight))
haptic_ability3_img = pg.image.load(os.path.join(currentfiles,'haptic_abilites2.png'))
haptic_ability3_img = pg.transform.scale(haptic_ability3_img, (128, abilityscaledheight))
Hap.attack1 = 'accumulation'
Hap.attack2 = 'flailing'
Hap.attack3 = 'acceleration'
Hap.vec = vec(20,15)
Hap.health = 60
Hap.shield = 0
Hap.agro = 1
Hap.immunities = []
Hap.momentum = 0
Hap.inc = 0
Hap.dodgec = 0
Hap.attacktwice = False
Hap.abilities = {Hap.attack3:[0,vec(47,17),'An ability which when activated the next turns attack will happen twice'],'increase':[0,vec(47,20),'Increase all attacks by 1'],'dodge':[0,vec(47,23),'allows haptic to dodge attacks']}
Hap.unlockedabilites = []
Hap.blessing = -1
Hap.exp = 0
Hap.lvl = 0
Hap.needtolvl = 10
Hap.combat_animation = {1:haptic_combat_img,2:haptic_combat2_img,3:haptic_combat3_img}
Hap.attacks = {Hap.attack1:[5,[{bleed:0}],False,1,haptic_ability1_img,[vec(18,31) + a for a in iconaura]],Hap.attack2:[5,[0],False,1,haptic_ability2_img,[vec(23,31) + a for a in iconaura]],Hap.attack3:[0,[0],True,1,haptic_ability3_img,[vec(28,31)+a for a in iconaura]]}
Hap.clickaura = []
for x in aura:
    Hap.clickaura.append(vec(x))

currentfiles = currentfileg + '/sillid'  

sillid = ally.sillid()
sillid_combat_img = pg.image.load(os.path.join(currentfiles,'Layer 1_sillid_combat1.png')).convert_alpha()
sillid_combat_img = pg.transform.scale(sillid_combat_img, (imagescaledwidth, imagescaledheight))
sillid_combat2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_sillid_combat2.png')).convert_alpha()
sillid_combat2_img = pg.transform.scale(sillid_combat2_img, (imagescaledwidth, imagescaledheight))
sillid_combat3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_sillid_combat3.png')).convert_alpha()
sillid_combat3_img = pg.transform.scale(sillid_combat3_img, (imagescaledwidth, imagescaledheight))
sillid_ability1_img = pg.image.load(os.path.join(currentfiles,'sillid_abilites1.png'))
sillid_ability1_img = pg.transform.scale(sillid_ability1_img, (128, abilityscaledheight))
sillid_ability2_img = pg.image.load(os.path.join(currentfiles,'sillid_abilites0.png'))
sillid_ability2_img = pg.transform.scale(sillid_ability2_img, (128, abilityscaledheight))
sillid_ability3_img = pg.image.load(os.path.join(currentfiles,'sillid_abilites2.png'))
sillid_ability3_img = pg.transform.scale(sillid_ability3_img, (128, abilityscaledheight))
sillid_ability4_img = pg.image.load(os.path.join(currentfiles,'sillid_abilites3.png'))
sillid_ability4_img = pg.transform.scale(sillid_ability4_img, (128, abilityscaledheight))
sillid.attack1 = 'iron arrow'
sillid.attack2 = 'dirt arrow'
sillid.attack3 = 'restock'
sillid.attack4 = 'uranium arrow'
sillid.vec = vec(20,15)
sillid.health = 35
sillid.shield = 0
sillid.agro = 1
sillid.immunities = []
sillid.acts = 0
sillid.inc = 0
sillid.chance = 0
sillid.abilities = {sillid.attack4:[0,vec(47,17),'access to uranium arrows appears sometimes when restocking'],'increase':[0,vec(47,20),'Increase all attacks by 1'],'critical':[0,vec(47,23),'crits bud']}
sillid.unlockedabilites = []
sillid.blessing = -1
sillid.exp = 0
sillid.lvl = 0
sillid.needtolvl = 10
sillid.combat_animation = {1:sillid_combat_img,2:sillid_combat2_img,3:sillid_combat3_img}
sillid.attacks = {sillid.attack1:[[10,1],[{bleed:1}],False,1,sillid_ability1_img,[vec(18,31) + a for a in iconaura]],sillid.attack2:[[5,3],[0],False,1,sillid_ability2_img,[vec(23,31) + a for a in iconaura]],sillid.attack3:[[0,0],[0],True,1,sillid_ability3_img,[vec(28,31)+a for a in iconaura]],sillid.attack4:[[5,1],[{fire:1,stun:1}],False,1,sillid_ability4_img,[vec(33,31) + a for a in iconaura]]}
sillid.clickaura = []
for x in aura:
    sillid.clickaura.append(vec(x))

playing = H
'''
NAMES 



milidity nothing yet
riteana nothing yet
atteva nothing yet

alummon nothing yet
tullate nothing yet

Coulion electric canon guy

zither xanth user comes from macrodoen, dancing assasins called the comerance, special dress called a nintine
lunal staff guy renrica in staff
sillid a fiedca
cri a crystal dosen't get along with fiedcas

adine psycic
heneric gas guy
fern fan laby
Striate plasma lady
delator boss guy/guy who's mother has same name and fights corparations 

maxine = Eso
Burton = all 
both wear helmets 

weapons:
zenite 


'''

class dialouge_master():
    class cri():
        pass
    class haptic():
        pass

D = dialouge_master()
haptic = D.haptic
class shopkeeper():
    def __init__(self):
        self.selectedshop = 0
        pos = vec(20,10)
        x = int(pos.x*WIDTHTILESIZE-230)
        y = int(pos.y*HEIGHTTILESIZE-35)
        rect = pg.Rect(x, y, 135, 30)
        self.exitbutton = pg.draw.rect(screen,BLACK,rect)
        self.exittext = ['Map',20,WHITE,x+5, y]
    def shopstart(self):
        self.selectedshop = 0
    def draw_shopkeeps(self):
        pos = self.clericvec
        img = self.cleric_img
        goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))    
        self.b = screen.blit(img, img.get_rect(center=goal_center))
        
        pos = self.armorervec
        img = self.armorer_img
        goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))    
        self.a = screen.blit(img, img.get_rect(center=goal_center))
        
        
        
        pg.draw.rect(screen,BLACK,self.exitbutton)
        a = self.exittext
        draw_text(a[0],a[1],a[2],a[3], a[4])
    def draw_shopinventory(self):
        if self.selectedshop == 'cleric':
            skcleric.draw_actions()
        if self.selectedshop == 'armorer':
            skarmorer.draw_actions()
    def selectingshop(self):
        if self.exitbutton.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
            main.current_state = 'map'
        if self.b.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
            self.selectedshop = 'cleric'
        if self.a.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
            self.selectedshop = 'armorer'
    def selectingshopaction(self):
        if self.selectedshop == 'cleric':
            skcleric.action()
        if self.selectedshop == 'armorer':
            skarmorer.action()
    class cleric():
        def action(self):
            if self.healone.collidepoint(int(mposraw.x),int(mposraw.y)) and main.amountmoney >= 15:
                self.heal = True
            elif self.heal == True and M.selectedchar != 0:
                M.allies[M.selectedchar][1] += 40
                if M.allies[M.selectedchar][1] >= M.selectedchar.health:
                    M.allies[M.selectedchar][1] = M.selectedchar.health
                self.heal = False
                main.amountmoney -= 15
            if self.healparty.collidepoint(int(mposraw.x),int(mposraw.y)) and main.amountmoney >= 40:
                for x in M.allies:
                    M.allies[x][1] += 40
                    if M.allies[x][1] >= x.health:
                        M.allies[x][1] = x.health
                main.amountmoney -= 40
            
            if self.resone.collidepoint(int(mposraw.x),int(mposraw.y)) and main.amountmoney >= 100:
                for x in M.alliessave:
                    if x not in M.allies:
                        pos = x.vec
                        eat = x.health
                        lean = x.shield
                        M.allies.update({x:[pos,eat,x.clickaura,lean,[]]})
                        main.amountmoney -= 100
                
                M.numberofallies()
        def draw_actions(self):
            pos = shop.clericvec
            x = int(pos.x*WIDTHTILESIZE-250)
            y = int(pos.y*HEIGHTTILESIZE-70)
            rect = pg.Rect(x, y, 135, 45)
            self.healparty = pg.draw.rect(screen,BLACK,rect)
            draw_text('heal party',20,WHITE,x+5, y)
            x2 = int(pos.x*WIDTHTILESIZE-300)
            y2 = int(pos.y*HEIGHTTILESIZE-70)
            rect = pg.Rect(x2, y2, 40, 45)
            pg.draw.rect(screen,BLACK,rect)
            draw_text('40',20,WHITE,x2+5, y2)
            
            y = int(pos.y*HEIGHTTILESIZE-10)
            rect = pg.Rect(x, y, 135, 45)
            self.healone = pg.draw.rect(screen,BLACK,rect)
            draw_text('heal individual',20,WHITE,x+5, y)
            y2 = int(pos.y*HEIGHTTILESIZE-10)
            rect = pg.Rect(x2, y2, 40, 45)
            pg.draw.rect(screen,BLACK,rect)
            draw_text('15',20,WHITE,x2+5, y2)

            y = int(pos.y*HEIGHTTILESIZE+50)
            rect = pg.Rect(x, y, 135, 45)
            self.resone = pg.draw.rect(screen,BLACK,rect)
            draw_text('res individual',20,WHITE,x+5, y)
            y2 = int(pos.y*HEIGHTTILESIZE+50)
            rect = pg.Rect(x2, y2, 40, 45)
            pg.draw.rect(screen,BLACK,rect)
            draw_text('100',20,WHITE,x2+5, y2)
    class armorer():
        def action(self):
            if self.shieldquater.collidepoint(int(mposraw.x),int(mposraw.y)) and main.amountmoney >= 25:
                self.shield = True
            elif self.shield == True and M.selectedchar != 0:
                M.allies[M.selectedchar][3] += M.selectedchar.health/4
                if M.allies[M.selectedchar][3] >= M.selectedchar.health:
                    M.allies[M.selectedchar][3] = M.selectedchar.health
                self.shield = False
                self.shieldh = False
                main.amountmoney -= 25
            if self.shieldhalf.collidepoint(int(mposraw.x),int(mposraw.y)) and main.amountmoney >= 50:
                self.shieldh = True
            elif self.shieldh == True and M.selectedchar != 0:
                M.allies[M.selectedchar][3] += M.selectedchar.health/2
                if M.allies[M.selectedchar][3] >= M.selectedchar.health:
                    M.allies[M.selectedchar][3] = M.selectedchar.health
                self.shieldh = False
                self.shield = False
                main.amountmoney -= 50
            if self.shieldparty.collidepoint(int(mposraw.x),int(mposraw.y)) and main.amountmoney >= 100:
                for x in M.allies:
                    M.allies[x][3] += 10
                    if M.allies[x][3] >= x.health:
                        M.allies[x][3] = x.health
                main.amountmoney -= 100

        def draw_actions(self):
            pos = shop.armorervec
            x = int(pos.x*WIDTHTILESIZE-250)
            y = int(pos.y*HEIGHTTILESIZE-70)
            rect = pg.Rect(x, y, 135, 45)
            self.shieldquater = pg.draw.rect(screen,BLACK,rect)
            draw_text('shield quater',20,WHITE,x+5, y)
            x2 = int(pos.x*WIDTHTILESIZE-300)
            y2 = int(pos.y*HEIGHTTILESIZE-70)
            rect = pg.Rect(x2, y2, 40, 45)
            pg.draw.rect(screen,BLACK,rect)
            draw_text('25',20,WHITE,x2+5, y2)
            
            y = int(pos.y*HEIGHTTILESIZE-10)
            rect = pg.Rect(x, y, 135, 45)
            self.shieldhalf = pg.draw.rect(screen,BLACK,rect)
            draw_text('shield half',20,WHITE,x+5, y)
            y2 = int(pos.y*HEIGHTTILESIZE-10)
            rect = pg.Rect(x2, y2, 40, 45)
            pg.draw.rect(screen,BLACK,rect)
            draw_text('50',20,WHITE,x2+5, y2)

            y = int(pos.y*HEIGHTTILESIZE+50)
            rect = pg.Rect(x, y, 135, 45)
            self.shieldparty = pg.draw.rect(screen,BLACK,rect)
            draw_text('shield party',20,WHITE,x+5, y)
            y2 = int(pos.y*HEIGHTTILESIZE+50)
            rect = pg.Rect(x2, y2, 40, 45)
            pg.draw.rect(screen,BLACK,rect)
            draw_text('100',20,WHITE,x2+5, y2)
shop = shopkeeper()

skcleric = shopkeeper.cleric()
skcleric.heal = False
shop.clericvec = vec(37,20)
shop.cleric_img = pg.image.load(os.path.join(filename,'cleric-1.png.png')).convert_alpha()
shop.cleric_img = pg.transform.scale(shop.cleric_img, (imagescaledwidth, imagescaledheight))

skarmorer = shopkeeper.armorer()
skarmorer.shield = False
skarmorer.shieldh = False
shop.armorervec = vec(43,10)
shop.armorer_img = pg.image.load(os.path.join(filename,'cleric-1.png.png')).convert_alpha()
shop.armorer_img = pg.transform.scale(shop.armorer_img, (imagescaledwidth, imagescaledheight))

shop.shopstart()

class main():
    def __init__(self):
        current_state = 0
    def checkstate(self):
        if self.savestate != self.current_state:
            self.savestate = self.current_state
            if self.current_state == 'overmap' or self.current_state == 'map':
                Bg.checkback()
    def draw_level(self):
        text = 'current level '+str(int(L.crossvec.x - 3))
        draw_text(text, 30, BLACK, 50, 10)
    def draw_money(self):
        text = 'Coins '+str(self.amountmoney)
        draw_text(text, 30, BLACK, 50, 10)
    def states(self):
        if self.current_state == 'battle':
            pass
    def battletop(self):
        if self.current_state == 'battle':
            if M.tutorial:
                if tut.togo():
                    if mpos in M.getaura() and M.selectedchar != 0 :
                        if M.attackselect == True and M.enemycanattack == False :
                            M.damage = {}
                            for x in M.enemy:
                                for y in M.enemy[x]:
                                    y[5] = []
                                    y[3] = 0
                            if M.selectedchar.attacks[M.selectedattack][2] != False:
                                if mpos in M.allies[M.ally1][2]:
                                        M.actions.append(M.selectedchar)
                                        M.selectedchar.support(M.ally1)
                                        M.attackselect = False
                                        M.checkifdead()
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
                        M.attackselect = False
                    if mpos in M.selectingattack():
                        M.selectattack()
            else:
                if mpos in M.getaura() and M.selectedchar != 0 and M.selectedattack != 0:
                    if len(M.actions) != len(M.allies) and M.selectedchar not in M.actions:
                        #print('line2439',M.selectedchar.attacks[M.selectedattack][8])
                        
                        if M.selectedchar.attacks[M.selectedattack][0][typeofattack][0] == sttatck: #straight attack
                            ccc = []

                            for x in collumcheck[M.unconversion[M.allies[M.selectedchar][0].x,M.allies[M.selectedchar][0].y][1]]:#check postions along column
                                if M.enemyspaces[x.x,x.y] != 0:
                                    ccc = [x]
                                    break
                        if M.selectedchar.attacks[M.selectedattack][0][support] != False:
                            for x in M.allies:
                                if mpos in M.allies[x][2]:
                                    M.actions.append(M.selectedchar)
                                    M.selectedchar.support(x)
                                    M.checkifdead()
                        elif M.unconversion[M.allies[M.selectedchar][0].x,M.allies[M.selectedchar][0].y] in M.selectedchar.attacks[M.selectedattack][0][whereattack] and bigmpos in ccc:
                            if M.selectedchar.attacks[M.selectedattack][0][heavy]:
                                M.actions.append(M.selectedchar)
                                M.allies[M.selectedchar][4].update({heavy:[M.allies[M.selectedchar][6],M.selectedattack]})
                                print(M.allyspaces)
                                
                                if M.unconversion[M.allies[M.selectedchar][0].x,M.allies[M.selectedchar][0].y] != M.unconversion[M.allies[M.selectedchar][6].x,M.allies[M.selectedchar][6].y]:
                                    M.allyspaces[M.unconversion[M.allies[M.selectedchar][6].x,M.allies[M.selectedchar][6].y]] = M.selectedchar
                                    M.allyspaces[M.unconversion[M.allies[M.selectedchar][0].x,M.allies[M.selectedchar][0].y]] = 0
                                M.allies[M.selectedchar][6] = M.allies[M.selectedchar][0]
                                
                                    
                                print('line 2493',M.allyspaces)
                                self.allyheavys.append(M.selectedchar)
                            else:
                                M.damage = {}
                                der,xxer = M.selectenemy()
                                if M.selectedchar.attacks[M.selectedattack][0][typeofattack][1] == 0:
                                    M.actions.append(M.selectedchar)
                                    M.selectedchar.attack((der,xxer),M.selectedattack)
                                    M.checkifdead()  
                                else:
                                    M.actions.append(M.selectedchar)
                                    pos = ccc[0]
                                    M.selectedchar.attack((der,xxer),M.selectedattack)
                                    for x in M.selectedchar.attacks[M.selectedattack][0][typeofattack][1]:
                                        new = pos + x
                                        new = (new.x,new.y)
                                        if new in M.enemyspaces:
                                            if M.enemyspaces[new] != 0:
                                                new = M.conversion[new[0],new[1]]
                                                der, xxer = M.areaselectenemy(new)
                                                M.selectedchar.attack((der,xxer),M.selectedattack)
                                             
                                    M.checkifdead()  
                        
                        
                        
                        
                elif M.moving:
                    if M.selectedchar not in M.actions and M.selectedchar != 0:
                        M.moveallies()
                    elif mpos not in M.selectingchar():
                        M.selectedchar = 0
                #elif mpos not in M.getaura() and mpos not in M.selectingattack():
                #    M.selectedchar = 0
                #    M.attackselect = False    

                if mpos in M.selectingchar():#and M.attackselect == False:
                    save = M.selectedchar
                    M.selectchar()
                    M.moving = True
                    if M.selectedchar != save:
                        M.selectedattack = 0
                    if M.allies[M.selectedchar][6] == False:
                        M.allies[M.selectedchar][6] = M.allies[M.selectedchar][0] 
                if mpos in M.selectingattack():
                    M.selectattack()
    def battlebottom(self):
        if current_time - self.anim_timer > 1000:
            M.current_animation += 1
            if M.current_animation == 4:
                M.current_animation = 1
            for x in M.enemy:
                for y in M.enemy[x]:
                    if y[6]:
                        y[7] += 1
                        if y[7] == 4:
                            y[7] = 1
                            y[6] = False
            self.anim_timer = pg.time.get_ticks()
        if self.current_state == 'battle':
            Bg.draw_background()
            M.draw_grid()
            M.draw_movement()
            M.draw_obstacles()
            M.draw_heavy()
            M.draw_allychar()
            M.draw_enemychar()
            M.draw_healthbar()
            M.draw_icons()
            
            M.draw_effects()
            M.draw_phase()
            M.draw_transition()
            
            if ui.pause:
                M.draw_allychar()
                M.draw_enemychar()
            if M.tutorial:
                tut.pause()
                if current_time - self.display_time > 1000 and tut.done == 6:
                    M.enemycanattack = False
                    
                    tut.togo()
                if M.victory:
                    for x in M.savelevel:
                        if M.savelevel[x] != 0:
                            pos = M.allies[x][0]
                            draw_text_center('LEVEL UP',40,YELLOW,pos.x*WIDTHTILESIZE,pos.y*HEIGHTTILESIZE+150)
                    draw_text_center('Victory',40,YELLOW,int(WIDTH/2),int(HEIGHT/2-200))
                    
            else:
                if len(M.actions) >= len(M.allies) and self.playertrunover == False and len(M.allies) > 0:
                    M.statuseffects(False)
                    self.enemy_attck_time = pg.time.get_ticks()
                    self.playertrunover = True
                    M.damage = {}
                    self.heavies = []
                    M.checkifdead()
                    M.phase = 'Enemy'
                    self.little = {}
                    self.k = 0
                    for x in M.enemy:
                        if len(M.enemy[x]) > 1:
                            for y in range(len(M.enemy[x])):
                                self.little.update({self.k:[x,y]})
                                self.k += 1
                        else:
                            self.little.update({self.k:[x,0]})
                            self.k += 1 
                            if x in boss.bosses:
                                self.little.update({self.k:[x,0]})
                                self.k += 1
                    self.attacks = 0
                    self.enemycanattack = True
                    
                
                if current_time - self.enemy_attck_time > 1000 and self.enemycanattack and len(M.allies) > 0 and not self.flop:
                    self.display_time_start = pg.time.get_ticks()  
                    self.enemy_damage = pg.time.get_ticks()
                    self.flop = True
                    if self.attacks not in M.heavyattacking:
                        
                        M.enemyattack(self.attacks,self.little[self.attacks][1])
                    else:
                        
                        
                        self.enemy_attck_time = pg.time.get_ticks()
                        self.heavies.append(self.attacks)
                        self.attacks += 1
                        if self.k != self.attacks:
                            self.enemy_attck_time = pg.time.get_ticks() -1000
                            self.flop = False
                    
                    
                if 1000 < current_time - self.enemy_damage and self.enemycanattack and self.flop:
                    
                    self.enemy_attck_time = pg.time.get_ticks()
                    self.flop = False
                    self.attacks += 1
                    M.checkifdead()
                    
                    if self.k <= self.attacks:
                        self.enemycanattack = False
                        
                        M.checkifdead()
                        self.startheavy = pg.time.get_ticks()
                        self.heavyattacks = 0
                        self.attackscanheavy = True
                        self.flop = False


                        self.heavies += self.allyheavys # adds ally heavies to overall heavies
                        self.allyheavys = []
                        self.heaviescopy = list(self.heavies)
                        self.heavies = {}
                        for pp in self.heaviescopy:
                            if isinstance(pp,int):
                                oo = main.little[pp][0]
                                ee = main.little[pp][1]
                                self.heavies.update({pp:[oo.speed,M.enemy[oo][ee][1]]})
                            else:
                                self.heavies.update({pp:[pp.speed,M.allies[pp][1]]})
                        
                        
                        self.heavies = sorted(self.heavies.items(), key=lambda kv:(kv[1][0],-kv[1][1]),reverse=True)
                        self.heaviescopy = dict(self.heavies)
                        self.heavies = []
                        for x in self.heaviescopy:
                            self.heavies.append(x)
                        #print(self.heaviescopy)
                        if self.heavyattacks >= len(self.heavies):
                            self.playertrunover = False
                            self.attackscanheavy = False

                            
                            M.actions = []
                            M.statuseffects(True)
                            M.checkifdead()
                            self.display_time_stop = pg.time.get_ticks()
                            for x in M.allies:
                                M.allies[x][6] = M.allies[x][0] 
                            if not len(M.actions) >= len(M.allies):
                                M.phase = 'Player'
                                for x in M.enemy:
                                    for y in M.enemy[x]:
                                        y[5] = []
                                        y[3] = 0
                            M.heavyattacking = []
                            for x in M.enemy:
                                for y in M.enemy[x]:
                                    if 'heavy' in y[4]:
                                        del y[4]['heavy']
                            k = 0
                            for x in M.enemy:
                                if len(M.enemy[x]) > 1:
                                    for y in range(len(M.enemy[x])):
                                        attack = x.heavyattacks
                                        chance = []
                                        attacks = []
                                        for ll in attack:
                                            chance.append(attack[ll][4])
                                            attacks.append(ll)
                                        attacking = random.choices(attacks,chance)[0] #selects attack

                                        damage = attack[attacking] #damage number

                                        able = damage[5][0] #type of attack eg straight
                                        pospos = damage[6] #vec where the enemy can attack from
                                        poopee = M.unconversion[(M.enemy[x][y][0].x,M.enemy[x][y][0].y)] #current vec
                                        checker = [vec(1,0),vec(0,1),vec(-1,0),vec(0,-1)] #vec check
                                        checked = [] #possible places the enemy can move to
                                        movement = x.movement +1 #gets movement 
                                        checked.append(vec(poopee)) #adds the enemy's current position to places it can move to

                                        for ll in range(0,movement): # checks the where the enemy can move 
                                            #print(x)
                                            if ll == 1: # first check around the enemy
                                                for ll in checker:
                                                    new = poopee+ ll
                                                    if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0: # restricts movements to the grid
                                                        checked.append(new)
                                            else: # second and more checks and if the movement is more
                                                oldchecked = list(checked)
                                                for ww in oldchecked: #grabs the already checked positions and checks around them
                                                    for ll in checker:
                                                        new = ww+ ll 
                                                        if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0:
                                                            if new not in checked: #prevents already checked vecs to be added to the list
                                                                checked.append(new)

                                        pot = [] # the potential positions the enemy can attack from
                                        possible = [] # is a simplified list 
                                        agros = [] #list of the agros of player characters which help the selection of attack
                                        hitmult = {} 
                                        potpos = {}
                                        for ll in checked:
                                            if ll in pospos:
                                                pot.append(ll)
                                        if len(pot) != 0:
                                            if random.choices([True,False],[5,5])[0]:
                                                M.heavyattacking.append(k)
                                                pos = random.choice(pot)
                                                M.enemy[x][y][4].update({'heavy':[attacking,pos]})
                                        k += 1
                                else:
                                    attack = x.heavyattacks
                                    chance = []
                                    attacks = []
                                    for ll in attack:
                                        chance.append(attack[ll][4])
                                        attacks.append(ll)
                                    attacking = random.choices(attacks,chance)[0] #selects attack
                                    damage = attack[attacking] #damage number
                                    able = damage[5][0] #type of attack eg straight
                                    pospos = damage[6] #vec where the enemy can attack from
                                    poopee = M.unconversion[(M.enemy[x][y][0].x,M.enemy[x][y][0].y)] #current vec
                                    checker = [vec(1,0),vec(0,1),vec(-1,0),vec(0,-1)] #vec check
                                    checked = [] #possible places the enemy can move to
                                    movement = x.movement +1 #gets movement 
                                    checked.append(vec(poopee)) #adds the enemy's current position to places it can move to
                                    for ll in range(0,movement): # checks the where the enemy can move 
                                        #print(x)
                                        if ll == 1: # first check around the enemy
                                            for ll in checker:
                                                new = poopee+ ll
                                                if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0: # restricts movements to the grid
                                                    checked.append(new)
                                        else: # second and more checks and if the movement is more
                                            oldchecked = list(checked)
                                            for y in oldchecked: #grabs the already checked positions and checks around them
                                                for ll in checker:
                                                    new = y+ ll 
                                                    if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0:
                                                        if new not in checked: #prevents already checked vecs to be added to the list
                                                            checked.append(new)
                                    pot = [] # the potential positions the enemy can attack from
                                    possible = [] # is a simplified list 
                                    agros = [] #list of the agros of player characters which help the selection of attack
                                    hitmult = {} 
                                    potpos = {}
                                    for ll in checked:
                                        if ll in pospos:
                                            pot.append(ll)
                                    if len(pot) != 0:
                                        if random.choices([True,False],[50,50])[0]:
                                            M.heavyattacking.append(k)
                                            M.enemy[x][y][4].update({'heavy':attacking})
                                        k += 1 
                                        if x in boss.bosses:
                                            if random.choices([True,False],[50,50])[0]:
                                                M.heavyattacking.append(k)
                                                M.enemy[x][y][4].update({'heavy':attacking})
                                            k += 1
                    
                        
                if 2000 < current_time - self.display_time_start:
                    M.draw_damage()
                M.draw_txt_attack()
                if current_time - self.display_time_stop > 3000 and self.playertrunover == False:
                    M.damage = {}
                    
                    #heavy attack part --- heavy attack part
                if current_time - self.startheavy > 1000 and self.attackscanheavy and len(M.allies) > 0 and not self.flop:
                    self.display_time_start = pg.time.get_ticks()  
                    self.heavy_enemy_damage = pg.time.get_ticks()
                    M.enemyheavyattack(self.heavies[self.heavyattacks])

                    self.flop = True
                    
                if 2000 < current_time - self.heavy_enemy_damage and self.attackscanheavy and self.flop:
                    self.startheavy = pg.time.get_ticks()
                    self.heavyattacks += 1
                    M.checkifdead()
                    self.flop = False
                    if self.heavyattacks >= len(self.heavies):
                        self.display_time_stop = pg.time.get_ticks()
                        self.playertrunover = False
                        self.attackscanheavy = False
                        
                        M.actions = []
                        M.statuseffects(True)
                        M.checkifdead()
                        for x in M.allies:
                            M.allies[x][6] = M.allies[x][0] 
                        if not len(M.actions) >= len(M.allies):
                            M.phase = 'Player'
                            for x in M.enemy:
                                for y in M.enemy[x]:
                                    y[5] = []
                                    y[3] = 0
                        M.heavyattacking = []
                        for x in M.enemy:
                            for y in M.enemy[x]:
                                if 'heavy' in y[4]:
                                    del y[4]['heavy']
                        k = 0
                        for x in M.enemy:
                            if len(M.enemy[x]) > 1:
                                for y in range(len(M.enemy[x])):
                                    attack = x.heavyattacks
                                    chance = []
                                    attacks = []
                                    for ll in attack:
                                        chance.append(attack[ll][4])
                                        attacks.append(ll)
                                    attacking = random.choices(attacks,chance)[0] #selects attack

                                    damage = attack[attacking] #damage number

                                    able = damage[5][0] #type of attack eg straight
                                    pospos = damage[6] #vec where the enemy can attack from
                                    poopee = M.unconversion[(M.enemy[x][y][0].x,M.enemy[x][y][0].y)] #current vec
                                    checker = [vec(1,0),vec(0,1),vec(-1,0),vec(0,-1)] #vec check
                                    checked = [] #possible places the enemy can move to
                                    movement = x.movement +1 #gets movement 
                                    checked.append(vec(poopee)) #adds the enemy's current position to places it can move to

                                    for ll in range(0,movement): # checks the where the enemy can move 
                                        #print(x)
                                        if ll == 1: # first check around the enemy
                                            for ll in checker:
                                                new = poopee+ ll
                                                if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0: # restricts movements to the grid
                                                    checked.append(new)
                                        else: # second and more checks and if the movement is more
                                            oldchecked = list(checked)
                                            for ww in oldchecked: #grabs the already checked positions and checks around them
                                                for ll in checker:
                                                    new = ww+ ll 
                                                    if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0:
                                                        if new not in checked: #prevents already checked vecs to be added to the list
                                                            checked.append(new)

                                    pot = [] # the potential positions the enemy can attack from
                                    possible = [] # is a simplified list 
                                    agros = [] #list of the agros of player characters which help the selection of attack
                                    hitmult = {} 
                                    potpos = {}
                                    for ll in checked:
                                        if ll in pospos:
                                            pot.append(ll)
                                    if len(pot) != 0:
                                        if random.choices([True,False],[5,5])[0]:
                                            M.heavyattacking.append(k)
                                            pos = random.choice(pot)
                                            M.enemy[x][y][4].update({'heavy':[attacking,pos]})
                                    k += 1
                            else:
                                attack = x.heavyattacks
                                chance = []
                                attacks = []
                                for ll in attack:
                                    chance.append(attack[ll][4])
                                    attacks.append(ll)
                                attacking = random.choices(attacks,chance)[0] #selects attack
                                damage = attack[attacking] #damage number
                                able = damage[5][0] #type of attack eg straight
                                pospos = damage[6] #vec where the enemy can attack from
                                poopee = M.unconversion[(M.enemy[x][y][0].x,M.enemy[x][y][0].y)] #current vec
                                checker = [vec(1,0),vec(0,1),vec(-1,0),vec(0,-1)] #vec check
                                checked = [] #possible places the enemy can move to
                                movement = x.movement +1 #gets movement 
                                checked.append(vec(poopee)) #adds the enemy's current position to places it can move to
                                for ll in range(0,movement): # checks the where the enemy can move 
                                    #print(x)
                                    if ll == 1: # first check around the enemy
                                        for ll in checker:
                                            new = poopee+ ll
                                            if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0: # restricts movements to the grid
                                                checked.append(new)
                                    else: # second and more checks and if the movement is more
                                        oldchecked = list(checked)
                                        for y in oldchecked: #grabs the already checked positions and checks around them
                                            for ll in checker:
                                                new = y+ ll 
                                                if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0:
                                                    if new not in checked: #prevents already checked vecs to be added to the list
                                                        checked.append(new)
                                pot = [] # the potential positions the enemy can attack from
                                possible = [] # is a simplified list 
                                agros = [] #list of the agros of player characters which help the selection of attack
                                hitmult = {} 
                                potpos = {}
                                for ll in checked:
                                    if ll in pospos:
                                        pot.append(ll)
                                if len(pot) != 0:
                                    if random.choices([True,False],[50,50])[0]:
                                        M.heavyattacking.append(k)
                                        M.enemy[x][y][4].update({'heavy':attacking})
                                    k += 1 
                                    if x in boss.bosses:
                                        if random.choices([True,False],[50,50])[0]:
                                            M.heavyattacking.append(k)
                                            M.enemy[x][y][4].update({'heavy':attacking})
                                        k += 1
                if M.victory:
                    for x in M.savelevel:
                        if M.savelevel[x] != 0:
                            pos = M.allies[x][0]
                            draw_text_center('LEVEL UP',40,YELLOW,pos.x*WIDTHTILESIZE,pos.y*HEIGHTTILESIZE+150)
                    draw_text_center('Victory',40,YELLOW,int(WIDTH/2),int(HEIGHT/2-200))
                    if current_time - self.endscreen_timer > 10000:
                        M.tran = True
                        if L.crossvec.x == 28:
                            if O.crossvec.x == 5:
                                M.tran = True
                            else:
                                main.current_state = 'overmap'
                                L.crossvec = vec(3,8)
                                L.get_connections()
                                L.turns = 0
                                L.border = 3
                                L.barrier = []
                        M.victory = False
                if M.loss:
                    main.little = {}
                    main.enemy_attck_time = 0
                    main.startheavy = 0
                    main.amountmoney = 50
                    main.enemycanattack = False
                    main.attackscanheavy = False
                    main.playertrunover = False
                    main.k = 0
                    main.little = {}
                    M.phase = 'player'
                    draw_text_center('You died',40,YELLOW,int(WIDTH/2),int(HEIGHT/2-200))
                    if current_time - self.endscreen_timer > 5000:
                        M.loss = False
                        M.restart()
                        main.current_state = 'menu'
                        main.endscreen_timer = 0

    def leveltop(self):
        if self.current_state == 'map':
            if M.tutorial:
                if tut.togo():
                    L.nextlevel()
                    L.clickmenu()
            else:
                L.nextlevel()
                L.clickmenu()
    def levelbottom(self):
        if self.current_state == 'map':
            Bg.draw_background()
            L.draw_currentposition()
            L.draw_linestoconnections()
            L.draw_icons()
            M.draw_transition()
            if M.tutorial:
                tut.pause()
    def shoptop(self):
        if self.current_state == 'shop':
            M.selectchar()
            shop.selectingshopaction()
            shop.selectingshop()      
    def shopbottom(self):
        if self.current_state == 'shop':
            shop.draw_shopkeeps()   
            shop.draw_shopinventory()
            M.draw_allychar()
    def eventtop(self):
        if self.current_state == 'event':
            re.click()
    def eventbottom(self):
        if self.current_state == 'event':
            Bg.draw_background()
            re.draw_event()
            M.draw_transition()
    def switchtop(self):
        if self.current_state == 'switch':
            if M.tutorial:
                if tut.togo():
                    M.selectchar()
                    M.switch()
            else:
                M.selectchar()
                M.switch()
    def switchbottom(self):
        if self.current_state == 'switch':
            M.draw_allychar()
            M.draw_switchbuttons()
            if M.tutorial:
                tut.pause()
    def overmaptop(self):
        if self.current_state == 'overmap':
            O.selectmap()
    def overmapbottom(self):
        if self.current_state == 'overmap':
            Bg.draw_background()
            O.draw_overmap()
    def menutop(self):
        if self.current_state == 'menu' or ui.pause:
            ui.buttons()
    def menubottom(self):
        if self.current_state == 'menu' or ui.pause:
            ui.menu()
    def questtop(self):
        if self.current_state == 'quest' or self.current_state == 'hunt':
            Q.click()
    def questbottom(self):
        if self.current_state == 'quest' or self.current_state == 'hunt':
            Bg.draw_background()
            Q.draw_quest()
            M.draw_transition()
    def creatortop(self):
        if self.current_state == 'creator':
            O.selectmapedit()
    def creatorbottom(self):
        if self.current_state == 'creator':
            O.draw_mapedit()
    def gameovertop(self):
        if self.current_state == 'gameover':
            go.reset()
    def gameoverbottom(self):
        if self.current_state == 'gameover':
            Bg.draw_background()
            go.draw_victory()
            M.draw_transition()
            
main.attacks = 0
class tutorial():
    def __init__(self):
        self.t = 0
    def togo(self):
        x = False
        if self.done == 13:
            main.current_state = 'overmap'
            Bg.checkback()
            M.restart()
            L.crossvec = vec(3,8)
            L.get_connections()
            M.tutorial = False
        if self.done == 12:
            if M.selectedchar != 0:
                for k in M.selectedchar.abilities:
                    if M.selectedchar.abilities[k][0].collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)) and M.selectedchar.abilities[k][2]:
                        if M.selectedability != 0 and k == M.selectedability and M.selectedchar.lvl > 0:
                            x = True
                            self.done += 1
                        else:
                            x = True
        if self.done == 11:
            if mpos in M.selectingchar():
                self.done += 1
                x = True
        if self.done == 10:
            if L.switchbutton.collidepoint(pos):
                self.done += 1
                x = True
        if self.done == 9:
            main.current_state = 'map'
            M.victory = False
            self.done += 1
        if self.done == 8:
            if mpos in M.selectingchar():
                x = True
            if mpos in M.selectingattack():
                M.selectattack()
                if M.selectedattack == M.selectedchar.attack1:
                    x = True
            der,xxer = M.selectenemy()  
            try:
                if der == spsword and M.selectedattack == M.selectedchar.attack1:
                    self.done += 1
                    x = True
            except:
                pass
        if self.done == 7:
            self.done += 1
        if self.done == 6:
            self.done += 1


        if self.done == 5:
            self.done += 1
            if len(M.actions) >= len(M.allies) and main.playertrunover == False:
                    M.statuseffects(False)
                    main.playertrunover = True
                    main.little = {}
                    main.k = 0
                    main.enemy_attck_time = pg.time.get_ticks()
                    for x in M.enemy:
                        if len(M.enemy[x]) > 1:
                            for y in range(len(M.enemy[x])):
                                main.little.update({main.k:[x,y]})
                                main.k += 1
                        else:
                            main.little.update({main.k:[x,0]})
                            main.k += 1 
                    main.k = 0
                    main.enemycanattack = True
                    M.checkifdead()
                
            
                    main.display_time = pg.time.get_ticks()  
                    main.enemy_attck_time = pg.time.get_ticks()
                    M.enemyattack(main.k,main.little[main.k][1])
                    main.k += 1
                    if main.k >= len(main.little):
                        main.enemycanattack = False
                        main.playertrunover = False
                        M.actions = []
                        M.statuseffects(True)
        if self.done == 4:
            self.done += 1
        if self.done == 1:
            if mpos in M.selectingchar():
                self.done += 1
                x = True
        if self.done == 2:
            if mpos in M.selectingattack():
                M.selectattack()
                if M.selectedattack == M.selectedchar.attack2:
                    self.done += 1
                    x = True
        if self.done == 3:
            der,xxer = M.selectenemy()
            if der == spsword:
                self.done += 1
                x = True
        if self.done == 0:
            if mpos2 == vec(14,8):
                self.done += 1 
                x = True
        
        return x
    def pause(self):
        if self.done != 6:
            s = pg.Surface((1920,1080))  # the size of your rect
            s.set_alpha(200)                # alpha level
            s.fill((100,100,100 ))           # this fills the entire surface
            screen.blit(s, (0,0))
            size = 40
        if self.done == 0:
            draw_text_center('This is the map click the dot right of the cross',size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            L.draw_currentposition()
        if self.done == 1:
            draw_text_center('Select the character on the left here',size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            M.draw_allychar()
        if self.done == 2:
            draw_text_center('Now select the attack on the right',size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            M.draw_icons()
            s = pg.Surface((130,150))  # the size of your rect
            s.set_alpha(200)                # alpha level
            s.fill((100,100,100 ))           # this fills the entire surface
            screen.blit(s, (490,880))
        if self.done == 3:
            draw_text_center('Now select the enemy',size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            M.draw_icons()
            M.draw_enemychar()
            s = pg.Surface((130,150))  # the size of your rect
            s.set_alpha(200)                # alpha level
            s.fill((100,100,100 ))           # this fills the entire surface
            screen.blit(s, (490,880))
        if self.done == 4:
            draw_text_center('You did 10 damage indicated by the number below the attack',size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            draw_text_center('click to continue',size-10,WHITE,int(WIDTH/2),int(HEIGHT/2+300))
            M.draw_icons()
            M.draw_enemychar()
            s = pg.Surface((130,150))  # the size of your rect
            s.set_alpha(200)                # alpha level
            s.fill((100,100,100 ))           # this fills the entire surface
            screen.blit(s, (490,880))
        if self.done == 5:
            draw_text_center("Now that your turn is over now it's the enemys turn ",size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            draw_text_center('click to continue',size-10,WHITE,int(WIDTH/2),int(HEIGHT/2+300))
            M.draw_enemychar()
        if self.done == 6:    
            M.draw_damage()
        if self.done == 7:
            draw_text_center("He missed doing 0 damage",size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            draw_text_center('click to continue',size-10,WHITE,int(WIDTH/2),int(HEIGHT/2+300))
            M.draw_damage()
            M.draw_allychar()
        if self.done == 8:
            draw_text_center('Now finish it off with the other attack',size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            M.draw_allychar()
            M.draw_icons()
            M.draw_enemychar()
        if self.done == 9:
            draw_text_center("You got him and looks like you've leveled up",size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            draw_text_center('click to continue',size-10,WHITE,int(WIDTH/2),int(HEIGHT/2+300))
            M.draw_allychar()
        if self.done == 10:
            draw_text_center("Click on party",size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            L.draw_icons()
        if self.done == 11:
            draw_text_center("Click on the character",size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            M.draw_allychar()
        if self.done == 12:
            draw_text_center("Click on an abilitiy/green squares see what to unlock and click again to unlock it",size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            M.draw_switchbuttons()
        if self.done == 13:
            draw_text_center("Good Job you've completed the tutorial now to the main game",size,WHITE,int(WIDTH/2),int(HEIGHT/2+200))
            draw_text_center('click to continue',size-10,WHITE,int(WIDTH/2),int(HEIGHT/2+300))
    def tutorial_restart(self):
        ally1 = H
        ally2 = nover
        ally3 = sillid
        ally4 = Cri
        
        M.selectedattack = 0
        M.selectedchar = 0
        M.current_animation = 1
        M.allies = {}
        M.enemy = {}
        M.l = []
        M.actions = []
        M.addchar(H)
    def create_map(self):
        L.levelid = {}
        L.drawdis = {}
        L.levelstatus = []
        L.path = {}
        L.pathloc = []
        tier = {}
        L.tierasi = {}
        L.closest = {}
        L.levelid = {}
        tier = 'battle'
        L.tierasiquest = (-1,-1)
        L.tiersecq = (-1,-1)
        Q.typeoq = 'none'
        Q.currentquest = 0
        for x in self.levels:
            if tier == 'battle':
                if x.x in L.levelmaster:
                    enemies = []
                    cost = L.levelmaster[x.x][0]
                    enemy = random.choices(L.levelmaster[x.x][1],L.levelmaster[x.x][2])
                    remove = L.get_cost(enemy)
                    cost -= remove
                    enemies.append(enemy[0])
                    L.make(enemies,tier,x)
            else:
                L.make(x,[],tier)
            if x.x == 28:
                L.levelid.update({x:[[cbm],'battle']})             

tut = tutorial()
tut.done = 0
tut.levels = []
levels = [(4, 8),(5, 8),(6, 8),(7, 8),(8, 8),(9, 8),(10, 8),(27, 8),(26, 8),(25, 8),(24, 8), (23, 8),(22, 8),
          (21, 8),(20, 8),(19, 8),(18, 8),(17, 8),(16, 8),(15, 8), (14, 8),(11, 8), (12, 8), (13, 8),]
for x in levels:
    if x not in tut.levels:
        tut.levels.append(vec(x))

main = main()

main.current_state = 'battle'
main.savestate = 0
main.amountmoney = 50
main.enemy_attck_time = 0
main.startheavy = 0
main.enemycanattack = False
main.allyheavys = []
main.attackscanheavy = False
main.playertrunover = False
main.display_time = 0
main.display_time_start = 0
main.display_time_stop = 0
main.enemy_damage = 0
main.heavy_enemy_damage = 0
main.k = 0
main.little = {}
main.endscreen_timer = 0
main.flop = False

def draw_grid():
    for x in range(0, WIDTH, HEIGHTTILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, HEIGHTTILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))
def draw_biggrid():
    for x in range(0, WIDTH, HEIGHTTILESIZE*2):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, HEIGHTTILESIZE*2 ):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))
        
class background():
    def __init__(self):
        self.vec = 0
    def checkback(self):
        if main.current_state == 'overmap':
            self.background_current = map_rica
        elif main.current_state == 'map':
            self.background_current = map_default
        elif main.current_state == 'event':
            self.background_current = re.eventmaster[re.currentevent]['map']
        elif main.current_state == 'quest':
            self.background_current = Q.questmaster[Q.currentquest]['map']
        elif O.crossvec.x == 5 or O.crossvec.x == 3:
            self.background_current = background_fall
    def draw_background(self):
        goal_center = int(WIDTH / 2), int(HEIGHT/ 2)
        screen.blit(self.background_current, self.background_current.get_rect(center=goal_center))
        
Bg = background()
Bg.menuback = []

        
background_fall = pg.image.load(os.path.join(filename,'backgorunds-2.png.png'))
background_fall = pg.transform.scale(background_fall, (WIDTH, HEIGHT))
background_dungeon = pg.image.load(os.path.join(filename,'dungeon.png'))
background_dungeon = pg.transform.scale(background_dungeon, (WIDTH, HEIGHT))
landscape_mountain = pg.image.load(os.path.join(filename,'landscape_mountain.png'))
landscape_mountain = pg.transform.scale(landscape_mountain, (WIDTH, HEIGHT))
Bg.menuback.append(landscape_mountain)
map_rica = pg.image.load(os.path.join(filename,'rica_map.png'))
map_rica = pg.transform.scale(map_rica, (WIDTH, HEIGHT))
Bg.menuback.append(map_rica)
map_default = pg.image.load(os.path.join(filename,'defaultmap.png'))
map_default = pg.transform.scale(map_default, (WIDTH, HEIGHT))


Bg.background_current = random.choice(Bg.menuback)

class gameover():
    def __init__(self):
        self.vec = 0
    def reset(self):
        if self.done == 1:
            M.tran = True
            M.restart()
            self.done = 0
        self.done += 1
    def draw_victory(self):
        M.draw_allychar()
        if self.done == 0:
            draw_text_center("You have slain the evil over the land",40,YELLOW,int(WIDTH/2),int(HEIGHT/2-200))
        elif self.done == 1:
            draw_text_center("Thank you for playing",40,YELLOW,int(WIDTH/2),int(HEIGHT/2-200))

go = gameover()
go.done = 0

class overmap():
    def __init__(self):
        self.over = 0
    def selectmap(self):
        if mpos2 == vec(0,0):
            main.current_state = 'map'
            main.test = True
            self.get_levelcontents()
            T.create_map()
            Bg.checkback()
        if mpos2 in self.connections:
            self.crossvec = mpos2
            self.get_connections()
            main.current_state = 'map'
            self.get_levelcontents()
            L.create_map()
            Bg.checkback()
    def get_levelcontents(self):
        pos = self.crossvec.x
        L.levelmaster = self.mapmaster[int((pos-2)/2)]
    def draw_overmap(self):
        s = pg.Surface((1920,1080))  # the size of your rect
        s.set_alpha(200)                # alpha level
        s.fill((100,100,100 ))           # this fills the entire surface
        screen.blit(s, (0,0)) 
        pos = self.crossvec
        goal_center = (int(pos.x * WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2), int(pos.y * HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2))
        screen.blit(cross, cross.get_rect(center=goal_center))
        for x in self.maps:
            pg.draw.circle(screen,WHITE,(int(x.x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(x.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)),10)
            pg.draw.circle(screen,BLACK,(int(x.x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(x.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)),5)
        for x in self.connections:
            pg.draw.line(screen, BLUE, (int(self.crossvec.x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(self.crossvec.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int(x.x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(x.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
    def draw_mapedit(self):
        if self.creating:
            if self.removal:
                draw_text('r',40,BLUE,7*WIDTHTILESIZE*2,15*HEIGHTTILESIZE*2)
            else:
                draw_text('r',40,BLACK,7*WIDTHTILESIZE*2,15*HEIGHTTILESIZE*2)
            draw_text(str(int((self.crossvec.x-2)/2)),40,BLUE,10*WIDTHTILESIZE*2,2*HEIGHTTILESIZE*2)
            draw_text("+",40,BLACK,11*WIDTHTILESIZE*2,2*HEIGHTTILESIZE*2)
            draw_text("-",40,BLACK,12*WIDTHTILESIZE*2,2*HEIGHTTILESIZE*2)
            y=0
            for ll in range(0,19):
                draw_text(str(ll),10,BLACK,0*WIDTHTILESIZE*2,y*HEIGHTTILESIZE*2)
                y+=1
            x = 5
            y = 3
            for ll in L.levelmaster:
                if ll == self.selectedlevel:
                    draw_text(str(ll),10,BLUE,x*WIDTHTILESIZE*2,y*HEIGHTTILESIZE*2)
                else:   
                    draw_text(str(ll),10,BLACK,x*WIDTHTILESIZE*2,y*HEIGHTTILESIZE*2)
                x += 1
                if x == 16:
                    y += 1
                    x = 5
            if self.selectedlevel != -1:
                draw_text('+',10,BLACK,6*WIDTHTILESIZE*2,10*HEIGHTTILESIZE*2)
                draw_text('-',10,BLACK,7*WIDTHTILESIZE*2,10*HEIGHTTILESIZE*2)
                draw_text(str(L.levelmaster[self.selectedlevel]),10,BLACK,8*WIDTHTILESIZE*2,10*HEIGHTTILESIZE*2)
                x = 5
                y = 12
                for ll in enemy.list:
                    draw_text(str(ll),10,BLACK,x*WIDTHTILESIZE*2,y*HEIGHTTILESIZE*2)
                    x += 5
                    if x >= 25:
                        y += 1
                        x = 5
        else:    
            self.draw_overmap()
    def selectmapedit(self):
        if self.creating:
            x = 5
            y = 3
            if mpos2 == (11,2):
                for ww in L.levelmaster:
                    ww += 1
                L.levelmaster.update({ww:[0,[],[]]})
            if mpos2 == (12,2):
                for ww in L.levelmaster:
                    ww=ww
                del L.levelmaster[ww]
                if len(L.levelmaster) == 0:
                    L.levelmaster.update({4:[0,[],[]]})
            for ll in L.levelmaster:
                if mpos2 == (x,y):
                    self.selectedlevel = ll
                x += 1
                if x == 16:
                    y += 1
                    x = 5
            if self.selectedlevel != -1:
                if mpos2 == (7,15):
                    if self.removal:
                        self.removal = False
                    else:
                        self.removal = True
                if mpos2 == (6,10):
                    L.levelmaster[self.selectedlevel][0] += 1
                if mpos2 == (7,10):
                    L.levelmaster[self.selectedlevel][0] -= 1
                x = 5
                y = 12
                for ll in enemy.list:
                    if mpos2 == (x,y):
                        if self.removal:
                            if ll in L.levelmaster[self.selectedlevel][1]:
                                chck = 0
                                for ww in L.levelmaster[self.selectedlevel][1]:
                                    if ww == ll:
                                        thing = chck
                                    chck += 1
                                L.levelmaster[self.selectedlevel][2][thing] -= 1
                                if L.levelmaster[self.selectedlevel][2][thing] < 1:
                                    L.levelmaster[self.selectedlevel][1].remove(ll)
                                    del L.levelmaster[self.selectedlevel][2][thing]

                        else:
                            if ll in L.levelmaster[self.selectedlevel][1]:
                                chck = 0
                                for ww in L.levelmaster[self.selectedlevel][1]:
                                    if ww == ll:
                                        thing = chck
                                    chck += 1
                                L.levelmaster[self.selectedlevel][2][thing] += 1
                            else:
                                L.levelmaster[self.selectedlevel][1].append(ll)
                                L.levelmaster[self.selectedlevel][2].append(1)
                    x += 5
                    if x >= 25:
                        y += 1
                        x = 5
        if mpos2 == vec(0,0):
            self.crossvec = vec(1,0)
            self.get_levelcontents()
            self.creating = True
        if mpos2 in self.connections:
            self.crossvec = mpos2
            self.get_levelcontents()
            self.creating = True
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
O.creating = False
O.selectedlevel = -1
O.removal = False
maps = [(5, 6), (5, 10), (7, 8), (9, 6), (9, 10), (7, 12), (7, 4), (7, 4), (9, 2), (9, 2), (9, 14), (11, 12), (11, 8), (11, 4), (13, 2), (13, 6), (13, 10), (13, 14), (15, 4), (15, 8), (15, 12), (17, 14), (17, 10), (17, 6), (17, 2), (19, 4), (19, 8), (19, 12), (21, 14), (21, 10), (21, 6), (21, 2), (23, 4), (25, 6), (27, 8), (25, 10), (23, 12), (23, 8)]
for x in maps:
    O.maps.append(vec(x))
O.mapmaster = {1:{0: [2,[swordguy,grosehound],[2, 1]],1: [2,[swordguy,grosehound],[2, 2]],2: [2,[swordguy,grosehound,magee],[2, 2, 1]],3: [2,[swordguy,grosehound,magee],[2, 2, 1]],4: [2,[swordguy,magee,archer,grosehound],[2, 1, 1, 1]],5: [3,[swordguy,magee,grosehound,archer],[2, 1, 1, 1]],6: [3,[magee,rentoron,archer],[1, 1, 1]],7: [3,[magee,archer,rentoron],[1, 1, 1]],8: [3,[archer,rentoron],[1, 1]],9: [3,[grosehound,rentoron,archer],[1, 2, 1]],10: [5,[magee,archer,rentoron,grosehound],[1, 2, 1, 2]],11: [5,[magee,archer,rentoron],[1, 2, 1]],12: [5,[grosehound,rentoron,swordguy],[1, 1, 1]],13: [5,[swordguy,magee,archer,grosehound],[1, 1, 2, 1]],14: [5,[swordguy,magee,rentoron],[1, 2, 1]],15: [7,[swordguy,magee,archer,grosehound],[1, 2, 1, 1]],16: [7,[magee,archer,grosehound],[1, 1, 1]],17: [7,[magee,conrift,archer],[1, 1, 1]],18: [7,[magee,conrift,archer],[1, 1, 1]],19: [7,[magee,conrift,archer,grosehound],[1, 1, 1, 1]],20: [9,[swordguy,magee,conrift,archer,rentoron],[3, 2, 1, 2, 1]],21: [9,[swordguy,magee,conrift,archer],[1, 1, 1, 1]],22: [9,[swordguy,magee,grosehound,rentoron,archer],[1, 1, 1, 1, 1]],23: [9,[swordguy,magee,conrift,archer],[1, 1, 1, 1]],24: [9,[swordguy,magee,conrift,archer],[1, 1, 1, 1]],25: [11,[magee,conrift],[1, 1]],26: [12,[magee,conrift,archer],[5, 3, 1]],27: [12,[magee,conrift,archer,rentoron],[1, 1, 1, 1]],28: [13,[magee,conrift,grosehound],[1, 1, 2]],29: [14,[magee,conrift,grosehound],[1, 1, 2]],30: [15,[magee,conrift,grosehound],[1, 1, 2]]},0:{4: [2,[dva],[1]],5: [10,[swordguy],[1]],6: [1,[stunte],[1]]},-1:{14: [2,[spsword],[1]],15: [2,[magee],[1]],16: [2,[magee],[1]],17: [2,[boulderine],[1]],18: [1,[archer],[1]]}}

O.get_connections()

class test():
    def create_map(self):
        L.levelid = {}
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
        tier = 'battle'
        L.tierasiquest = vec(0,0)
        L.tiersecq = vec(0,0)
        Q.currentquest = 0
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
                    L.make(enemies,tier,x)
            else:
                L.make(line,[],tier,x)
            if x.x == 28:
                L.levelid.update({(x.x,x.y):[[cbm],'battle']})
            line += 1         
                
T = test()


class level():
    def __init__(self):
        self.level = 0
        self.crossvec = 0

    def clickmenu(self):
        if self.switchbutton.collidepoint(pos):
            main.current_state = 'switch'
    def create_icons(self):
        pos = vec(20,30)
        x = int(pos.x*WIDTHTILESIZE-230)
        y = int(pos.y*HEIGHTTILESIZE-35)
        rect = pg.Rect(x, y, 135, 30)
        self.switchbutton = pg.draw.rect(screen,BLACK,rect)
        self.switchtext = ['Party',20,WHITE,x+5, y]
    def draw_icons(self):
        pg.draw.rect(screen,BLACK,self.switchbutton)
        a = self.switchtext
        draw_text(a[0],a[1],a[2],a[3], a[4])
    def draw_currentposition(self):
        pos = self.crossvec
        goal_center = (int(pos.x * WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2), int(pos.y * HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2))
        screen.blit(cross, cross.get_rect(center=goal_center))
        ll =  0
        for x in self.levelid:
            loc = vec(x)
            #try:
                #draw_text(str(self.display_costs[ll]),20,BLACK,loc.x*HEIGHTTILESIZE*2,loc.y*HEIGHTTILESIZE*2)
                #print(self.display_costs[ll],'ll',ll)
                #print(len(self.levelid))
            #except:
             #   pass
            
            ll += 1
            if x in self.barrier:
                pg.draw.circle(screen,RED,(int(loc.x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(loc.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)),5)
            elif self.levelid[x][1] == 'shop':
                pg.draw.circle(screen,BLUE,(int(loc.x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(loc.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)),5)
            elif x == self.tierasiquest or x == self.tiersecq and Q.active == True:
                pg.draw.circle(screen,YELLOW,(int(loc.x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(loc.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)),5)
            else:
                pg.draw.circle(screen,BLACK,(int(loc.x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(loc.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)),5)
    def draw_linestoconnections(self):
        if not M.tutorial:
            for x in self.connections:
                pg.draw.line(screen, BLUE, (int(self.crossvec.x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(self.crossvec.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int(x.x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(x.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
        #a,b = self.finddis(self.crossvec)
        #print(a ** random.choice([1.5,1.55,1.6]))
        #pg.draw.line(screen, BLUE, (int(self.crossvec.x*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2),int(self.crossvec.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int(b.x*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2),int(b.y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
        for x in self.drawdis:
            x2 = int(x)
            y = self.tierasi[x]
            dis = self.drawdis[x]
            dis2 = int(dis)
            once = True
            while dis > 0:
                if dis <= dis2/2 and once:
                    pg.draw.line(screen, BLUE, (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int((x+2)*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
                    x += 2
                    once = False
                pg.draw.line(screen, BLUE, (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int((y-1)*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
                y -= 1
                dis -= 1
                
            while dis < 0:
                if dis >= dis2/2 and once:
                    pg.draw.line(screen, BLUE, (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int((x+2)*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
                    x += 2
                    once = False
                pg.draw.line(screen, BLUE, (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int((y+1)*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
                y += 1
                dis += 1
            while x != x2 + 4:
                pg.draw.line(screen, BLUE, (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int((x+1)*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
                x += 1
    def create_map(self):
        self.levelid = {}
        self.drawdis = {}
        self.levelstatus = []
        self.path = {}
        self.pathloc = []
        tier = {}
        self.tierasi = {}
        line = 0
        self.closest = {}
        self.tierasiquest = 0
        tierquest = []
        self.tiersecq = []
        char = random.choices(Q.events,Q.eventchance)[0]
        Q.currentquest = char
        typeoq = Q.questmaster[char]['typeoq']
        for x in self.levels:
            if x.x % 4 == 1:
                if x.x not in tier:
                    tier.update({x.x:[x.y]})
                else:
                    tier[x.x].append(x.y)
            elif 7 < x.x < 12:
                tierquest.append(x)
            if typeoq == 'hunt':
                if x.x > 15:
                    self.tiersecq.append(x)
        for x in tier:
            l = random.choice(tier[x])
            self.tierasi.update({x:l})
        
        l = random.choice(tierquest)
        self.tierasiquest = l
        if typeoq == 'gauntlet':
            Q.glevel = 0
        if typeoq == 'hunt':
            self.tiersecq = random.choice(self.tiersecq)
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
                    pg.draw.line(screen, BLUE, (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int((x+1)*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
                    x += 2
                    once = False
                    self.pathloc.append(vec(x,y))
                pg.draw.line(screen, BLUE, (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int((y-1)*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
                y -= 1
                dis -= 1
                self.pathloc.append(vec(x,y))
            while dis < 0:
                if dis >= dis2/2 and once:
                    pg.draw.line(screen, BLUE, (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int((x+1)*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
                    x += 2
                    once = False
                    self.pathloc.append(vec(x,y))
                pg.draw.line(screen, BLUE, (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int((y+1)*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
                y += 1
                dis += 1
                self.pathloc.append(vec(x,y))
            while x != x2 + 4:
                pg.draw.line(screen, BLUE, (int(x*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)), (int((x+1)*WIDTHTILESIZE*2+WIDTHTILESIZE*2/2),int(y*HEIGHTTILESIZE*2+HEIGHTTILESIZE*2/2)))
                x += 1
                self.pathloc.append(vec(x,y))
        save = 0
        self.display_costs = []
        for x in self.levels:
            level = 0
            tier = random.choices(['battle','event'],[70,30])[0]
            if x.x in self.tierasi:
                if x.y == self.tierasi[x.x]:
                    tier = 'shop'
            if x == self.tierasiquest:
                tier = 'quest'
            if typeoq == 'hunt':
                if x == self.tiersecq:
                    tier = 'quest'
            if tier == 'event':
                enemies = random.choices(re.events,re.eventchance)[0]
                self.make(enemies,tier,x)
            elif tier == 'battle':
                if x.x in self.levelmaster:
                    level,b = self.finddis(x)
                    enemies = []
                    level **= random.choice([1.4,1.41,1.42,1.43,1.45,1.46,1.47,1.48,1.49,1.5])
                    level += x.x**0.85
                    level = int(round(level))
                    if level > save:
                        save = level
                    if level > 30:
                        level = 30
                    cost = self.levelmaster[level][0]
                    
                    while cost >= 1:
                        if len(enemies) == 5:
                            break
                        enemy = random.choices(self.levelmaster[level][1],self.levelmaster[level][2])
                        remove = self.get_cost(enemy)
                        cost -= remove
                        enemies.append(enemy[0])
                    self.make(enemies,tier,x)
            elif tier == 'quest':
                self.make(char,tier,x)
                self.savequest = x
                self.savex = x
            else:
                self.make([],tier,x)
            if x.x == 28:
                self.make([cbm,magee,magee],'battle',x)
            self.display_costs.append(level)
            line += 1         
    def get_connections(self):
        self.connections = []
        possible = [vec(1,0),vec(1,-1),vec(1,1),vec(0,1),vec(0,-1),vec(-1,0),vec(-1,-1),vec(-1,1)]
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
        
        if magee in target:
            cost += 5
        if swordguy in target:
            cost += 4
        if conrift in target:
            cost += 7
        if archer in target:
            cost += 3
        if boulderine in target:
            cost += 5
        if spsword in target:
            cost += 2
        if rentoron in target:
            cost += 4
        if grosehound in target:
            cost += 2
        if dva in target:
            cost += 9
        if stunte in target:
            cost += 1
        return cost
    def make(self,enemies,tier,x):
        self.levelid.update({(x.x,x.y):[enemies,tier]})
    def nextlevel(self):
        if lock == True:
            if mpos2 in self.connections:
                self.turns += 1
                if self.click == True:
                    if self.turns % 3 == 0:#creates barrier red dots 
                        self.border += 1
                        for ll in self.levels:
                            if ll.x == self.border:
                                self.barrier.append(ll)
                                L.levelid[(ll.x,ll.y)][0] = [barrier] #creates barrier red dots 

                    self.crossvec = mpos2
                    self.level = mpos2.x - 3
                    e,tier = self.getlevel()
                    if self.level == 1:
                        pass
                        #M.restart()
                    if mpos2 in self.barrier:
                        M.start()
                        tier = 'battle'
                    elif 'battle' == tier:
                        M.start()
                        M.typeobattle = 'normal'
                    elif 'shop' == tier:
                        shop.shopstart()
                    L.get_connections()
                    self.savestate = tier
                    M.tran = True
                    self.click = False
        else:
            if self.click == True:
                self.turns += 1
                self.crossvec = mpos2
                self.level = mpos2.x - 3
                e,tier = self.getlevel()
                if self.level == 1:
                    pass
                    #M.restart()
                if mpos2 in self.barrier:
                    M.start()
                    tier = 'battle'
                elif 'battle' == tier:
                    M.start()
                    M.typeobattle = 'normal'
                elif 'shop' == tier:
                    shop.shopstart()
                L.get_connections()
                self.savestate = tier
                M.tran = True
                
                self.click = False
    def getlevel(self):
        if mpos2 in self.levelstatus and mpos2 not in self.barrier:
            main.current_state = 'map'
            e = 0
            tier = 'map'
        else:
            for x in self.levelid:
                if x == mpos2:
                    e = self.levelid[x][0]
                    tier = self.levelid[x][1]
        return e,tier


cross = pg.image.load(os.path.join(filename,'cross-1.png.png'))
cross = pg.transform.scale(cross, (WIDTHTILESIZE*2, HEIGHTTILESIZE*2))

L = level()
L.level = 0
L.crossvec = vec(3,8)
L.connections =[]
L.click = False
L.levelindex = {}
L.levels = []
L.turns = 0
L.border = 3
L.barrier = []
levels = [(4, 7), (4, 8), (4, 9), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (10, 14), (10, 13), (10, 12), (10, 11), (10, 10), (10, 9), (10, 8), (10, 7), (10, 6), (10, 5), (10, 4), (10, 3), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2), (21, 2), (22, 2), (27, 8), (27, 7), (27, 9), (26, 9), (26, 8), (26, 7), (26, 6), (26, 10), (25, 10), (25, 11), (25, 9), (25, 8), (25, 7), (25, 6), (25, 5), (24, 5), (24, 4), (23, 3), (23, 4), (11, 14), (12, 14), (13, 14), (14, 14), (15, 14), (24, 12), (24, 11), (23, 12), (23, 13), (22, 13), (22, 14), (21, 14), (20, 14), (18, 14), (19, 14), (17, 14), (16, 14), (16, 13), (15, 13), (13, 13), (14, 13), (12, 13), (11, 13), (11, 12), (12, 12), (13, 12), (14, 12), (15, 12), (16, 12), (17, 12), (17, 13), (18, 13), (18, 12), (19, 12), (19, 13), (20, 13), (20, 12), (21, 12), (21, 13), (22, 12), (22, 11), (23, 11), (23, 10), (24, 10), (24, 9), (23, 9), (24, 8), (23, 8), (24, 7), (23, 7), (24, 6), (23, 6), (23, 5), (22, 5), (22, 4), (22, 3), (21, 3), (21, 4), (20, 4), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (11, 4), (12, 4), (13, 4), (14, 4), (15, 4), (16, 4), (17, 4), (19, 4), (18, 4), (18, 5), (17, 5), (16, 5), (15, 5), (14, 5), (13, 5), (12, 5), (11, 5), (11, 6), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6), (19, 5), (20, 5), (20, 6), (21, 6), (21, 5), (22, 6), (22, 7), (22, 8), (22, 9), 
(22, 10), (21, 10), (21, 11), (21, 9), (21, 8), (21, 7), (20, 7), (20, 8), (20, 9), (20, 10), (20, 11), (19, 11), (19, 10), (19, 9), (19, 8), (19, 7), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11), (17, 11), (17, 10), (17, 
9), (17, 8), (17, 7), (16, 7), (16, 8), (16, 9), (16, 10), (16, 11), (15, 11), (15, 10), (15, 9), (15, 8), (15, 7), (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (13, 11), (12, 11), (11, 11), (11, 10), (12, 10), (13, 10), 
(13, 9), (12, 9), (11, 9), (11, 8), (12, 8), (13, 8), (13, 7), (12, 7), (11, 7),[28, 8]]
for x in levels:
    if x not in L.levels:
        L.levels.append(vec(x))

L.create_icons()

class quest():
    def __init__(self):
        self.vec = 0
    def addevent(self,char,dialouge,enemies,typeoq,chance,back):
        self.questmaster.update({char:{'enemies':enemies,'dialouge':dialouge,'typeoq':typeoq,'map':back}})
        self.events.append(char)
        self.eventchance.append(chance)
    def getmap(self):
        return self.questmaster[self.currentquest]['map']
    def click(self):
        self.done += 1

        if self.questmaster[self.currentquest]['typeoq'] == 'hunt':
            if L.crossvec == L.tierasiquest:
                if self.done >= len(self.questmaster[self.currentquest]['dialouge'][0]):
                    M.addchar(self.currentquest)
                    main.current_state = 'map'
                    self.active = True
                    self.done = 0
                    self.savedone += 1
            else:
                if self.done >= len(self.questmaster[self.currentquest]['dialouge'][1]):
                    main.current_state = 'battle'
                    L.levelid.update({(L.savequest.x,L.savequest.y):[self.questmaster[self.currentquest]['enemies'],'battle']})
                    M.start()
                    self.done = 0
                    self.savedone = 0
        if self.questmaster[self.currentquest]['typeoq'] == 'gauntlet':
            if self.done >= len(self.questmaster[self.currentquest]['dialouge']):
                if self.active:
                    main.current_state = 'battle'
                    M.typeobattle = 'gauntlet'
                    L.levelid.update({(L.savequest.x,L.savequest.y):[self.questmaster[self.currentquest]['enemies'][self.glevel],'battle']})
                    self.glevel += 1
                    if self.glevel == len(self.questmaster[self.currentquest]['enemies']):
                        self.glevel = 0
                        self.done = 0
                    M.start()
                else:
                    M.addchar(self.currentquest)
                    main.current_state = 'battle'
                    L.levelid.update({(L.savequest.x,L.savequest.y):[self.questmaster[self.currentquest]['enemies'][self.glevel],'battle']})
                    self.glevel += 1
                    M.typeobattle = 'gauntlet'
                    M.start()
                    self.active = True
        else:
            if self.done >= len(self.questmaster[self.currentquest]['dialouge']):
                if self.questmaster[self.currentquest]['typeoq'] == 'battle':
                    M.addchar(self.currentquest)
                    main.current_state = self.questmaster[self.currentquest]['typeoq']
                    L.levelid.update({(L.savequest.x,L.savequest.y):[self.questmaster[self.currentquest]['enemies'],'battle']})
                    M.start()
                    self.done = 0
                
                
    def draw_quest(self):
        x = int(WIDTH/2)
        y = int(HEIGHT/2+300)
        rect = pg.Rect(0, 0, 1400, 400)
        rect.center = x,y
        pg.draw.rect(screen,BLACK,rect)

        
        if type(self.questmaster[self.currentquest]['dialouge'][0]) is not list:
            txt = self.questmaster[self.currentquest]['dialouge'][self.done]
        else:
            txt = self.questmaster[self.currentquest]['dialouge'][self.savedone][self.done]
        if txt != 0:
            draw_text_center(txt,50,WHITE,x,y)
        else:
            self.click()
    def eventstart(self):
        self.currentquest,e = L.getlevel()
        Bg.background_current = self.questmaster[self.currentquest]['map']

Q = quest()
Q.questmaster = {}
Q.events = []
Q.eventchance = []
Q.done = 0
Q.savedone = 0
Q.active = False
Q.addevent(Cri,['There is a audible fight happening over the ridge','You approach and find a mage battling a large enemy'],[swordguy],'battle',60,background_fall)
Q.addevent(Hap,[['You reach the entrance to an inn',"As you're about to enter some one flies through the door",'he picks him self up sighing "no one will help me"','Help you with what','A vendeta',"you take a second","I'll help, if you join me",'deal'],['There he is you ready',"As ready as i'll ever be"]],[swordguy],'hunt',40,background_fall)
Q.addevent(nover,['empty','empty'],[[swordguy],[rentoron]],'gauntlet',40,background_dungeon)

class ui():
    def __init__(self):
        x = int(WIDTH/2)
        y = int(HEIGHT/2-300)
        text = 'HALOOD'
        self.gamenametext = [text,80,RED,x, y-5]
        
        
        
        x = int(WIDTH/2)
        y = int(HEIGHT/2-100)
        self.play = pg.Rect(0, 0, 300, 80)
        self.play.center = x,y
        text = 'Play'
        self.playtext = [text,50,WHITE,x, y-5]
        x = int(WIDTH/2)
        y = int(HEIGHT/2+200)
        self.quit = pg.Rect(0, 0, 300, 80)
        self.quit.center = x,y
        text = 'Quit'
        self.quittext = [text,50,WHITE,x, y-5]
        x = int(WIDTH/2)
        y = int(HEIGHT/2)
        self.continuebutton = pg.Rect(0, 0, 300, 80)
        self.continuebutton.center = x,y
        text = 'Continue'
        self.continuetext = [text,50,WHITE,x, y-5]
        x = int(WIDTH/2)
        y = int(HEIGHT/2+100)
        self.setbutton = pg.Rect(0, 0, 300, 80)
        self.setbutton.center = x,y
        text = 'Settings'
        self.settext = [text,50,WHITE,x, y-5]
        
        
        x = int(WIDTH/2)
        y = int(HEIGHT/2-100)
        self.pausebutton = pg.Rect(0, 0, 300, 80)
        self.pausebutton.center = x,y
        text = 'continue'
        self.pausetext = [text,50,WHITE,x, y-5]
        x = int(WIDTH/2)
        y = int(HEIGHT/2)
        self.menubutton = pg.Rect(0, 0, 300, 80)
        self.menubutton.center = x,y
        text = 'menu'
        self.menutext = [text,50,WHITE,x, y-5]
        
        x = int(WIDTH/2)
        y = int(HEIGHT/2-100)
        self.fancybutton = pg.Rect(0, 0, 550, 80)
        self.fancybutton.center = x,y
        text = 'turn on/off fancy graphics'
        self.fancytext = [text,50,WHITE,x, y-5]
        self.fancydisp = pg.Rect(0, 0, 200, 80)
        self.fancydisp.center = x+400,y
        text = 0
        self.fancydisptext = [text,50,WHITE,x+400, y-5]
        
        x = int(WIDTH/2)
        y = int(HEIGHT/2)
        self.musicvolbutton = pg.Rect(0, 0, 550, 80)
        self.musicvolbutton.center = x,y
        text = 'music volume'
        self.musicvoltext = [text,50,WHITE,x, y-5]
        self.musicvoldisp = pg.Rect(0, 0, 200, 80)
        self.musicvoldisp.center = x+400,y
        text = 0
        self.musicvoldisptext = [text,50,WHITE,x+400, y-5]
        
        x = int(WIDTH/2)
        y = int(HEIGHT/2+100)
        self.donebutton = pg.Rect(0, 0, 300, 80)
        self.donebutton.center = x,y
        text = 'done'
        self.donetext = [text,50,WHITE,x, y-5]
        
    def display_dialouge(self):
        if main.current_state == 'quest':
            Q.l.quest_dialouge(0)
        if main.current_state == 'hunt':
            Q.l.quest_dialouge(1)
    def dialouge(self):
        self.done += 1
    def drawbuttons(self):
        if self.pause:
            pg.draw.rect(screen,BLACK,self.pausebutton)
            a = self.pausetext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
            pg.draw.rect(screen,BLACK,self.menubutton)
            a = self.menutext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
            pg.draw.rect(screen,BLACK,self.quit)
            a = self.quittext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
        elif self.settings:
            pg.draw.rect(screen,BLACK,self.fancybutton)
            a = self.fancytext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
            pg.draw.rect(screen,BLACK,self.fancydisp)
            a = self.fancydisptext
            draw_text_center(str(M.fancy),a[1],a[2],a[3],a[4])
            
            pg.draw.rect(screen,BLACK,self.musicvolbutton)
            a = self.musicvoltext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
            
            pg.draw.rect(screen,BLACK,self.musicvoldisp)
            a = self.musicvoldisptext
            draw_text_center(str(round(pg.mixer.music.get_volume()*10)*10),a[1],a[2],a[3],a[4])
            
            
            pg.draw.rect(screen,BLACK,self.donebutton)
            a = self.donetext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
        else:
            a = self.gamenametext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
            pg.draw.rect(screen,BLACK,self.play)
            a = self.playtext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
            
            pg.draw.rect(screen,BLACK,self.continuebutton)
            a = self.continuetext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
            
            pg.draw.rect(screen,BLACK,self.setbutton)
            a = self.settext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
            
            pg.draw.rect(screen,BLACK,self.quit)
            a = self.quittext
            draw_text_center(a[0],a[1],a[2],a[3],a[4])
            
        
        
        
    def menu(self):
        s = pg.Surface((1920,1080))  # the size of your rect
        s.set_alpha(200)                # alpha level
        s.fill((100,100,100 ))           # this fills the entire surface
        screen.blit(s, (0,0)) 
        self.drawbuttons()
    def buttons(self):
        if self.pause:
            if self.play.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
                self.pause = False
            if self.menubutton.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
                self.save_state = main.current_state
                main.current_state = 'menu'
                self.pause = False
        elif self.settings:
            if self.donebutton.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
                self.settings = False
            if self.fancybutton.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
                if M.fancy:
                    M.fancy = False
                else:
                    M.fancy = True
            if self.musicvolbutton.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
                ll = pg.mixer.music.get_volume() + 0.2
                if ll > 1:
                    ll = 0.0
                pg.mixer.music.set_volume(ll)
                
        else:    
            if self.play.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
                main.current_state = 'map'
                L.levelmaster = O.mapmaster[-1]
                tut.create_map()
                L.crossvec = vec(13,8)
                L.get_connections()
                tut.tutorial_restart()
                H.exp = 9
                M.tutorial = True
            if self.continuebutton.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
                main.current_state = self.save_state
            if self.setbutton.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
                self.settings = True
        if self.quit.collidepoint(int(truepos.x),int(truepos.y)):
            self.running = False
            pg.quit
        
    
ui = ui()

ui.pause = False
ui.settings = False
ui.save_state = 'overmap'
ui.done = 0



class randomevent():
    def __init__(self):
        self.vec = 0
    def addevent(self,name,dialouge,typeoe,reward,chance,back):
        self.eventmaster.update({name:{'type':typeoe,'dialouge':dialouge,'reward':reward,'map':back}})
        self.events.append(name)
        self.eventchance.append(chance)
    def getmap(self):
        return self.eventmaster[self.currentevent]['map']
    def click(self):
        if self.savedone == -1:
            self.done += 1
        else: 
            self.done += 1
            self.savedone  = -1
        if self.done >= len(self.eventmaster[self.currentevent]['dialouge']):
            M.tran = True
            self.done = 0
            if self.eventmaster[self.currentevent]['type'] == 'gold':
                main.amountmoney += self.eventmaster[self.currentevent]['reward']
            if self.eventmaster[self.currentevent]['type'] == 'blessing':
                B.addinventory(self.eventmaster[self.currentevent]['reward'])
            if self.eventmaster[self.currentevent]['type'] == 'xp':
                for x in M.allies:
                    x.exp += 10
                    x.checklevel()
            if self.eventmaster[self.currentevent]['type'] == 'better blessing':
                B.addbetterinventory(self.eventmaster[self.currentevent]['reward'])
    def draw_event(self):
        x = int(WIDTH/2)
        y = int(HEIGHT/2+300)
        rect = pg.Rect(0, 0, 1400, 400)
        rect.center = x,y
        pg.draw.rect(screen,BLACK,rect)
        
        if type(self.eventmaster[self.currentevent]['dialouge'][self.done]) is not list:
            txt = self.eventmaster[self.currentevent]['dialouge'][self.done]
        else:
            if self.savedone != -1:
                txt = self.savedone
            else:    
                self.savedone = random.choice(self.eventmaster[self.currentevent]['dialouge'][self.done])
                txt = self.savedone
        if txt != 0:
            draw_text_center(txt,50,WHITE,x,y)
        else:
            self.click()
    def eventstart(self):
        self.currentevent,e = L.getlevel()
re = randomevent()
re.eventmaster = {}
re.events = []
re.eventchance = []
re.done = 0
re.savedone = -1
re.addevent('unimportant hill',['You found a small hill nothing important',['The earth is stained with what looks like a fight that happend eons ago',0,'It seems that the hill is man made']],'empty',0,60,background_fall)
re.addevent('improtant hill',['You found a small hill seems like a battle happend','You found 20 gold'],'gold',20,40,background_fall)
re.addevent('broken ultar',['You found a hidden ultar','As you aproach, the ultar glows','then crumbles'],'blessing',0,10,background_fall)
re.addevent('functioning ultar',['You found a hidden ultar','As you aproach, the ultar glows','Then burns'],'blessing',1,10,background_fall)
re.addevent('devine ultar',['You found a hidden ultar','As you aproach, the ultar glows','Light fills the air'],'better blessing',1,5,background_fall)
re.addevent('unispiring plains',['You come across some plains','The reeds whistle in the wind','You find nothing important'],'empty',0,60,background_fall)
re.addevent('ispiring plains',['You come across some plains','The reeds whistle in the wind','You find that some how, you learnt something'],'xp',10,30,landscape_mountain)

class blessings():
    def __init__(self):
        self.vec = 0
    def draw_blessingi(self):
        pass
    def checkblessing(self,version,when,amount,target,aimed,dup):
        if when == 'attacking':
            amount = version.attack(amount,target,aimed,dup)
        if when == 'passive':
            amount = version.passive(amount,target)
        if when == 'endpassive':
            amount = version.endpassive(amount,target)
        if when == 'defending':
            amount = version.defend(amount,target,aimed,dup)
        return amount
    def init_inventory(self):
        for z in self.inventory:
            pos = self.inventory[z][1]
            x = int(pos.x*WIDTHTILESIZE-230)
            y = int(pos.y*HEIGHTTILESIZE-35)
            rect = pg.Rect(x, y, 50, 50)
            self.inventory[z][0] = rect
    def addblessing(self,thing,less,norm,great,ultra,chan):
        self.master.update({thing:[less,norm,great,ultra]})
        self.masterrand.append(thing)
        self.masterchance.append(chan)
    def addinventory(self,amount):
        for x in range(0,amount):
            gen = random.choices(self.masterrand,self.masterchance)[0]
            spec = random.choices(self.master[gen],[60,30,20,10])[0]
            i = 0
            for y in self.inventory:
                i +=1
            self.inventory.update({i:[gen,spec]})
            self.test.append(spec)
    def addbetterinventory(self,amount):
        for x in range(0,amount):
            gen = random.choices(self.masterrand,self.masterchance)[0]
            spec = random.choices(self.master[gen],[30,40,30,20])[0]
            i = 0
            for y in self.inventory:
                i +=1
            self.inventory.update({i:[gen,spec]})
            self.test.append(spec)
    class halood():
        def __init__(self):
            self.vec = 0
        class lesser():
            def __init__(self):
                self.vec = 0
            def attack(self,amount,target,aimed,dup):
                M.allies[target][1] -= 5
                return amount
            def passive(self,amount,target):
                return amount
            def endpassive(self,amount,target):
                M.allies[target][1] += 10
                return amount
            def defend(self,amount,target,aimed,dup):
                return amount
        class normal():
            def __init__(self):
                self.vec = 0
            def attack(self,amount,target,aimed,dup):
                amount += 10
                hit = random.choice([True,False])
                if hit:
                    M.allies[target][1] -= 5
                return amount
            def passive(self,amount,target):
                return amount
            def endpassive(self,amount,target):
                M.allies[target][1] += 10
                return amount
            def defend(self,amount,target,aimed,dup):
                return amount
        class greater():
            def __init__(self):
                self.vec = 0
            def attack(self,amount,target,aimed,dup):
                amount += 10
                hit = random.choices([True,False],[30,70])[0]
                if hit:
                    M.allies[target][1] -= 5
                return amount
            def passive(self,amount,target):
                M.allies[target][1] += 5
                return amount
            def endpassive(self,amount,target):
                return amount
            def defend(self,amount,target,aimed,dup):
                return amount
        class ultrated():
            def __init__(self):
                self.vec = 0
            def attack(self,amount,target,aimed,dup):
                amount += 10
                return amount
            def passive(self,amount,target):
                M.allies[target][1] += 5
                if M.allies[target][1] > target.health:
                    M.allies[target][1] = target.health
                return amount
            def endpassive(self,amount,target):
                M.allies[target][1] += 5
                if M.allies[target][1] > target.health:
                    M.allies[target][1] = target.health
                return amount
            def defend(self,amount,target,aimed,dup):
                return amount
    class tulem():
        def __init__(self):
            self.vec = 0
        class lesser():
            def __init__(self):
                self.vec = 0
            def attack(self,amount,target,aimed,dup):
                amount += 10
                return amount
            def passive(self,amount,target):
                return amount
            def endpassive(self,amount,target):
                return amount
            def defend(self,amount,target,aimed,dup):
                return amount
        class normal():
            def __init__(self):
                self.vec = 0
            def attack(self,amount,target,aimed,dup):
                if bleed in M.enemy[aimed][dup][4]:
                    M.enemy[aimed][dup][4][bleed] += 1
                else:
                    M.enemy[aimed][dup][4].update({bleed:1})
                amount += 10
                return amount
            def passive(self,amount,target):
                return amount
            def endpassive(self,amount,target):
                return amount
            def defend(self,amount,target,aimed,dup):
                return amount
        class greater():
            def __init__(self):
                self.vec = 0
            def attack(self,amount,target,aimed,dup):
                amount += 10
                if bleed in M.enemy[aimed][dup][4]:
                    M.enemy[aimed][dup][4][bleed] += 1
                else:
                    M.enemy[aimed][dup][4].update({bleed:1})
                hit = random.choices([True,False],[30,70])[0]
                if hit:
                    if pierce in M.enemy[aimed][dup][4]:
                        M.enemy[aimed][dup][4][pierce] += 1
                    else:
                        M.enemy[aimed][dup][4].update({pierce:1})
                return amount
            def passive(self,amount,target):
                return amount
            def endpassive(self,amount,target):
                return amount
            def defend(self,amount,target,aimed,dup):
                return amount
        class ultrated():
            def __init__(self):
                self.vec = 0
            def attack(self,amount,target,aimed,dup):
                amount *= 2
                if bleed in M.enemy[aimed][dup][4]:
                    M.enemy[aimed][dup][4][bleed] += 1
                else:
                    M.enemy[aimed][dup][4].update({bleed:1})
                if pierce in M.enemy[aimed][dup][4]:
                    M.enemy[aimed][dup][4][pierce] += 1
                else:
                    M.enemy[aimed][dup][4].update({pierce:1})
                return amount
            def passive(self,amount,target):
                return amount
            def endpassive(self,amount,target):
                return amount
            def defend(self,amount,target,aimed,dup):
                hit = random.choices([True,False],[30,70])
                if hit == True:
                    amount /= 2
                return amount

B = blessings()
B.inventory = {}
B.master = {}
B.masterrand = []
B.masterchance = []
B.test = []

haloodblessing = B.halood()

hblesser = haloodblessing.lesser()
hblesser.text = 'Halood Lesser'
hblesser.txt = 'Attacks will remove 5 health, also at the end of combat 10 health will be restored.'
hb_lesser_img = pg.image.load(os.path.join(filename,'halood_blessing0.png')).convert_alpha()
hblesser.img = pg.transform.scale(hb_lesser_img, (64, 64))
hbnormal = haloodblessing.normal()
hbnormal.text = 'Halood Normal'
hbnormal.txt = 'Attacks will deal more damage and randomly remove 10 health, also at the end of combat 10 health will be restored.'
hb_normal_img = pg.image.load(os.path.join(filename,'halood_blessing1.png')).convert_alpha()
hbnormal.img = pg.transform.scale(hb_normal_img, (64, 64))
hbgreater = haloodblessing.greater()
hbgreater.text = 'Halood Greater'
hbgreater.txt = 'Attacks will deal more damage and rarely remove 10 health, also at the end of each turn 5 health will be restored.'
hb_greater_img = pg.image.load(os.path.join(filename,'halood_blessing2.png')).convert_alpha()
hbgreater.img = pg.transform.scale(hb_greater_img, (64, 64))
hbultrated = haloodblessing.ultrated()
hbultrated.text = 'Halood Ultrated'
hbultrated.txt = 'Attacks will deal more damage will never remove health, also at the end of each turn and combat 5 health will be restored.'
hb_ultra_img = pg.image.load(os.path.join(filename,'halood_blessing3.png')).convert_alpha()
hbultrated.img = pg.transform.scale(hb_ultra_img, (64, 64))
chance = 60
B.addblessing(haloodblessing,hblesser,hbnormal,hbgreater,hbultrated,chance)

tulemblessing = B.tulem()

tblesser = tulemblessing.lesser()
tblesser.text = 'Tulem Lesser'
tblesser.txt = 'Attacks will deal more damage.'
lesser_img = pg.image.load(os.path.join(filename,'tulem_blessing0.png')).convert_alpha()
tblesser.img = pg.transform.scale(lesser_img, (64, 64))
tbnormal = tulemblessing.normal()
tbnormal.text = 'Tulem Normal'
tbnormal.txt = 'Attacks will deal more damage and apply bleed.'
normal_img = pg.image.load(os.path.join(filename,'tulem_blessing1.png')).convert_alpha()
tbnormal.img = pg.transform.scale(normal_img, (64, 64))
tbgreater = tulemblessing.greater()
tbgreater.text = 'Tulem Greater'
tbgreater.txt = 'Attacks will deal more damage and apply bleed with the chance of piercing.'
greater_img = pg.image.load(os.path.join(filename,'tulem_blessing2.png')).convert_alpha()
tbgreater.img = pg.transform.scale(greater_img, (64, 64))
tbultrated = tulemblessing.ultrated()
tbultrated.text = 'Tulem Ultrated'
tbultrated.txt = 'Attacks will deal more damage and apply bleed and piercing, also chance to reduce damage by half.'
tb_ultra_img = pg.image.load(os.path.join(filename,'tulem_blessing3.png')).convert_alpha()
tbultrated.img = pg.transform.scale(tb_ultra_img, (64, 64))
chance = 60
B.addblessing(tulemblessing,tblesser,tbnormal,tbgreater,tbultrated,chance)
'''
insen
'''
tt = 0
o = 1
for x in range(0,100):
    o = 1
    B.inventory = {}
    while tbultrated not in B.test:
        
        B.addbetterinventory(1)
        o+=1
        if o % 20 == 0:
            print(o)
            B.inventory = {}
    tt += len(B.test)
    
    B.test = []
print(tt/100)

#B.inventory = {}
#B.addinventory(5)
class obstacles():
    def __init__(self):
        self.vec = 0
    def checkifdead():
        test = dict(M.obstacles)
        for x in test:
            for y in test[x]:
                if int(y[1]) <= 0:
                    save = y[0]
                    M.obstacles[x].remove(y)
                    save = M.unconversion[save.x,save.y]
                    if save in M.allyspaces:
                        M.allyspaces[save] = 0
                    if save in M.enemyspaces:
                        M.enemyspaces[save] = 0
            if len(test[x]) <= 0:
                save = M.obstacles[x][0][0]
                del M.obstacles[x]
                save = M.unconversion[save.x,save.y]
                if save in M.allyspaces:
                    M.allyspaces[save] = 0
                if save in M.enemyspaces:
                    M.enemyspaces[save] = 0

    class tree():
        def __init__(self):
            self.vec = 0
        def areaoeffect(self):
            pass
        def damage(self,ll,damage,engaged):
            M.obstacles[self][ll][1] -= 1
            obstacles.checkifdead()
                
        
obstacles.allothem = []

tree = obstacles.tree()
tree_img = pg.image.load(os.path.join(filename,'tree0.png')).convert_alpha()
tree_img = pg.transform.scale(tree_img, (obstaclesscaledwidth, obstaclesscaledheight))
tree_img2 = pg.image.load(os.path.join(filename,'tree0.png')).convert_alpha()
tree_img2 = pg.transform.scale(tree_img2, (obstaclesscaledwidth, obstaclesscaledheight))
tree_img3 = pg.image.load(os.path.join(filename,'tree0.png')).convert_alpha()
tree_img3 = pg.transform.scale(tree_img3, (obstaclesscaledwidth, obstaclesscaledheight))
tree.combat_animation = {1:tree_img,2:tree_img2,3:tree_img3}
tree.health = 3
tree.agro = 1
tree.immunities = []
auras = [(1, 2), (0, 2), (-1, 2), (-2, 2), (-3, 2), (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (1, 0), (0, 0), (-1, 0), (-2, 0), (-3, 0), (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (1, -2), (0, -2), (-1, -2), (-2, -2), (-3, -2)]
tree.clickaura = []
for aura in auras:
    tree.clickaura.append(vec(aura))
obstacles.allothem.append(tree)
            
class battle():
    def __init__(self):
        self.current_animation = 0
        self.allies = 0
        self.enemy = 0
        self.display = 0
        self.damage = 0
        
        pos = vec(25,30)
        x = int(pos.x*WIDTHTILESIZE-230)
        y = int(pos.y*HEIGHTTILESIZE-35)
        self.swapbutton = pg.Rect(x, y, 135, 30)
        pg.draw.rect(screen,BLACK,self.swapbutton)
        self.swaptext = [0,20,WHITE,x+5, y]
        
        pos = vec(20,30)
        x = int(pos.x*WIDTHTILESIZE-230)
        y = int(pos.y*HEIGHTTILESIZE-35)
        self.exitbutton = pg.Rect(x, y, 135, 30)
        pg.draw.rect(screen,BLACK,self.exitbutton)
        text = 'map'
        self.exittext = [text,20,WHITE,x+5, y]
        
        pos = vec(30,30)
        x = int(pos.x*WIDTHTILESIZE-230)
        y = int(pos.y*HEIGHTTILESIZE-35)
        self.blessingbutton = pg.Rect(x, y, 135, 30)
        pg.draw.rect(screen,BLACK,self.blessingbutton)
        self.blessingtext = [0,20,WHITE,x+5, y]
        
    def draw_switchbuttons(self):
        
        pg.draw.rect(screen,BLACK,self.swapbutton)
        a = self.swaptext
        text = 'done'
        if self.swap == False:
            text = 'change order'
        draw_text(text,a[1],a[2],a[3],a[4])
        
        pg.draw.rect(screen,BLACK,self.exitbutton)
        a = self.exittext
        draw_text(a[0],a[1],a[2],a[3],a[4])
        
        pg.draw.rect(screen,BLACK,self.blessingbutton)
        a = self.blessingtext
        text = 'skills'
        if self.skills == False:
            text = 'blessings'
        draw_text(text,a[1],a[2],a[3],a[4])

        if self.skills == False:
            if self.selectedchar != 0:
                ally.draw_skilltree(self.selectedchar)
                if self.selectedability != 0:
                    draw_text(self.selectedchar.abilities[self.selectedability][2],20,BLACK,(self.selectedchar.abilities[self.selectedability][1].x-5)*WIDTHTILESIZE,self.selectedchar.abilities[self.selectedability][1].y*HEIGHTTILESIZE)
        else:
            pos = vec(18,4)
            for k in B.inventory:
                cur = B.inventory[k][1].img.copy()
                
                goal_center = (int(pos.x * WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2), int(pos.y * HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2))
                
                for x in M.allies:
                    if x.blessing == k:
                        cur.fill((105, 105, 105, 255),special_flags=pg.BLEND_RGB_MULT) 
                screen.blit(cur, cur.get_rect(center=goal_center))
                pos += (2,0)
                if pos.x > 26:
                    pos.x = 18
                    pos += (0,2)
            pos = vec(18,4)
            for k in B.inventory:
                if k == self.selectedblessing:  
                    if pos.x < 24:
                        rect = pg.Rect(pos.x* WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2+40,pos.y* HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2 - 80, 500, 200)
                        pg.draw.rect(screen,BLACK,rect)
                        draw_text(B.inventory[k][1].text,30,WHITE,pos.x* WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2+45,pos.y* HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2 - 80)
                        olim = 0
                        lim = 50
                        amo = 0
                        while len(B.inventory[k][1].txt) > lim:
                            lic = int(lim)
                            lim = lic + 50
                            while B.inventory[k][1].txt[lic] != ' ':
                                lic -= 1
                            lic += 1
                            draw_text(B.inventory[k][1].txt[olim:lic],20,WHITE,pos.x* WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2+45,pos.y* HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2 - 40+20*amo)
                            olim = lic
                            amo += 1

                        draw_text(B.inventory[k][1].txt[olim:],20,WHITE,pos.x* WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2+45,pos.y* HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2 - 40+20*amo)
                    else:
                        locate = 580
                        rect = pg.Rect(pos.x* WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2+40-locate,pos.y* HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2 - 80, 500, 200)
                        pg.draw.rect(screen,BLACK,rect)
                        draw_text(B.inventory[k][1].text,30,WHITE,pos.x* WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2+45-locate,pos.y* HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2 - 80)
                        olim = 0
                        lim = 50
                        amo = 0
                        while len(B.inventory[k][1].txt) > lim:
                            lic = int(lim)
                            lim = lic + 50
                            while B.inventory[k][1].txt[lic] != ' ':
                                lic -= 1
                            lic += 1
                            draw_text(B.inventory[k][1].txt[olim:lic],20,WHITE,pos.x* WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2+45-locate,pos.y* HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2 - 40+20*amo)
                            olim = lic
                            amo += 1

                        draw_text(B.inventory[k][1].txt[olim:],20,WHITE,pos.x* WIDTHTILESIZE*2 + WIDTHTILESIZE*2 / 2+45-locate,pos.y* HEIGHTTILESIZE*2 + HEIGHTTILESIZE*2 / 2 - 40+20*amo)
                pos += (2,0)
                if pos.x > 26:
                    pos.x = 18
                    pos += (0,2)
    def switch(self):
        if self.skills == False:
            if self.selectedchar != 0:
                for k in self.selectedchar.abilities:
                    if self.selectedchar.abilities[k][0].collidepoint(int(mposraw.x),int(mposraw.y)) and k not in self.selectedchar.unlockedabilites:
                        if self.selectedability != 0 and k == self.selectedability and self.selectedchar.lvl > 0:
                            self.selectedchar.skill(k)
                            self.selectedchar.lvl -= 1
                            self.selectedability = 0
                        else:
                            self.selectedability = k
        else:
            ble = False
            ple = False
            pos = vec(18,4)
            for k in B.inventory:
                if pos == (int(mpos.x/2),int(mpos.y/2)):
                    self.selectedblessing = k
                    ble = True
                pos += (2,0)
                if pos.x > 26:
                    pos.x = 18
                    pos += (0,2)
            if mpos in self.selectingchar():
                ple = True
            if ble == False and ple == False:
                self.selectedblessing = -2
                self.selectedchar = 0
            if self.selectedblessing != -2 and self.selectedchar != 0:
                self.selectedchar.blessing = self.selectedblessing
                self.selectedblessing = -2
        
            
                    
        if self.swapbutton.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
            if self.swap == False:
                self.swap = True
            elif self.swap == True:
                self.swap = False
        
        if self.blessingbutton.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
            self.selectedchar = 0
            if self.skills == False:
                self.skills = True
            elif self.skills == True:
                self.skills = False
        
        if self.exitbutton.collidepoint(int(mpos.x*WIDTHTILESIZE),int(mpos.y*HEIGHTTILESIZE)):
            main.current_state = 'map'
            L.create_icons()
            
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


    def restart(self):
        ally1 = H
        ally2 = nover
        ally3 = Cri
        
        self.selectedattack = 0
        self.selectedchar = 0
        self.current_animation = 1
        self.allies = {}
        self.enemy = {}
        self.l = []
        self.actions = []
        
        L.turns = 0
        L.border = 3
        L.barrier = []
        for x in M.alliessave:
            x.unlockedabilites = []
            x.exp = 0
            x.lvl = 0
            x.needtolvl = 10
        self.alliessave = []
        O.crossvec = vec(3,8)
        O.get_connections()
        L.crossvec = vec(3,8)
        L.get_connections()
        M.enemy = {}
        #self.addchar(playing)
        
        self.addchar(playing)
        twoo = Cri
        self.addchar(twoo)
        for k in playing.abilities:
            playing.skill(k)
        
        for k in twoo.abilities:
            twoo.skill(k)
        self.numberofallies()
        #for x in range(1,3):#range(1,random.randint(2,3))
    def addchar(self,new):
        pos = new.vec
        eat = new.health
        lean = new.shield
        new.skill(0)
        self.allies.update({new:[pos,eat,new.clickaura,lean,{},[],False]})
        self.alliessave.append(new)
        self.numberofallies()
        ally.init_skilltree(new)
        s = pg.Surface((1920,1080))  # the size of your rect
        s.fill((255,255,255 ))           # this fills the entire surface
        screen.blit(s, (0,0))
    def start(self):
        #enemy,tier = L.getlevel()
        enemy = [swordguy,swordguy]
        self.savecost = enemy
        for x in enemy:
            if x in self.enemy:
                tout = x.vec
                eat = x.health
                attack = x.attacks
                self.enemy[x].append([tout,eat,x.clickaura,0,{},[],False,1]) # 4 = heavy attack, 6 = animation start, 7 = animation attack frame
            else: 
                tout = x.vec
                eat = x.health
                attack = x.attacks
                self.enemy.update({x:[[tout,eat,x.clickaura,0,{},[],False,1]]})

        self.numberofenemy()
        self.spawnobstacles()
        k = 0
        self.heavyattacking = []
        for x in M.enemy:
            if len(M.enemy[x]) > 1:
                for y in range(len(M.enemy[x])):
                    attack = x.heavyattacks
                    chance = []
                    attacks = []
                    for ll in attack:
                        chance.append(attack[ll][4])
                        attacks.append(ll)
                    attacking = random.choices(attacks,chance)[0] #selects attack

                    damage = attack[attacking] #attack

                    able = damage[5][0] #type of attack eg straight
                    pospos = damage[6] #vec where the enemy can attack from
                    poopee = M.unconversion[(M.enemy[x][y][0].x,M.enemy[x][y][0].y)] #current vec
                    checker = [vec(1,0),vec(0,1),vec(-1,0),vec(0,-1)] #vec check
                    checked = [] #possible places the enemy can move to
                    movement = x.movement +1 #gets movement 
                    checked.append(vec(poopee)) #adds the enemy's current position to places it can move to

                    for ll in range(0,movement): # checks the where the enemy can move 
                        #print(x)
                        if ll == 1: # first check around the enemy
                            for ll in checker:
                                new = poopee+ ll
                                if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0: # restricts movements to the grid
                                    checked.append(new)
                        else: # second and more checks and if the movement is more
                            oldchecked = list(checked)
                            for ww in oldchecked: #grabs the already checked positions and checks around them
                                for ll in checker:
                                    new = ww+ ll 
                                    if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0:
                                        if new not in checked: #prevents already checked vecs to be added to the list
                                            checked.append(new)

                    pot = [] # the potential positions the enemy can attack from
                    possible = [] # is a simplified list 
                    agros = [] #list of the agros of player characters which help the selection of attack
                    hitmult = {} 
                    potpos = {}
                    for ll in checked:
                        if ll in pospos:
                            pot.append(ll)
                    if len(pot) != 0:
                        if random.choices([True,False],[1,0])[0]:
                            self.heavyattacking.append(k)
                            pos = random.choice(pot)
                            M.enemy[x][y][4].update({'heavy':[attacking,pos]})
                    k += 1
            else:
                attack = x.heavyattacks
                chance = []
                attacks = []
                for ll in attack:
                    chance.append(attack[ll][4])
                    attacks.append(ll)
                attacking = random.choices(attacks,chance)[0] #selects attack
                damage = attack[attacking] #damage number
                able = damage[5][0] #type of attack eg straight
                pospos = damage[6] #vec where the enemy can attack from
                poopee = M.unconversion[(M.enemy[x][y][0].x,M.enemy[x][y][0].y)] #current vec
                checker = [vec(1,0),vec(0,1),vec(-1,0),vec(0,-1)] #vec check
                checked = [] #possible places the enemy can move to
                movement = x.movement +1 #gets movement 
                checked.append(vec(poopee)) #adds the enemy's current position to places it can move to
                for ll in range(0,movement): # checks the where the enemy can move 
                    #print(x)
                    if ll == 1: # first check around the enemy
                        for ll in checker:
                            new = poopee+ ll
                            if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0: # restricts movements to the grid
                                checked.append(new)
                    else: # second and more checks and if the movement is more
                        oldchecked = list(checked)
                        for y in oldchecked: #grabs the already checked positions and checks around them
                            for ll in checker:
                                new = y+ ll 
                                if 10 > new.x > 5 and 6 > new.y >= 2 and M.enemyspaces[new.x,new.y] == 0:
                                    if new not in checked: #prevents already checked vecs to be added to the list
                                        checked.append(new)
                pot = [] # the potential positions the enemy can attack from
                possible = [] # is a simplified list 
                agros = [] #list of the agros of player characters which help the selection of attack
                hitmult = {} 
                potpos = {}
                for ll in checked:
                    if ll in pospos:
                        pot.append(ll)
                if len(pot) != 0:
                    if random.choices([True,False],[50,50])[0]:
                        self.heavyattacking.append(k)
                        M.enemy[x][y][4].update({'heavy':attacking})
                    k += 1 
                    if x in boss.bosses:
                        if random.choices([True,False],[50,50])[0]:
                            self.heavyattacking.append(k)
                            M.enemy[x][y][4].update({'heavy':attacking})
                        k += 1
        main.little = {}
        main.k = 0
        for x in M.enemy:
            if len(M.enemy[x]) > 1:
                for y in range(len(M.enemy[x])):
                    main.little.update({main.k:[x,y]})
                    main.k += 1
            else:
                main.little.update({main.k:[x,0]})
                main.k += 1 
                if x in boss.bosses:
                    main.little.update({main.k:[x,0]})
                    main.k += 1
    def draw_allychar(self):
        for x in self.allies:
            ani = dict(x.combat_animation)
            pos = self.allies[x][0]
            cur = ani[self.current_animation]
            #HEIGHTTILESIZE = 150
            goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
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
            if heavy in self.allies[x][4]:
                pos = self.allies[x][4][heavy][0]
                cur = cur.copy( )
                cur.fill((105, 105, 105, 100),special_flags=pg.BLEND_RGB_MULT)  
                cur.set_alpha(100)
                goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                screen.blit(cur, cur.get_rect(center=goal_center))
    def draw_obstacles(self):
        for x in self.obstacles:   
            for y in self.obstacles[x]:
                ani = x.combat_animation
                pos = y[0]
                goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                screen.blit(ani[self.current_animation], ani[self.current_animation].get_rect(center=goal_center))
    def draw_heavy(self):
        for x in range(0,main.k):
            if x in self.heavyattacking:
                pos = self.enemy[main.little[x][0]][main.little[x][1]][0]
                pos = vec(M.unconversion[pos.x,pos.y])
                attack = self.enemy[main.little[x][0]][main.little[x][1]][4]['heavy'][0]
                attpos = self.enemy[main.little[x][0]][main.little[x][1]][4]['heavy'][1]
                attack = main.little[x][0].heavyattacks[attack]
                if attack[5][0] == 'spec 1st column':
                    targetpos = (5,attpos.y)
                    for ll in attack[5][1]:
                        new = targetpos+ ll
                        rect = pg.Surface((int(WIDTH/(64/5)), int(HEIGHT/(36/5))))
                        rect.set_alpha(64)
                        rect.fill(WHITE)
                        screen.blit(rect,(int(new.x*(WIDTH/(64/5))+(WIDTH/(32/1))),int(new.y*(HEIGHT/(36/5)))))  
                        
                
                
    def draw_healthbar(self):
        for x in self.allies:
            pos = self.allies[x][0]
            heat = self.allies[x][1]
            if self.victory != True:
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE - 10), int(pos.y*HEIGHTTILESIZE - 120), int(heat), 20)
                pg.draw.rect(screen,RED,rect)
                if self.allies[x][3] > 0:
                    text = '+'+str(self.allies[x][3])
                    draw_text(text, 20,BLUE , pos.x*WIDTHTILESIZE + 40, pos.y*HEIGHTTILESIZE - 150)
                    rect = pg.Rect(int(pos.x*WIDTHTILESIZE - 10), int(pos.y*HEIGHTTILESIZE - 120), int(self.allies[x][3]   ), 20)
                    pg.draw.rect(screen,BLUE,rect)

                text = str(heat)+'/'+str(x.health)
                draw_text(text, 20, BLACK, pos.x*WIDTHTILESIZE - 10, pos.y*HEIGHTTILESIZE - 150)
            else:
                
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE - 10), int(pos.y*HEIGHTTILESIZE - 120), int(50), 20)
                pg.draw.rect(screen,BLACK,rect)
                proport = 50/x.needtolvl
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE - 10), int(pos.y*HEIGHTTILESIZE - 120), int(x.exp*proport), 20)
                pg.draw.rect(screen,YELLOW,rect)
                text = str(x.exp)+'/'+str(x.needtolvl)
                draw_text(text, 20, BLACK, pos.x*WIDTHTILESIZE - 10, pos.y*HEIGHTTILESIZE - 150)
        for x in self.enemy:
            for y in self.enemy[x]:
                pos = y[0]
                heat = y[1] 
                text = str(round(heat))+'/'+str(x.health)
                draw_text(text, 20, BLACK, pos.x*WIDTHTILESIZE - 10, pos.y*HEIGHTTILESIZE - 150)
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE - 10), int(pos.y*HEIGHTTILESIZE - 120), int(heat), 20)
                pg.draw.rect(screen,RED,rect)
        for x in self.obstacles:
            for y in self.obstacles[x]:
                pos = y[0]
                heat = y[1] 
                text = str(round(heat))+'/'+str(x.health)
                draw_text(text, 20, BLACK, pos.x*WIDTHTILESIZE - 10, pos.y*HEIGHTTILESIZE - 150)
                rect = pg.Rect(int(pos.x*WIDTHTILESIZE - 10), int(pos.y*HEIGHTTILESIZE - 120), int(heat/x.health*50), 20)
                pg.draw.rect(screen,RED,rect)
    def draw_enemychar(self):
        for x in self.enemy:   
            for y in self.enemy[x]:
                if y[6]:
                    ani = x.attack_animation
                    pos = y[0]
                    goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                    screen.blit(ani[y[7]], ani[y[7]].get_rect(center=goal_center))
                else:
                    ani = x.combat_animation
                    pos = y[0]
                    goal_center = (int(pos.x * WIDTHTILESIZE + WIDTHTILESIZE / 2), int(pos.y * HEIGHTTILESIZE + HEIGHTTILESIZE / 2))
                    screen.blit(ani[self.current_animation], ani[self.current_animation].get_rect(center=goal_center))
                
    def draw_grid(self):
        for x in range(int(WIDTH/(16/3)), int(WIDTH/(1920/1561)), int(WIDTH/(64/5))):
            pg.draw.line(screen, BLACK, (x, int(HEIGHT/((18/5)))), (x, int(HEIGHT/(6/5))))
            if int(WIDTH/(48/25)) > x > int(WIDTH/(32/15)):

                pg.draw.line(screen, RED, (x, int(HEIGHT/((18/5)))), (x, int(HEIGHT/(6/5))))
        for y in range(int(HEIGHT/(18/5)), int(HEIGHT/(1080/901)), int(HEIGHT/(36/5))):
            pg.draw.line(screen, BLACK, (int(WIDTH/(16/3)), y), (int(WIDTH/(1920/1560)), y))

    def draw_phase(self):
        if self.fancy:
            if self.phase == 'Enemy':
                if self.decrease == 50:
                    self.toggle = True
                if self.toggle:
                    self.decrease *= 0.89
                    self.phasetext += vec(0,self.decrease)
                    if self.decrease < 1:
                        self.toggle = False
            if self.phase == 'Player':
                if self.decrease <= 1:
                    self.toggle = True
                if self.toggle:
                    self.decrease /= 0.89
                    self.phasetext += vec(0,self.decrease)
                    if self.decrease > 80:
                        self.toggle = False
                        self.decrease = 50
                        self.phasetext = vec(WIDTH/2,-30)
        else:
            if self.phase == 'Enemy':
                self.phasetext = vec(WIDTH/2,400)
            if self.phase == 'Player':
                self.phasetext = vec(WIDTH/2,-30)
        draw_text_center(self.phase, 50, BLACK, self.phasetext.x,self.phasetext.y)
    def draw_transition(self):
        if self.fancy:
            if self.tran == True:
                self.tranrect += self.speed
                self.speed *= 1.11
                rect = pg.Rect(int(0), int(self.tranrect- 600),1920,600 )
                pg.draw.rect(screen,BLACK,rect)
                rect = pg.Rect(int(0),int(HEIGHT-self.tranrect) ,1920, 600)
                pg.draw.rect(screen,BLACK,rect)
                if self.tranrect > HEIGHT/2:
                    self.speed = 50
                    self.trantime = pg.time.get_ticks()
                    self.tran = -1
            elif self.tran == False:
                self.tranrect -= self.speed
                self.speed *= 1.11
                rect = pg.Rect(int(0), int(self.tranrect- 600),1920,600 )
                pg.draw.rect(screen,BLACK,rect)
                rect = pg.Rect(int(0),int(HEIGHT-self.tranrect) ,1920, 600)
                pg.draw.rect(screen,BLACK,rect)
                if self.tranrect < 0:
                    self.tran = -1
                    self.speed = 50


            if current_time - self.trantime > 500 and self.trantime != 0:
                self.tran = False
                self.trantime = 0
                if main.current_state == 'gameover':
                    main.current_state = 'menu'
                elif main.current_state == 'map':
                    main.current_state = L.savestate
                    if 'event' == L.savestate:
                        re.eventstart()
                    elif 'quest' == L.savestate:
                        Q.eventstart()
                elif main.current_state != 'map':
                    if L.crossvec.x != 28:    
                        main.current_state = 'map' 
                    else:
                        main.current_state = 'gameover'
                Bg.checkback()
            rect = pg.Rect(int(0), int(self.tranrect- 600),1920,600 )
            pg.draw.rect(screen,BLACK,rect)
            rect = pg.Rect(int(0),int(HEIGHT-self.tranrect) ,1920, 600)
            pg.draw.rect(screen,BLACK,rect)
        else:
            if self.tran:
                if main.current_state != 'map':
                    main.current_state = 'map' 
                elif main.current_state == 'map':
                    main.current_state = L.savestate
                    if 'event' == L.savestate:
                        re.eventstart()
                    elif 'quest' == L.savestate:
                        Q.eventstart()
                self.tran = False
                Bg.checkback()
    def draw_icons(self):
        for x in self.allies:
            if self.selectedchar == x:
                if self.selectedattack != 0:
                    
                    pos = vec(18,31)
                    for attack in self.selectedchar.attacks:  
                        if attack in self.selectedchar.abilities:
                            if self.selectedchar.attack3 not in self.selectedchar.unlockedabilites:
                                if attack == self.selectedchar.attack3:
                                    continue
                        try:
                            if self.selectedchar.attack4 not in self.selectedchar.unlockedabilites:
                                if attack == self.selectedchar.attack4:
                                    continue
                        except:
                            pass
                        if attack == self.selectedattack:
                            rect = pg.Rect(int(pos.x*WIDTHTILESIZE-55), int(pos.y*HEIGHTTILESIZE-55),140, 160)
                            pg.draw.rect(screen,WHITE,rect)
                        pos += vec(5,0)
                    
                x.draw_icons() 
                pos = vec(18,31)  
                for x in M.selectedchar.attacks:
                    if M.selectedchar.attacks[x][0][whereattack] != False:
                        if M.unconversion[M.allies[M.selectedchar][0].x,M.allies[M.selectedchar][0].y] not in M.selectedchar.attacks[x][0][whereattack]:
                            rect = pg.Surface((140, 160))
                            rect.set_alpha(128)
                            rect.fill(BLACK)
                            screen.blit(rect,(int(pos.x*WIDTHTILESIZE-55), int(pos.y*HEIGHTTILESIZE-55)))
                    pos += vec(5,0)
    def draw_movement(self):
        for x in self.allies:
            if self.selectedchar == x and self.allies[self.selectedchar][6] != False:
                poopee = M.unconversion[(self.allies[self.selectedchar][6].x,self.allies[self.selectedchar][6].y)]
                checker = [vec(1,0),vec(0,1),vec(-1,0),vec(0,-1)]
                checked = []
                movement = self.selectedchar.movement +1
                for x in range(0,movement):
                    if x == 1:
                        for x in checker:
                            new = poopee+ x
                            if 5 >= new.x >= 2 and 6 > new.y >= 2:
                                checked.append(new)
                                rect = pg.Surface((int(WIDTH/(64/5)), int(HEIGHT/(36/5))))
                                rect.set_alpha(64)
                                rect.fill(WHITE)
                                screen.blit(rect,(int(new.x*(WIDTH/(64/5))+(WIDTH/(32/1))),int(new.y*int(HEIGHT/(36/5)))))  
                    else:
                        oldchecked = list(checked)
                        for y in oldchecked:
                            for x in checker:
                                new = y+ x
                                if new not in checked:
                                    if 5 >= new.x >= 2 and 6 > new.y >= 2:
                                        checked.append(new)
                                        bbb = int(WIDTH/(64/5))
                                        aaa = int(HEIGHT/(36/5))
                                        rect = pg.Surface((bbb,aaa))
                                        rect.set_alpha(64)
                                        rect.fill(WHITE)
                                        screen.blit(rect,(int(new.x*(WIDTH/(64/5))+(WIDTH/(32/1))),int(new.y*int(HEIGHT/(36/5)))))
                if self.selectedattack != 0:
                    if self.selectedchar.attacks[self.selectedattack][0][whereattack] != False:
                        for new in self.selectedchar.attacks[self.selectedattack][0][whereattack]:
                            rect = pg.Surface((150, 150))
                            rect.set_alpha(64)
                            rect.fill(GREEN)
                            screen.blit(rect,(int(new.x*150+50),int(new.y*150)))
                    else:
                        for new in M.allyspaces:
                            new = vec(new)
                            rect = pg.Surface((150, 150))
                            rect.set_alpha(64)
                            rect.fill(GREEN)
                            screen.blit(rect,(int(new.x*150+50),int(new.y*150)))
    def draw_damage(self):
        for x in self.damage:
            damage = 0
            for y in self.damage[x]:
                if y == 'dodged':
                    draw_text('dodged',30,RED,self.allies[x][0].x*WIDTHTILESIZE, self.allies[x][0].y*HEIGHTTILESIZE-130,align="bottomright") 
                else:
                    if y == 0:
                        draw_text('miss',30,RED,self.allies[x][0].x*WIDTHTILESIZE, self.allies[x][0].y*HEIGHTTILESIZE-170,align="bottomright")  
                    damage += y
            if x in self.allies:
                draw_text(str(damage),30,RED,self.allies[x][0].x*WIDTHTILESIZE, self.allies[x][0].y*HEIGHTTILESIZE-150,align="bottomright")  
    def draw_txt_attack(self):
        for x in self.enemy:
            lel = 0
            add = 0
            for y in self.enemy[x]:
                if y[3] != 0:
                    if type(y[3]) is list:
                        for ww in range(0,len(y[3])):
                            draw_text(str(y[3][ww]),30,RED,self.enemy[x][lel][0].x*WIDTHTILESIZE, (self.enemy[x][lel][0].y-add)*HEIGHTTILESIZE-150,align="bottomright") 
                            add += 1
                    else:
                        draw_text(str(y[3]),30,RED,self.enemy[x][lel][0].x*WIDTHTILESIZE, self.enemy[x][lel][0].y*HEIGHTTILESIZE-150,align="bottomright") 
                lel += 1
    def draw_effects(self):
        for x in self.allies:
            if bleed in self.allies[x][4]:
                draw_text('bleed',10, RED, self.allies[x][0].x*WIDTHTILESIZE + 25, self.allies[x][0].y*HEIGHTTILESIZE-10,align="bottomright")
            if fire in self.allies[x][4]:
                draw_text('fire',10, YELLOW, self.allies[x][0].x*WIDTHTILESIZE + 25, self.allies[x][0].y*HEIGHTTILESIZE,align="bottomright")
            if stun in self.allies[x][4]:
                draw_text('stun',10, YELLOW, self.allies[x][0].x*WIDTHTILESIZE + 25, self.allies[x][0].y*HEIGHTTILESIZE+10,align="bottomright")
            if pierce in self.allies[x][4]:
                draw_text('pierce',10, ORANGE, self.allies[x][0].x*WIDTHTILESIZE + 25, self.allies[x][0].y*HEIGHTTILESIZE+20,align="bottomright")
        for x in self.enemy:
            lel = 0
            for ll in self.enemy[x]:
                if x == dva:
                    if 'weapon' in M.enemy[x][lel][4]:
                        txt = str(dva.weapons[M.enemy[x][lel][4]['weapon']])
                        draw_text(txt,10, BLACK, self.enemy[x][lel][0].x*WIDTHTILESIZE + 25, self.enemy[x][lel][0].y*HEIGHTTILESIZE-10,align="bottomright")
                if bleed in self.enemy[x][lel][4]:
                    draw_text('bleed',10, RED, self.enemy[x][lel][0].x*WIDTHTILESIZE + 25, self.enemy[x][lel][0].y*HEIGHTTILESIZE-10,align="bottomright")
                if fire in self.enemy[x][lel][4]:
                    draw_text('fire',10, YELLOW, self.enemy[x][lel][0].x*WIDTHTILESIZE + 25, self.enemy[x][lel][0].y*HEIGHTTILESIZE,align="bottomright")
                if stun in self.enemy[x][lel][4]:
                    draw_text('stun',10, YELLOW, self.enemy[x][lel][0].x*WIDTHTILESIZE + 25, self.enemy[x][lel][0].y*HEIGHTTILESIZE-10,align="bottomright")
                if pierce in self.enemy[x][lel][4]:
                    draw_text('pierce',10, ORANGE, self.enemy[x][lel][0].x*WIDTHTILESIZE + 25, self.enemy[x][lel][0].y*HEIGHTTILESIZE-20,align="bottomright")
                if needle in self.enemy[x][lel][4]:
                    ahe = 'needle'+ str(self.enemy[x][lel][4][needle][0])+str(self.enemy[x][lel][4][needle][1])
                    draw_text(ahe,10, PURPLE, self.enemy[x][lel][0].x*WIDTHTILESIZE + 25, self.enemy[x][lel][0].y*HEIGHTTILESIZE-30,align="bottomright")
                if 'heavy' in self.enemy[x][lel][4]:
                    draw_text('yes',10, BLACK, self.enemy[x][lel][0].x*WIDTHTILESIZE + 25, self.enemy[x][lel][0].y*HEIGHTTILESIZE-30,align="bottomright")
                lel += 1
    def checkifdead(self):
        test = dict(self.enemy)
        for x in test:
                for y in test[x]:
                    if int(y[1]) <= 0:
                        self.enemy[x].remove(y)
                        self.killhistory.append(self.selectedchar)
                if len(test[x]) <= 0:
                    del self.enemy[x]
                    self.killhistory.append(self.selectedchar)
            #else:
            #    if test[x][0][1] <=0 :
            #        del self.enemy[x]
            #        self.killhistory.append(self.selectedchar)
        test = dict(self.allies)
        for x in test:
            if test[x][1] <= 0:
                del self.allies[x]
                if x == self.selectedchar:
                    self.selectedchar = 0
                    self.selectedattack = 0
                for w in self.allyspaces:
                    if self.allyspaces[w] == x:
                        self.allyspaces[w] = 0
        if len(self.allies) <= 0:
            self.loss = True
            main.endscreen_timer = pg.time.get_ticks()
            main.enemy_attck_time = 0
            main.little = {}
            L.turns = 0
            L.border = 3
            L.barrier = []
            O.crossvec = vec(3,8)
            for x in self.alliessave:
                x.needtolvl = 20
                x.xp = 0
                x.unlockedablilites = []
        elif len(self.enemy) <= 0:
            if main.current_state == 'battle' and self.typeobattle != 'gauntlet':
                L.levelstatus.append(mpos2)
            self.savelevel = {}
            for x in self.allies:
                x.passive_endturn()
                self.savelevel.update({x:x.lvl})
            self.selectedattack = 0
            self.selectedchar = 0
            self.enemy = {}
            self.l = []
            self.actions = []
            coins = L.get_cost(self.savecost)
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
            for x in self.allies:
                self.savelevel[x] = self.savelevel[x] - x.lvl
            main.endscreen_timer = pg.time.get_ticks()
            if self.typeobattle == 'gauntlet':
                if Q.glevel != 0:
                    Q.click()
                else:
                    L.levelstatus.append(mpos2)
                    self.victory = True
            else:
                self.victory = True

            self.damage = {}
    def numberofenemy(self):
        pot = []
        for x in self.enemyspaces:
            pot.append(x)
        for x in self.enemy:
            for y in self.enemy[x]:
                cho = random.choice(pot)
                while self.enemyspaces[cho] != 0:
                    cho = random.choice(pot)
                
                self.enemyspaces[cho] = x
                y[0] = vec(M.conversion[cho])
                y[2] = [y[0]+ x for x in x.clickaura] 
    def spawnobstacles(self):
        thang = random.randint(5,12)
        for x in range(0,thang):
            picked = random.choice(self.spaces)
            con = True
            if picked in self.enemyspaces:
                if self.enemyspaces[picked] == 0:
                    con = False
            if picked in self.allyspaces:
                if self.allyspaces[picked] == 0:
                    con = False        
            while con:
                picked = random.choice(self.spaces)
                con = True
                if picked in self.enemyspaces:
                    if self.enemyspaces[picked] == 0:
                        con = False
                if picked in self.allyspaces:
                    if self.allyspaces[picked] == 0:
                        con = False   
            
                
            obstacle = random.choice(obstacles.allothem)
            if picked in self.enemyspaces:
                self.enemyspaces[picked] = obstacle
            if picked in self.allyspaces:
                self.allyspaces[picked] = obstacle
                
            if obstacle in self.obstacles:
                eat = obstacle.health
                self.obstacles[obstacle].append([vec(M.conversion[picked]),eat,[vec(M.conversion[picked])+ x for x in obstacle.clickaura],0,{},[],False,1]) # 6 = animation start, 7 = animation attack frame
            else: 
                eat = obstacle.health
                self.obstacles.update({obstacle:[[vec(M.conversion[picked]),eat,[vec(M.conversion[picked])+ x for x in obstacle.clickaura],0,{},[],False,1]]})
    def numberofallies(self):
        #vec(14,11) vec(19,11) vec(24,11) vec(29,11)
        for x in self.allyspaces:
            self.allyspaces[x] = 0
        pot = []
        for x in self.allyspaces:
            pot.append(x)
        for y in self.allies:
            cho = random.choice(pot)
            while self.allyspaces[cho] != 0:
                cho = random.choice(pot)
            
            self.allyspaces[cho] = y
            self.allies[y][0] = vec(M.conversion[cho])
            self.allies[y][2] = [self.allies[y][0]+ x for x in y.clickaura]
    def moveallies(self):
        if (bigmpos.x,bigmpos.y) in M.allyspaces:
            poopee = M.unconversion[(self.allies[self.selectedchar][6].x,self.allies[self.selectedchar][6].y)]
            checker = [vec(1,0),vec(0,1),vec(-1,0),vec(0,-1)]
            checked = []
            movement = self.selectedchar.movement +1
            for x in range(0,movement):
                if x == 1:
                    for x in checker:
                        new = poopee+ x
                        if 5 >= new.x >= 2 and 6 > new.y >= 2:
                            checked.append(new)
                else:
                    oldchecked = list(checked)
                    for y in oldchecked:
                        for x in checker:
                            new = y+ x
                            if new != checked:
                                if 5 >= new.x >= 2 and 6 > new.y >= 2:
                                    checked.append(new)
            if (bigmpos.x,bigmpos.y) == M.unconversion[self.allies[self.selectedchar][0].x,self.allies[self.selectedchar][0].y]:
                self.allies[self.selectedchar][0]
                M.actions.append(self.selectedchar)
                M.moving = False
                M.attackselect = False
            else:
                if self.allyspaces[(bigmpos.x,bigmpos.y)] == 0 and bigmpos in checked: #and self.allies[self.selectedchar][6] == self.allies[self.selectedchar][0]:
                    self.allyspaces[M.unconversion[self.allies[self.selectedchar][0].x,self.allies[self.selectedchar][0].y]] = 0
                    self.allies[self.selectedchar][0] = vec(M.conversion[(bigmpos.x,bigmpos.y)])
                    self.allyspaces[(bigmpos.x,bigmpos.y)] = self.selectedchar
                    self.allies[self.selectedchar][2] = [self.allies[self.selectedchar][0]+ x for x in self.selectedchar.clickaura] 
                else:
                    self.allyspaces[M.unconversion[self.allies[self.selectedchar][0].x,self.allies[self.selectedchar][0].y]] = 0
                    M.allies[M.selectedchar][0] = M.allies[M.selectedchar][6]
                    self.allyspaces[M.unconversion[self.allies[self.selectedchar][0].x,self.allies[self.selectedchar][0].y]] = self.selectedchar
                    M.allies[M.selectedchar][2] = [M.allies[M.selectedchar][0]+ x for x in M.selectedchar.clickaura] 
                    self.selectedchar = 0
                    self.selectedattack = 0
                    M.moving = False
                    M.attackselect = False
            
        else:
            if mpos not in self.selectingattack():
                self.allyspaces[M.unconversion[self.allies[self.selectedchar][0].x,self.allies[self.selectedchar][0].y]] = 0
                M.allies[M.selectedchar][0] = M.allies[M.selectedchar][6]
                self.allyspaces[M.unconversion[self.allies[self.selectedchar][0].x,self.allies[self.selectedchar][0].y]] = self.selectedchar
                M.allies[M.selectedchar][2] = [M.allies[M.selectedchar][0]+ x for x in M.selectedchar.clickaura] 
                self.selectedchar = 0
                self.selectedattack = 0
                M.moving = False
                M.attackselect = False
    def getaura(self):
        y = []
        for x in self.enemy:
            if len(self.enemy[x]) > 1:
                for z in self.enemy[x]:
                    y += z[2]
            else:
                y += self.enemy[x][0][2]
        for x in self.obstacles:
            if len(self.obstacles[x]) > 1:
                for z in self.obstacles[x]:
                    y += z[2]
            else:
                y += self.obstacles[x][0][2]
        if M.selectedattack != 0 and M.selectedchar != 0:
            if M.selectedchar.attacks[M.selectedattack][2] != False:
                for x in self.allies:
                    y += self.allies[x][2]
        return y
    def selectingattack(self):
        y = []
        if self.selectedchar != 0:
            for w in self.selectedchar.attacks:
                if w in self.selectedchar.abilities:
                    if self.selectedchar.attack3 not in self.selectedchar.unlockedabilites:
                        if w == self.selectedchar.attack3:
                            continue
                    try:
                        if self.selectedchar.attack4 not in self.selectedchar.unlockedabilites:
                            if w == self.selectedchar.attack4:
                                continue
                    except:
                        pass
                y += self.selectedchar.attacks[w][2]
        return y
    def selectingchar(self):
        y = []
        for z in self.allies:
            for x in self.allies[z][2]:
                y.append(x)
        return y
    def selectattack(self):
        for x in self.selectedchar.attacks:
            if mpos in self.selectedchar.attacks[x][2]:
                if x in self.selectedchar.abilities:
                    if self.selectedchar.attack3 not in self.selectedchar.unlockedabilites:
                        if x == self.selectedchar.attack3:
                            continue
                    try:
                        if self.selectedchar.attack4 not in self.selectedchar.unlockedabilites:
                            if x == self.selectedchar.attack4:
                                continue
                    except:
                        pass
                save = self.selectedattack
                self.selectedattack = x
                self.attackselect = True
                if save == self.selectedattack:
                    self.selectedattack = 0
                    self.attackselect = False
    def selectchar(self):
        for x in self.allies:
            if mpos in self.allies[x][2]:
                self.selectedchar = x
                self.selectedability = 0
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
        for x in self.obstacles:
            if len(self.obstacles[x]) > 1:
                lel = 0
                for z in self.obstacles[x]:
                    if mpos in self.obstacles[x][lel][2]:
                        cur_enemyspecific = lel
                        cur_enemyclass = x
                    lel += 1
            else:   
                if mpos in self.obstacles[x][0][2]:
                    cur_enemyspecific = 0
                    cur_enemyclass = x
        return cur_enemyclass,cur_enemyspecific
    def areaselectenemy(self,pos):
        cur_enemyspecific = 'pass'
        cur_enemyclass = 'pass'
        for x in self.enemy:
            if len(self.enemy[x]) > 1:
                lel = 0
                for z in self.enemy[x]:
                    if pos == self.enemy[x][lel][0]:
                        cur_enemyspecific = lel
                        cur_enemyclass = x
                    lel += 1
            else:   
                if pos == self.enemy[x][0][0]:
                    cur_enemyspecific = 0
                    cur_enemyclass = x
        for x in self.obstacles:
            if len(self.obstacles[x]) > 1:
                lel = 0
                for z in self.obstacles[x]:
                    if pos == self.obstacles[x][lel][0]:
                        cur_enemyspecific = lel
                        cur_enemyclass = x
                    lel += 1
            else:   
                if pos == self.obstacles[x][0][0]:
                    cur_enemyspecific = 0
                    cur_enemyclass = x
        return cur_enemyclass,cur_enemyspecific
    def enemyattack(self,cur,spec):
        self.attacking = True
        x = main.little[cur][0]
        ll = int(spec)
        if stun in self.enemy[x][ll][4]:
            if self.enemy[x][ll][4][stun] > 1:
                self.enemy[x][ll][4][stun] -= 1
            else:
                del self.enemy[x][ll][4][stun]
        else: 
            x.thunk(ll)
    def enemyheavyattack(self,cur):
        if isinstance(cur,int):
            self.attacking = True
            x = main.little[cur][0]
            ll = int(main.little[cur][1])
            if stun in self.enemy[x][ll][4]:
                if self.enemy[x][ll][4][stun] > 1:
                    self.enemy[x][ll][4][stun] -= 1
                else:
                    del self.enemy[x][ll][4][stun]
            else: 
                x.heavythunk(ll)
        else:
            cur.heavythunk()
    def workingattack(self,attack,effect):
        pass
    def statuseffects(self,when):
        if when:
            for x in self.allies:
                if stun in self.allies[x][4]:
                    self.allies[x][4][stun] -= 1
                    self.actions.append(x)
                    if self.allies[x][4][stun] == 0:
                        del self.allies[x][4][stun]
            for x in self.enemy:
                lel = 0
                for y in self.enemy[x]:
                    if bleed in self.enemy[x][lel][4]:
                        self.enemy[x][lel][4][bleed] -= 0.5
                        self.enemy[x][lel][1] -= 2
                        if self.enemy[x][lel][4][bleed] == 0:
                            del self.enemy[x][lel][4][bleed]
                    if fire in self.enemy[x][lel][4]:
                        self.enemy[x][lel][4][fire] -= 1
                        self.enemy[x][lel][1] -= 5
                        if self.enemy[x][lel][4][fire] == 0:
                            del self.enemy[x][lel][4][fire]
                    if needle in self.enemy[x][lel][4]:
                        self.enemy[x][lel][4][needle][1] -= 1
                        if self.enemy[x][lel][4][needle][1] == 0:
                            del self.enemy[x][lel][4][needle]
                    if 'ps' in self.enemy[x][lel][4]:
                        self.enemy[x][lel][4]['ps'] -= 0.5
                        if self.enemy[x][lel][4]['ps'] == 0:
                            del self.enemy[x][lel][4]['ps']
                    lel += 1
                
        if not when:
            for x in self.allies:
                if bleed in self.allies[x][4]:
                    self.allies[x][4][bleed] -= 0.5
                    self.allies[x][1] -= 2
                    if self.allies[x][4][bleed] == 0:
                        del self.allies[x][4][bleed]
                if fire in self.allies[x][4]:
                    self.allies[x][4][fire] -= 1
                    self.allies[x][1] -= 5
                    if self.allies[x][4][fire] == 0:
                        del self.allies[x][4][fire]
                if weakness in self.allies[x][4]:
                    if self.allies[x][4][weakness] == 0:
                        del self.allies[x][4][weakness]
                if pierce in self.allies[x][4]:
                    del self.allies[x][4][pierce]
            for x in self.enemy:
                lel = 0
                for y in self.enemy[x]:
                    if dodge in self.enemy[x][lel][4]:
                        self.enemy[x][lel][4][dodge] -= 1
                        if self.enemy[x][lel][4][dodge] == 0:
                            del self.enemy[x][lel][4][dodge]
                    if pierce in self.enemy[x][lel][4]:
                        self.enemy[x][lel][4][pierce] -= 1
                        if self.enemy[x][lel][4][pierce] == 0:
                            del self.enemy[x][lel][4][pierce]
                    lel += 1
            
M = battle()
M.tranrect = 1
M.speed = 50
M.trantime = 0

M.alliessave = []

M.allyspaces = {}
M.enemyspaces = {}
M.spaces = []
M.conversion = {}
M.unconversion = {}
first = vec(2,2) #vec(19,11) vec(24,11) vec(29,11)
funnywidth = round(WIDTH/(32/7)/WIDTHTILESIZE) #14
print(funnywidth)
print(HEIGHT/(36/11)/HEIGHTTILESIZE) #11
print(WIDTH/(64/5)/WIDTHTILESIZE) #5 width
print(HEIGHT/(36/5)/HEIGHTTILESIZE) #5 height
second = vec(int(funnywidth),int(HEIGHT/(36/11)/HEIGHTTILESIZE)) 
for x in range(0,32):
    M.spaces.append((first.x,first.y))
    if first.x < 6:
        M.allyspaces.update({(first.x,first.y):0})
    else:
        M.enemyspaces.update({(first.x,first.y):0})
    M.conversion.update({(first.x,first.y):(second.x,second.y)})
    M.unconversion.update({(second.x,second.y):(first.x,first.y)})
    first.x += 1
    second.x += int(WIDTH/(64/5)/WIDTHTILESIZE)
    if first.x > 9:
        first.x = 2
        first.y += 1
        second.x = funnywidth
        second.y += int(HEIGHT/(36/5)/HEIGHTTILESIZE)
M.moving = False

M.obstacles = {}

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

primopsed va


'''
#L.levelmaster = O.mapmaster[1]
#for x in range(0,1):
#    L.create_map()

M.targetedenemy = 0


M.savecost = []

M.selected1 = 0
M.selected2 = 0
M.swap = False

M.hov = False
M.selectedability = 0
M.hovertime = 9999


M.killhistory = []

M.damage = {}
M.attackselect = False
#M.clickaura = [vec(-1,-1)]
M.typeobattle = 'normal'


main.anim_timer = pg.time.get_ticks()
M.enemycanattack = False

M.victory = False
M.loss = False

M.tutorial = False 

M.restart()

M.attacking = False
M.cur = -1
M.spec = -1

M.skills = False
M.selectedblessing = -2

M.phasetext = vec(WIDTH/2,-30)
M.phase = 'Player'
M.decrease = 50
M.toggle = False
M.fancy = True

M.tran = False

shop.draw_shopkeeps()

mpos = vec(0,0)
create = []
lock = True

M.start()
Bg.checkback()

pg.mixer.music.load(os.path.join(filename,'walking through.wav'))
pg.mixer.music.play(2,0,2000)
pg.mixer.music.set_volume(0.0)

music = ['walking through.wav','rushed adventure.wav']

L.get_connections()
ui.running = True
while ui.running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does #print: event
        # write important things here 
        # duh
        if main.current_state == 'switch':
            mpos = vec(pg.mouse.get_pos()) #// HEIGHTTILESIZE
            mpos = vec(int(mpos.x/WIDTHTILESIZE),int(mpos.y/HEIGHTTILESIZE))
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if main.current_state == 'battle' or main.current_state == 'shop' or main.current_state == 'switch' or main.current_state == 'menu' or ui.pause:
                    truepos = vec(pg.mouse.get_pos())
                    mpos = vec(pg.mouse.get_pos()) #// HEIGHTTILESIZE
                    mpos = vec(int(mpos.x/WIDTHTILESIZE),int(mpos.y/HEIGHTTILESIZE))
                    mposraw = vec(pg.mouse.get_pos())
                    create.append(mpos)
                    bigmpos = vec(pg.mouse.get_pos())
                    bigmpos = vec(int(int(bigmpos.x-int(WIDTH/(108/5)))/(WIDTH/(64/5))),int(bigmpos.y/(HEIGHT/(36/5))))
                if main.current_state == 'creator' or main.current_state == 'map' or main.current_state == 'tutorial' or main.current_state == 'overmap' and not ui.pause:
                    mpos2 = vec(pg.mouse.get_pos()) #// (HEIGHTTILESIZE*2)
                    mpos = vec(int(mpos.x/(WIDTHTILESIZE*2)),int(mpos.y/HEIGHTTILESIZE*2))
                    pos = pg.mouse.get_pos()
                    pos = vec(pos.x/WIDTHTILESIZE,pos.y/30)
                    L.click = True
                #L.crossvec =  mpos2
                #O.maps.append(vec(mpos2))
                #if ui.pause != True:
                #    main.leveltop()
                if M.victory:
                    if not M.tutorial:
                        M.victory = False
                        M.tran = True
                        if L.crossvec.x == 28:
                            if O.crossvec.x == 5:
                                M.tran = True
                            else:
                                main.current_state = 'overmap'
                                L.crossvec = vec(3,8)
                                L.get_connections()
                                L.turns = 0
                                L.border = 3
                                L.barrier = []
                if ui.pause != True:
                    main.eventtop()
                    main.questtop()
                    main.leveltop()
                    main.overmaptop()
                    main.battletop()
                    main.switchtop()
                    main.shoptop()
                main.gameovertop()
                main.menutop()
                main.creatortop()
                mpos = vec(0,0)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                if main.current_state == 'switch':
                    main.current_state = 'map'
                else:
                    M.enemy = {}
                    M.checkifdead()
                    M.hov = False
            if event.key == pg.K_e:
                M.actions = [1,1,1,1]
            if event.key == pg.K_q:
                screen = pg.display.set_mode((WIDTH, HEIGHT),pg.FULLSCREEN,display = 1)
            if event.key == pg.K_c:
                M.selectedchar.lvl += 1
            if event.key == pg.K_h:
                main.amountmoney += 100
            if event.key == pg.K_n:
                L.create_map()
            if event.key == pg.K_l:
                if lock == True:
                    lock = False
                else:
                    lock = True
            if event.key == pg.K_k:
                for x in M.allies:
                    x.exp = 0
            #if event.key == pg.K_a:
            #    print([(int(loc.x -  M.clericvec.x), int(loc.y - M.clericvec.y)) for loc in create])
            if event.key == pg.K_m:
                main.current_state = 'creator'
                M.addchar(nover)
            if event.key == pg.K_ESCAPE:
                if main.current_state != 'menu':
                    if main.current_state != 'gameover':
                        if ui.pause:
                            ui.pause = False
                        else:
                            ui.pause = True
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            ui.running = False
            pg.quit() 
        main.checkstate()
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
    main.questbottom()
    main.eventbottom()
    if main.current_state != 'menu':
        if main.current_state != 'creator':
            if M.tutorial != True: 
                main.draw_money()
    else:
        Bg.draw_background()
    main.menubottom()
    main.gameoverbottom()
    main.creatorbottom()
    if not pg.mixer.music.get_busy():
        pg.mixer.music.unload()
        pg.mixer.music.load(os.path.join(filename,random.choice(music)))
        pg.mixer.music.play(2,0,2000)
        pg.mixer.music.set_volume(0.0)
        
    pg.display.flip() # dose the changes goto doccumentation for other ways

listt = '{'
for ll in O.mapmaster:
    listt += str(ll) + ':{'
    for ww in O.mapmaster[ll]:
        listt += str(ww) + ': [' +str(O.mapmaster[ll][ww][0])+',['
        for ee in O.mapmaster[ll][ww][1]:
            listt += str(type(ee).__name__)+','
        str1 = listt
        list1 = list(str1)
        list2 = list1[:-1]
        listt = ''
        for x in list2:
            listt += x
        listt += '],'+str(O.mapmaster[ll][ww][2]) +'],'
    str1 = listt
    list1 = list(str1)
    list2 = list1[:-1]
    listt = ''
    for x in list2:
        listt += x
    listt += '},'
str1 = listt
list1 = list(str1)
list2 = list1[:-1]
listt = ''
for x in list2:
    listt += x
listt += '}'
if main.current_state == 'creator':
    print(listt)