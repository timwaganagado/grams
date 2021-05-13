
import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

''' Instructions
To select player or ai scroll down to the dictionary player calsses and change from 'ai' or 'player' ai will play it self and player will allow you to be a player

To Exit
press close on the window

Rules
each player will roll for the order highest goes last

each player will then choose a begging square to choose from

you can move to any square as long as it isnt occupied by another player your goal is to reach zero points you do this by:
moving to a square that has no other players adjacent 
moving to a square adjacent to a player 
if adjacent to one player you will give the other player a point and remove one from yourself
if adjacent to two players you will pick a player to give a point the other player you didnt choose will lose a point and yourself will lose a point
if adjacent to three players you will pick a player to give a point the other players you didnt choose will lose a point and yourself will lose a point

when a player reachs zero points the game ends and the player with zero points wins

caution 
when completing a game the next game may skip the first persons G.turn  

8.3/10 rohan
like it jackson
8/10 curtis
7/10 ozzy
4/4 dan bread
4/5 scarlet
6/5 jayden
9.9/10 trent
'''
DISPSIZE = 30 +30*2
GRIDWIDTH = 11 #+3*2
GRIDHEIGHT = 9 #+3*2
WIDTH = DISPSIZE * GRIDWIDTH
HEIGHT = DISPSIZE * GRIDHEIGHT #810
TILESIZE = DISPSIZE * 3
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

font_name = pg.font.match_font('hack')
def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)
    
