import pygame as pg
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
vec = pg.math.Vector2


# continue with interacting with combat
# switch movemnt in to game
# lock movemnt on attack select
# create system for actions with restructure of grid system
# change update cells 

pg.init()
infoobject = pg.display.Info()

WIDTH = infoobject.current_w
HEIGHT = infoobject.current_h

screen = pg.display.set_mode((WIDTH, HEIGHT),display=0)


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

def draw_text_center(text=str, size=int, color=tuple, x=int, y=int):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x,y))
    screen.blit(text_surface, text_rect)




clock = pg.time.Clock()

check_cell_connections = ((0,-1),(1,0),(0,1),(-1,0))
check_tile_connections = ((0,-0.5),(0.5,0),(0,0.5),(-0.5,0))

filename = os.path.dirname(sys.argv[0])
gridinfo = shelve.open(filename+'/gridinfo.txt',writeback=True)


cell_size = 50

rundefaultgridgen = False

def check_gridinfo():
    if "0" not in gridinfo:
        rundefaultgridgen = True

class defaultbutton:
    def __init__(self,name,pos,sizex = 300,sizey= 50):
        self.name = name
        self.pos = pos
        self.rect = pg.Rect((self.pos.x-sizex/2), (self.pos.y-sizey/2), sizex, sizey)
    def draw(self):
        pg.draw.rect(screen,BLACK,self.rect)
        draw_text_center(self.name,40,WHITE,self.pos.x,self.pos.y)
        

class attack(defaultbutton):
    def pressed(self,mpos):
        Gm.addtoconsole(self.name)


class defcha:
    def __init__(self,pos,centering):
        self.pos = pos
        self.testsize = cell_size - 6
        self.centering = centering
        self.health = 10
    def draw(self):
        self.draw_test()
    def draw_test(self):
        xcenter,ycenter = self.centering.x,self.centering.y
        rect = pg.Surface((int(self.testsize), int(self.testsize)))
        rect.fill(RED)
        x = (self.pos.x*cell_size+xcenter+cell_size/2) - self.testsize/2
        y = (self.pos.y*cell_size+ycenter+cell_size/2) - self.testsize/2
        screen.blit(rect,(int(x),int(y))) 

class defpla(defcha):    
    def __init__(self, pos, centering):
        super().__init__(pos, centering)    
        self.create_buttons()
    
    def draw(self):
        self.draw_buttons()
        super().draw()

    def create_buttons(self):
        self.buttons = [attack("punch",vec(WIDTH/2,HEIGHT*(4/6))),attack("blunch",vec(WIDTH/2,HEIGHT*(5/6)))]
    
    def draw_buttons(self,spec=5):
        for x in self.buttons:
            x.draw()
    def press_buttons(self,selected):
        for x in self.buttons:
            if x.rect.collidepoint((mpos.x,mpos.y)):
                if x == selected:    
                    x.pressed(mpos)
                else:
                    return x
            return 0

class defene(defcha):
    def __init__(self, pos, centering):
        super().__init__(pos, centering)



class tile():
    def __init__(self,grid_x,grid_y,pos_x,pos_y,elev=0):
        self.x = grid_x
        self.y = grid_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.connections = []
        self.occupying = 0
        self.elevation = elev

class wall():
    def __init__(self,grid_x,grid_y,pos_x,pos_y,ori) -> None:
        self.x = grid_x
        self.y = grid_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.ori = ori
        self.passable = True
    def draw(self):
        if not self.passable:
            pg.draw.circle(screen,GREEN,(self.pos_x,self.pos_y),5)
            return
        pg.draw.circle(screen,RED,(self.pos_x,self.pos_y),5)
    def __str__(self):
        return f"grid = {self.x,self.y}, ori = {self.ori}, pass = {self.passable}"

def vectotup(vect):
    return vect.x,vect.y

