import skills
import pygame as pg
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
import time


vec = pg.math.Vector2




TILESIZE = 30
GRIDWIDTH = 9
GRIDHEIGHT = 9
WIDTH = 700
HEIGHT = 700
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
def draw_text(text=str, size=int, color=tuple, x=float, y=float, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)

def draw_text_center(text=str, size=int, color=tuple, x=int, y=int):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x,y))
    screen.blit(text_surface, text_rect)
    
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

def current_milli_time():
    return round(time.time() * 1000)


filename = os.path.dirname(sys.argv[0])

highscores = shelve.open(filename+'/scorestopdown.txt',writeback=True)

musicname = filename +'/othermusics'

filename += '/images'

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

class enemymanager:
    def __init__(self):
        self.enemies = []
        self.obstacles = []
        self.limit = 5
        self.pos = vec(0,0)
        self.spawnobstaclesstart()
        self.variety = 0
        self.listofenemies = []
        self.create_randomenemies()
    def create_randomenemies(self):
        self.listofenemies.append([random.randint(5,50),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.uniform(0.5,4),random.randint(10,50)])
    def spawnenemy(self):
        if state.israndom:
            chosenside = random.randint(0,3)
            if chosenside == 0: #top side
                pos = vec(-20,random.randint(0,WIDTH))
            if chosenside == 1: #right side
                pos = vec(random.randint(0,HEIGHT),WIDTH+20)
            if chosenside == 2: #right side
                pos = vec(HEIGHT+20,random.randint(0,WIDTH))
            if chosenside == 3: #right side
                pos = vec(random.randint(0,HEIGHT),-20)
            chosenenemy = random.randint(0,self.variety)
            return lvl1(pos,self.listofenemies[chosenenemy])

        else:
            chosenside = random.randint(0,3)
            if chosenside == 0: #top side
                pos = vec(-20,random.randint(0,WIDTH))
            if chosenside == 1: #right side
                pos = vec(random.randint(0,HEIGHT),WIDTH+20)
            if chosenside == 2: #right side
                pos = vec(HEIGHT+20,random.randint(0,WIDTH))
            if chosenside == 3: #right side
                pos = vec(random.randint(0,HEIGHT),-20)

            chosenenemy = random.randint(0,self.variety)
            if chosenenemy == 0:
                return lvl1(pos)
            if chosenenemy == 1:
                return lvl2(pos)
    def spawnobstacle(self,pos):
        return tree(pos)
    def spawnobstaclelive(self):
        chosenside = random.randint(0,3)
        if chosenside == 0: #top side
            pos = vec(-20,random.randint(0,WIDTH))
        if chosenside == 1: #right side
            pos = vec(random.randint(0,HEIGHT),WIDTH+20)
        if chosenside == 2: #right side
            pos = vec(HEIGHT+20,random.randint(0,WIDTH))
        if chosenside == 3: #right side
            pos = vec(random.randint(0,HEIGHT),-20)
        return tree(pos)
    def spawnobstaclesstart(self):
        for x in range(0,10):
            pos = vec(random.randint(-200,WIDTH+200),random.randint(-200,HEIGHT+200))
            self.obstacles.append(self.spawnobstacle(pos))
    def checkobstacles(self):
        for x in self.obstacles:
            if not -200<x.pos.x<WIDTH+200 or not -200<x.pos.y<HEIGHT+200:
                self.obstacles.remove(x)
                self.obstacles.append(self.spawnobstaclelive())
    def checkspawn(self):
        if len(self.enemies) < self.limit:
            self.enemies.append(self.spawnenemy())
    def draw_enemies(self):
        for x in self.enemies:
            x.draw()
        for x in self.obstacles:
            x.draw()
    def move(self,direction):
        for x in self.enemies:
            x.pos += direction
            x.update_rect()
        for x in self.obstacles:
            x.pos += direction
            x.update_rect()
    def enemove(self,target):
        for x in self.enemies:
            test = list(self.enemies)
            test.remove(x)
            new = self.makerects(test)
            position = target.pos
            if position == vec(-202,-202) :
                if x.randompos == None:
                    chosenside = random.randint(0,3)
                    if chosenside == 0: #top side
                        pos = vec(-201,random.randint(0,WIDTH))
                    if chosenside == 1: #right side
                        pos = vec(random.randint(0,HEIGHT),WIDTH+201)
                    if chosenside == 2: #right side
                        pos = vec(HEIGHT+201,random.randint(0,WIDTH))
                    if chosenside == 3: #right side
                        pos = vec(random.randint(0,HEIGHT),-201)
                    x.randompos = pos
                position = x.randompos
            if (position.y-x.pos.y) != 0:
                self.ang = math.atan((position.x-x.pos.x)/(position.y-x.pos.y))
                ver = math.cos(self.ang)
                hor = math.sin(self.ang)
            else:
                self.ang = 0
                ver = 0
                if (position.x-x.pos.x)<0:
                    hor = -1
                    self.degrees = -90
                else:
                    hor = 1
            if (position.y-x.pos.y) < 0:
                x.pos += vec(hor,ver) *-1* x.speed
                x.update_rect()
                if pg.Rect.collidelist(x.rect,new) != -1:
                    bumped = pg.Rect.collidelist(x.rect,new)
                    if bumped != -1:
                        for ww in self.enemies+self.obstacles:
                            if ww.rect == new[bumped]:
                                if (ww.pos.y-x.pos.y) != 0:
                                    self.ang = math.atan((ww.pos.x-x.pos.x)/(ww.pos.y-x.pos.y))
                                    ver = math.cos(self.ang)
                                    hor = math.sin(self.ang)
                                else:
                                    self.ang = 0
                                    ver = 0
                                    if (ww.pos.x-x.pos.x)<0:
                                        hor = -1
                                        self.degrees = -90
                                    else:
                                        hor = 1
                                if (ww.pos.y-x.pos.y) < 0:
                                    x.pos -= vec(hor,ver)*-1
                                    x.update_rect()
                                else:
                                    x.pos -= vec(hor,ver) 
                                    x.update_rect()
                        #bumped = pg.Rect.collidelist(x.rect,new)
                        #x.pos -= vec(hor,ver) *-1
                        #x.update_rect()
                        
            else:
                x.pos += vec(hor,ver)* x.speed
                x.update_rect()
                if pg.Rect.collidelist(x.rect,new) != -1:
                    bumped = pg.Rect.collidelist(x.rect,new)
                    for ww in self.enemies+self.obstacles:
                        if ww.rect == new[bumped]:
                            if (ww.pos.y-x.pos.y) != 0:
                                self.ang = math.atan((ww.pos.x-x.pos.x)/(ww.pos.y-x.pos.y))
                                ver = math.cos(self.ang)
                                hor = math.sin(self.ang)
                            else:
                                self.ang = 0
                                ver = 0
                                if (ww.pos.x-x.pos.x)<0:
                                    hor = -1
                                    self.degrees = -90
                                else:
                                    hor = 1
                            if (ww.pos.y-x.pos.y) < 0:
                                x.pos -= vec(hor,ver) *-1
                                ww.update_rect()
                            else:
                                x.pos -= vec(hor,ver)
                                x.update_rect()
                    #x.pos -= vec(hor,ver) 
                    #x.update_rect()  
            if not -200<x.pos.x<WIDTH+200 or not -200<x.pos.y<HEIGHT+200:
                self.enemies.remove(x)
                self.checkspawn()
    def checkhit(self,target):
        global invincible_timer
        if target.invincible:
            new = []
            for ww in self.enemies:
                new.append(ww.rect)
            for ww in self.obstacles:
                new.append(ww.rect)
            rect = pg.Rect(target.pos.x,target.pos.y,10,20)
            col = pg.Rect.collidelist(rect,new)
            if col != -1: 
                for ww in self.enemies+self.obstacles:
                    if ww.rect == new[col]:
                        if not over.invincible:
                            target.health_current -= 1
                            target.invincible = False
                            invincible_timer = pg.time.get_ticks()
                            ang = math.atan((ww.pos.x-target.pos.x)/(ww.pos.y-target.pos.y))
                            ver = math.cos(ang)
                            hor = math.sin(ang)
                            if (ww.pos.y-target.pos.y) < 0:
                                self.move(vec(hor,ver)*50 *-1)
                                continue
                            self.move(vec(hor,ver)*50)
    def makerects(self,test=0):
        new = []
        if test == 0:
            test = self.enemies
        for ww in test:
            new.append(ww.rect)
        for ww in self.obstacles:
            new.append(ww.rect)
        return new
    def checkhealth(self):
        for x in self.enemies:
            if x.health_current <= 0:
                self.spawnexp(x.pos,1)
                self.enemies.remove(x)
                
        for x in self.obstacles:
            if x.health_current <= 0:
                self.obstacles.remove(x)
    def spawnexp(self,pos,lvl):
        if lvl == 1:
            pm.experince.append(exp1(pos))
 