class state():
    def __init__(self):
        self.state = 0
    def game(self):
        if G.playerclass[G.turnp] == 'player':
            if event.type == pg.MOUSEBUTTONDOWN:
                #print(G.turnp)
                placecheck = []
                mpos = vec(pg.mouse.get_pos())//TILESIZE
                #print(mpos)
                #print(placecheck)
                #print(random.choice([vec(0,0),vec(0,1),vec(0,2),vec(1,0),vec(1,1),vec(1,2),vec(2,0),vec(2,1),vec(2,2)]))
               
                for pos in G.players:
                    placecheck.append(G.players[pos])
                if event.button == 1:

                    if G.turn == 'roll' :
                        if G.subturn == 'go':
                            G.playerorder[G.turnp] = random.randint(1,6)
                            G.subturn = 'wait'
                    elif G.turn == 'place':
                        if mpos not in placecheck:
                            G.players[G.turnp] = mpos
                            #print(mpos)
                            if G.turnp == G.playerorder[0][0]:
                                G.turnp = G.playerorder[1][0]
                            elif G.turnp == G.playerorder[1][0]:
                                G.turnp = G.playerorder[2][0]
                            elif G.turnp == G.playerorder[2][0]:
                                G.turnp = G.playerorder[3][0]
                            elif G.turnp == G.playerorder[3][0]:
                                G.turn = 'play'
                                G.turnp = G.playerorder[0][0]
                    elif G.turn == 'play':
                       #print(G.turnp)
                        G.subturn = 'wait'
                        #print(confirm)
                        #print()
                        if mpos not in placecheck and G.confirm != True:
                            G.moved = True
                            G.players[G.turnp] = mpos
                            around = [G.players[G.turnp] + thing for thing in G.check]
                            for attack in G.players:
                                can = G.players[attack]
                                if can in around:
                                    G.attack.update({attack:can})
                        #print(len(G.attack))
                        #print(G.attack)
                        #print(mpos)
                        sorted(G.attack.items(), key = lambda t:t[0])
                        if G.moved == True:
                            if len(G.attack) == 0:
                                G.playerspoints[G.turnp] += -1
                                G.subturn = 'go'
                               #print('here')
                                G.moved = False
                            elif len(G.attack) == 1:
                                #print(G.attack)
                                G.moved = False
                                G.playerspoints[G.turnp] += -1
                                for attacking in G.attack:
                                    G.playerspoints[attacking] += 1

                                    G.attack = {}
                                    around = [G.players[attacking] + thing for thing in G.check]
                                    for attack in G.players:
                                        can = G.players[attack]
                                        if can in around:
                                            G.attack.update({attack:can})        
                                    if len(G.attack) >= 1:
                                        #print(G.attack)
                                        del G.attack[G.turnp]
                                        if len(G.attack) >= 1:
                                            G.playerspoints[attacking] += -1
                                            for otherword in G.attack:
                                                G.playerspoints[otherword] += 1

                                                G.attack = {}
                                                around = [G.players[otherword] + thing for thing in G.check]
                                                for attack in G.players:
                                                    can = G.players[attack]
                                                    if can in around:
                                                        G.attack.update({attack:can})        
                                                if len(G.attack) >= 1:
                                                    #print(G.attack)
                                                    del G.attack[attacking]
                                                    if len(G.attack) >= 1:
                                                        G.playerspoints[otherword] += -1
                                                        for attacking in G.attack:
                                                            G.playerspoints[attacking] += 1
                                G.subturn = 'go'
                            elif len(G.attack) == 2:
                                G.confirm = True
                                for attacking in G.attack:
                                    pos = G.attack[attacking]
                                    if pos in placecheck:
                                        G.attackey.append(pos)

                                #print(attackey)
                                #print('mpos',mpos)
                                if mpos in G.attackey:
                                    G.moved = False
                                    G.playerspoints[G.turnp] -= 1
                                    for attacking in G.attack:
                                        pos = G.attack[attacking]
                                        if pos != mpos:
                                            G.playerspoints[attacking] -= 1

                                            del G.attack[attacking]
                                            #print(G.attack)
                                            break
                                    for attacking in G.attack:
                                        G.playerspoints[attacking] += 1
                                        G.attack = {}
                                        around = [G.players[attacking] + thing for thing in G.check]
                                        for attack in G.players:
                                            can = G.players[attack]
                                            if can in around:
                                                G.attack.update({attack:can})        
                                        if len(G.attack) >= 1:
                                            #print(G.attack)
                                            del G.attack[G.turnp]
                                            #print(G.attack)
                                            if len(G.attack) >= 1:
                                                G.playerspoints[attacking] += -1
                                                for otherword in G.attack:
                                                    G.playerspoints[otherword] += 1
                                                    #print(G.playerspoints)
                                                    G.attack = {}
                                                    around = [G.players[otherword] + thing for thing in G.check]
                                                    for attack in G.players:
                                                        can = G.players[attack]
                                                        if can in around:
                                                            G.attack.update({attack:can})        
                                                    if len(G.attack) >= 1:
                                                        #print(G.attack)
                                                        del G.attack[attacking]
                                                        if len(G.attack) >= 1:
                                                            G.playerspoints[otherword] += -1
                                                            for attacking in G.attack:
                                                                G.playerspoints[attacking] += 1
                                    G.confirm = False
                                    G.subturn = 'go'       
                            elif len(G.attack) == 3:
                                #print(check)
                                G.confirm = True
                                for attacking in G.attack:
                                    pos = G.attack[attacking]
                                    if pos in placecheck:
                                        G.attackey.append(pos)

                                if mpos in G.attackey:
                                    G.moved = False
                                    G.playerspoints[G.turnp] -= 1
                                    for attacking in G.attack:
                                        pos = G.attack[attacking]

                                        if pos == mpos:
                                            G.playerspoints[attacking] += 1

                                            del G.attack[attacking]
                                            #print(G.attack)
                                            break
                                    for attacking in G.attack:
                                        G.playerspoints[attacking] -= 1
                                    G.confirm = False
                                    G.subturn = 'go' 
                            if G.confirm == False:
                                if G.turnp == G.playerorder[0][0]:
                                    G.turnp = G.playerorder[1][0]
                                elif G.turnp == G.playerorder[1][0]:
                                    G.turnp = G.playerorder[2][0]
                                elif G.turnp == G.playerorder[2][0]:
                                    G.turnp = G.playerorder[3][0]
                                elif G.turnp == G.playerorder[3][0]:
                                    G.turnp = G.playerorder[0][0]
                                G.move_timer = 0
                                G.subturn = 'wait'
                                G.attack = {}
                                G.attackey =[]
                                G.attackeyl ={}
                                G.move_timer = pg.time.get_ticks()
                            #print(G.playerorder)
                            for pointer in G.playerspoints:
                                #print(pointer)
                                point = G.playerspoints[pointer]
                                #print(point)
                                if point <= 0:
                                    G.turn = 'end'
                                    G.winner = pointer
                    elif G.turn == 'end':
                        G.playerorder = {name1:0, name2:0, name3:0, name4:0}
                        G.players = {name1:vec(-1,-1), name2:vec(-1,-1),name3:vec(-1,-1),name4:vec(-1,-1)}
                        G.playerspoints = {name1:5, name2:5,name3:5,name4:5}
                        G.attack = {}
                        G.turn = 'roll'
                        G.subturn = 'go'
                        G.turnp = name1
    def aiplay(self):
        placecheck = []
        for pos in G.players:
            placecheck.append(G.players[pos])
        #print(move_timer)
        if G.turn == 'roll' :
                if G.subturn == 'go':
                    G.playerorder[G.turnp] = random.randint(1,6)               
        elif G.turn == 'place' and G.move_timer == 0:
            mpos = random.choice([vec(0,0),vec(0,1),vec(0,2),vec(1,0),vec(1,1),vec(1,2),vec(2,0),vec(2,1),vec(2,2)]) 
            while mpos in placecheck:
                mpos = random.choice([vec(0,0),vec(0,1),vec(0,2),vec(1,0),vec(1,1),vec(1,2),vec(2,0),vec(2,1),vec(2,2)])
                
            G.players[G.turnp] = mpos
            G.move_timer=pg.time.get_ticks()
            #print(G.turnp)
            end = True
    
        elif G.turn == 'play' and  G.current_time - G.move_timer > 2000:
           #print(G.turnp)
            G.subturn = 'wait'
            aipos = random.choice([vec(0,0),vec(0,1),vec(0,2),vec(1,0),vec(1,1),vec(1,2),vec(2,0),vec(2,1),vec(2,2)]) 
            while aipos in placecheck:
                aipos = random.choice([vec(0,0),vec(0,1),vec(0,2),vec(1,0),vec(1,1),vec(1,2),vec(2,0),vec(2,1),vec(2,2)]) 
            #print(aipos)             
            G.players[G.turnp] = aipos
            around = [G.players[G.turnp] + thing for thing in G.check]
            for attack in G.players:
                can = G.players[attack]
                if can in around:
                    G.attack.update({attack:can})
            #print(len(G.attack))
            #print(G.attack)
            #print(mpos)
            sorted(G.attack.items(), key = lambda t:t[0])
            if len(G.attack) == 0:
                G.playerspoints[G.turnp] += -1
                G.subturn = 'go'
                 
            elif len(G.attack) == 1:
                #print(G.attack)
                #print(G.attack)
                G.playerspoints[G.turnp] += -1
                for attacking in G.attack:
                    G.playerspoints[attacking] += 1
                    G.attack = {}
                    around = [G.players[attacking] + thing for thing in G.check]
                    for attack in G.players:
                        can = G.players[attack]
                        if can in around:
                            G.attack.update({attack:can})        
                    if len(G.attack) >= 1:
                        #print(G.attack)
                        del G.attack[G.turnp]
                        if len(G.attack) >= 1:
                            G.playerspoints[attacking] += -1
                            for otherword in G.attack:
                                G.playerspoints[otherword] += 1
                                G.attack = {}
                                around = [G.players[otherword] + thing for thing in G.check]
                                for attack in G.players:
                                    can = G.players[attack]
                                    if can in around:
                                        G.attack.update({attack:can})        
                                if len(G.attack) >= 1:
                                    #print(G.attack)
                                    del G.attack[attacking]
                                    if len(G.attack) >= 1:
                                        G.playerspoints[otherword] += -1
                                        for attacking in G.attack:
                                            G.playerspoints[attacking] += 1
                
                
                G.confirm = False
                G.subturn = 'go'
                
                
            elif len(G.attack) == 2:
                G.confirm = True
                for attacking in G.attack:
                    pos = G.attack[attacking]
                    if pos in placecheck:
                        G.attackey.append(pos)
                #print(attackey)
                #print('mpos',mpos)
                aipos = random.choice(G.attackey)
                G.playerspoints[G.turnp] -= 1
                for attacking in G.attack:
                    pos = G.attack[attacking]
                    if pos != aipos:
                        G.playerspoints[attacking] -= 1
                        del G.attack[attacking]
                        #print(G.attack)
                        break
                for attacking in G.attack:
                    G.playerspoints[attacking] += 1
                    G.attack = {}
                    around = [G.players[attacking] + thing for thing in G.check]
                    for attack in G.players:
                        can = G.players[attack]
                        if can in around:
                            G.attack.update({attack:can})        
                    if len(G.attack) >= 1:
                        #print(G.attack)
                        del G.attack[G.turnp]
                        #print(G.attack)
                        if len(G.attack) >= 1:
                            G.playerspoints[attacking] += -1
                            for otherword in G.attack:
                                G.playerspoints[otherword] += 1
                                #print(G.playerspoints)
                                G.attack = {}
                                around = [G.players[otherword] + thing for thing in G.check]
                                for attack in G.players:
                                    can = G.players[attack]
                                    if can in around:
                                        G.attack.update({attack:can})        
                                if len(G.attack) >= 1:
                                    #print(G.attack)
                                    del G.attack[attacking]
                                    if len(G.attack) >= 1:
                                        G.playerspoints[otherword] += -1
                                        for attacking in G.attack:
                                            G.playerspoints[attacking] += 1
                G.confirm = False
                G.subturn = 'go'     
            elif len(G.attack) == 3:
                #print(check)
                G.confirm = True
                for attacking in G.attack:
                    pos = G.attack[attacking]
                    if pos in placecheck:
                        G.attackey.append(pos)
                aipos = random.choice(G.attackey)
                G.playerspoints[G.turnp] -= 1
                for attacking in G.attack:
                    pos = G.attack[attacking]
                    if pos == aipos:
                        G.playerspoints[attacking] += 1
                        del G.attack[attacking]
                        #print(G.attack)
                        break
                for attacking in G.attack:
                    G.playerspoints[attacking] -= 1
                
                G.confirm = False
                G.subturn = 'go'
            if G.turnp == G.playerorder[0][0]:
                G.turnp = G.playerorder[1][0]
            elif G.turnp == G.playerorder[1][0]:
                G.turnp = G.playerorder[2][0]
            elif G.turnp == G.playerorder[2][0]:
                G.turnp = G.playerorder[3][0]
            elif G.turnp == G.playerorder[3][0]:
                G.turnp = G.playerorder[0][0]
            G.move_timer = 0
            G.subturn = 'wait'
            G.attack = {}
            G.attackey =[]
            G.attackeyl ={}
            G.move_timer = pg.time.get_ticks()
            
            #print(G.playerorder)
            for pointer in G.playerspoints:
                #print(pointer)
                point = G.playerspoints[pointer]
                #print(point)
                if point <= 0:
                    G.turn = 'end'
                    G.winner = pointer
        elif G.turn == 'end':
                G.playerorder = {name1:0, name2:0, name3:0, name4:0}
                G.players = {name1:vec(-1,-1), name2:vec(-1,-1),name3:vec(-1,-1),name4:vec(-1,-1)}
                G.playerspoints = {name1:5, name2:5,name3:5,name4:5}
                G.attack = {}
                G.subturn = 'go'
                G.turnp = name1
                #G.playerclass[G.turnp] = 'player'
                if allclasss == True:
                    G.playerclass[G.turnp] = 'player'
                else:
                    if G.move_timer == 0:
                        G.move_timer = pg.time.get_ticks()

