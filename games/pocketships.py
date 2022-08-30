from select import select
from turtle import pos
from unicodedata import name
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
WIDTH = 500
HEIGHT = 500
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
def draw_text(text, size, color, x, y, align="topleft"):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class cmap:
    def __init__(self):
        self.locations = []
        self.ships = []
        self.create_location((250,250),'Rav',True)
        self.unlock_locations(self.locations[0])
        self.update_inventories()
        self.create_ship(self.locations[0],'DS Glass')
        self.create_ship(self.locations[0],'HS Surri')
        #for x in range(0,20):
        #    self.create_ship(self.locations[0])
        self.mpos_ori = 0
        self.selectedloc = 0
        self.selectedship = 0
        self.selectingcargo = False
        self.selectedcargo = []
        self.second = 0
        self.menu = 0
        self.buttons = []
        self.locmenu = 0
    def draw_locations(self):
        for x in self.locations:
            pos = x.pos
            pygame.draw.circle(screen,WHITE,pos,5)
            draw_text(x.name,25,WHITE,x.pos.x+5,x.pos.y)
        for x in self.ships:
            pos = x.pos
            pygame.draw.circle(screen,BLUE,pos,5)
    def move(self):
        if self.mpos_ori and not self.selectedloc:
            cur = vec(pygame.mouse.get_pos())
            direction = cur - self.mpos_ori
            for x in self.locations:
                x.pos += direction
            for x in self.ships:
                x.pos += direction
            self.mpos_ori = cur
    def create_location(self,specloc=0,specname=0,lock=False):
        ll = location(specloc,specname,lock)
        self.locations.append(ll)
    def selectlocation(self):
        for x in self.locations:
            cur = math.sqrt((self.mpos_ori.x-x.pos.x)**2+(self.mpos_ori.y-x.pos.y)**2)
            if cur < 5:
                self.selectedloc = x
                self.menu = 0
                self.locmenu = 'cargo'
                self.buttons.append(nextpagebutton(vec(145,455)))
                self.buttons.append(backpagebutton(vec(255,455)))
                self.buttons.append(hangerpagebutton(vec(35,455)))
                
    def unlock_locations(self,target):
        amo = random.randint(1,3)
        limit = 200
        cant = 50
        for ll in range(0,amo):
            allg = True
            while allg:
                x = random.randint(-limit,limit)
                y = random.randint(-limit,limit)
                cur = target.pos + vec(x,y)
                
                check = math.sqrt((cur.x-target.pos.x)**2+(cur.y-target.pos.y)**2)
                while check < cant:
                    x = random.randint(-limit,limit)
                    y = random.randint(-limit,limit)
                    cur = target.pos + vec(x,y)
                    check = math.sqrt((cur.x-target.pos.x)**2+(cur.y-target.pos.y)**2)
                
                once = True
                for yy in self.locations:
                    check = math.sqrt((cur.x-yy.pos.x)**2+(cur.y-yy.pos.y)**2)
                    if check < cant:
                        once = False
                if once:
                    allg = False
            self.create_location(cur)
    def draw_distance(self):
        if self.selectedloc and self.second:
            fir = self.selectedloc.pos
            sec = self.second.pos
            pygame.draw.line(screen,WHITE,fir,sec,width=2)
            dis = math.sqrt((fir.x-sec.x)**2+(fir.y-sec.y)**2)
            mid = vec((fir.x+sec.x)/2,(fir.y+sec.y)/2)
            draw_text(str(dis),30,WHITE,mid.x+15,mid.y)
    def draw_loc(self):
        if self.selectedloc:
            pygame.draw.rect(screen,BLUE,(50,50,400,400))
            draw_text(str(self.selectedloc),30,WHITE,int(WIDTH/10),int(HEIGHT*(1/20)))
            if self.locmenu == 'cargo':
                draw_text(str('{}/{}'.format(len(self.selectedloc.inventory),self.selectedloc.limit)),30,WHITE,int(WIDTH/4),int(HEIGHT*(1/20)))
                draw_text('Name',20,WHITE,55,55)
                draw_text('Price',20,WHITE,175,55)
                draw_text('Space',20,WHITE,225,55)
                draw_text('Destination',20,WHITE,275,55)
                self.selectedloc.draw_inventroy(self.menu)
                if self.selectedship:
                    draw_text(str('{}/{}'.format(self.selectedship.space_current,self.selectedship.space)),30,WHITE,int(WIDTH/2),int(HEIGHT*(1/20)))
            if self.locmenu == 'hanger':
                draw_text(str('{}'.format(len(self.selectedloc.hanger))),30,WHITE,int(WIDTH/4),int(HEIGHT*(1/20)))
                draw_text('Name',20,WHITE,55,55)
                draw_text('Speed',20,WHITE,175,55)
                draw_text('Space',20,WHITE,225,55)
                self.selectedloc.draw_hanger(self.menu)
    def update_inventories(self,spec=0):
        
        if spec:
            amo = random.randint(1,spec.limit)
            for x in range(amo):
                name = random.choice(cargonames)
                spec.inventory.append(cargo(name,spec,self))
            spec.inventory = sorted(spec.inventory, key=distance_sort,reverse=True)
        else:
            for yy in self.locations:
                amo = random.randint(1,yy.limit)
                for x in range(amo):
                    name = random.choice(cargonames)
                    yy.inventory.append(cargo(name,yy,self))
                yy.inventory = sorted(yy.inventory, key=distance_sort,reverse=True)
    def create_ship(self,where,name=0):
        ll = ship(where,name)
        self.ships.append(ll)
    def draw_buttons(self):
        for x in self.buttons:
            x.draw()
    def press_buttons(self):
        for x in self.buttons:
            x.pressed()
    def press_menu(self):
        if self.locmenu == 'hanger':
            for x in range(0,20):
                pos = vec(55,50+19*(x+1))
                rect = pygame.Rect(pos.x,pos.y,400,19)
                if rect.collidepoint(mpos.x,mpos.y):
                    self.selectedship = self.selectedloc.hanger[x+20*self.menu]
                    self.buttons.append(selectshipbutton(vec(365,455)))
                    break
        if self.selectingcargo:
            for x in range(0,20):
                pos = vec(55,50+19*(x+1))
                rect = pygame.Rect(pos.x,pos.y,400,19)
                if rect.collidepoint(mpos.x,mpos.y):
                    if self.selectedloc.inventory[x+20*self.menu] in self.selectedcargo:
                        self.selectedcargo.remove(self.selectedloc.inventory[x+20*self.menu])
                        self.selectedship.space_current -= self.selectedloc.inventory[x+20*self.menu].space
                    else:
                        if self.selectedloc.inventory[x+20*self.menu].space+self.selectedship.space_current <=self.selectedship.space:
                            self.selectedcargo.append(self.selectedloc.inventory[x+20*self.menu])
                            self.selectedship.space_current += self.selectedloc.inventory[x+20*self.menu].space
                    break
                
def distance_sort(target):
    return target.distance

shipidentifier = ['DS','DGS','HS','RS','RSNS','RTS','HSS','EHAS']
shiptanslate = {'DS':"Devines' Ship","DGS":"Devines' Gaurd Ship","HS":"Heavy Supplier","RS":"Rica Ship","RCNS":"Rican Supply Network Ship","RTS":"Royal Tulem Ship","HSS":"Hunter Supply Ship","EHAS":"Everdines' High Astro Service"}
            
class ship:
    def __init__(self,loc,name):
        if not name:
            name = '{} '.format(random.choice(shipidentifier))
            for x in range(random.randint(3,10)):
                name += random.choices(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'],[1,6,57,37,35,9,19,38,37,16,43,29,17,9,13,15,1,6,28,1,1,23,5,11,34,15])[0]
        
        self.name = name
        
        self.destination_current = 0
        self.destination_target = loc
        self.pos = vec(self.destination_target.pos)
        self.add_self()
        
        self.c = random.randint(1,3)
        self.space = 50
        self.space_current = 0
    def add_self(self):
        self.destination_current = self.destination_target
        self.destination_target = 0
        self.destination_current.hanger.append(self)

class location:
    def __init__(self,pos,text,unlocked=False):
        if not text:
            text = ''
            for x in range(random.randint(1,6)):
                text += random.choices(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'],[1,6,57,37,35,9,19,38,37,16,43,29,17,9,13,15,1,6,28,1,1,23,5,11,34,15])[0]
        
        self.name = text
        self.pos = vec(pos)
        self.unlocked = unlocked
        self.inventory = []
        self.hanger = []
        self.limit = 40
    def draw_inventroy(self,menu):
        added = 1
        for x in self.inventory[0+20*menu:20+20*menu]:
            pos = vec(55,55+19*added)
            if x in curmap.selectedcargo:
                draw_text(str(x.name),15,BLACK,pos.x,pos.y)
                draw_text(str(x.value),15,BLACK,pos.x+125,pos.y)
                draw_text(str(x.space),15,BLACK,pos.x+175,pos.y)
                draw_text(str(x.destination),15,BLACK,pos.x+225,pos.y)
                draw_text(str(x.distance),15,BLACK,pos.x+275,pos.y)
            else:
                draw_text(str(x.name),15,WHITE,pos.x,pos.y)
                draw_text(str(x.value),15,WHITE,pos.x+125,pos.y)
                draw_text(str(x.space),15,WHITE,pos.x+175,pos.y)
                draw_text(str(x.destination),15,WHITE,pos.x+225,pos.y)
                draw_text(str(x.distance),15,WHITE,pos.x+275,pos.y)
            added +=1
    def draw_hanger(self,menu):
        added = 1
        for x in self.hanger[0+20*menu:20+20*menu]:
            pos = vec(55,55+19*added)
            if x == curmap.selectedship:
                draw_text(str(x.name),15,BLACK,pos.x,pos.y)
                draw_text(str(x.c),15,BLACK,pos.x+125,pos.y)
                draw_text(str(x.space),15,BLACK,pos.x+175,pos.y)
            else:
                draw_text(str(x.name),15,WHITE,pos.x,pos.y)
                draw_text(str(x.c),15,WHITE,pos.x+125,pos.y)
                draw_text(str(x.space),15,WHITE,pos.x+175,pos.y)
            added +=1
    def __repr__(self):
        return "{}".format(self.name)


class cargo:
    def __init__(self,name,origin,curmap):
        self.name = name
        temp = list(curmap.locations)
        temp.remove(origin)
        self.destination = random.choice(temp)
        self.distance = math.sqrt((origin.pos.x-self.destination.pos.x)**2+(origin.pos.y-self.destination.pos.y)**2)
        self.value = random.randint(50,100)
        self.space = random.randint(1,10)
    def update_rect(self,pos):
        self.rect = pygame.Rect(pos.x,pos.y,200,50)
    

class defaultlocbutton:
    def __init__(self):
        self.rect = pygame.Rect(self.pos.x,self.pos.y,100,25)
    def draw(self):
        pygame.draw.rect(screen,WHITE,self.rect)
        draw_text(self.name,30,BLACK,self.pos.x+2.5,self.pos.y,)
    def pressed(self):
        if self.rect.collidepoint((mpos.x,mpos.y)):
            return True
    def __repr__(self):
        return self.name

class nextpagebutton(defaultlocbutton):
    def __init__(self,pos):
        self.name = 'Next Page'
        self.pos = pos
        super().__init__()
    def pressed(self):
        if super().pressed():
            curmap.menu += 1
            
class backpagebutton(defaultlocbutton):
    def __init__(self,pos):
        self.name = 'Back Page'
        self.pos = pos
        super().__init__()
    def pressed(self):
        if self.rect.collidepoint((mpos.x,mpos.y)):
            curmap.menu -=1
            

class hangerpagebutton(defaultlocbutton):
    def __init__(self,pos):
        self.name = 'Hanger'
        self.pos = pos
        super().__init__()
    def pressed(self):
        if super().pressed():
            curmap.menu = 0
            if self.name == 'Hanger':
                self.name = 'Cargo'
            else:
                self.name = 'Hanger'
            if curmap.locmenu == 'hanger':
                curmap.locmenu = 'cargo'
            else:
                curmap.locmenu = 'hanger'

class selectshipbutton(defaultlocbutton):
    def __init__(self,pos):
        self.name = 'Select'
        self.pos = pos
        super().__init__()
    def pressed(self):
        if super().pressed():
            curmap.locmenu = 'cargo'
            curmap.selectingcargo = True
            for x in curmap.buttons:
                if x.name == 'Cargo':
                    x.name = 'Hanger'
                    curmap.buttons.remove(self)
                    curmap.buttons.append(embarkbutton(self.pos))
                    break
        
class embarkbutton(defaultlocbutton):
    def __init__(self,pos):
        self.name = 'Embark'
        self.pos = pos
        super().__init__()        

cargonames = []

def add_cargo(name):
    cargonames.append(name)

add_cargo('Solar Panels')
add_cargo('Engine Scrap')
add_cargo('Weapon Components')

curmap = cmap()

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
                curmap = cmap()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos =vec(pygame.mouse.get_pos())
            if event.button == 1:
                curmap.mpos_ori = vec(pygame.mouse.get_pos())
                curmap.selectlocation()
                curmap.press_buttons()
                curmap.press_menu()
            if event.button == 3:
                curmap.selectedloc = 0
                curmap.buttons = []
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                curmap.mpos_ori = 0
                
        if event.type == pygame.QUIT: # allows for quit when clicking on the X 
            running = False
            pygame.quit() 
            running = False
    pygame.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(BLACK) # fills screnn with color
    curmap.draw_locations()
    curmap.move()
    curmap.draw_distance()
    curmap.draw_loc()
    curmap.draw_buttons()
    # anything down here will be displayed ontop of anything above
    pygame.display.flip() # dose the changes goto doccumentation for other ways