class exp1:
    def __init__(self,pos):
        self.pos = pos
        self.amount = 1
        self.update_rect()
    def update_rect(self):
        self.rect = pg.Rect(self.pos.x, self.pos.y, 5, 5)
    def draw(self):
        pg.draw.rect(screen,YELLOW,self.rect)




class defaultenemy:
    def __init__(self,pos,thing):
        self.pos = pos
        self.randompos = None
        self.sizey = 25
        if state.israndom:
            self.health_current = thing[0]
            self.color = thing[1]
            self.speed = thing[2]
            self.sizey = thing[3]
        self.sizex = self.sizey*0.6
        self.update_rect()
    def draw(self):
        pg.draw.rect(screen,self.color,self.rect)
        if state.show_hitbox:
            rect = pg.Rect(self.pos.x, self.pos.y, 1, 1)
            pg.draw.rect(screen,BLACK,rect)
    def update_rect(self):
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.sizex, self.sizey)    
        
class lvl1(defaultenemy):
    def __init__(self,pos,things=list):
        self.health_current = 10
        self.color = GREEN
        self.speed = 1
        super().__init__(pos,things)
        
        
class lvl2(defaultenemy):
    def __init__(self,pos,things=list):
        self.health_current = 15
        self.color = BLUE
        self.speed = 1.5
        super().__init__(pos,things)
        

    
