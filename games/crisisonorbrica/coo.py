import pygame 
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
vec = pygame.math.Vector2

TILESIZE = 30
GRIDWIDTH = 9
GRIDHEIGHT = 9
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

font_name = pygame.font.match_font('hack')
def draw_text_wraped_created(new):
    for text_surface,text_rect in new:
        screen.blit(text_surface, text_rect)
def draw_text(text, size, color, x, y, align="topleft"):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)
def create_draw_text_wraped(text=str, size=int, color=tuple, x=float, y=float, x_bound=int, y_bound=10, draw_rect=False, align="topleft"):
    font = pygame.font.Font(font_name, size)
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

        rect = pygame.Rect(x,y, x_bound, text_rect[3]*box_size-y_bound)
        pygame.draw.rect(screen,BLACK,rect)
    current_text = ''
    space_text = ''
    text_rect_segments = []
    for qq in text:
        space_text += qq
        text_surface = font.render(current_text + space_text, True, color)
        
        text_rect = text_surface.get_rect(**{align: (x, y+5)})
        if text_rect[0]+text_rect[2] > x_bound + x:
            text_surface = font.render(current_text , True, color)
            text_rect = text_surface.get_rect(**{align: (x+10, y+5)})
            text_rect_segments.append((text_surface,text_rect))
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
    text_rect_segments.append((text_surface,text_rect))
    return text_rect_segments
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
def lvl_sort(target):
    return target.lvl

class crisis:
    def __init__(self,name,affects,chance):
        self.crisisname = name
        self.effects = affects
        self.chance = chance
    def draw(self):
        cover = pygame.Surface((WIDTH,HEIGHT))
        cover.fill((128,128,128))
        cover.set_alpha(256-64)
        goal_center = int(WIDTH/2), int(HEIGHT/2)
        screen.blit(cover, cover.get_rect(center=goal_center))
        draw_text(self.crisisname,50,BLACK,WIDTH/2,HEIGHT*(1/6),"center")
        

class energycollapse(crisis):
    def __init__(self):
        super().__init__("Energy Collapse","Energy",1)
    def activate(self,target):
        for x in target.structures:
            if x.name == self.effects:
                removing = x.lvl*2
                x.value -= removing
                x.upgrade(-1,target)
                test = list(target.structures)
                test.remove(x)
                save = x
        test = sorted(test,key=lvl_sort)
        indextest = 0
        affecteddict = {}
        while 0 >= save.value - removing:
            if test[indextest].lvl > 0 and save in target.reqs[test[indextest].name][test[indextest].lvl-1]:
                if test[indextest] in affecteddict:
                    affecteddict[test[indextest]] += 1
                else:
                    affecteddict.update({test[indextest]:1})
                test[indextest].upgrade(-1,target)
                save.value += target.reqs[test[indextest].name][test[indextest].lvl][save]
                
                if test[indextest].name == "People":
                    target.peoplelimit = target.people.lvl *50
            indextest += 1
            if indextest >= len(test):
                indextest = 0
            removing -= 1
        affectedtext = ''
        for count,value in enumerate(affecteddict):
            affectedtext += "{} was affected {} times, ".format(value.name,affecteddict[value])
            if count == len(affecteddict)-1:
                affectedtext = affectedtext[:-2]+'.'
        if affectedtext == '':
            affectedtext = "fortunatley none were affected."
        text = "Major infustructre: energy systems collapse, causes have not been determined, however other infustrucure was affected: " + affectedtext
        self.text = create_draw_text_wraped(text,50,BLACK,WIDTH/2,HEIGHT*(2/6),WIDTH/3,align='center')
    def draw(self):
        super().draw()
        draw_text_wraped_created(self.text)
class falsealarm(crisis):
    def __init__(self):
        super().__init__("False Alarm", "none", 4)
    def activate(self,target):
        text = "A crisis alarm was called fortunately it was a false alarm."
        self.text = create_draw_text_wraped(text,50,BLACK,WIDTH/2,HEIGHT*(2/6),WIDTH/3,align='center')
    def draw(self):
        super().draw()
        draw_text_wraped_created(self.text)
        
        
def orbricacrisislist():
    return [energycollapse(),falsealarm()]

