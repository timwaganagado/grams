import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

TILESIZE = 48
GRIDWIDTH = 28
GRIDHEIGHT = 15
WIDTH = TILESIZE * GRIDWIDTH
HEIGHT = TILESIZE * GRIDHEIGHT
FPS = 30
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
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()





checkmove = [vec(0,1),vec(1,0),vec(0,-1),vec(-1,0)]
checkmove += [vec(-1, 1), vec(2, 0), vec(1, -1), vec(-2, 0),vec(0,2),vec(1,1),vec(0,-2),vec(-1,-1)]
checkmove += [vec(2, 1), vec(-2, 1), vec(2, -1), vec(-2, -1),vec(1,2),vec(3,0),vec(1,-2),vec(-3,0),
vec(1, 2), vec(-1, 2), vec(1, -2), vec(-1, -2),vec(0,3),vec(2,1),vec(0,-3),vec(-2,1)]



font_name = pg.font.match_font('hack')
def draw_text(text, size, color, x, y,fade, align="topleft"):
    if fade >= 0:
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_surface.set_alpha(fade)
        M.fade -= 5
        text_rect = text_surface.get_rect(**{align: (x, y)})
        screen.blit(text_surface, text_rect)

class map():
    def __int__():
        self.moveable = []
        self.player = ()
        self.diff = []
        self.movingani = []
        self.enemy = []
        self.title = []
        self.turn = ''
        self.fade = 0
        self.ediff = []
        self.emovingani = []
        self.ani = bool
        self.eani = bool
        self.lowestq = 0
        self.test = []
        
    def draw(self):
        for move in self.moveable:
            rect = pg.Rect(move * TILESIZE, (TILESIZE, TILESIZE))
            pg.draw.rect(screen, LIGHTGRAY, rect)
        
    def drawchar(self):   
       #print"draw",self.player)

        x,y = self.player
        rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen,WHITE,rect)
        x,y = self.enemy
        rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
        pg.draw.rect(screen,RED,rect)
        for test in self.test:
            rect = pg.Rect(test * TILESIZE, (TILESIZE, TILESIZE))
            pg.draw.rect(screen, YELLOW, rect)

    def animate(self,mpos,skip):    
        s = 2
        if not self.ani:
            self.movingani = (mpos.x*TILESIZE,mpos.y*TILESIZE)         
            self.diff = ((mpos.x*TILESIZE)- (self.player.x*TILESIZE),(mpos.y*TILESIZE)- (self.player.y*TILESIZE))
            self.player = (self.player.x*TILESIZE,self.player.y*TILESIZE)  
            self.ani = True
        else:
            x,y = self.player
            self.diff = (self.movingani[0]- self.player[0],self.movingani[1]- self.player[1])
            if self.diff[0] == 0 and self.diff[1] == 0 or skip:
                #print(check)
                self.ani = False
                
                M.turn = 'enemy'
               #print"before conversion",self.player)
                x,y = self.movingani[0]//TILESIZE,self.movingani[1]//TILESIZE
                self.player = vec(x,y)
                x,y = self.player
                rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                pg.draw.rect(screen,WHITE,rect)
                skip = False
                self.fade = 200
               #print"afterconversion",self.player)
            elif  0 >= self.diff[0] or self.diff[0] >= 0 or 0 >= self.diff[1] or self.diff[1] >= 0:
                if self.diff[0] > 0:
                    #print('x',x)
                    x += s
                elif self.diff[0] < 0:
                    x -= s
                elif self.diff[1] > 0:
                    #print('x',x)
                    y += s
                elif self.diff[1] < 0:
                    y -= s
                #print(self.player)
                print(self.movingani,self.diff ,(self.player[0]//TILESIZE,self.player[1]//TILESIZE ))
                self.player = int(x),int(y)
                rect = pg.Rect(x , y , TILESIZE, TILESIZE)
                pg.draw.rect(screen,WHITE,rect)   
        return skip
    def text(self):
        if self.turn != 'all':
            draw_text(str(f'{self.turn} phase'),100, GREY,self.title.x*TILESIZE,self.title.y*TILESIZE,self.fade,align="topleft")
    def enemymove(self):
        avaliblemovement = [movement + self.enemy for movement in checkmove]
        #compare avaliblemovement to player  
        lowestediff = (self.player.x- avaliblemovement[0].x,self.player.y- avaliblemovement[0].y)   
        if lowestediff[0] > 0:
                lowestediff = (lowestediff[0]*-1,lowestediff[1])
        if lowestediff[1] > 0:
            lowestediff = (lowestediff[0],lowestediff[1]*-1)
            
        lowestcombineddiff = lowestediff[0] + lowestediff[1] 
        if lowestcombineddiff > 0:
            lowestcombineddiff *= -1
        print(lowestcombineddiff)
        self.lowestq = avaliblemovement[0]
        for a in avaliblemovement:
            print(a)
            
            
            if a.x < 0:
                break
            ediff = (self.player.x- a.x,self.player.y- a.y)
            if ediff[0] > 0:
                ediff = (ediff[0]*-1,ediff[1])
            if ediff[1] > 0:
                ediff = (ediff[0],ediff[1]*-1)
            combinedediff = ediff[0] + ediff[1]
            #print(a)
            
            
            #print(ediff)
            #print('combined',combinedediff)
            if combinedediff >= lowestcombineddiff:
                print(self.player)
                print('set new q',a)
                lowestcombineddiff =  combinedediff 
                self.lowestq = a
            print(ediff)
            print(combinedediff)
            
            
            
        #print(self.lowestq)
        self.enemyanimate()
        self.test.append(self.lowestq)
    
    def enemyanimate(self): 
        
        s = 1
        if not self.eani:
            self.emovingani = (self.lowestq.x*TILESIZE,self.lowestq.y*TILESIZE)         
            self.ediff = ((self.lowestq.x*TILESIZE)- (self.enemy[0]*TILESIZE),(self.lowestq.y*TILESIZE)- (self.enemy[1]*TILESIZE))
            self.enemy = (self.enemy[0]*TILESIZE,self.enemy[1]*TILESIZE)  
            self.eani = True
            #print(self.emovingani,self.ediff ,self.enemy )
        else:
            x,y = self.enemy
            self.ediff = (self.emovingani[0]- self.enemy[0],self.emovingani[1]- self.enemy[1])
            if self.ediff[0] == 0 and self.ediff[1] == 0 :
                print(self.lowestq)
                print(check)
                self.eani = False
                
                M.turn = 'player'
               #print"before conversion",self.player)
                x,y = self.emovingani[0]//TILESIZE,self.emovingani[1]//TILESIZE
                self.enemy = vec(x,y)
                x,y = self.enemy
                rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
                pg.draw.rect(screen,RED,rect)
                
                self.fade = 200
               #print"afterconversion",self.player)
            elif  0 >= self.ediff[0] or self.ediff[0] >= 0 or 0 >= self.ediff[1] or self.ediff[1] >= 0:
                if self.ediff[0] > 0:
                    #print('x',x)
                    x += s
                elif self.ediff[0] < 0:
                    x -= s
                elif self.ediff[1] > 0:
                    #print('x',x)
                    y += s
                elif self.ediff[1] < 0:
                    y -= s
                #*print(self.emovingani,self.ediff ,(self.enemy[0]//TILESIZE,self.enemy[1]//TILESIZE  ))
                #print(self.player)
                self.enemy = int(x),int(y)
                rect = pg.Rect(x , y , TILESIZE, TILESIZE)
                pg.draw.rect(screen,RED,rect)   
        

M = map()
M.player = vec(0,1)
M.enemy = vec(5,5)
M.title = vec(9, 1)
M.fade = 200
M.turn = 'all'
M.ani = False
M.eani = False
M.test = [vec(-1,-1)]

moving = False
skip = False
n = 2
done = False




running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_m:
                print(M.title)
        if event.type == pg.MOUSEBUTTONDOWN:
            if not M.ani :
                if M.turn == 'player' or M.turn == 'all':
               #    printani)
                    mpos = vec(pg.mouse.get_pos()) // TILESIZE

                    if event.button == 1:


                        M.moveable = [movement + M.player for movement in checkmove]
                        #M.test = [movement + M.enemy for movement in checkmove]
                        print(M.moveable)
                        if moving == False:
                            moving = True

                        else:
                            if mpos in M.moveable:
                                skip = M.animate(mpos,skip)
                                M.ani = True
                                moving = False  
                                done = False
                            else:
                                moving = False   
                    elif event.button == 3:

                        M.player = mpos 

                    #if event.button == 3:
            
            else:
                skip = True
        elif M.turn == 'enemy'and  done == False:
            M.enemymove()    
            done = True          
                    
                    
        if event.type == pg.QUIT:
            running = False
        
    screen.fill(DARKGRAY)
    if moving:
        M.draw()
    
    M.drawchar()
    if M.ani:
        skip = M.animate(mpos,skip)
    if M.eani:
        M.enemyanimate()
    M.text() 
    pg.display.flip()