class grid:
    def __init__(self,cell_size,sizex,sizey,posx,posy,center='true'):
        self.cell_size = cell_size 
        self.cell_amo_x = sizex
        self.cell_amo_y = sizey
        self.update_grid()
        self.grid_pos_x = posx
        if center == 'true':
            self.grid_pos_x -= self.grid_size_x/2
        self.grid_pos_y = posy
    def update_grid(self):

        self.grid_size_x = self.cell_size * self.cell_amo_x
        self.grid_size_x = round(self.grid_size_x/self.cell_size) * self.cell_size

        self.grid_size_y = self.cell_size * self.cell_amo_y
        self.grid_size_y = round(self.grid_size_y/self.cell_size) * self.cell_size

    def update_cells(self):
        self.cells = {}

        for x in range(0,self.cell_amo_x):
            rawx = x
            x = x*self.cell_size+self.grid_pos_x + self.cell_size/2
            for y in range(0,self.cell_amo_y):
                rawy = y
                y = y*self.cell_size+self.grid_pos_y + self.cell_size/2
                self.cells.update({(rawx,rawy):tile(rawx,rawy,x,y)})

    def draw_grid(self):
        #vertical lines
        for x in range(int(self.grid_pos_x), int(self.grid_pos_x+self.grid_size_x+1), self.cell_size):
            pg.draw.line(screen, BLACK, (x, int(self.grid_pos_y)), (x, int(self.grid_pos_y+self.grid_size_y-1)))
        #horizontal lines
        for y in range(int(self.grid_pos_y), int(self.grid_pos_y+self.grid_size_y+1), self.cell_size):
            pg.draw.line(screen, BLACK, (int(self.grid_pos_x), y), (int(self.grid_pos_x+self.grid_size_x-1), y))

class board(grid):
    def __init__(self) -> None:
        posx = WIDTH/2
        posy = 50
        grid.__init__(self,cell_size,20,8,posx,posy)
        self.close = False  

        self.update_cells()
        
        self.init_walls()

        self.centering = vec(self.grid_pos_x,self.grid_pos_y)

        self.selectedchar = 0
    def translate_gridtopos(self):
        pass
    def init_walls(self):
        
        self.walls = {}
        for pos in self.cells:
            temp_connections = {}
            cell = self.cells[pos]

            for x in check_cell_connections:
                cellcon = (pos[0]+x[0],pos[1]+x[1])
                if cellcon in self.cells:

                    wallpos = (pos[0]+x[0]/2,pos[1]+x[1]/2)

                    wallx = wallpos[0]
                    wallx += 0.5
                    wallxpos = wallx*self.cell_size+self.grid_pos_x

                    wally = wallpos[1]
                    wally += 0.5
                    wallypos = wally*self.cell_size+self.grid_pos_y

                    ori = "vertical"
                    if wallx % 1 == 0.5:
                        ori = "horizontal"

                    if (wallx,wally) not in self.walls:
                        wallactual = wall(wallx,wally,wallxpos,wallypos,ori)
                        self.walls.update({(wallx,wally):wallactual})
                        temp_connections.update({cellcon:wallactual})
                    else:
                        wallactual = self.walls[(wallx,wally)]
                        temp_connections.update({cellcon:wallactual})
            cell.connections = temp_connections

        #draw wall
        
        #for pos in self.cells:
        #    connections = self.cells[pos].connections
        #    for othercell in connections:
        #        wallactual = connections[othercell]
        #        self.walls.update({(wallactual.x,wallactual.y):wallactual})



    def old_init_walls(self):
        self.walls = {}
        
        for x in range(0,self.cell_amo_x):
            rawwallx = x + 0.5
            x+=1
            wallx = x*self.cell_size+self.grid_pos_x
            for y in range(0,self.cell_amo_y):
                rawwally = y 
                y +=0.5
                wally = y*self.cell_size+self.grid_pos_y 
                self.walls.update({(rawwallx,rawwally):wall(rawwallx,rawwally,wallx,wally,"vertical")})  
        for x in range(0,self.cell_amo_x):
            rawwallx = x 
            x +=0.5
            wallx = x*self.cell_size+self.grid_pos_x
            for y in range(0,self.cell_amo_y):
                rawwally = y + 0.5
                y+=1
                wally = y*self.cell_size+self.grid_pos_y 
                self.walls.update({(rawwallx,rawwally):wall(rawwallx,rawwally,wallx,wally,"horizontal")})
        
        for pos in self.cells:
            temp_connections = {}
            cell = self.cells[pos]
            for x in check_tile_connections:
                x = (pos[0]+x[0],pos[1]+x[1])
                if x in self.walls:
                    temp_connections.update({x:self.walls[x]})
            cell.connections = temp_connections

    def checkcon(self,tartile):
        cons = []
        for x in check_tile_connections:
            targetwall = tartile[0] + x[0] , tartile[1] + x[1]
            if targetwall in self.pot_wall_pos:
                cons.append((targetwall))
        return cons
    
    def draw(self):
        grid.draw_grid(self)
        self.shows_places()
        self.show_connections()

    def shows_places(self): 
        for x in self.cells:
            cell = self.cells[x]
            pg.draw.circle(screen,BLACK,(cell.pos_x,cell.pos_y),5)
        for x in self.walls:
            wall = self.walls[x]
            wall.draw()
    
    def save_grid_info(self):
        gridinfo_temp = {}
        for x in self.walls:
            wallclass = self.walls[x]
            #gridinfo["grid"].update({x:(wallclass.x,wallclass.y,wallclass.ori,wallclass.passable)})

    def find_closest(self):
        m = mpos
        m = (m[0]),(m[1])

        target = 0
        shortest = float("inf")
        for x in self.cells:
            x = self.cells[x]
            length = math.sqrt((m[0] - x.pos_x) ** 2 + (m[1] - x.pos_y) ** 2)
            if length < shortest:
                shortest = length
                target = x
        self.close = target
        for y in self.close.connections:
            y = self.close.connections[y]
    def show_connections(self):
        if self.close:
            m = mpos
            pg.draw.circle(screen,GREEN,(m[0],m[1]),5)
            for y in self.close.connections:
                y = self.close.connections[y]
                pg.draw.line(screen,RED, (self.close.pos_x,self.close.pos_y), (y.pos_x,y.pos_y))

    def make_wall(self,dir):
        dir = vec(dir)
        if self.close:
            dir += vec(self.close.x,self.close.y)
            vecdir = vectotup(dir)
            if vecdir in self.close.connections:
                Gm.addtoconsole(f"wallbefore, {self.close.connections[vecdir]}")
                self.close.connections[vecdir].passable = False
                Gm.addtoconsole(f"wallafter, {self.close.connections[vecdir]}")
            self.close = False

    def update_cell_occupy(self,cell,target):
        for x in self.cells:
            tile = self.cells[x]
            if tile.occupying == target:
                tile.occupying = 0
        self.cells[vectotup(cell)].occupying = target
    def movechar(self,dir):
        dir = vec(dir)
        pos = self.selectedchar.pos
        dir += pos
        if vectotup(dir) in self.cells[vectotup(pos)].connections:
            Gm.addtoconsole(self.cells[vectotup(pos)].connections[vectotup(dir)])
            if self.cells[vectotup(dir)].occupying == 0 and self.cells[vectotup(pos)].connections[vectotup(dir)].passable == True:
                self.selectedchar.pos = dir
                self.update_cell_occupy(dir,self.selectedchar)