class game():
    def __int__(self):
        self.players = 0
        self.playerorder = 0
        self.playerspoints = 0
        self.attack = 0
        self.turnp = 0
        self.turn = 0
        self.subturn = 0
        self.check = 0
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))

    def drawchar(self):  
        for player in self.players: 
            x,y = self.players[player]
            rect = pg.Rect(x * TILESIZE +TILESIZE/3, y * TILESIZE+TILESIZE/3, TILESIZE/3, TILESIZE/3)
            pg.draw.rect(screen,BLACK,rect)
            text = player[0]+player[1]
            if self.turnp == player:
                draw_text(text,90,RED,x* TILESIZE +TILESIZE/2.75,y * TILESIZE+TILESIZE/2.75,align='topleft')
            else:
                draw_text(text,90,WHITE,x* TILESIZE +TILESIZE/2.75,y * TILESIZE+TILESIZE/2.75,align='topleft')
            draw_text(str(self.playerspoints[player]),90,BLACK,x* TILESIZE +TILESIZE/2.5,y * TILESIZE+TILESIZE/1.5,align='topleft')

class menu():
    def __init__(self):
        self.buttonclass = 0

pg.init()
#print(WIDTH,WIDTH*2/3)
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

G = game()
S = state()
M = menu()
name1 = 'burton'
name2 = 'jim'
name3 = 'p3'
name4 = 'p4'

G.playerorder = {name1:0, name2:0, name3:0, name4:0}
G.players = {name1:vec(-1,-1), name2:vec(-1,-1),name3:vec(-1,-1),name4:vec(-1,-1)}
G.playerspoints = {name1:5, name2:5,name3:5,name4:5}
G.attack = {}
G.playerclass = {name1:'player',name2:'player',name3:'ai',name4:'ai'}

G.turn = 'roll'
G.subturn = 'go'
G.turnp = name1
waittime = 10
G.check = [vec(0,1),vec(1,0),vec(0,-1),vec(-1,0)]
placecheck = []
G.attackey = []
attackeyl = {}
G.confirm = False
G.move_timer = 0
allclasss = False
end = False
G.moved = False
G.winner = 0

S.state = 'play'

M.buttonclasspos = {name1:(100,100)}
M.buttonclass = {name1:'player'}

for x in G.playerclass:
        classs = G.playerclass[x]
        if classs == 'player':
            allclasss = True

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_m:
               print(placecheck)
               print(G.attack)
        if event.type == pg.QUIT:
            run = False
            pg.quit() 
        
        if S.state == 'play':
            S.game()
    if S.state == 'play':
        if G.playerclass[G.turnp] == 'ai':
            S.aiplay()
        
    G.current_time = pg.time.get_ticks()
    #print(f'current time{ G.current_time} ai move time {move_timer}')
    screen.fill(WHITE)
    
    if S.state == 'play':
        G.draw_grid()
        G.drawchar()
        if G.turn == 'place' and G.playerclass[G.turnp] == 'ai':
            if end != True:
            
                if  G.current_time - G.move_timer > 2000:
                    if G.turnp == G.playerorder[0][0]:
                        G.turnp = G.playerorder[1][0]
                    elif G.turnp == G.playerorder[1][0]:
                        G.turnp = G.playerorder[2][0]
                    elif G.turnp == G.playerorder[2][0]:
                        G.turnp = G.playerorder[3][0]
                    elif G.turnp == G.playerorder[3][0]:
                        G.turn = 'play'
                        G.turnp = G.playerorder[0][0]
                        G.subturn = 'wait'
                    G.move_timer = 0
                   #print(subturn)
            else:
               #print(G.turnp)
                end = False
        if G.turn == 'end' and allclasss == False:
            if  G.current_time - G.move_timer > 2000:
                G.turn = 'roll'
                G.move_timer = 0
                G.subturn = 'go'
        if G.turn == 'roll':
            if G.subturn == 'go':
                text = str(G.turnp) + ' roll for order'
                draw_text(text, 30,RED,DISPSIZE/2,DISPSIZE/7,align='topleft')   
                if G.playerclass[G.turnp] == 'ai':
                    if waittime < 0:
                        G.subturn = 'wait'
                        waittime = 10
                        G.move_timer = 0
                    else:
                        waittime -= 1

            else:           
                text = str(G.turnp) + ' rolled a ' + str(G.playerorder[G.turnp])
                draw_text(text, 30,RED,DISPSIZE/2,DISPSIZE/7,align='topleft')
                if waittime < 0:
                    G.subturn = 'go'
                    waittime = 10
                    if G.turnp == name1:
                        G.turnp = name2
                    elif G.turnp == name2:
                        G.turnp = name3
                    elif G.turnp == name3:
                        G.turnp = name4
                    elif G.turnp == name4:
                        G.playerorder = sorted(G.playerorder.items(), key = lambda t:t[1])
                        #print(G.playerorder)
                        G.turnp = G.playerorder[0][0]
                        G.turn = 'place'
                       #print(G.playerorder)
                else:
                    waittime -= 1
        if G.turn == 'place' or G.turn == 'play':
            draw_text('order', int(TILESIZE/5),RED,int(WIDTH*5/6),5,align='topleft')
            draw_text(str(G.playerorder[0][0]), int(TILESIZE/4),RED,int(WIDTH*5/6),int(HEIGHT/23),align='topleft') #WIDTH 11*90 = 990*5/6 = 825 HEIGHT 9*90 = 810/35 = 23.14 810/80 = 10 810/125 = 6.48 810/170 = 4.76
            draw_text(str(G.playerorder[1][0]), int(TILESIZE/4),RED,int(WIDTH*5/6),int(HEIGHT/10),align='topleft')
            draw_text(str(G.playerorder[2][0]), int(TILESIZE/4),RED,int(WIDTH*5/6),int(HEIGHT/6.5),align='topleft')
            draw_text(str(G.playerorder[3][0]), int(TILESIZE/4),RED,int(WIDTH*5/6),int(HEIGHT/4.8),align='topleft')
        if True:
            text = 0
            for player in G.playerspoints:
                points = G.playerspoints[player]
                text += points
            draw_text(str(text), int(TILESIZE/4),RED,int(WIDTH*5/6),int(HEIGHT*9/10),align='topleft')
        if G.turn == 'place':
            text = str(G.turnp) + ' pick starting position'
            draw_text(text, 30,RED,DISPSIZE/2,DISPSIZE/7,align='topleft')
        if G.turn == 'play':
            draw_text('turn', int(TILESIZE/4),RED,int(WIDTH*5/6),int(HEIGHT*17/48),align='topleft')
            text = str(G.turnp) 
            draw_text(text, int(TILESIZE/4),RED,int(WIDTH*5/6),int(HEIGHT*1/2),align='topleft')
        if G.turn == 'end':
            text = str(G.winner) + ' is the winner'
            draw_text(text, 50,RED,DISPSIZE/2,DISPSIZE/7,align='topleft')
    
    pg.display.flip()