class structure:
    def __init__(self,name,pos):
        self.lvl = random.randint(0,3)
        self.name = name
        self.pos = vec(pos,HEIGHT*(1/6))
        self.size = vec(150,70)
        self.check_rects()
        self.value = 50
    def __repr__(self):
        return self.name
    def check_rects(self):
        ret = []
        for x in range(self.lvl):
            pos = vec(self.pos.x,HEIGHT*((9-x)/12))
            ret.append(pygame.Rect(pos.x-self.size.x/2,pos.y-self.size.y/2,self.size.x,self.size.y))
        
        self.pos = vec(self.pos.x,HEIGHT*((10-self.lvl)/12))
        self.rects = ret,pygame.Rect(self.pos.x-self.size.x/2,self.pos.y-self.size.y/2,self.size.x,self.size.y)
    def pressed(self):
        if self.rects[1].collidepoint(mpos):
            return True
    def upgrade(self,way,over):
        if over.people in over.reqs[self.name][self.lvl] and way > 0:
            over.currentworkingpeople += over.reqs[self.name][self.lvl][over.people]
        self.lvl += way
        if self.lvl < 0:
            self.lvl = 0
        if over.people in over.reqs[self.name][self.lvl] and way < 0:
            over.currentworkingpeople -= over.reqs[self.name][self.lvl][over.people]
        if self.lvl > 5:
            self.lvl = 5
        self.check_rects()
    def draw(self):
        for x in self.rects[0]:
            pygame.draw.rect(screen,GREY,x)
        #pygame.draw.rect(screen,BLACK,self.rect)
        pygame.draw.rect(screen,BLACK,self.rects[1])
        draw_text(self.name+str(self.lvl),30,WHITE,self.pos.x,self.pos.y,"center")
        draw_text(str(self.value),30,RED,self.pos.x,HEIGHT*(11/12),"center")
        if self.lvl != 5:
            inc = 0
            for x in over.reqs[self.name][self.lvl]:
                inc += 1
                if x.name == "People":
                    if over.currentworkingpeople + over.reqs[self.name][self.lvl][x]<over.people.value:
                        draw_text("{} : {}".format(x.name,over.reqs[self.name][self.lvl][x]),30,RED,self.pos.x,self.pos.y-HEIGHT*(inc/12),"center")
                        continue
                elif x.value >= over.reqs[self.name][self.lvl][x]:
                    draw_text("{} : {}".format(x.name,over.reqs[self.name][self.lvl][x]),30,RED,self.pos.x,self.pos.y-HEIGHT*(inc/12),"center")
                    continue
                draw_text("{} : {}".format(x.name,over.reqs[self.name][self.lvl][x]),30,BLACK,self.pos.x,self.pos.y-HEIGHT*(inc/12),"center")
    
    
class manager:
    def __init__(self):
        self.water = structure("Water",WIDTH*(1/6))
        self.food = structure("Food",WIDTH*(2/6))
        self.mining = structure("Mining",WIDTH*(3/6))
        self.people = structure("People",WIDTH*(4/6))
        self.people.value = 200
        self.peoplelimit = self.people.lvl *200
        self.energy = structure("Energy",WIDTH*(5/6))
        self.energy.value = 0
        for x in range(self.energy.lvl):
            self.energy.value += (x+1) *2
        
        self.structures = [self.water,self.food,self.mining,self.people,self.energy]
        self.reqs = {"Water":{0:{self.mining:10,self.people:10},1:{self.mining:50,self.people:50,self.energy:1},2:{self.mining:100,self.people:25,self.energy:1},3:{self.mining:200,self.people:50,self.energy:1},4:{self.mining:200,self.food:100,self.energy:2},5:{self.mining:400,self.people:50,self.energy:2}},
                     "Food":{0:{self.water:5,self.mining:5,self.people:10},1:{self.water:25,self.mining:25,self.people:50,self.energy:1},2:{self.water:50,self.mining:50,self.people:100,self.energy:1},3:{self.water:100,self.mining:50,self.people:100,self.energy:1},4:{self.water:300,self.mining:100,self.people:100,self.energy:2},5:{self.mining:500,self.people:100,self.energy:2}},
                     "Mining":{0:{self.people:10,},1:{self.people:50,self.energy:1},2:{self.water:50,self.mining:50,self.people:75,self.energy:1},3:{self.water:100,self.mining:25,self.people:150,self.energy:1},4:{self.mining:200,self.people:50,self.energy:2},5:{self.mining:350,self.people:75,self.energy:2}},
                     "People":{0:{self.water:10,self.food:10,self.mining:10},1:{self.water:75,self.food:50,self.mining:75,self.energy:1},2:{self.water:150,self.food:100,self.mining:150,self.energy:1},3:{self.water:200,self.food:100,self.mining:200,self.people:50,self.energy:2},4:{self.water:300,self.food:300,self.mining:400,self.people:100,self.energy:2},5:{self.water:500,self.food:500,self.mining:750,self.people:150,self.energy:1}},
                     "Energy":{0:{self.people:10},1:{self.mining:25,self.people:50},2:{self.water:100,self.mining:50,self.people:75},3:{self.food:150,self.mining:75,self.people:100},4:{self.mining:150,self.people:200},5:{self.mining:400,self.people:50}}}
            
        self.currentworkingpeople = 0
        for x in self.structures:
            if x.lvl == 0:
                continue
            print(self.energy.value)
            print('xsname',x.name,x.lvl)
            for y in self.reqs[x.name]:
                
                if self.energy in self.reqs[x.name][y]:
                    self.energy.value -= self.reqs[x.name][y][self.energy]
                    print(x.name,self.energy.value)
                if self.people in self.reqs[x.name][y]:
                    self.currentworkingpeople += self.reqs[x.name][y][self.people]
                print(y,x.lvl)
                if y == x.lvl-1:
                    break
        self.crisischance = 0
        self.crisises = orbricacrisislist()
        self.crisiscurrent = 0
    def draw(self):
        draw_text(str(self.currentworkingpeople),30,BLACK,WIDTH*(4/6),HEIGHT*(17/18),"center")
        for x in self.structures:
            x.draw()
        if self.crisiscurrent:
            self.crisiscurrent.draw()
    def press(self,downgrade=False):
        if self.crisiscurrent:
            self.crisiscurrent = 0
            return
        for x in self.structures:
            if x.pressed() and x.lvl != 5:
                way = -1
                if not downgrade:
                    way = 1
                    test = []
                    if self.people in self.reqs[x.name][x.lvl]:
                        if self.people.value - self.reqs[x.name][x.lvl][self.people] < self.currentworkingpeople:
                            test.append(False)
                    for y in self.reqs[x.name][x.lvl]:
                        if y.value >= self.reqs[x.name][x.lvl][y]:
                            test.append(True)
                            continue
                        test.append(False)
                    if False in test:
                        break
                    for y in self.reqs[x.name][x.lvl]:
                        if y.value >= self.reqs[x.name][x.lvl][y]:
                            if y == self.people:
                                continue
                            
                            y.value -= self.reqs[x.name][x.lvl][y]
                if way == -1:
                    if x.name == "People":
                        self.peoplelimit = self.people.lvl *200 *way
                    if x.name == "Energy":
                        x.value -= (x.lvl)*2
                x.upgrade(way,self)
                if way == 1:
                    if x.name == "People":
                        self.peoplelimit = self.people.lvl *200
                    if x.name == "Energy":
                        x.value += x.lvl*2
                    return
                print('dense')
                for y in self.reqs[x.name][x.lvl]:
                    if y == self.people:
                        continue
                    y.value += self.reqs[x.name][x.lvl][y]
                
    def nextturn(self):
        self.water.value += int(self.water.lvl*100-self.people.value/3)
        self.food.value += int(self.food.lvl*100-self.people.value/3)
        self.mining.value += self.mining.lvl*10
        pibor = int(self.water.value/(self.people.value/10) + self.food.value/(self.people.value/10))

        if self.people.value <= self.peoplelimit and int(self.people.lvl*pibor) >= 0:
            self.people.value += random.randint(int((self.people.lvl*pibor)*0.2),int(self.people.lvl*pibor))
        elif self.people.value <= self.peoplelimit*2 and int(self.people.lvl*pibor) >= 0:
            self.people.value += random.randint(int((self.people.lvl*pibor)*0.2/10),int(self.people.lvl*pibor/10))
        if self.water.value < 0 or self.food.value < 0:
            self.people.value -= random.randint(int(self.people.value/100),int(self.people.value/10))
        self.crisis()
    def crisis(self):
        chance = random.choices([True,False],[self.crisischance,4+self.crisischance/2])[0]
        crisises = self.crisises
        crisiseschance = []
        for x in crisises:
            crisiseschance.append(x.chance)
        self.crisischance +=1 
        if chance:
            randcrisis = random.choices(crisises,crisiseschance)[0]
            randcrisis.activate(self)
            self.crisischance = 0
            self.crisiscurrent = randcrisis
        

over = manager()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit
            if event.key == pygame.K_r:
                over = manager()
            if event.key == pygame.K_n:
                over.nextturn()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = vec(pygame.mouse.get_pos())
            if event.button == 1:
                over.press()    
            if event.button == 3:
                over.press(True)
                
        if event.type == pygame.QUIT: # allows for quit when clicking on the X 
            running = False
            pygame.quit() 
    pygame.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    over.draw()
    # anything down here will be displayed ontop of anything above
    pygame.display.flip() # dose the changes goto doccumentation for other ways