class game:
    def __init__(self):
        self.G = board()
        G = self.G

        self.consoletext = []

        self.playerCha = {}
        self.addtogrid_player(vec(0,0),defpla(vec(0,0),G.centering))
        
        for x in G.cells:
            tile = G.cells[x]
            if tile.occupying != 0:
                self.selectedchar = tile.occupying
                G.selectedchar = tile.occupying
                break
        self.selectedattack = 0
        self.enemyCha = {}
        self.addtogrid_enemy(vec(2,2),defene(vec(2,2),G.centering))
    def addtogrid_player(self,pos,ent):
        self.addtogrid(pos,ent)
        self.playerCha.update({ent:pos})
    
    def addtogrid_enemy(self,pos,ent):
        self.addtogrid(pos,ent)
        self.enemyCha.update({ent:pos})

    def addtogrid(self,pos,ent):
        G = self.G
        G.update_cell_occupy(pos,ent)

    def movechar(self,dir):
        self.addtoconsole(f"selectedatack, {self.selectedattack}")
        if self.selectedattack == 0:
            self.G.movechar(dir)


    def buttonpress(self):
        if self.selectedchar:
            self.selectedattack = self.selectedchar.press_buttons(self.selectedattack)
            

    def draw(self):
        self.draw_charaters()
        self.draw_console()

    def draw_charaters(self):
        for ent in self.playerCha:
            ent.draw()
        for ent in self.enemyCha:
            ent.draw()
    
    def addtoconsole(self,text):
        self.consoletext.append(text)
        if len(self.consoletext) > 10:
            self.consoletext.pop(0)
    
    def draw_console(self):
        for x,y in enumerate(self.consoletext):
            #print(x,y)
            draw_text(f"{y}",20,BLACK,WIDTH*(8/10),HEIGHT*(1/5)+HEIGHT*(1/20)*x)
        
Gm = game()

mpos = False

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit

            dir = vec(0,0)
            if event.key == pg.K_w:
                dir = vec(0,-1)
            if event.key == pg.K_a:
                dir = vec(-1,0)
            if event.key == pg.K_s:
                dir = vec(0,1)
            if event.key == pg.K_d:
                dir = vec(1,0)
            
            if Gm.G.selectedchar != 0:
                Gm.movechar(dir)
            Gm.G.make_wall(dir)

        if event.type == pg.MOUSEBUTTONDOWN:  
            mpos = vec(pg.mouse.get_pos())
            Gm.buttonpress()     
            Gm.G.find_closest()     
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    Gm.G.draw()
    Gm.draw()
    # anything down here will be displayed ontop of anything above
    pg.display.flip() # dose the changes goto doccumentation for other ways
Gm.G.save_grid_info()