class tree:
    def __init__(self,pos):
        self.pos = pos
        self.health_current = 1000
        self.image = treeimage
        self.image = pg.transform.scale(self.image,(40,50))
        self.update_rect()
    def draw(self):
        screen.blit(self.image,(self.pos.x-10,self.pos.y-7))
        if state.show_hitbox:
            #rect = pg.Rect(self.pos.x, self.pos.y, 40, 50)
            pg.draw.rect(screen,GREEN,self.rect)
    def update_rect(self):
        self.rect = pg.Rect(self.pos.x, self.pos.y, 25, 40)
    
class player:
    def __init__(self,pos,col,speed):
        self.pos = pos
        self.sizex = 10
        self.sizey = 20
        self.color = col
        self.speed = speed
        self.health = 3
        self.health_current = 3
        self.lvl = 0
        self.exeperince = 0
        self.exp_need = 5
        self.range = 5
        self.damage = 0
        self.weapon_speed = 1
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.invincible = True
        self.fire_speed = 500
        self.shoot = False
    def move(self,direction):
        if direction == 'left':
            self.left = True
        if direction == 'right':
            self.right = True
        if direction == 'down':
            self.down = True
        if direction == 'up':
            self.up = True
    def update_move(self):
        if self.left and self.up:
            return  vec(-0.7,-0.7) * self.speed
        if self.right and self.up:
            return  vec(0.7,-0.7)* self.speed
        if self.right and self.down:
            return  vec(0.7,0.7)    * self.speed
        if self.left and self.down:
            return vec(-0.7,0.7)   * self.speed
        if self.up:
            return vec(0,-1)* self.speed
        if self.down:
            return vec(0,1)* self.speed
        if self.left:
            return vec(-1,0)* self.speed
        if self.right:
            return vec(1,0)* self.speed
        return vec(0,0)
        #self.up = False
        #self.down = False
        #self.left = False
        #self.right = False
    def draw(self):
        self.draw_health()
        self.draw_player()
        self.draw_lvl()
    def draw_player(self):
        if state.show_hitbox:
            rect = pg.Rect(P.pos.x-((20+P.range-10)/2),(P.pos.y)-(P.range/2),20+(P.range),20+(P.range))
            pg.draw.rect(screen,BLUE,rect)
        rect = pg.Rect(self.pos.x, self.pos.y, self.sizex, self.sizey)
        pg.draw.rect(screen,self.color,rect)
        if self.invincible == False:
            rect = pg.Rect(self.pos.x+5, self.pos.y+10, 5, 10)
            pg.draw.rect(screen,BLUE,rect)
        
    def draw_health(self):
        txt = '{}/{}'.format(self.health_current, self.health)
        draw_text(txt,30,RED,0,20)
    def draw_lvl(self):
        rect = pg.Rect(5, 5, WIDTH-10, 20)
        pg.draw.rect(screen,self.color,rect)
        rect = pg.Rect(5, 5, (WIDTH-10)*(self.exeperince/self.exp_need), 20)
        pg.draw.rect(screen,YELLOW,rect)
        txt = 'level {}'.format(P.lvl)
        draw_text_center(txt,30,BLACK,WIDTH/2,17)
        

class playermanager:
    def __init__(self):
        self.projectiles = []
        self.experince = []
        self.check_weapon()
    def check_weapon(self):
        selected = state.current_weapon
        if selected == 'Lightning':
            self.lightning_bounce = 0
            self.lightning_size = 1
            self.lightning_range = 0
        if selected == 'Phoenix Gun':
            self.flat_damage = 0
            self.bullet_pierce =0
    def spawnweapon(self,origin,moving):
        selected = state.current_weapon
        if selected == 'Lightning':
            return lightning(origin,moving)
        if selected == 'Phoenix Gun':
            return bullet(origin,moving)
    def addbullet(self,origin,moving):
        self.projectiles.append(self.spawnweapon(origin,moving))
    def move_objects(self,direction):
        for x in self.projectiles:
            x.pos += direction
            x.update_rect()
        for x in self.experince:
            x.pos += direction
            x.update_rect()
    def projmove(self):
        for x in self.projectiles:
            x.pos += x.trajectory
            x.update_rect()
            
            
            x.collide()
            eneman.checkhealth()
            if not -200<x.pos.x<WIDTH+200 or not -200<x.pos.y<HEIGHT+200 or x.exsistence():
                if x in self.projectiles:
                    self.projectiles.remove(x)
    def draw(self):
        for x in self.projectiles:
            x.draw()
        for x in self.experince:
            x.draw()
    def check_exp(self):
        new = []
        for x in self.experince:
            new.append(x.rect)
        rect = pg.Rect(P.pos.x-((20+P.range-10)/2),(P.pos.y)-(P.range/2),20+(P.range),20+(P.range))
        col = pg.Rect.collidelist(rect,new)
        if col != -1: 
            for ww in self.experince:
                if ww.rect == new[col]:
                    P.exeperince += ww.amount
                    self.experince.remove(ww)
            lvl = P.exeperince - P.exp_need
            if lvl >= 0 :
                P.exeperince = 0 + lvl
                P.exp_need += 5
                P.lvl += 1
                over.create_skills()
    
class bullet:
    def __init__(self,origin,moving):
        self.pos = vec(origin.pos.x,origin.pos.y)
        self.update_rect()
        self.damage = 5
        self.ticks_current = 0
        self.ticks = 50
        self.piercing = pm.bullet_pierce
        self.pierced = []
        if (self.pos.y-moving.y) != 0:
            self.ang = math.atan((self.pos.x-moving.x)/(self.pos.y-moving.y))
            #if random.choice([True,False]):
            spread = random.uniform(-0.1,0.15)
            print(spread)
            self.ang = self.ang + spread
            ver = math.cos(self.ang)
            hor = math.sin(self.ang)
            self.save = True
            if (self.pos.y-moving.y) < 0:
                self.save =False
            self.degrees = math.degrees(self.ang)
        else:
            self.ang = 0
            ver = 0
            if (self.pos.x-moving.x)<0:
                hor = -1
                self.degrees = -90
            else:
                hor = 1
                self.degrees = 90
            self.save = True
            if (self.pos.y-moving.y) < 0:
                self.save =False
        if (self.pos.y-moving.y) < 0:
            self.trajectory = vec(hor,ver) *5*P.weapon_speed
        else:
            self.trajectory = vec(hor,ver) *5*P.weapon_speed *-1
    def collide(self):
        new = eneman.makerects()
        col = pg.Rect.collidelist(self.rect,new)
        if col != -1:
            for ww in eneman.enemies + eneman.obstacles:
                if ww.rect == new[col] and ww not in self.pierced:
                    ww.health_current -= (self.damage + pm.flat_damage)* (1+P.damage) 
                    if self.piercing == len(self.pierced):
                        pm.projectiles.remove(self)
                    self.pierced.append(ww)
    def exsistence(self):
        self.ticks_current += 1
        if self.ticks_current >= self.ticks:
            return True
    def draw(self):
        mysurf = bulletimage
        if self.save:
            mysurf = pg.transform.rotate(mysurf,self.degrees+180)
        else:
            mysurf = pg.transform.rotate(mysurf,self.degrees)
        mysurf = pg.transform.scale(mysurf,(15,15))
        #mysurf.fill(BLACK)
        screen.blit(mysurf,(self.rect[0],self.rect[1]))
        if state.show_hitbox:
            surf = pg.Surface((15,15))
            surf.fill(GREEN)
            surf.set_alpha(100) 
            screen.blit(surf,(self.rect[0],self.rect[1]))
    def update_rect(self):
        self.rect = pg.Rect(self.pos.x, self.pos.y, 15, 15)

bulletimage = pg.image.load(os.path.join(filename,'New Piskel.png'))


class lightning:
    def __init__(self,origin,moving,bounce = 0,ticks = 4):
        self.pos = vec(origin.pos.x+origin.sizex/2,origin.pos.y+origin.sizey/2)
        self.update_rect()
        self.damage = 10
        self.radius = 20 *pm.lightning_size
        self.bounced = bounce
        self.ticks_current = 0
        self.ticks = ticks
        if ticks != 1:
            self.ticks = ticks + pm.lightning_range
        if moving != 0:
            if (self.pos.y-moving.y) != 0:
                self.ang = math.atan((self.pos.x-moving.x)/(self.pos.y-moving.y))
                ver = math.cos(self.ang)
                hor = math.sin(self.ang)
                self.save = True
                if (self.pos.y-moving.y) < 0:
                    self.save =False
                self.degrees = math.degrees(self.ang)
            else:
                self.ang = 0
                ver = 0
                if (self.pos.x-moving.x)<0:
                    hor = -1
                    self.degrees = -90
                else:
                    hor = 1
                    self.degrees = 90
                self.save = True
                if (self.pos.y-moving.y) < 0:
                    self.save =False
            if (self.pos.y-moving.y) < 0:
                self.trajectory = vec(hor,ver) *(P.weapon_speed+20)
            else:
                self.trajectory = vec(hor,ver) *((P.weapon_speed+20) *-1)
        else:
            self.trajectory = vec(0,0)
    def collide(self):  
        for x in eneman.enemies:
            new = x.pos + vec(15, 25)/2
            c = math.sqrt(pow(new.x-self.pos.x,2)+pow(new.y-self.pos.y,2))
            if c <= self.radius:
                x.health_current -= self.damage
                if self.bounced != pm.lightning_bounce:
                    self.bounced+=1
                    pm.projectiles.append(lightning(x,0,self.bounced,1))
    def exsistence(self):
        self.ticks_current += 1
        if self.ticks_current >= self.ticks:
            return True
    def draw(self):
        if state.show_hitbox:
            pg.draw.circle(screen,BLUE,self.pos,self.radius)
        mysurf = lightning_still
        if self.save:
            mysurf = pg.transform.rotate(mysurf,self.degrees+180)
        else:
            mysurf = pg.transform.rotate(mysurf,self.degrees)
        if self.trajectory != vec(0,0):
            mysurf = random.choice([lightning_move_1,lightning_move_2])
            if self.save:
                mysurf = pg.transform.rotate(mysurf,self.degrees+180)
            else:
                mysurf = pg.transform.rotate(mysurf,self.degrees)
        mysurf = pg.transform.scale(mysurf,(int(self.radius),int(self.radius)))
        screen.blit(mysurf,(self.rect[0]-(self.radius/2),self.rect[1]-(self.radius/2)))
        
    def update_rect(self):
        self.rect = pg.Rect(self.pos.x, self.pos.y, 15, 15)

