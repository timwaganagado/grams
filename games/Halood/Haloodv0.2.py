from pickle import TRUE
from tempfile import tempdir
from tkinter import CENTER
from turtle import pos
from numpy import place
import pygame as pg
import pygame.freetype
from os import path, times
import random
import shelve
import os , sys
import math

vec = pg.math.Vector2

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
def draw_text_fit(text, size, color, x, y, xbound, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    while text_rect[2] > xbound:
        size -= 1
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)
def create_text_lister(text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    return text_surface, text_rect
def create_text_fit_lister(text, size, color, x, y, xbound, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    while text_rect[2] > xbound:
        size -= 1
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
    return text_surface, text_rect
def draw_text_list(new):
    text_surface,text_rect = new
    screen.blit(text_surface, text_rect)
def draw_text_fit_color(text, size, color, x, y, xbound, othercolor, where, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    while text_rect[2] > xbound:
        size -= 1
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
    savesize = pg.Surface((text_surface.get_width(), text_surface.get_height()), pg.SRCALPHA)
    place = 1
    dis = 0
    for xx in text:
        if where[0]>=place>where[1]:
            text_surface = font.render(xx, True, othercolor)
        else:
            text_surface = font.render(xx, True, color)
        
        savesize.blit(text_surface,((dis, 0)))
        dis+= text_surface.get_width()
        place += 1
    align = 'center'
    text_rect = savesize.get_rect(**{align: (x, y)})
    screen.blit(savesize,text_rect)
def create_text_fit_color_lister(text, size, color, x, y, xbound, othercolor, where, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    while text_rect[2] > xbound:
        size -= 1
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
    savesize = pg.Surface((text_surface.get_width(), text_surface.get_height()), pg.SRCALPHA)
    place = 1
    dis = 0
    for xx in text:
        if where[0]>=place>where[1]:
            text_surface = font.render(xx, True, othercolor)
        else:
            text_surface = font.render(xx, True, color)
        
        savesize.blit(text_surface,((dis, 0)))
        dis+= text_surface.get_width()
        place += 1
    align = 'center'
    text_rect = savesize.get_rect(**{align: (x, y)})
    return savesize,text_rect
def draw_text_wraped(text=str, size=int, color=tuple, x=float, y=float, x_bound=int, y_bound=10, draw_rect=False, align="topleft"):
    font = pg.font.Font(font_name, size)
    if draw_rect:
        current_text = ''
        space_text = ''
        ty = y
        box_size = 1 
        for qq in text:
            space_text += qq
            text_surface = font.render(current_text + space_text, True, color)
            text_rect = text_surface.get_rect(**{align: (x, y)})
            if text_rect[0]+text_rect[2] > x_bound + x:

                text_surface = font.render(current_text , True, color)
                text_rect = text_surface.get_rect(**{align: (x, y)})
                ty += text_rect[3]
                current_text = ''
                current_text += space_text
                space_text = ''
                box_size += 1
            elif qq == ' ':
                current_text += space_text
                space_text = ''
        box_size +=1
        #if text == '':
        #    text_rect = [0,0,0,50]

        rect = pg.Rect(x,y, x_bound, text_rect[3]*box_size-y_bound)
        pg.draw.rect(screen,BLACK,rect)
    current_text = ''
    space_text = ''
    for qq in text:
        space_text += qq
        text_surface = font.render(current_text + space_text, True, color)
        
        text_rect = text_surface.get_rect(**{align: (x, y+5)})
        if text_rect[0]+text_rect[2] > x_bound + x:
            text_surface = font.render(current_text , True, color)
            text_rect = text_surface.get_rect(**{align: (x+10, y+5)})
            screen.blit(text_surface, text_rect)
            y += text_rect[3]
            current_text = ''
            current_text += space_text
            space_text = ''

        elif qq == ' ':
            current_text += space_text
            space_text = ''
        
    current_text += space_text
    text_surface = font.render(current_text, True, color)
    text_rect = text_surface.get_rect(**{align: (x+10, y+5)})
    screen.blit(text_surface, text_rect)

pg.init()
screen = pg.display.set_mode((0, 0),pg.FULLSCREEN)
clock = pg.time.Clock()
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
class defaultchar:
    def __init__(self,hp,spd,pos):
        self.speedrand = 6
        self.fix_position(pos)
        self.name = 'fix'
        self.type = 'fix'
        self.health = hp
        self.health_current = int(self.health)
        self.health_display = int(self.health_current)
        self.speed = spd
        self.rect_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.defaulteffects()
        self.effects = []
        size = 100
        self.health_rect = pg.Rect(self.pos.x-(size/2),HEIGHT*(2/4),size,10)
        self.update_health()
    def defaulteffects(self):
        self.damageattack_percent = 0
        self.speedincrease = 0
    def fix_position(self,pos):
        change = 150
        self.pos = vec(pos)
        self.rect = pg.Rect((self.pos.x+(change/2)-(charspritesize/2)), (self.pos.y-(charspritesize/2)), charspritesize-change, charspritesize)
    def draw(self):
        #ani = dict(self.combat_animation)
        pg.draw.rect(screen,self.rect_colour,self.rect)
        pos = self.pos
        #cur = ani[self.animation]
        cur = self.combat_animation[self.animation]
        goal_center = (int(pos.x), int(pos.y))
        if self in L.enemies:
            cur = pg.transform.flip(cur,True,False)
        if self == L.selectedchar:
            lol = cur.copy()
            lol = pg.transform.scale(lol, (charspritesize+25, charspritesize+20))
            lol.fill((0, 0, 0),special_flags=pg.BLEND_RGB_MULT)
            lel = lol.get_rect(center=goal_center)
            lel[1] -=2
            screen.blit(lol, lel)
        
        screen.blit(cur, cur.get_rect(center=goal_center))
    def draw_health(self):
        pygame.draw.rect(screen,BLACK,self.health_rect)
        pygame.draw.rect(screen,RED,self.health_currentrect)
    def update_health(self):
        size = 100
        self.health_currentrect = pg.Rect(self.pos.x-(size/2),HEIGHT*(2/4),size*(self.health_current/self.health),10)
    def check_ret(self):
        return 5
    def takedamage(self,damage,sender):
        self.health_current -= damage
        if sender.speed*2 <= self.speed:
            sender.takedamage(self.check_ret(),self) 
        self.update_health()
    def cleanse(self):
        for x in self.effects:
            x.cleanse(self)
    def checkspeed(self):
        speed = self.speed + random.randint(0,self.speedrand) + self.speedincrease
        if speedlimit() in self.effects:
            self.speedincrease = 0
        return speed

class defaultability:
    def __init__(self,pos,owner,c=True) :
        self.pos = vec(pos)
        self.rect = pg.Rect(int(self.pos.x-64), int(self.pos.y-64), 128, 128)
        self.owner = owner
        self.attackarea = [1,2]
        self.attackwhere = [1,2,3,4]
        if c:
            self.name += ' (incomplete)'
        self.checktext()
        self.effects = []
    def draw(self):
        if L.selectedattack == self:
            pg.draw.rect(screen,BLACK,self.rect)
            
        goal_center = (int(self.pos.x), int(self.pos.y))
        screen.blit(self.icon, self.icon.get_rect(center=goal_center))
    def checktext(self):
        self.text = []
        txt = '{}X{}'.format(int(self.damagetest(self.owner,0)),self.timestest(0,0))
        color = BLACK
        self.text.append(create_text_fit_color_lister(txt,50,BLACK,1525,1005,140,color,(len(txt),len(txt)-len(str(self.timestest(0,0)))),'center'))
        txt = '{}'.format(self.name)
        self.text.append(create_text_lister(txt,50,BLACK,400,885,))
    def drawtext(self):
        for x in self.text:
            draw_text_list(x)
    def pressed(self,mpos):
        if self.rect.collidepoint((mpos.x,mpos.y)):
            if self != L.selectedattack:
                L.selectedattack = self
            else:
                L.selectedattack = 0
                L.selectedenemy = 0
    def check_damage(self,ini,tar):
        return int(self.damagetest(ini,tar) * self.timestest(ini,tar))
    def damagetest(self,ini,tar):
        change = 0
        damage = random.randint(self.damage[0],self.damage[1])
        if tar:
            change -= (damage*ini.damageattack_percent)
        return  damage + change
    def timestest(self,ini,tar):
        extra = 1
        return self.times * extra
    def attack(self,target,sender):
        for x in self.effects:
            target.effects.append(find_effect(x))
        damage = self.check_damage(sender,target)
        target.takedamage(damage,sender)
        sender.cleanse()
        return damage

def find_effect(effect):
    if effect == 'dull':
        return dull()

class hemo(defaultchar):
    def __init__(self,pos):
        super().__init__(30,60,pos)
        self.combat_animation = {1:swordguy_img,2:swordguy2_img,3:swordguy3_img}
        self.attack_animation = swordguy_attacking3_img
        self.hurt_animation = swordguy_hurt_img
        self.icon = swordguy_icon_img
        self.animation = random.randint(1,len(self.combat_animation))
        self.abilites_current = ['Blunt Slash','Slash','Wild Flailing']
        self.abilites_actual = []
        
    def abilites_create(self):
        self.abilites_actual = []
        temp = self.abilites_current
        positions = []
        for x in range(4):
            positions.append((456+136*x,800))
        for x in temp:
            for y in positions:
                positions.remove(y)
                if x == 'Blunt Slash':
                    self.abilites_actual.append(hemo_ability_bluntslash(y,self))
                if x == 'Slash':
                    self.abilites_actual.append(hemo_ability_slash(y,self))
                if x == 'Wild Flailing':
                    self.abilites_actual.append(hemo_ability_wildflailing(y,self))
                break 
        


class hemo_ability_bluntslash(defaultability):
    def __init__(self,pos,owner):
        self.name = 'Blunt Slash'
        self.damage = 1,2
        self.times = 2
        super().__init__(pos,owner)
        self.icon = swordguy_ability1_img
        self.attackarea = [1,2]
        
class hemo_ability_slash(defaultability):
    def __init__(self,pos,owner):
        self.name = 'Slash'
        self.damage = 2,4
        self.times = 2
        super().__init__(pos,owner)
        self.icon = swordguy_ability2_img
        self.attackarea = [1,2]
        

class hemo_ability_wildflailing(defaultability):
    def __init__(self,pos,owner):
        self.name = 'Wild Flailing'
        self.damage = 6,10
        self.times = 2
        super().__init__(pos,owner)
        self.icon = swordguy_ability3_img
        self.attackarea = [1,2]
        
class cri(defaultchar):
    def __init__(self,pos):
        self.name = "Cri"
        self.type = "Crystal"
        super().__init__(30, 40, pos)

class heplane(defaultchar):
    def __init__(self,pos):
        
        
        
        self.combat_animation = {1:heplane_combat_img,2:heplane_combat2_img,3:heplane_combat3_img}
        self.hurt_animation = heplane_hurt_img
        self.attack_animation = heplane_attack_img
        self.animation = random.randint(1,len(self.combat_animation))
        self.abilites_current = ['Punch','Coilent']
        self.abilites_actual = []
        super().__init__(50,30,pos)
        self.name = 'Heplane'
        self.type = 'Halood'
    def draw_icon(self):
        pg.draw.rect(screen,BLACK,self.rect)
        pos = self.pos
        #cur = ani[self.animation]
        cur = heplane_icon_img
        goal_center = (int(pos.x), int(pos.y))
        
        if self == L.selectedchar:
            lol = cur.copy()
            lol = pg.transform.scale(lol, (70, 70))
            lol.fill((0, 0, 0),special_flags=pg.BLEND_RGB_MULT)
            lel = lol.get_rect(center=goal_center)
            lel[1] -=2
            screen.blit(lol, lel)
        
        screen.blit(cur, cur.get_rect(center=goal_center))
    def abilites_create(self):
        self.abilites_actual = []
        temp = self.abilites_current
        positions = []
        for x in range(4):
            positions.append((456+136*x,800))
        for x in temp:
            for y in positions:
                positions.remove(y)
                if x == 'Punch':
                    self.abilites_actual.append(heplane_ability_punch(y,self))
                    break
                if x == 'Coilent':
                    self.abilites_actual.append(heplane_ability_coilent(y,self))
                    break
                


        
class heplane_ability_punch(defaultability):
    def __init__(self,pos,owner):
        self.name = 'Punch'
        self.damage = 3,7
        self.times = 1
        super().__init__(pos,owner)
        self.icon = heplane_ability2_img
        self.attackarea = [1,2]
        
class heplane_ability_coilent(defaultability):
    def __init__(self,pos,owner):
        self.name = 'Coilent'
        self.damage = 8,10
        self.times = 1
        super().__init__(pos,owner)
        self.effects = ['dull']
        self.icon = heplane_ability1_img
        self.attackarea = [1,2]
    def check_damage(self,sender,target):
        damage = self.damagetest(sender,target) 
        damage += +damage*(self.owner.health_current/self.owner.health) 
        return int(damage * self.timestest(sender,target))



class defaulteffect:
    def __init__(self):
        self.turns = 2
    def turn(self,target):
        if self.turns == 0:
            target.effects.remove(self)
            return
        self.turns -= 1
    def cleanse(self):
        print(self.name,'dosent have cleanse')
class dull(defaulteffect):
    def __init__(self):
        self.name = 'Dull'
        self.colour = GREY
        super().__init__()
    def turn(self,target):
        super().turn()
        target.damageattack_percent = 0.4
    def cleanse(self,target):
        target.damageattack_percent = 0
    def draw(self,target):
        draw_text(self.name,50,self.colour,int(target.pos.x),int(HEIGHT/7),'center')

class speedlimit(defaulteffect):
    def __init__(self):
        self.name = 'Speed Limit'
        self.colour = GREEN
        super().__init__()
    def turn(self,target):
        super().turn()
        target.speedincrease = 50
    def draw(self,target):
        draw_text(self.name,50,self.colour,int(target.pos.x),int(HEIGHT/7),'center')

filename = os.path.dirname(sys.argv[0])
filename += '/Halood_images'
charspritesize = 256
abilityspritesize = 100

currentfileg =  filename +'/enemies'

currentfiles = currentfileg + '/swordguy'
swordguy_img = pg.image.load(os.path.join(currentfiles,'0.png')).convert_alpha()
swordguy_img = pg.transform.scale(swordguy_img, (charspritesize, charspritesize))
swordguy2_img = pg.image.load(os.path.join(currentfiles,'1.png')).convert_alpha()
swordguy2_img = pg.transform.scale(swordguy2_img, (charspritesize, charspritesize))
swordguy3_img = pg.image.load(os.path.join(currentfiles,'2.png')).convert_alpha()
swordguy3_img = pg.transform.scale(swordguy3_img, (charspritesize, charspritesize))

swordguy_attacking3_img = pg.image.load(os.path.join(currentfiles,'3.png')).convert_alpha()
swordguy_attacking3_img = pg.transform.scale(swordguy_attacking3_img, (charspritesize, charspritesize))

swordguy_hurt_img = pg.image.load(os.path.join(currentfiles,'4.png')).convert_alpha()
swordguy_hurt_img = pg.transform.scale(swordguy_hurt_img, (charspritesize, charspritesize))

swordguy_icon_img = pg.image.load(os.path.join(currentfiles,'icon0.png')).convert_alpha()
swordguy_icon_img = pg.transform.scale(swordguy_icon_img, (50, 50))
swordguy_ability1_img = pg.image.load(os.path.join(currentfiles,'hemo_abilites0.png'))
swordguy_ability1_img = pg.transform.scale(swordguy_ability1_img, (abilityspritesize, abilityspritesize))
swordguy_ability2_img = pg.image.load(os.path.join(currentfiles,'hemo_abilites1.png'))
swordguy_ability2_img = pg.transform.scale(swordguy_ability2_img, (abilityspritesize, abilityspritesize))
swordguy_ability3_img = pg.image.load(os.path.join(currentfiles,'hemo_abilites2.png'))
swordguy_ability3_img = pg.transform.scale(swordguy_ability3_img, (abilityspritesize, abilityspritesize))

currentfileg =  filename +'/allies'  

currentfiles = currentfileg + '/heplane'

heplane_icon_img = pg.image.load(os.path.join(currentfiles,'icon0.png')).convert_alpha()
heplane_icon_img = pg.transform.scale(heplane_icon_img, (50, 50))

heplane_combat_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat1.png')).convert_alpha()
heplane_combat_img = pg.transform.scale(heplane_combat_img, (charspritesize, charspritesize))
heplane_combat2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat2.png')).convert_alpha()
heplane_combat2_img = pg.transform.scale(heplane_combat2_img, (charspritesize, charspritesize))
heplane_combat3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat3.png')).convert_alpha()
heplane_combat3_img = pg.transform.scale(heplane_combat3_img, (charspritesize, charspritesize))

heplane_hurt_img = pg.image.load(os.path.join(currentfiles,'heplane_hurt0.png')).convert_alpha()
heplane_hurt_img = pg.transform.scale(heplane_hurt_img, (charspritesize, charspritesize))

heplane_attack_img = pg.image.load(os.path.join(currentfiles,'heplane_attack.png')).convert_alpha()
heplane_attack_img = pg.transform.scale(heplane_attack_img, (charspritesize, charspritesize))

heplane_ability1_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites0.png'))
heplane_ability1_img = pg.transform.scale(heplane_ability1_img, (abilityspritesize, abilityspritesize))
heplane_ability2_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites1.png'))
heplane_ability2_img = pg.transform.scale(heplane_ability2_img, (abilityspritesize, abilityspritesize))
heplane_ability3_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites2.png'))
heplane_ability3_img = pg.transform.scale(heplane_ability3_img, (abilityspritesize, abilityspritesize))
heplane_ability4_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites3.png')).convert_alpha()
heplane_ability4_img = pg.transform.scale(heplane_ability4_img, (abilityspritesize, abilityspritesize))

#currentfiles = currentfileg + '/fallen'
#fallen_icon_img = pg.image.load(os.path.join(currentfiles,'fallen_icon.png')).convert_alpha()
#fallen_icon_img = pg.transform.scale(fallen_icon_img, (50, 50))
#
#fallen_combat_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat1.png')).convert_alpha()
#fallen_combat_img = pg.transform.scale(fallen_combat_img, (charspritesize, charspritesize))
#fallen_combat2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat2.png')).convert_alpha()
#fallen_combat2_img = pg.transform.scale(fallen_combat2_img, (charspritesize, charspritesize))
#fallen_combat3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat3.png')).convert_alpha()
#fallen_combat3_img = pg.transform.scale(fallen_combat3_img, (charspritesize, charspritesize))
#
#fallen_hurt_img = pg.image.load(os.path.join(currentfiles,'heplane_hurt0.png')).convert_alpha()
#fallen_hurt_img = pg.transform.scale(fallen_hurt_img, (charspritesize, charspritesize))
#
#fallen_attack_img = pg.image.load(os.path.join(currentfiles,'heplane_attack.png')).convert_alpha()
#fallen_attack_img = pg.transform.scale(fallen_attack_img, (charspritesize, charspritesize))

class text:
    def __init__(self,txt,size,color,x,y,limit,allign):
        self.text = create_text_fit_lister(txt,size,color,x,y,limit,allign)
    def draw(self):
        draw_text_list(self.text)
    def __repr__(self):
        return "{}".format(self.name)

class gamemanager:
    def __init__(self):
        self.reset()
    def reset(self):
        self.currentturn = 0
        self.click = 0
        self.showpos = False
        self.selectedchar = 0
        self.selectedattack = 0
        self.selectedenemy = 0
        self.animtimer = 0
        self.allies = []
        self.npcallies = []
        self.enemies =[]
        self.act_allies = {1:0,2:0,3:0,4:0}
        self.act_enemies = {1:0,2:0,3:0,4:0}
        self.animations = 0
        self.texts = []
        self.phase = 0
        
        
        self.ally_postovec = {}
        for x in self.act_allies:
            self.ally_postovec.update({x:((WIDTH/2-150*x),300)})
        
        self.enemy_postovec = {}
        for x in self.act_enemies:
            self.enemy_postovec.update({x:((WIDTH/2+150*x),300)})
        
        self.spawn()    
        self.create_order()
    def spawn(self):
        self.spec_spawn('heplane',1,'player')
        self.spec_spawn('hemo',1,'enemy')
        self.spec_spawn('hemo',2,'enemy')
    def spec_spawn(self,target,place,afil):
        if afil == 'player':
            pla = self.ally_postovec[place]
            xx = self.get_cla(target,pla)
            self.act_allies[place] = xx
            self.allies.append(xx)
        if afil == 'ally':
            pla = self.ally_postovec[place]
            xx = self.get_cla(target,pla)
            self.act_allies[place] = xx
            self.allies.append(xx)
            self.npcallies.append(xx)
        if afil == 'enemy':
            pla = self.enemy_postovec[place]
            xx = self.get_cla(target,pla)
            self.act_enemies[place] = xx
            self.enemies.append(xx)
    def get_cla(self,tar,pla):
        if tar == 'heplane':
            return heplane(pla)
        if tar == 'hemo':
            return hemo(pla)
    def draw_objects(self):
        for x in self.allies:
            x.draw()
            x.draw_health()
        for x in self.enemies:
            x.draw()
            x.draw_health()
    def draw_selection(self):
        cur = self.selectedchar
        if cur:
            for x in cur.abilites_actual:
                x.draw()
            
            for x in self.texts:
                x.draw()
            
            
        tar = self.selectedattack
        if tar:
            tar.drawtext()
            rect = pg.Surface((50, 10))
            rect.set_alpha(64)
            rect.fill(RED)
            for new in self.attackarea:
                if self.selectedchar in self.allies:
                    new = vec(self.enemy_postovec[new])
                elif self.selectedchar in self.enemies:
                    new = vec(self.ally_postovec[new])
                screen.blit(rect,(int(new.x-(50/2)),int(new.y+(10/2)))) 
        tar = self.selectedenemy
        if tar:
            for x in self.enemytext:
                draw_text_list(x)
            screen.blit(self.enemyspeedimage[0],self.enemyspeedimage[1]) 
            
    def draw_selection_char(self):
        tar = self.selectedchar
        if tar:
            ani = dict(tar.combat_animation)
            pos = vec(WIDTH*(1/9),HEIGHT*(6/8))
            cur = ani[tar.animation]
            goal_center = (int(pos.x), int(pos.y))
            screen.blit(cur, cur.get_rect(center=goal_center))
        tar = self.selectedenemy
        if tar:
            ani = dict(tar.combat_animation)
            pos = vec(WIDTH*(8/9),HEIGHT*(7/9))
            cur = ani[tar.animation]
            #HEIGHTTILESIZE = 150
            cur = pg.transform.flip(cur,True,False)
            goal_center = (int(pos.x), int(pos.y))
            screen.blit(cur, cur.get_rect(center=goal_center))
    def draw_background(self):
        goal_center = int(WIDTH / 2), int(HEIGHT / 2)
        screen.blit(background_fall, background_fall.get_rect(center=goal_center))
    def mpostopos(self):
        ll = vec(pg.mouse.get_pos())
        return (ll.x,ll.y)
    def updateani(self):
        if current_time - 1000 >self.animtimer:
            for x in self.allies:
                x.animation += 1
                if x.animation > len(x.combat_animation):
                    x.animation = 1
            for x in self.enemies:
                x.animation += 1
                if x.animation > len(x.combat_animation):
                    x.animation = 1
            self.animtimer = pg.time.get_ticks()
    def showclick(self):
        if self.click:
            txt = str(pg.mouse.get_pos())
            draw_text(txt,50,BLACK,pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
    def selectchar(self):
        pos = self.mpostopos()  
        for x in self.allies:
            self.leleol(pos,x)
        for x in self.enemies:
            self.leleol(pos,x)
            
    def leleol(self,pos,x):
        if x.rect.collidepoint(pos):        
            if self.selectedchar != x:
                #if self.selectedchar:
                #    temp = self.translate(self.selectedchar.pos)
                #    self.grid[temp] = 0
                self.select(x)
                
            else:
                self.unselect()
            return
    def unselect(self):
        self.selectedattack = 0
    def select(self,tar):
        self.selectedchar = tar
        self.selectedattack = 0
        tar.abilites_create()
        self.texts = []
        txt = '{}/{}'.format(tar.health_current,tar.health)
        self.texts.append(text(txt,75,RED,87,965,120,'center'))
        self.texts.append(text('{}'.format(tar.name),50,BLACK,175,750,100,'topleft'))
        self.texts.append(text("{}".format(tar.type),30,BLACK,175,800,100,'topleft'))
    def selectattack(self):
        if self.selectedchar:
            for x in self.selectedchar.abilites_actual:
                x.pressed(mpos)
                if self.selectedattack:
                    temp = []
                    for xx in x.attackarea:
                        temp.append(xx)
                    self.attackarea = temp
    def draw_ui(self):
        goal_center = int(WIDTH / 2), int(HEIGHT/ 2)
        screen.blit(ui_fall, ui_fall.get_rect(center=goal_center))
    def draw_movement(self,target):
        point = self.currentmovementdraw
        if target == self.turn:
            point = self.turn_movementdraw
        for new in point:
            screen.blit(new[0],new[1])
    def translate(self,new):
        return self.vectopos[(new.x,new.y)]
    def untranslate(self,new):
        return self.postovec[(new.x,new.y)]
    def locate(self,new):
        return self.grid[new.x,new.y]
    def create_order(self):
        test = []
        highestspd = 0
        for x in self.allies:
            test.append(x)
            if x.speed > highestspd:
                highestspd = x.speed
        for x in self.enemies:
            test.append(x)
            if x.speed > highestspd:
                highestspd = x.speed
        self.heavies = sorted(test, key=speed_sort,reverse=True)
        self.whose = 0
        self.turn = self.heavies[self.whose]
        self.nextturn()
    def update_pos(self,target,position):
        position = vec(position)
        pos = self.vectopos[(target.pos.x,target.pos.y)]
        self.grid[pos] = 0
        self.grid[(position.x,position.y)] = target
        ll = self.postovec[(position.x,position.y)]
        target.pos = vec(ll)
    def temp_pos(self,target,position):
        position = vec(position)
        pos = self.vectopos[(target.pos_temp.x,target.pos_temp.y)]
        self.grid[pos] = 0
        self.grid[(position.x,position.y)] = target
        ll = self.postovec[(position.x,position.y)]
        target.pos_temp = vec(ll)
    def nextturn(self):
        for x in self.allies:
            if x.health_current <= 0:
                self.allies.remove(x)
        for x in self.enemies:
            if x.health_current <= 0:
                self.enemies.remove(x)
                self.heavies.remove(x)
                move = False
                for key,y in self.act_enemies.items():
                    if y == 0:
                        break
                    if move:
                        print('key',key,'y',y)
                        print(self.act_enemies)
                        self.act_enemies[key] = 0
                        self.act_enemies[key-1] = y
                        pla = self.enemy_postovec[key-1]
                        y.fix_position(pla)
                    if y == x:
                        move = True 
                        self.act_enemies[key] = 0
        if len(self.allies) == 0 or len(self.enemies) == 0:
            self.reset()
            return
        if self.whose >= len(self.heavies):
            self.whose = 0
        self.turn = self.heavies[self.whose]
        
        self.whose += 1
        if self.phase == 'Enemy':
            #self.enemyselectedattack.attack(self.enemytarget,self.enemywho)
            self.update_text(self.enemywho,self.enemytarget)
        self.phase = 'Player'
        if self.turn in self.enemies:
            self.phase = 'Enemy'
        if self.turn in self.npcallies:
            self.phase = 'ally'
        if self.phase == 'Player' or self.phase == 'ally':
            self.select(self.turn)
        for x in self.turn.effects:
            x.turn(self.turn)
    def enemy_turn(self):
        if self.phase == 'Enemy':
            tar = self.turn
            for x in self.act_enemies:
                if self.act_enemies[x] == tar:
                    tarpos = x
                    break
            
            
            if len(tar.abilites_actual) == 0:
                tar.abilites_create()
            
            
            simpally = []
            for x in self.act_allies:
                if self.act_allies[x]:
                    simpally.append(x)
            move = True
            for x in tar.abilites_actual:
                for y in simpally:
                    if y in x.attackarea:
                        if tarpos in x.attackwhere:
                            move = False
                            break
            attack = random.choice(tar.abilites_actual)
            check = True
            for y in self.act_allies:
                if self.act_allies[y] and y in attack.attackarea:
                    check = False
                    break
            if check:
                for x in tar.abilites_actual:
                    if tarpos in x.attackwhere:
                        attack = x
            
            possibletargets = []
            for x in attack.attackarea:
                if self.act_allies[x]:
                    possibletargets.append(x)
            
            att = self.act_allies[random.choice(possibletargets)]
            
            self.enemywho = tar
            self.enemytarget = att
            self.animations = animationmove(tar,attack,att)
            self.moveanimation = True
            
            self.phase = 0
            
            
        if self.phase == 'ally':
            tar = self.turn
            for x in self.act_allies:
                if self.act_allies[x] == tar:
                    tarpos = x
                    break
            
            
            if len(tar.abilites_actual) == 0:
                tar.abilites_create()
            
            
            simpenem = []
            for x in self.act_enemies:
                if self.act_enemies[x]:
                    simpenem.append(x)
            move = True
            for x in tar.abilites_actual:
                for y in simpenem:
                    if y in x.attackarea:
                        if tarpos in x.attackwhere:
                            move = False
                            break
            attack = random.choice(tar.abilites_actual)
            check = True
            for y in self.act_enemies:
                if self.act_enemies[y] and y in attack.attackarea:
                    check = False
                    break
            if check:
                for x in tar.abilites_actual:
                    if tarpos in x.attackwhere:
                        attack = x
            
            possibletargets = []
            for x in attack.attackarea:
                if self.act_allies[x]:
                    possibletargets.append(x)
            
            att = self.act_enemies[random.choice(possibletargets)]
            
            self.enemywho = tar
            self.enemytarget = att
            self.animations = animationmove(tar,attack,att)
            self.moveanimation = True
            self.phase = 0
            
    def ally_turn(self):
        if not self.selectedattack:
            L.selectchar()
        if self.phase == 'Player':
            player = self.selectedchar
            if player == self.turn:
                for x in self.enemies:
                    target = 0
                    if x.rect.collidepoint(self.mpostopos()):
                        target = x
                    if target:
                        if self.selectedenemy == target and target != 0:
                            self.animations = animationmove(self.selectedchar,self.selectedattack,self.selectedenemy)
                            self.moveanimation = True

                        if self.selectedattack and target in self.enemies:
                            for xx in self.act_enemies:
                                if self.act_enemies[xx] == target:
                                    pos = xx
                            if pos in self.attackarea:
                                self.selectedenemy = x
                                self.update_text(player,x)
                                break
    def update_text(self,player,x):
        self.enemytext = []
        self.selectedattack.checktext()
        
        txt = '{}'.format(x.speed)
        self.enemytext.append(create_text_fit_lister(txt,70,GREEN,1845,605,65,'center'))
        
        txt = '{}/{}'.format(x.health_current,x.health)
        self.enemytext.append(create_text_fit_lister(txt,75,RED,1670,1005,100,'center'))
        txt = '{}/{}'.format(x.health_current-self.selectedattack.check_damage(player,x),x.health)
        self.enemytext.append(create_text_fit_lister(txt,75,RED,1825,1005,100,'center'))
        goal_center = int(1765), int(605)
        if x.speed < player.speed:
            self.enemyspeedimage = ui_slow,ui_slow.get_rect(center=goal_center)
        elif x.speed >= player.speed*2:
            self.enemyspeedimage = ui_fast, ui_fast.get_rect(center=goal_center)
        else:
            self.enemyspeedimage = ui_same, ui_same.get_rect(center=goal_center)
    
class animationmove:
    def __init__(self,enemywho,selectedattack,enemytarget):
        self.enemywho = enemywho
        self.selectedattack = selectedattack
        self.enemytarget = enemytarget
        self.plaani = self.enemytarget.combat_animation
        self.eneani = self.enemywho.combat_animation

        self.step = 0
        self.pos = 0
        self.steptwosteps = 1
        self.count = 0
    def steptwo(self):
        cover = pg.Surface((WIDTH,HEIGHT/2))
        cover.fill((128,128,128))
        cover.set_alpha(128)
        goal_center = int(WIDTH/2), int(HEIGHT/4)
        screen.blit(cover, cover.get_rect(center=goal_center))
        
        ani = dict(self.plaani)
        placur = ani[self.enemytarget.animation]
        plagoal_center = int(self.enemytarget.pos.x), int(HEIGHT/4)
        
        
        ani = dict(self.eneani)
        enecur = ani[self.enemywho.animation]
        enegoal_center = (int(self.enemywho.pos.x), int(HEIGHT/4))
        
        if self.steptwosteps == 0:
            if self.pos < 15:
                self.pos += 1
            else:
                self.pos = 0
                self.steptwosteps += 1
        if self.steptwosteps == 1:
            
            if self.count < len(self.enemywho.effects):
                self.enemywho.effects[self.count].draw(self.enemywho)
                enecur= self.enemywho.hurt_animation
                if self.pos < 30:
                    self.pos += 1
                else:
                    self.pos = 0
                    self.count += 1
            else:
                self.steptwosteps += 1
                self.count = 0
            
        if self.steptwosteps == 2 : #attack name for enemy
            draw_text(self.selectedattack.name,50,BLACK,int(self.enemywho.pos.x), int(HEIGHT/7),'center')
           
            if self.pos < 30:
                self.pos += 1
            else:
                self.pos = 0
                self.steptwosteps += 1
        if self.steptwosteps == 3: #attack animation for initiate and hurt for target
            if self.pos == 0:
                self.damage = self.selectedattack.attack(self.enemytarget,self.enemywho)
            enecur = self.enemywho.attack_animation
            placur = self.enemytarget.hurt_animation
            draw_text(str(self.damage),50,RED,int(self.enemytarget.pos.x), int(HEIGHT/7-self.pos),'center')
            if self.pos <15:
                ani = dict(self.enemywho.combat_animation)
                enecur = ani[1]
            if self.pos < 40:
                self.pos += 1
            else:
                self.pos = 0
                self.steptwosteps += 1
        if self.steptwosteps == 4: # return attack for target and hurt for initiated
            if self.enemytarget.speed >= self.enemywho.speed*2:
                placur = self.enemytarget.attack_animation
                enecur= self.enemywho.hurt_animation
                draw_text(str(self.enemytarget.check_ret()),50,RED,int(self.enemywho.pos.x), int(HEIGHT/7-self.pos),'center')
                if self.pos <15:
                    ani = dict(self.enemytarget.combat_animation)
                    placur = ani[1]
                if self.pos < 40:
                    self.pos += 1
                else:
                    self.pos = 0
                    self.steptwosteps += 1
            else:
                self.steptwosteps += 1
        if self.steptwosteps == 5:
            self.step +=1
            
        if self.enemytarget in L.enemies:
            placur = pg.transform.flip(placur,True,False)
        placur = pg.transform.scale(placur,(250,250))
        screen.blit(placur, placur.get_rect(center=plagoal_center))
        if self.enemywho in L.enemies:
            enecur = pg.transform.flip(enecur,True,False)
        enecur = pg.transform.scale(enecur,(250,250))
        screen.blit(enecur, enecur.get_rect(center=enegoal_center))
    def enemymove(self):
        if self.step == 0:
            self.steptwo()
        if self.step == 1:
            self.pos += 1
            if self.pos > 15:
                self.step += 1
        if self.step == 2:    
            L.nextturn()
            L.animations = 0
def speed_sort(target):
    return target.checkspeed()
        
ui_fall = pg.image.load(os.path.join(filename,'battle_ui.png'))
ui_fall = pg.transform.scale(ui_fall, (WIDTH, HEIGHT))

ui_slow = pg.image.load(os.path.join(filename,'speedicon0.png'))
ui_slow = pg.transform.scale(ui_slow, (50, 50))
ui_fast = pg.image.load(os.path.join(filename,'speedicon1.png'))
ui_fast = pg.transform.scale(ui_fast, (50, 50))
ui_same = pg.image.load(os.path.join(filename,'speedicon2.png'))
ui_same = pg.transform.scale(ui_same, (50, 50))

background_fall = pg.image.load(os.path.join(filename,'backgorunds-2.png.png'))
background_fall = pg.transform.scale(background_fall, (int(WIDTH), int(HEIGHT)))
            
current_time = pg.time.get_ticks()
L = gamemanager()

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does : event
        # write important things here 
        # duh
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit
            if event.key == pg.K_w:
                L.nextturn()
                L.update_pos(L.selectedchar,L.translate(L.selectedchar.pos_temp))
            if event.key == pg.K_s:
                L.gridsize -= 1
            if event.key == pg.K_e:
                L.showpos = True
        if event.type == pg.MOUSEBUTTONDOWN:
            mpos = vec(pg.mouse.get_pos())
            if event.button == 1:
                L.selectattack()
                L.ally_turn()
            if event.button == 3:
                L.unselect()
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    current_time = pg.time.get_ticks()
    L.updateani()
    L.enemy_turn()
    L.draw_background()
    L.draw_objects()
    L.draw_selection_char()
    L.draw_ui()
    L.draw_selection()
    if L.animations:
        L.animations.enemymove()
    L.showclick()
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways