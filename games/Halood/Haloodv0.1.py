from pickle import TRUE
from tempfile import tempdir
import pygame as pg
import pygame.freetype
from os import path, times
import random
import shelve
import os , sys
import math

vec = pg.math.Vector2

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
screen = pg.display.set_mode((WIDTH, HEIGHT),display = 0)
clock = pg.time.Clock()

class defaultchar:
    def __init__(self,hp,spd,mp):
        self.health = hp
        self.health_current = int(self.health)
        self.speed = spd
        self.speed_current = 0
        self.movement = mp
    def check_ret(self):
        return 5
    def takedamage(self,damage,sender):
        self.health_current -= damage
        if sender.speed*2 <= self.speed:
            sender.takedamage(self.check_ret(),self) 

class hemo(defaultchar):
    def __init__(self,pos):
        super().__init__(30,60,2)
        self.pos = vec(pos)
        self.drawn_pos = vec(pos)
        self.combat_animation = {1:swordguy_img,2:swordguy2_img,3:swordguy3_img}
        self.attack_animation = {1:swordguy_attacking2_img,2:swordguy_attacking3_img}
        self.animation = random.randint(1,len(self.combat_animation))
        self.abilites_current = ['Blunt Slash','Slash','Wild Flailing']
        self.abilites_actual = []
    def draw(self):
        #ani = dict(self.combat_animation)
        pos = self.drawn_pos
        #cur = ani[self.animation]
        cur = swordguy_icon_img
        goal_center = (int(pos.x), int(pos.y))
        
        if self == L.selectedchar:
            lol = cur.copy()
            lol = pg.transform.scale(lol, (60, 60))
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
            positions.append((WIDTH*((3+x)/9),HEIGHT*(3/5)))
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
            
class defaultability:
    def __init__(self,pos,owner) :
        self.pos = vec(pos)
        self.rect = pg.Rect(int(self.pos.x-64), int(self.pos.y-64), 128, 128)
        self.owner = owner
        self.checktext()
    def draw(self):
        if L.selectedattack == self:
            pg.draw.rect(screen,BLACK,self.rect)
            
        goal_center = (int(self.pos.x), int(self.pos.y))
        screen.blit(self.icon, self.icon.get_rect(center=goal_center))
    def checktext(self):
        self.text = []
        txt = '{}X{}'.format(int(self.damagetest()),self.timestest())
        color = BLACK
        if L.selectedenemy:
            if L.selectedenemy.speed*2 <= L.selectedchar.speed:
                txt = '{}X{}'.format(int(self.damagetest()),self.timestest())
                color = GREEN
        self.text.append(create_text_fit_color_lister(txt,50,BLACK,1525,1005,140,color,(len(txt),len(txt)-len(str(self.timestest()))),'center'))
        txt = '{}'.format(self.name)
        self.text.append(create_text_fit_lister(txt,50,BLACK,595,745,200,))
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
    def check_damage(self):
        return self.damagetest() * self.timestest()
    def damagetest(self):
        return self.damage
    def timestest(self):
        extra = 1
        if L.selectedenemy:
            if L.selectedchar.speed >= L.selectedenemy.speed*2:
                extra = 2
        return self.times * extra
    def attack(self,target,sender):
        target.takedamage(self.check_damage(),sender)


class hemo_ability_bluntslash(defaultability):
    def __init__(self,pos,owner):
        self.icon = swordguy_ability1_img
        self.range = 1
        self.damage = 3
        self.times = 2
        self.name = 'Blunt Slash'
        super().__init__(pos,owner)
class hemo_ability_slash(defaultability):
    def __init__(self,pos,owner):
    
        self.icon = swordguy_ability2_img
        self.range = 1
        self.damage = 3
        self.times = 2
        self.name = 'Slash'
        super().__init__(pos,owner)