lightning_move_1 = pg.image.load(os.path.join(filename,'1.png'))
lightning_move_2 = pg.image.load(os.path.join(filename,'2.png'))
lightning_still = pg.imgae.load(os.path.join(filename,'0.png'))

class manager:
    def __init__(self):
        self.start_time = current_milli_time()
        self.minutes = 0
        self.rate_enemy = 1000
        self.check_spawn_timer = pg.time.get_ticks()
        self.limit_increase_timer = pg.time.get_ticks()
        self.rate_enemy_timer = pg.time.get_ticks()
        self.fire_speed_timer = pg.time.get_ticks()
        self.pause_time = False
        self.specialpause_time = False
        self.pause_timer = 0
        self.oldpausetime = 0
        self.ticktimer = 0
        self.oldpausetick = 0
        self.newenemytimer = 0
        self.invincible = False
        self.skilling =False
        self.addvariety = 60000
        self.newenemy =False
    def draw_time(self):
        new_time=0
        if self.pause_time or self.specialpause_time:
            #new =self.start_time-
            new_time= time.time() * 1000 - self.pause_timer
        displaytime = time.time() * 1000 - self.start_time - self.oldpausetime- new_time
        minutes = 0
        if int(round(displaytime/1000,0)) > 60:
            minutes = int((int(round(displaytime/1000,0)) - int(round(displaytime/1000,0))%60) /60)
            displaytime -= 60000 *minutes
        displaytime = int(round(displaytime/1000,0))
        if displaytime < 10 and minutes < 10:
            displaytime = '0{}:0{}'.format(minutes,displaytime)
        elif displaytime < 10:
            displaytime = '{}:0{}'.format(minutes,displaytime)
        elif minutes < 10:
            displaytime = '0{}:{}'.format(minutes,displaytime)
        else:
            displaytime = '{}:{}'.format(minutes,displaytime)
        draw_text_center(displaytime,40,BLACK,WIDTH-50,70)
        if state.show_hitbox:
            seconds = str(round(new_time%1000))
            new_time = str(str(int(new_time/1000))+':'+seconds)
            draw_text(new_time,20,BLACK,WIDTH-50,30)
        #displaytime = str(time.time())
        #draw_text(displaytime,20,BLACK,WIDTH-100,30)
    def draw_newenemy(self):
        if self.newenemy:
            draw_text_center('You Have a Bad Feeling',30,RED,WIDTH/2,HEIGHT*(2/5))
    def timers(self):
        if P.shoot and current_time -  over.fire_speed_timer> P.fire_speed + self.ticktimer:
            pm.addbullet(P,vec(pg.mouse.get_pos()))
            over.fire_speed_timer = pg.time.get_ticks()
        if P.invincible == False:
            if current_time - invincible_timer > 2000 + self.ticktimer:
                P.invincible = True
        if current_time - self.check_spawn_timer > self.rate_enemy + self.ticktimer:
            eneman.checkspawn()
            self.check_spawn_timer = pg.time.get_ticks()
        if current_time - self.limit_increase_timer > 5000 + self.ticktimer:
            eneman.limit += 1
            self.limit_increase_timer = pg.time.get_ticks()
        if current_time - self.rate_enemy_timer - 15000 + self.ticktimer:
            self.rate_enemy -= 500
            self.rate_enemy_timer = pg.time.get_ticks()
        new_time=0
        if self.pause_time:
            #new =self.start_time-
            new_time= time.time() * 1000 - self.pause_timer
        if time.time() * 1000 - self.start_time - self.oldpausetime- new_time >= self.addvariety:
            self.newenemy = True
            self.newenemytimer = pg.time.get_ticks()
            self.addvariety += self.addvariety
            if state.israndom:
                eneman.create_randomenemies()
                eneman.variety += 1
            else:
                eneman.variety += 1
                if eneman.variety > 1:
                    eneman.variety = 1
        if self.newenemy:        
            if current_time - self.newenemytimer > 5000:
                self.newenemy = False
                self.newenemytimer = 0
    def create_skills(self):
        self.skills = []
        self.skilling = True
        self.pause()
        P.invincible = True
        for x in skillspaces:
            self.skills.append(skillicon(x,random.choice(skill+specific_skill_dict[state.current_weapon])))
    def pause(self):
        self.pause_time = True
        self.pause_timer=current_milli_time()
        self.ticktimer = pg.time.get_ticks()
    def pausespecial(self):
        self.specialpause_time = True
        self.pause_timer=current_milli_time()
        #self.ticktimer = pg.time.get_ticks()
    def unpause(self):
        self.pause_time =False
        self.oldpausetime += time.time() * 1000 - self.pause_timer
        self.ticktimer = 0
    def select_skill(self,mpos):
        if self.skilling:
    
            for x in self.skills:
                if x.rect.collidepoint((mpos.x,mpos.y)):
                    for qq in x.actions:
                        if qq in P.__dict__:
                            P.__dict__[qq] += x.actions[qq]
                        else:
                            pm.__dict__[qq] += x.actions[qq]
                    self.skilling = False
                    self.unpause()
    def draw_levelup(self):
        if self.skilling:
            for x in self.skills:
                pg.draw.rect(screen,RED,x.rect)
                draw_text_wraped(x.description,30,WHITE,x.pos.x+60,x.pos.y,400,draw_rect = True)
            
