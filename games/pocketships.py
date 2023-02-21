from pickle import TRUE
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
        self.unselect()
        
        self.money = 500
        
        self.timer = 10000
    def unselect(self):
        self.selectedloc = 0
        self.selectingcargo = False
        self.selectingtravel = False
        self.selectedtravel = []
        
        self.selectedship = 0
        self.selectedcargo = []
        self.menu = 0
        self.buttons = []
        self.locmenu = 0
        self.cost = 0
        self.unlocking = 0
    def draw_locations(self):
        for x in self.locations:
            pos = x.pos
            if x.unlocked:
                pygame.draw.circle(screen,WHITE,pos,5)
                draw_text(x.name,25,WHITE,x.pos.x+5,x.pos.y)
            else:
                pygame.draw.circle(screen,GREY,pos,5)
                draw_text(x.name,25,GREY,x.pos.x+5,x.pos.y)
        for x in self.ships:
            pos = x.pos
            pygame.draw.circle(screen,BLUE,pos,5)
    def move(self):
        if self.mpos_ori and (not self.selectedloc or self.selectingtravel):
            cur = vec(pygame.mouse.get_pos())
            direction = cur - self.mpos_ori
            for x in self.locations:
                x.pos += direction
            for x in self.ships:
                x.pos += direction
            self.mpos_ori = cur
        for x in self.ships:
            if x.traveling:
                x.move()
    def create_location(self,specloc=0,specname=0,unlock=False):
        if len(self.locations) <= 1:
            unlock = True 
        ll = location(specloc,specname,unlock,self)
        self.locations.append(ll)
    def selectlocation(self):
        for x in self.locations:
            cur = math.sqrt((self.mpos_ori.x-x.pos.x)**2+(self.mpos_ori.y-x.pos.y)**2)
            if cur < 5:
                if not self.selectedloc:
                    if x.unlocked:
                        self.selectedloc = x
                        self.menu = 0
                        self.locmenu = 'cargo'
                        self.buttons.append(nextpagebutton(vec(145,455)))
                        self.buttons.append(backpagebutton(vec(255,455)))
                        self.buttons.append(hangerpagebutton(vec(35,455)))
                    else:
                        self.unlocking = x
                        self.buttons.append(unlockbutton(vec(200,455)))
                if self.selectingtravel:
                    if self.selectedtravel[-1] == x:
                        if len(self.selectedtravel) > 1:
                            dis = math.sqrt((self.selectedtravel[-2].pos.x-self.selectedtravel[-1].pos.x)**2+(self.selectedtravel[-2].pos.y-self.selectedtravel[-1].pos.y)**2)
                            self.cost -= round(dis / self.selectedship.engine)
                            self.selectedtravel.remove(x)
                    else:
                        print(x.pos)
                        dis = math.sqrt((x.pos.x-self.selectedtravel[-1].pos.x)**2+(x.pos.y-self.selectedtravel[-1].pos.y)**2)
                        print(dis)
                        self.cost += round(dis / self.selectedship.engine)
                        self.selectedtravel.append(x)


                
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
            self.create_location(cur,unlock=False)
    def draw_distance(self):
        if self.selectingtravel and len(self.selectedtravel)>=1:
            pos = 0
            for x in self.selectedtravel:
                if pos != 0:
                    pygame.draw.line(screen,YELLOW,x.pos,self.selectedtravel[pos-1].pos)
                pos+=1
    def draw_monies(self):
        if self.selectingtravel:
            draw_text('{}-{}'.format(self.money,self.cost),30,WHITE,5,5)
        else:
            draw_text(str(self.money),30,WHITE,5,5)
            draw_text(str(self.timer),30,WHITE,50,5)
    def draw_travels(self):
        for x in self.ships:
            if x.traveling:
                pos = 0
                for yy in x.flightplan:
                    if pos != 0:
                        pygame.draw.line(screen,YELLOW,yy.pos,x.flightplan[pos-1].pos)
                    pos+=1
    def draw_loc(self):
        if self.unlocking:
            pygame.draw.rect(screen,BLUE,(50,50,400,400))
            draw_text(str(self.unlocking),30,WHITE,int(WIDTH/10),int(HEIGHT*(1/20)))
            draw_text("unlock {} for {}".format(self.unlocking.name,self.unlocking.cost),50,WHITE,250,250,"center")
        if self.selectedloc and not self.selectingtravel:
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
    def update(self):
        self.timer -= 1
        if self.timer < 0:
            self.update_inventories()
            self.timer = 10000
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
                    try:
                        self.selectedship = self.selectedloc.hanger[x+20*self.menu]
                        self.buttons.append(selectshipbutton(vec(365,455)))
                    except:
                        pass
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
        
        self.inventory = []
        self.flightplan = []
        self.traveling = False
        
        self.distance_need = 0
        self.distance = 0
        self.current_destination = 0
        
        self.engine = 1
    def add_self(self):
        self.destination_current = self.destination_target
        self.destination_target = 0
        self.destination_current.hanger.append(self)
    def check_deliver(self):
        print(self.inventory)
        remove = []
        for x in self.inventory:
            print(x.destination,self.destination_target)
            if x.destination == self.destination_target:
                remove.append(x)
                self.space_current -= x.space
                curmap.money += x.value
        for x in remove:
            self.inventory.remove(x)
        print(self.inventory)
    def update_movement(self):
        print(self.destination_current)
        self.destination_current.hanger.remove(self)
        self.check_deliver()
        
        self.destination_current = self.flightplan[self.current_destination-1]
        self.destination_target = self.flightplan[self.current_destination]
        self.distance_need = math.sqrt((self.destination_current.pos.x-self.destination_target.pos.x)**2+(self.destination_current.pos.y-self.destination_target.pos.y)**2)
        self.distance = 0
        cur = self.destination_current
        tar = self.destination_target
        if (cur.pos.y-tar.pos.y) != 0:
            self.ang = math.atan((cur.pos.x-tar.pos.x)/(cur.pos.y-tar.pos.y))
            ver = math.cos(self.ang)
            hor = math.sin(self.ang)
        else:
            self.ang = 0
            ver = 0
            if (cur.pos.x-tar.pos.x)<0:
                hor = -1
                self.degrees = -90
            else:
                hor = 1
        self.ver = ver
        self.hor = hor
                
    def move(self):
        if self.distance >= self.distance_need:
            self.current_destination += 1
            print(self.flightplan,self.current_destination)
            if self.current_destination >= len(self.flightplan):
                self.check_deliver()
                self.traveling = False
                self.flightplan = []
                self.current_destination = 0
                self.pos = vec(self.destination_target.pos)
                print(self.inventory)
                self.destination_target.inventory += self.inventory
                self.add_self()
            else:
                self.update_movement()
        else:
            self.distance += self.c
            
            if (self.destination_current.pos.y-self.destination_target.pos.y) < 0:
                self.pos += vec(self.hor,self.ver) *1* self.c
            else:
                self.pos += vec(self.hor,self.ver)*-1* self.c