class hemo_ability_wildflailing(defaultability):
    def __init__(self,pos,owner):
        
        self.icon = swordguy_ability3_img
        self.range = 1
        self.damage = 10
        self.times = 2
        self.name = 'Wild Flailing'
        super().__init__(pos,owner)


class heplane(defaultchar):
    def __init__(self,pos):
        super().__init__(50,120,2)
        self.pos = vec(pos)
        self.pos_temp = vec(pos)
        self.combat_animation = {1:heplane_combat_img,2:heplane_combat2_img,3:heplane_combat3_img}
        self.animation = random.randint(1,len(self.combat_animation))
        self.abilites_current = ['Punch','Coilent']
        self.abilites_actual = []
    def draw(self):
        #ani = dict(self.combat_animation)
        pos = self.pos_temp
        #cur = ani[self.animation]
        cur = hepane_icon_img
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
            positions.append((WIDTH*((3+x)/9),HEIGHT*(3/5)))
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
        self.icon = heplane_ability2_img
        self.range = 1
        self.damage = 10
        self.times = 1
        self.name = 'Punch'
        super().__init__(pos,owner)
class heplane_ability_coilent(defaultability):
    def __init__(self,pos,owner):
        self.icon = heplane_ability1_img
        self.range = 1
        self.damage = 10
        self.times = 1
        self.name = 'Coilent'
        super().__init__(pos,owner)
    def check_damage(self):
        return self.damage +self.damage*(self.owner.health/self.owner.health_current)  
    

filename = os.path.dirname(sys.argv[0])
filename += '/Halood_images'
charspritesize = 512
abilityspritesize = 100

currentfileg =  filename +'/enemies'

currentfiles = currentfileg + '/swordguy'
swordguy_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat1.png')).convert_alpha()
swordguy_img = pg.transform.scale(swordguy_img, (charspritesize, charspritesize))
swordguy2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat2.png')).convert_alpha()
swordguy2_img = pg.transform.scale(swordguy2_img, (charspritesize, charspritesize))
swordguy3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_swordguy_combat3.png')).convert_alpha()
swordguy3_img = pg.transform.scale(swordguy3_img, (charspritesize, charspritesize))

swordguy_attacking2_img = pg.image.load(os.path.join(currentfiles,'swordguy_attacking1.png')).convert_alpha()
swordguy_attacking2_img = pg.transform.scale(swordguy_attacking2_img, (charspritesize, charspritesize))
swordguy_attacking3_img = pg.image.load(os.path.join(currentfiles,'swordguy_attacking2.png')).convert_alpha()
swordguy_attacking3_img = pg.transform.scale(swordguy_attacking3_img, (charspritesize, charspritesize))

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
heplane_combat_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat1.png')).convert_alpha()
heplane_combat_img = pg.transform.scale(heplane_combat_img, (charspritesize, charspritesize))
heplane_combat2_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat2.png')).convert_alpha()
heplane_combat2_img = pg.transform.scale(heplane_combat2_img, (charspritesize, charspritesize))
heplane_combat3_img = pg.image.load(os.path.join(currentfiles,'Layer 1_heplane_combat3.png')).convert_alpha()
heplane_combat3_img = pg.transform.scale(heplane_combat3_img, (charspritesize, charspritesize))
heplane_ability1_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites0.png'))
heplane_ability1_img = pg.transform.scale(heplane_ability1_img, (abilityspritesize, abilityspritesize))
heplane_ability2_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites1.png'))
heplane_ability2_img = pg.transform.scale(heplane_ability2_img, (abilityspritesize, abilityspritesize))
heplane_ability3_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites2.png'))
heplane_ability3_img = pg.transform.scale(heplane_ability3_img, (abilityspritesize, abilityspritesize))
heplane_ability4_img = pg.image.load(os.path.join(currentfiles,'heplane_abilites3.png')).convert_alpha()
heplane_ability4_img = pg.transform.scale(heplane_ability4_img, (abilityspritesize, abilityspritesize))
hepane_icon_img = pg.image.load(os.path.join(currentfiles,'icon0.png')).convert_alpha()
hepane_icon_img = pg.transform.scale(hepane_icon_img, (50, 50))