class skillicon:
    def __init__(self,pos,target):
        self.pos = pos
        target = skill_dict[target]
        self.name = target
        self.description = target['description']
        self.actions = target['action']
        self.update_rect()
    def update_rect(self):
        self.rect = pg.Rect(self.pos.x, self.pos.y, 50, 50)
        



skillspaces = [vec(WIDTH*(1/5),HEIGHT*(3/10)),vec(WIDTH*(1/5),HEIGHT*(4/10)),vec(WIDTH*(1/5),HEIGHT*(5/10)),vec(WIDTH*(1/5),HEIGHT*(6/10)),vec(WIDTH*(1/5),HEIGHT*(7/10))]

class Menu:
    def __init__(self):
        self.title = 'Surviving Klov'
        pg.mixer.music.load(os.path.join(musicname,'landing.mp3'))
        pg.mixer.music.play(-1,0,2000)
        self.buttons = [Play(vec(WIDTH/2,HEIGHT*(2/5))),Randombutton(vec(WIDTH/2,HEIGHT*(5/10))),SelectWeapon(vec(WIDTH/2,HEIGHT*(4/5))),Leaderboardbutton(vec(WIDTH/2,HEIGHT*(6/10)))]
    def draw_buttons(self):
        draw_text_center(self.title,50,RED,WIDTH/2,HEIGHT*(1/5))
        for x in self.buttons:
            x.draw()
    def press_buttons(self,mpos):
        for x in self.buttons:
            x.pressed(mpos)

class defaultbutton:
    def __init__(self,sizex = 300,sizey= 50):
        self.rect = pg.Rect((self.pos.x-sizex/2), (self.pos.y-sizey/2), sizex, sizey)
    def draw(self):
        pg.draw.rect(screen,BLACK,self.rect)
        draw_text_center(self.name,40,WHITE,self.pos.x,self.pos.y)

class Leaderboardbutton(defaultbutton):
    def __init__(self,pos):
        self.name = 'Leaderboard'
        self.pos = pos
        super().__init__()
    def pressed(self,mpos):
        global over,P,pm,eneman,menu
        if self.rect.collidepoint((mpos.x,mpos.y)):
            menu = leaderboard()

class leaderboard:
    def __init__(self):
        self.title = 'Leaderboard'
        self.buttons = [returntomenu(vec(WIDTH/2,HEIGHT*(8/10)))]
        create_highscores(self)
    def draw_buttons(self):
        draw_text_center(self.title,50,RED,WIDTH/2,HEIGHT*(1/10))
        for x in self.buttons:
            x.draw()
        draw_highscores(self)
    def press_buttons(self,mpos):
        for x in self.buttons:
            x.pressed(mpos)

def draw_highscores(target):
    draw_text_center('Level',40,BLACK,WIDTH/4,HEIGHT*(2/11))
    draw_text_center('Time',40,BLACK,WIDTH*(2/4),HEIGHT*(2/11))
    draw_text_center('Weapon',40,BLACK,WIDTH*(3/4),HEIGHT*(2/11))
    for x in target.highscores:
        x.draw()

class Play(defaultbutton):
    def __init__(self,pos):
        self.name = 'Play'
        self.pos = pos
        super().__init__()
    def pressed(self,mpos):
        global over,P,pm,eneman,menu
        if self.rect.collidepoint((mpos.x,mpos.y)):
            state.current_state = 'gameplay'
            over = manager()
            P = player(vec(WIDTH/2,HEIGHT/2),RED,-2)
            pm = playermanager()
            eneman = enemymanager()
            menu = None

class Randombutton(defaultbutton):
    def __init__(self,pos):
        self.name = 'Random'
        if state.israndom:
            self.name = 'Survive'
        self.pos = pos
        super().__init__()
    def pressed(self,mpos):
        if self.rect.collidepoint((mpos.x,mpos.y)):
            if state.israndom:
                self.name = 'Random'
                state.israndom = False
            else:
                self.name = 'Survive'
                state.israndom = True


class SelectWeapon(defaultbutton):
    def __init__(self,pos):
        self.name = 'Change Weapon'
        self.pos = pos
        super().__init__()
    def pressed(self,mpos):
        global menu
        if self.rect.collidepoint((mpos.x,mpos.y)):
            state.current_state = 'menu'
            menu = weaponselectmenu()
    
class pausemenu:
    def __init__(self):
        self.title = 'Paused'
        self.buttons = [resume(vec(WIDTH/2,HEIGHT*(4/10))),restart(vec(WIDTH/2,HEIGHT*(5/10))),returntomenu(vec(WIDTH/2,HEIGHT*(6/10)))]
    def draw_buttons(self):
        draw_text_center(self.title,50,RED,WIDTH/2,HEIGHT*(1/5))
        for x in self.buttons:
            x.draw()
    def press_buttons(self,mpos):
        for x in self.buttons:
            x.pressed(mpos)

class resume(defaultbutton):
    def __init__(self,pos):
        self.name = 'Resume'
        self.pos = pos
        super().__init__()
    def pressed(self,mpos):
        if self.rect.collidepoint((mpos.x,mpos.y)):
            state.current_state = 'gameplay'
            over.unpause()

class restart(defaultbutton):
    def __init__(self,pos):
        self.name = 'Restart'
        self.pos = pos
        super().__init__()
    def pressed(self,mpos):
        global over,P,pm,eneman,menu
        if self.rect.collidepoint((mpos.x,mpos.y)):
            state.current_state = 'gameplay'
            over = manager()
            P = player(vec(WIDTH/2,HEIGHT/2),RED,-2)
            pm = playermanager()
            eneman = enemymanager()



class Gameover:
    def __init__(self) :
        pg.mixer.music.load(os.path.join(musicname,'death.mp3'))
        pg.mixer.music.play(-1,0,5000)
        newtime = round((time.time() * 1000 - over.start_time - over.oldpausetime)/1000)
        lvl = P.lvl
        weapon = state.current_weapon
        self.highscores = []
        for x in highscores['highscores']:
            if x[1] < newtime:
                highscores['highscores'].pop()
                highscores['highscores'].append([lvl,newtime,weapon])
                highscores['highscores'] = sorted(highscores['highscores'], key=lambda kv:(kv[1]),reverse=True)
                break
            #else:
            #    self.highscores.append(highscoreclass(pos,x,BLACK))
            #inta += 1
        create_highscores(self,newtime,lvl)
        self.title = 'Gameover'
        self.buttons = [restart(vec(WIDTH/2,HEIGHT*(7/10))),returntomenu(vec(WIDTH/2,HEIGHT*(8/10)))]
    def draw_buttons(self):
        draw_text_center(self.title,50,RED,WIDTH/2,HEIGHT*(1/10))
        for x in self.buttons:
            x.draw()
        draw_highscores(self)
    def press_buttons(self,mpos):
        for x in self.buttons:
            x.pressed(mpos)

class highscoreclass:
    def __init__(self,pos,info,col):
        self.pos = pos
        self.lvl = str(info[0])
        self.time = info[1]
        self.weapon = str(info[2])
        self.color = col
    def draw(self):
        if self.color == RED:
            draw_text_center("New Highscore",30,self.color,WIDTH/9,self.pos.y)
        draw_text_center(self.lvl,30,self.color,WIDTH/4,self.pos.y)
        time = self.time
        minutes = 0
        if time > 60:
            minutes = int((time - int(time%60)) /60)
            time -= 60 *minutes
        if time < 10 and minutes < 10:
            displaytime = '0{}:0{}'.format(minutes,time)
        elif time < 10:
            displaytime = '{}:0{}'.format(minutes,time)
        elif minutes < 10:
            displaytime = '0{}:{}'.format(minutes,time)
        else:
            displaytime = '{}:{}'.format(minutes,time)
        draw_text_center(displaytime,30,self.color,WIDTH*(2/4),self.pos.y)
        
        draw_text_center(self.weapon,30,self.color,WIDTH*(3/4),self.pos.y)

def create_highscores(target,newtime=0,lvl=0):
    inta = 0
    once = True
    if 'highscores' not in target.__dict__:
        target.highscores = []
    for x in highscores['highscores']:
        pos = vec(WIDTH/2,HEIGHT*((3+inta)/12))
        if x[1] == newtime and x[0] == lvl and once:
            target.highscores.append(highscoreclass(pos,x,RED))
            once = False
        else:
            target.highscores.append(highscoreclass(pos,x,BLACK))
        inta += 1

class returntomenu(defaultbutton):
    def __init__(self,pos):
        self.name = 'Menu'
        self.pos = pos
        super().__init__()
    def pressed(self,mpos):
        global over,P,pm,eneman,menu
        if self.rect.collidepoint((mpos.x,mpos.y)):
            state.current_state = 'menu'
            over = None
            P = None
            pm = None
            eneman = None
            menu = Menu()

#for x in highscores['highscores']:
#    x.append('lightning')

class weaponselectmenu:
    def __init__(self):
        self.title = 'Weapons'
        self.buttons = [returntomenu(vec(WIDTH*(7/10),HEIGHT*(1/20)))]
        amountofweapons = len(state.weaponlist)
        square = 1
        while square**2 < amountofweapons:
            square += 1
        ratio = square * 2
        startx = 1
        curx = startx
        cury = startx
        inta = 0
        for x in state.weaponlist:
            pos = vec(WIDTH*(curx/ratio),HEIGHT*(cury/ratio)+30)
            self.buttons.append(weaponbutton(x,pos))
            curx += 2
            if curx > ratio :
                curx = startx
                cury += 2
        
    def draw_buttons(self):
        draw_text_center(self.title,50,RED,WIDTH*(3/10),HEIGHT*(1/20))
        for x in self.buttons:
            x.draw()
    def press_buttons(self,mpos):
        for x in self.buttons:
            x.pressed(mpos)

class weaponbutton(defaultbutton):
    def __init__(self,name,pos):
        self.name = name
        self.pos = pos
        super().__init__(50)
    def pressed(self,mpos):
        if self.rect.collidepoint((mpos.x,mpos.y)):
            state.current_weapon = self.name

        
        
class state:
    def __init__(self):
        self.current_state = 'menu'
        self.israndom = False
        self.show_hitbox = False
        self.current_weapon = 'Phoenix Gun'
        self.weaponlist = ['Phoenix Gun','Lightning']
        for x in range(0,11):
            self.weaponlist.append('test{}'.format(x))
    def statestop(self):
        if self.current_state == 'gameplay':
            self.gametop()
        if self.current_state == 'menu':
            self.menutop()
        if self.current_state == 'pause':
            self.pausetop()
        if self.current_state == 'gameover':
            self.gameovertop()
    def statesbottom(self):
        if self.current_state == 'gameplay'or self.current_state == 'pause' or self.current_state == 'gameover':
            self.gamebottom()
            if self.current_state == 'pause':
                self.pausebottom()
            if self.current_state == 'gameover':
                self.gameoverbottom()
        if self.current_state == 'menu':
            self.menubottom()
    def gameovertop(self):
        if event.type == pg.MOUSEBUTTONDOWN:
            gameover.press_buttons(vec(pg.mouse.get_pos()))
    def gameoverbottom(self):
        gameover.draw_buttons()
    def pausetop(self):
        if event.type == pg.MOUSEBUTTONDOWN:
            pausemen.press_buttons(vec(pg.mouse.get_pos()))
    def pausebottom(self):
        pausemen.draw_buttons()
    def menutop(self):
        if event.type == pg.MOUSEBUTTONDOWN:
            menu.press_buttons(vec(pg.mouse.get_pos()))
    def menubottom(self):
        menu.draw_buttons()
    def gametop(self):
        global pausemen
        if event.type == pg.MOUSEBUTTONDOWN:
            over.select_skill(vec(pg.mouse.get_pos()))
            P.shoot =True
        if event.type == pg.MOUSEBUTTONUP:
            P.shoot = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.current_state = 'pause'
                over.pause()
                pausemen = pausemenu()
            if event.key == pg.K_w:
                P.up = True
            if event.key == pg.K_s:
                P.down = True
            if event.key == pg.K_d:
                P.right = True
            if event.key == pg.K_a:
                P.left = True
            if event.key == pg.K_0:
                P.range += 5
            if event.key == pg.K_1:
                if self.show_hitbox:
                    self.show_hitbox = False
                else:
                    self.show_hitbox = True
            if event.key == pg.K_2:
                over.create_skills()
            if event.key == pg.K_3:
                P.health_current = 0
            if event.key == pg.K_4:
                if over.invincible:
                    over.invincible =False
                else:
                    over.invincible =True
        if event.type == pg.KEYUP:
            if event.key == pg.K_w:
                P.up = False
            if event.key == pg.K_s:
                P.down = False
            if event.key == pg.K_d:
                P.right = False
            if event.key == pg.K_a:
                P.left = False
    def gamebottom(self):
        global P,pm,eneman,over,gameover
        P.draw()
        pm.draw()
        eneman.draw_enemies()
        over.draw_time()
        over.draw_levelup()
        if not over.pause_time:
            eneman.move(P.update_move())
            pm.move_objects(P.update_move())
            pm.check_exp()
            eneman.pos = vec(pg.mouse.get_pos())
            eneman.enemove(P)
            eneman.checkhit(P)
            eneman.checkobstacles()
            pm.projmove()
            if P.health_current <= 0:
                self.current_state = 'gameover'
                gameover = Gameover()
                P = player(vec(-202,-202),RED,-2)
                over.pausespecial()
                
                
        over.draw_newenemy()
        if not over.specialpause_time:
            over.timers()

skills.test()

skill_dict = skills.get_skills(highscores)[0]
skill = skills.get_skills(highscores)[1]
specific_skill_dict = skills.get_skills(highscores)[2]

treeimage = pg.image.load(os.path.join(filename,'tree0.png'))


state = state()
menu = Menu()

running =True

while running:
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
             
        
        state.statestop()
    #over.pausetime()
    current_time = pg.time.get_ticks()
    
    #pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    state.statesbottom()
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways
pg.quit()
highscores.close()