class location:
    def __init__(self,pos,text,unlocked,curmap):
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
        self.cost = random.randint(100,(200+100*len(curmap.locations)))
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
            elif x.origin != curmap.selectedloc:
                draw_text(str(x.name),15,RED,pos.x,pos.y)
                draw_text(str(x.value),15,RED,pos.x+125,pos.y)
                draw_text(str(x.space),15,RED,pos.x+175,pos.y)
                draw_text(str(x.destination),15,RED,pos.x+225,pos.y)
                draw_text(str(x.distance),15,RED,pos.x+275,pos.y)
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
        print(curmap.locations)
        print(temp)
        tempdel = []
        for x in temp:
            if not x.unlocked:
                print(x)
                tempdel.append(x)
        for x in tempdel:
            temp.remove(x)
        self.destination = random.choice(temp)
        self.distance = math.sqrt((origin.pos.x-self.destination.pos.x)**2+(origin.pos.y-self.destination.pos.y)**2)
        self.origin = origin
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
            curmap.selectingcargo = False
            curmap.selectedship = 0
            for x in curmap.selectedcargo:
                print(x.space)
                curmap.selectedship.space_current -= x.space
            curmap.selectedcargo = []
            for x in curmap.buttons:
                if x.name == 'Plan Trip':
                    curmap.buttons.remove(x)
                    break
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
            curmap.buttons.append(planbutton(self.pos))
            for x in curmap.buttons:
                if x.name == 'Cargo':
                    x.name = 'Hanger'
                    curmap.buttons.remove(self)
                    break
        
class planbutton(defaultlocbutton):
    def __init__(self,pos):
        self.name = 'Plan Trip'
        self.pos = pos
        super().__init__()        
    def pressed(self):
        if super().pressed():
            curmap.selectingtravel = True
            curmap.buttons = []
            curmap.selectingcargo = False
            curmap.buttons.append(embarkbutton(self.pos))
            curmap.buttons.append(backbutton(vec(35,455)))
            curmap.selectedtravel.append(curmap.selectedloc)

class embarkbutton(defaultlocbutton):
    def __init__(self,pos):
        self.name = 'Embark'
        self.pos = pos
        super().__init__()
    def pressed(self):
        if super().pressed():
            curmap.selectedship.inventory = curmap.selectedcargo
            curmap.selectedship.flightplan = curmap.selectedtravel
            curmap.selectedship.traveling = True
            curmap.money -= curmap.cost
            curmap.cost = 0
            curmap.unselect()

class backbutton(defaultlocbutton):
    def __init__(self,pos):
        self.name = 'Back'
        self.pos = pos
        super().__init__()
    def pressed(self):
        if super().pressed():
            curmap.selectingtravel = False
            curmap.selectingcargo = True
            curmap.buttons = []
            curmap.buttons.append(nextpagebutton(vec(145,455)))
            curmap.buttons.append(backpagebutton(vec(255,455)))
            curmap.buttons.append(hangerpagebutton(vec(35,455)))
            curmap.buttons.append(planbutton(vec(365,455)))

class unlockbutton(defaultlocbutton):
    def __init__(self,pos):
        self.name = "Unlock"
        self.pos = pos
        super().__init__()
    def pressed(self):
        if super().pressed():
            curmap.unlocking.unlocked = True
            curmap.buttons = []
            curmap.money -= curmap.unlocking.cost
            curmap.unlock_locations(curmap.unlocking)
            curmap.unlocking = 0
            
            

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
                if curmap.selectedcargo:
                    for x in curmap.selectedcargo:
                        curmap.selectedship.space_current -= x.space
                curmap.unselect()
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
    curmap.draw_travels()
    curmap.draw_loc()
    curmap.draw_buttons()
    curmap.draw_monies()
    curmap.update()
    # anything down here will be displayed ontop of anything above
    pygame.display.flip() # dose the changes goto doccumentation for other ways