class gamemanager:
    def __init__(self):
        self.currentturn = 0
        self.grid = {}
        self.gridsize = 39
        self.click = 0
        self.showpos = False
        self.selectedchar = 0
        self.selectedattack = 0
        self.selectedenemy = 0
        self.animtimer = 0
        self.objects = []
        self.allies = []
        self.enemies = []
        self.animations = 0
        self.texts = {}
        
        
        
        self.gridamo = 8
        self.widthpos = WIDTH*(self.gridsize/100)
        widthlim = WIDTH-self.widthpos
        widthdis = widthlim-self.widthpos
        self.xstep = round(widthdis/self.gridamo)
        self.xcheck = self.xstep*self.gridamo +self.widthpos
        
        self.ypos = 50
        ylim = widthdis+self.ypos
        ydis = ylim-self.ypos
        self.ystep = round(ydis/self.gridamo)
        self.ycheck = self.ystep*self.gridamo + self.ypos
        
        
        for x in range(self.gridamo):
            for y in range(self.gridamo):
                self.grid.update({(x,y):0})
        
        self.vectopos = {}
        self.postovec = {}
        posx = self.widthpos
        posy = self.ypos
        step = self.xstep
        for x in self.grid:
            xx = posx+step*x[0]+step/2
            yy = posy+step*x[1]+step/2
            self.vectopos.update({(xx,yy):x})
            self.postovec.update({x:(xx,yy)})
            
        self.spawn()    
        self.create_order()
    def spawn(self):
        self.grid[0,1] = heplane(self.postovec[0,1])
        self.objects.append(self.grid[0,1])
        self.allies.append(self.grid[0,1])
        ll = hemo(self.postovec[0,0])
        self.grid[0,0] = ll
        self.objects.append(ll)
        self.enemies.append(ll)
        #ll = hemo(self.postovec[6,7])
        #self.grid[6,7] = ll
        #self.objects.append(ll)
        #self.enemies.append(ll)
    def draw_grid(self):
        for x in range(int(self.widthpos), int(self.xcheck+1), self.xstep):
            pg.draw.line(screen, BLACK, (x, int(self.ypos)), (x, int(self.ycheck)))
        for y in range(int(self.ypos), int(self.ycheck+1), self.ystep):
            pg.draw.line(screen, BLACK, (int(self.widthpos), y), (int(self.xcheck), y))
    def draw_gridobjects(self):
        for x in self.grid:
            if self.showpos:
                xx,yy = self.postovec[x[0],x[1]]
                txt = '{},{}'.format(int(x[0]),int(x[1]))
                draw_text(txt,20,YELLOW,xx,yy)
            if self.grid[x]:
                self.grid[x].draw()
    def draw_selection(self):
        cur = self.selectedchar
        if cur:
            for x in cur.abilites_actual:
                x.draw()
            
            if self.texts['player health']:
                screen.blit(self.texts['player health'][0],self.texts['player health'][1])
            if self.texts['player speed']:
                screen.blit(self.texts['player speed'][0],self.texts['player speed'][1])
            
            goal_center = int(440), int(843)
            if cur.speed < self.turn.speed:
                screen.blit(ui_slow, ui_slow.get_rect(center=goal_center))
            elif cur.speed > self.turn.speed:
                screen.blit(ui_fast, ui_slow.get_rect(center=goal_center))
            else:
                screen.blit(ui_same, ui_slow.get_rect(center=goal_center))
            
            self.draw_movement(cur)
        tar = self.selectedattack
        if tar:
            tar.drawtext()
            rect = pg.Surface((int(self.xstep), int(self.xstep)))
            rect.set_alpha(64)
            rect.fill(RED)
            for new in self.attackarea:
                new = vec(self.postovec[(new.x,new.y)])
                screen.blit(rect,(int(new.x-(self.xstep/2)),int(new.y-(self.xstep/2)))) 
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
            goal_center = (int(pos.x), int(pos.y))
            screen.blit(cur, cur.get_rect(center=goal_center))
    def mpostopos(self):
        ll = vec(pg.mouse.get_pos()[0]-self.widthpos,pg.mouse.get_pos()[1]-self.ypos)//self.xstep
        return (ll.x,ll.y)
    def updateani(self):
        if current_time - 1000 >self.animtimer:
            for x in self.grid:
                if self.grid[x]:
                    self.grid[x].animation += 1
                    if self.grid[x].animation > len(self.grid[x].combat_animation):
                        self.grid[x].animation = 1
            self.animtimer = pg.time.get_ticks()
    def showclick(self):
        if self.click:
            txt = str(pg.mouse.get_pos())
            draw_text(txt,50,BLACK,pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
    def selectchar(self):
        pos = self.mpostopos()  
        if pos in self.grid:
            if self.grid[pos]:         
                if self.selectedchar != self.grid[pos]:
                    #if self.selectedchar:
                    #    temp = self.translate(self.selectedchar.pos)
                    #    self.grid[temp] = 0
                    self.select(self.grid[pos])
                    
                else:
                    self.selectedchar = 0
                    self.selectedattack = 0
                    self.selectedenemy = 0
                    self.texts.update({'player health':0})
                    self.texts.update({'player speed':0})
    def select(self,tar):
        self.selectedchar = tar
        self.selectedattack = 0
        tar.abilites_create()
        temp = self.translate(tar.pos)
        txt = '{}/{}'.format(tar.health_current,tar.health)
        self.texts.update({'player health':create_text_fit_lister(txt,75,RED,480,670,120,'center')})
        txt = '{}'.format(tar.speed)
        self.texts.update({'player speed':create_text_fit_lister(txt,70,GREEN,517,840,70,'center')})
        self.currentmovement = self.movement(temp,tar.movement+1)
        self.currentmovementdraw = []
        for new in self.currentmovement:
            rect = pg.Surface((int(self.xstep), int(self.xstep)))
            rect.set_alpha(64)
            rect.fill(BLACK)
            new = vec(self.postovec[(new.x,new.y)])
            self.currentmovementdraw.append((rect,(int(new.x-(self.xstep/2)),int(new.y-(self.xstep/2)))))
    def selectattack(self):
        if self.selectedchar:
            for x in self.selectedchar.abilites_actual:
                x.pressed(mpos)
                if self.selectedattack:
                    group = self.enemies
                    if self.selectedchar in self.enemies:
                        group = self.allies
                    for x in group:
                        temp = self.vectopos[(x.pos.x,x.pos.y)]
                        self.attackarea = self.movement(temp,self.selectedattack.range+1,False,True)
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
    def snap_move(self,target,ll,save):
        ll = self.postovec[(ll.x,ll.y)]
        target.pos = vec(ll)
        self.grid[self.translate(save)] = 0
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
        if self.whose == len(self.heavies):
            self.whose = 0
        self.turn = self.heavies[self.whose]
        self.whose += 1
        
        self.phase = 'Player'
        if self.turn in self.enemies:
            self.phase = 'Enemy'
            self.selectedchar = self.turn
            temp = self.translate(self.selectedchar.pos)
            self.currentmovement = self.movement(temp,self.selectedchar.movement+1)
        temp = self.vectopos[(self.turn.pos.x,self.turn.pos.y)]
        self.turn_movement = self.movement(temp,self.turn.movement+1)
        self.turn_movementdraw = []
        for new in self.turn_movement:
            rect = pg.Surface((int(self.xstep), int(self.xstep)))
            rect.set_alpha(64)
            rect.fill(BLACK)
            new = vec(self.postovec[(new.x,new.y)])
            self.turn_movementdraw.append((rect,(int(new.x-(self.xstep/2)),int(new.y-(self.xstep/2)))))
    def enemy_turn(self):
        if self.phase == 'Enemy':
            tar = self.turn
            tarpos = tar.pos
            tarpos = vec(self.vectopos[(tarpos.x,tarpos.y)]) 
            new = self.allies[0]
            newpos = vec(self.vectopos[(new.pos.x,new.pos.y)])
            distance = math.sqrt(pow(newpos.x-tarpos.x,2)+pow(newpos.y-tarpos.y,2))
            closest = distance
            att = new
            for x in self.allies:
                new = x
                newpos = vec(self.vectopos[(new.pos.x,new.pos.y)])
                distance = math.sqrt(pow(newpos.x-tarpos.x,2)+pow(newpos.y-tarpos.y,2))
                if distance < closest:
                    closest = distance
                    att = new
            movement = tar.movement + 1
            
            checked = self.movement(tarpos,movement,add=True)
            
            if len(tar.abilites_actual) == 0:
                tar.abilites_create()
            
            
            
            attack = random.choice(tar.abilites_actual)
            newchecked = [] 
            attpos = vec(self.vectopos[(att.pos.x,att.pos.y)])
            attrange = attack.range + 1 
            newchecked = self.movement(attpos,attrange,seethrough=True)
            x = checked[0]
            y = newchecked[0]
            distance = math.sqrt(pow(y.x-x.x,2)+pow(y.y-x.y,2))
            closest = distance
            idealpos = x
            attackpos = y
            for x in checked:
                for y in newchecked:
                    distance = math.sqrt(pow(y.x-x.x,2)+pow(y.y-x.y,2))
                    if distance < closest:
                        closest = distance
                        idealpos = x
                        attackpos = y
            self.enemywho = tar
            self.enemyidealpos = idealpos
            self.whereattack = attackpos
            self.enemyselectedattack = attack
            self.enemytarget = att
            self.animations = animationmove()
            self.moveanimation = True
            self.phase = 0
            self.selectedattack = self.enemyselectedattack
            self.selectedenemy = self.enemytarget
            self.update_text(self.enemywho,self.enemytarget)
            
            
    def ally_turn(self):
        if not self.selectedattack:
            L.selectchar()
        if self.phase == 'Player':
            player = self.selectedchar
            if player == self.turn:
                self.checkmove()
                if self.mpostopos() in self.grid:
                    target = self.locate(vec(self.mpostopos()))
                    if self.selectedenemy == target and target != 0:
                        self.selectedattack.attack(target,player)
                        self.nextturn()
                        self.update_pos(player,self.translate(player.pos_temp))
                    if self.selectedattack and target in self.enemies:
                        for x in self.enemies:
                            temp = self.vectopos[(x.pos.x,x.pos.y)]
                            attackarea = self.movement(temp,self.selectedattack.range+1,False,True)
                            if self.translate(player.pos_temp) in attackarea:
                                self.selectedenemy = x
                                self.enemytext = []
                                self.update_text(player,x)
                                break
    def update_text(self,player,x):
        self.enemytext = []
        self.selectedattack.checktext()
        txt = '{}/{}'.format(player.health_current,player.health)
        self.enemytext.append(create_text_fit_lister(txt,75,RED,1665,605,100,'center'))
        
        if x.speed >= player.speed*2:
            txt = '{}/{}'.format(player.health_current-x.check_ret(),player.health)
            
        self.enemytext.append(create_text_fit_lister(txt,75,RED,1505,605,100,'center'))
        txt = '{}'.format(x.speed)
        self.enemytext.append(create_text_fit_lister(txt,70,GREEN,1845,605,65,'center'))
        
        txt = '{}/{}'.format(x.health_current,x.health)
        self.enemytext.append(create_text_fit_lister(txt,75,RED,1670,1005,100,'center'))
        txt = '{}/{}'.format(x.health_current-self.selectedattack.check_damage(),x.health)
        self.enemytext.append(create_text_fit_lister(txt,75,RED,1825,1005,100,'center'))
        goal_center = int(1765), int(605)
        if x.speed < player.speed:
            self.enemyspeedimage = ui_slow,ui_slow.get_rect(center=goal_center)
        elif x.speed >= player.speed*2:
            self.enemyspeedimage = ui_fast, ui_fast.get_rect(center=goal_center)
        else:
            self.enemyspeedimage = ui_same, ui_same.get_rect(center=goal_center)
    def checkmove(self):
        if self.mpostopos() in self.turn_movement:
            self.temp_pos(self.selectedchar,self.mpostopos())
    
    def movement(self,pos,movement,add=True,seethrough =False):
        
        checker = [vec(1,0),vec(0,1),vec(-1,0),vec(0,-1)] #vec check
        checked = [] 

        for x in range(0,movement): # checks the where the enemy can move 
            if x == 1: # first check around the enemy
                for x in checker:
                    new = pos+ x
                    if self.gridamo > new.x >= 0 and self.gridamo > new.y >= 0 and (self.grid[new.x,new.y] == 0 or  seethrough): # restricts movements to the grid
                        checked.append(new)
            else: # second and more checks and if the movement is more
                oldchecked = list(checked)
                for y in oldchecked: #grabs the already checked positions and checks around them
                    for x in checker:
                        new = y+ x 
                        if self.gridamo > new.x >= 0 and self.gridamo > new.y >= 0 and (self.grid[new.x,new.y] == 0 or  seethrough):
                            if new not in checked: #prevents already checked vecs to be added to the list
                                checked.append(new)
        if add:                        
            checked.append(vec(pos))
        return checked
class animationmove:
    def __init__(self):
        self.step = 0
        self.enemywho = L.enemywho
        self.savestart = vec(L.enemywho.pos)
        self.idealpos = L.enemyidealpos
        self.ww = vec(L.untranslate(L.enemyidealpos))
        self.selectedattack = L.selectedattack
        self.enemyidealpos =L.enemyidealpos
        self.whereattack = L.whereattack 
        self.enemytarget = L.enemytarget
        self.plaani = self.enemytarget.combat_animation
        self.eneani = self.enemywho.combat_animation
        self.x = vec(L.enemywho.drawn_pos)
        self.xgrt = False
        if self.ww.x < self.x.x:
            self.xgrt = True
        self.ygrt = False
        if self.ww.y < self.x.y:
            self.ygrt = True
        self.move()
        rect = pg.Rect(0,0,WIDTH*(2/3)/2,0)
        self.rightpart = pg.transform.chop(background_fall,rect)
        rect = pg.Rect(WIDTH*(2/3)/2,0,WIDTH*(2/3)/2,0)
        self.leftpart = pg.transform.chop(background_fall,rect)
        self.pos = -400
        self.steptwosteps = 1
    def move(self):
        ww = self.ww
        x = self.x
        if (ww.y-x.y) != 0:
            self.ang = math.atan((ww.x-x.x)/(ww.y-x.y))
            ver = math.cos(self.ang)
            hor = math.sin(self.ang)
        else:
            self.ang = 0
            ver = 0
            if (ww.x-x.x)<0:
                hor = -1
                self.degrees = -90
            else:
                hor = 1
        if (ww.y-x.y) < 0:
            self.enemywho.drawn_pos -= vec(hor,ver)
        else:
            self.enemywho.drawn_pos -= vec(hor,ver) *-1
        
    def stepone(self):
        self.move()
        cot1,cot2 = False,False
        
        if self.enemywho.drawn_pos.x != self.ww.x:
            if self.xgrt:
                if self.enemywho.drawn_pos.x < self.ww.x:
                    cot1 = True
            else:
                if self.enemywho.drawn_pos.x > self.ww.x:
                    cot1 = True
        else:
            cot1 = True
        
        if self.enemywho.drawn_pos.y != self.ww.y:
            if self.ygrt:
                if self.enemywho.drawn_pos.y < self.ww.y:
                    cot2 = True
            else:
                if self.enemywho.drawn_pos.y > self.ww.y:
                    cot2 = True
        else:
            cot2 = True
        if cot1 and cot2:
            self.step +=1
            L.snap_move(self.enemywho,self.idealpos,self.savestart)
            L.update_pos(self.enemywho,self.idealpos)
            if L.selectedattack:
                group = L.enemies
                if L.selectedchar in L.enemies:
                    group = L.allies
                for x in group:
                    temp = L.vectopos[(x.pos.x,x.pos.y)]
                    L.attackarea = L.movement(temp,self.selectedattack.range+1,False,True)
            if self.enemyidealpos != self.whereattack:
                self.step += 1
                
    def steptwo(self):
        cover = pg.Surface((WIDTH,HEIGHT))
        cover.fill((128,128,128))
        cover.set_alpha(128)
        goal_center = int(WIDTH/2), int(HEIGHT/2)
        screen.blit(cover, cover.get_rect(center=goal_center))
        goal_center = int(self.pos), int(HEIGHT/2)
        screen.blit(self.leftpart, self.leftpart.get_rect(center=goal_center))
        goal_center = int(WIDTH-self.pos), int(HEIGHT/2)
        screen.blit(self.rightpart, self.rightpart.get_rect(center=goal_center))
        
        ani = dict(self.plaani)
        cur = ani[self.enemytarget.animation]
        goal_center = (int(self.pos), int(HEIGHT/2))
        cur = pg.transform.scale(cur,(250,250))
        screen.blit(cur, cur.get_rect(center=goal_center))
        
        ani = dict(self.eneani)
        cur = ani[self.enemywho.animation]
        #HEIGHTTILESIZE = 150
        cur = pg.transform.scale(cur,(250,250))
        goal_center = (int(WIDTH-self.pos), int(HEIGHT/2))
        screen.blit(cur, cur.get_rect(center=goal_center))
        if self.steptwosteps == 1:
            if self.pos < WIDTH*1/3:
                self.pos += 30
            else:
                self.pos = WIDTH*1/3
                self.steptwosteps += 1
        if self.steptwosteps == 2:
            draw_text(L.enemyselectedattack.name,50,BLACK,int(WIDTH-self.pos-100), int(HEIGHT/3))
        if self.steptwosteps == 3:
            self.step +=1
            print(L.enemyselectedattack)
            L.enemyselectedattack.attack(self.enemytarget,self.enemywho)
    def enemymove(self):
        if self.step == 0:
            self.stepone()
            
        if self.step == 1:
            self.steptwo()
        if self.step == 2:    
            L.nextturn()
            L.animations = 0
def speed_sort(target):
    return target.speed            
        
ui_fall = pg.image.load(os.path.join(filename,'battle_ui.png'))
ui_fall = pg.transform.scale(ui_fall, (WIDTH, HEIGHT))

ui_slow = pg.image.load(os.path.join(filename,'speedicon0.png'))
ui_slow = pg.transform.scale(ui_slow, (50, 50))
ui_fast = pg.image.load(os.path.join(filename,'speedicon1.png'))
ui_fast = pg.transform.scale(ui_fast, (50, 50))
ui_same = pg.image.load(os.path.join(filename,'speedicon2.png'))
ui_same = pg.transform.scale(ui_same, (50, 50))

background_fall = pg.image.load(os.path.join(filename,'backgorunds-2.png.png'))
background_fall = pg.transform.scale(background_fall, (int(WIDTH*(2/3)), int(HEIGHT*(2/3))))
            
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
                L.click = True
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    current_time = pg.time.get_ticks()
    L.draw_grid()
    L.draw_gridobjects()
    L.updateani()
    L.enemy_turn()
    L.draw_selection_char()
    L.draw_ui()
    L.draw_selection()
    if L.animations:
        L.animations.enemymove()
    L.showclick()
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways