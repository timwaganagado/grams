
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
when completing a game the next game may skip the first persons turn  
'''
DISPSIZE = 30 +30*2
GRIDWIDTH = 11 #+3*2
GRIDHEIGHT = 9 #+3*2
WIDTH = DISPSIZE * GRIDWIDTH
HEIGHT = DISPSIZE * GRIDHEIGHT
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

class game():
    def __int__(self):
        self.players = 0
        self.playerorder = 0
        self.playerspoints = 0
        self.attack = 0
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
            draw_text(str(player),90,WHITE,x* TILESIZE +TILESIZE/2.75,y * TILESIZE+TILESIZE/2.75,align='topleft')
            draw_text(str(self.playerspoints[player]),90,BLACK,x* TILESIZE +TILESIZE/2.5,y * TILESIZE+TILESIZE/1.5,align='topleft')

pg.init()
print(WIDTH,WIDTH*2/3)
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

G = game()
name1 = 'po'
name2 = 'p2'
name3 = 'p3'
name4 = 'p4'

G.playerorder = {name1:0, name2:0, name3:0, name4:0}
G.players = {name1:vec(-1,-1), name2:vec(-1,-1),name3:vec(-1,-1),name4:vec(-1,-1)}
G.playerspoints = {name1:5, name2:5,name3:5,name4:5}
G.attack = {}
G.playerclass = {name1:'player',name2:'player',name3:'player',name4:'ai'}

turn = 'roll'
subturn = 'go'
turnp = name1
waittime = 10
check = [vec(0,1),vec(1,0),vec(0,-1),vec(-1,0)]
placecheck = []
attackey = []
attackeyl = {}
confirm = False
move_timer = 0
allclasss = False
end = False

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
        placecheck = []
        if event.type == pg.QUIT:
            run = False
            pg.quit() 
        if G.playerclass[turnp] == 'player':
            if event.type == pg.MOUSEBUTTONDOWN:
                #print(turnp)

                mpos = vec(pg.mouse.get_pos())//TILESIZE
                #print(mpos)
                #print(placecheck)
                #print(random.choice([vec(0,0),vec(0,1),vec(0,2),vec(1,0),vec(1,1),vec(1,2),vec(2,0),vec(2,1),vec(2,2)]))
               
                for pos in G.players:
                    placecheck.append(G.players[pos])
                if event.button == 1:

                    if turn == 'roll' :
                        if subturn == 'go':
                            G.playerorder[turnp] = random.randint(1,6)
                            subturn = 'wait'
                    elif turn == 'place':
                        if mpos not in placecheck:
                            G.players[turnp] = mpos
                            #print(mpos)
                            if turnp == G.playerorder[0][0]:
                                turnp = G.playerorder[1][0]
                            elif turnp == G.playerorder[1][0]:
                                turnp = G.playerorder[2][0]
                            elif turnp == G.playerorder[2][0]:
                                turnp = G.playerorder[3][0]
                            elif turnp == G.playerorder[3][0]:
                                turn = 'play'
                                turnp = G.playerorder[0][0]
                    elif turn == 'play':
                        print(turnp)
                        subturn = 'wait'
                        #print(confirm)
                        #print()
                        if mpos not in placecheck and confirm != True:
                            G.players[turnp] = mpos
                            around = [G.players[turnp] + thing for thing in check]
                            for attack in G.players:
                                can = G.players[attack]
                                if can in around:
                                    G.attack.update({attack:can})
                        #print(len(G.attack))
                        #print(G.attack)
                        #print(mpos)
                        sorted(G.attack.items(), key = lambda t:t[0])
                        if len(G.attack) == 0:
                            G.playerspoints[turnp] += -1
                            subturn = 'go'
                        elif len(G.attack) == 1:
                            #print(G.attack)
                            G.playerspoints[turnp] += -1
                            for attacking in G.attack:
                                G.playerspoints[attacking] += 1

                                G.attack = {}
                                around = [G.players[attacking] + thing for thing in check]
                                for attack in G.players:
                                    can = G.players[attack]
                                    if can in around:
                                        G.attack.update({attack:can})        
                                if len(G.attack) >= 1:
                                    #print(G.attack)
                                    del G.attack[turnp]
                                    if len(G.attack) >= 1:
                                        G.playerspoints[attacking] += -1
                                        for otherword in G.attack:
                                            G.playerspoints[otherword] += 1

                                            G.attack = {}
                                            around = [G.players[otherword] + thing for thing in check]
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
                            subturn = 'go'
                        elif len(G.attack) == 2:
                            confirm = True
                            for attacking in G.attack:
                                pos = G.attack[attacking]
                                if pos in placecheck:
                                    attackey.append(pos)

                            #print(attackey)
                            #print('mpos',mpos)
                            if mpos in attackey:
                                G.playerspoints[turnp] -= 1
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
                                    around = [G.players[attacking] + thing for thing in check]
                                    for attack in G.players:
                                        can = G.players[attack]
                                        if can in around:
                                            G.attack.update({attack:can})        
                                    if len(G.attack) >= 1:
                                        #print(G.attack)
                                        del G.attack[turnp]
                                        #print(G.attack)
                                        if len(G.attack) >= 1:
                                            G.playerspoints[attacking] += -1
                                            for otherword in G.attack:
                                                G.playerspoints[otherword] += 1
                                                #print(G.playerspoints)
                                                G.attack = {}
                                                around = [G.players[otherword] + thing for thing in check]
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
                                confirm = False
                                subturn = 'go'       
                        elif len(G.attack) == 3:
                            #print(check)
                            confirm = True
                            for attacking in G.attack:
                                pos = G.attack[attacking]
                                if pos in placecheck:
                                    attackey.append(pos)

                            if mpos in attackey:
                                G.playerspoints[turnp] -= 1
                                for attacking in G.attack:
                                    pos = G.attack[attacking]

                                    if pos == mpos:
                                        G.playerspoints[attacking] += 1

                                        del G.attack[attacking]
                                        #print(G.attack)
                                        break
                                for attacking in G.attack:
                                    G.playerspoints[attacking] -= 1
                                confirm = False
                                subturn = 'go' 
                        if confirm == False:
                            if turnp == G.playerorder[0][0]:
                                turnp = G.playerorder[1][0]
                            elif turnp == G.playerorder[1][0]:
                                turnp = G.playerorder[2][0]
                            elif turnp == G.playerorder[2][0]:
                                turnp = G.playerorder[3][0]
                            elif turnp == G.playerorder[3][0]:
                                turnp = G.playerorder[0][0]
                            move_timer = 0
                            subturn = 'wait'
                            G.attack = {}
                            attackey =[]
                            attackeyl ={}
                        #print(G.playerorder)
                        for pointer in G.playerspoints:
                            #print(pointer)
                            point = G.playerspoints[pointer]
                            #print(point)
                            if point <= 0:
                                turn = 'end'
                                winner = pointer
                    elif turn == 'end':
                        G.playerorder = {name1:0, name2:0, name3:0, name4:0}
                        G.players = {name1:vec(-1,-1), name2:vec(-1,-1),name3:vec(-1,-1),name4:vec(-1,-1)}
                        G.playerspoints = {name1:5, name2:5,name3:5,name4:5}
                        G.attack = {}
                        turn = 'roll'
                        subturn = 'go'
                        turnp = name1
    
    if G.playerclass[turnp] == 'ai':
        placecheck = []
        for pos in G.players:
            placecheck.append(G.players[pos])
        #print(move_timer)
        if turn == 'roll' :
                if subturn == 'go':
                    G.playerorder[turnp] = random.randint(1,6)               
        elif turn == 'place' and move_timer == 0:
            mpos = random.choice([vec(0,0),vec(0,1),vec(0,2),vec(1,0),vec(1,1),vec(1,2),vec(2,0),vec(2,1),vec(2,2)]) 
            while mpos in placecheck:
                mpos = random.choice([vec(0,0),vec(0,1),vec(0,2),vec(1,0),vec(1,1),vec(1,2),vec(2,0),vec(2,1),vec(2,2)])
                
            G.players[turnp] = mpos
            move_timer=pg.time.get_ticks()
            #print(turnp)
            end = True
    
        elif turn == 'play' and move_timer == 0:
            print(turnp)
            subturn = 'wait'
            aipos = random.choice([vec(0,0),vec(0,1),vec(0,2),vec(1,0),vec(1,1),vec(1,2),vec(2,0),vec(2,1),vec(2,2)]) 
            while aipos in placecheck:
                aipos = random.choice([vec(0,0),vec(0,1),vec(0,2),vec(1,0),vec(1,1),vec(1,2),vec(2,0),vec(2,1),vec(2,2)]) 
            #print(aipos)             
            G.players[turnp] = aipos
            around = [G.players[turnp] + thing for thing in check]
            for attack in G.players:
                can = G.players[attack]
                if can in around:
                    G.attack.update({attack:can})
            #print(len(G.attack))
            #print(G.attack)
            #print(mpos)
            sorted(G.attack.items(), key = lambda t:t[0])
            if len(G.attack) == 0:
                G.playerspoints[turnp] += -1
                subturn = 'go'
                 
            elif len(G.attack) == 1:
                #print(G.attack)
                #print(G.attack)
                G.playerspoints[turnp] += -1
                for attacking in G.attack:
                    G.playerspoints[attacking] += 1
                    G.attack = {}
                    around = [G.players[attacking] + thing for thing in check]
                    for attack in G.players:
                        can = G.players[attack]
                        if can in around:
                            G.attack.update({attack:can})        
                    if len(G.attack) >= 1:
                        #print(G.attack)
                        del G.attack[turnp]
                        if len(G.attack) >= 1:
                            G.playerspoints[attacking] += -1
                            for otherword in G.attack:
                                G.playerspoints[otherword] += 1
                                G.attack = {}
                                around = [G.players[otherword] + thing for thing in check]
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
                
                
                confirm = False
                subturn = 'go'
                
                
            elif len(G.attack) == 2:
                confirm = True
                for attacking in G.attack:
                    pos = G.attack[attacking]
                    if pos in placecheck:
                        attackey.append(pos)
                #print(attackey)
                #print('mpos',mpos)
                aipos = random.choice(attackey)
                G.playerspoints[turnp] -= 1
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
                    around = [G.players[attacking] + thing for thing in check]
                    for attack in G.players:
                        can = G.players[attack]
                        if can in around:
                            G.attack.update({attack:can})        
                    if len(G.attack) >= 1:
                        #print(G.attack)
                        del G.attack[turnp]
                        #print(G.attack)
                        if len(G.attack) >= 1:
                            G.playerspoints[attacking] += -1
                            for otherword in G.attack:
                                G.playerspoints[otherword] += 1
                                #print(G.playerspoints)
                                G.attack = {}
                                around = [G.players[otherword] + thing for thing in check]
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
                confirm = False
                subturn = 'go'     
            elif len(G.attack) == 3:
                #print(check)
                confirm = True
                for attacking in G.attack:
                    pos = G.attack[attacking]
                    if pos in placecheck:
                        attackey.append(pos)
                aipos = random.choice(attackey)
                G.playerspoints[turnp] -= 1
                for attacking in G.attack:
                    pos = G.attack[attacking]
                    if pos == aipos:
                        G.playerspoints[attacking] += 1
                        del G.attack[attacking]
                        #print(G.attack)
                        break
                for attacking in G.attack:
                    G.playerspoints[attacking] -= 1
                
                confirm = False
                subturn = 'go'
                    
            move_timer = pg.time.get_ticks()
            
            #print(G.playerorder)
            for pointer in G.playerspoints:
                #print(pointer)
                point = G.playerspoints[pointer]
                #print(point)
                if point <= 0:
                    turn = 'end'
                    winner = pointer
        elif turn == 'end':
                G.playerorder = {name1:0, name2:0, name3:0, name4:0}
                G.players = {name1:vec(-1,-1), name2:vec(-1,-1),name3:vec(-1,-1),name4:vec(-1,-1)}
                G.playerspoints = {name1:5, name2:5,name3:5,name4:5}
                G.attack = {}
                subturn = 'go'
                turnp = name1
                #G.playerclass[turnp] = 'player'
                if allclasss == True:
                    G.playerclass[turnp] = 'player'
                else:
                    if move_timer == 0:
                        move_timer = pg.time.get_ticks()
        if event.type == pg.QUIT:
            run = False
            pg.quit() 
    current_time = pg.time.get_ticks()
    #print(f'current time{current_time} ai move time {move_timer}')
    if turn == 'place' and G.playerclass[turnp] == 'ai':
        if end != True:
            
            if current_time - move_timer > 2000:
                if turnp == G.playerorder[0][0]:
                    turnp = G.playerorder[1][0]
                elif turnp == G.playerorder[1][0]:
                    turnp = G.playerorder[2][0]
                elif turnp == G.playerorder[2][0]:
                    turnp = G.playerorder[3][0]
                elif turnp == G.playerorder[3][0]:
                    turn = 'play'
                    turnp = G.playerorder[0][0]
                    subturn = 'wait'
                move_timer = 0
                print(subturn)
        else:
            print(turnp)
            end = False
    if turn == 'play'and subturn == 'go':
        if current_time - move_timer > 2000:
            #print(move_timer)
            if turnp == G.playerorder[0][0]:
                turnp = G.playerorder[1][0]
            elif turnp == G.playerorder[1][0]:
                turnp = G.playerorder[2][0]
            elif turnp == G.playerorder[2][0]:
                turnp = G.playerorder[3][0]
            elif turnp == G.playerorder[3][0]:
                turnp = G.playerorder[0][0]
            move_timer = 0
            subturn = 'wait'
            G.attack = {}
            attackey =[]
            attackeyl ={}
            #print('check')
    
    if turn == 'end' and allclasss == False:
        if current_time - move_timer > 2000:
            turn = 'roll'
            move_timer = 0
            subturn = 'go'
    screen.fill(WHITE)
    G.draw_grid()
    G.drawchar()
    if turn == 'roll':
        if subturn == 'go':
            text = str(turnp) + ' roll for order'
            draw_text(text, 30,RED,DISPSIZE/2,DISPSIZE/7,align='topleft')   
            if G.playerclass[turnp] == 'ai':
                if waittime < 0:
                    subturn = 'wait'
                    waittime = 10
                    move_timer = 0
                else:
                    waittime -= 1

        else:           
            text = str(turnp) + ' rolled a ' + str(G.playerorder[turnp])
            draw_text(text, 30,RED,DISPSIZE/2,DISPSIZE/7,align='topleft')
            if waittime < 0:
                subturn = 'go'
                waittime = 10
                if turnp == name1:
                    turnp = name2
                elif turnp == name2:
                    turnp = name3
                elif turnp == name3:
                    turnp = name4
                elif turnp == name4:
                    G.playerorder = sorted(G.playerorder.items(), key = lambda t:t[1])
                    #print(G.playerorder)
                    turnp = G.playerorder[0][0]
                    turn = 'place'
                    print(G.playerorder)
            else:
                waittime -= 1
    if turn == 'place' or turn == 'play':
        draw_text('order', 20,RED,280,5,align='topleft')
        draw_text(str(G.playerorder[0][0]), 20,RED,290,20+15*0,align='topleft')
        draw_text(str(G.playerorder[1][0]), 20,RED,290,20+15*1,align='topleft')
        draw_text(str(G.playerorder[2][0]), 20,RED,290,20+15*2,align='topleft')
        draw_text(str(G.playerorder[3][0]), 20,RED,290,20+15*3,align='topleft')
    if True:
        text = 0
        for player in G.playerspoints:
            points = G.playerspoints[player]
            text += points
        draw_text(str(text), 20,RED,290,190,align='topleft')
    if turn == 'place':
        text = str(turnp) + ' pick starting position'
        draw_text(text, 30,RED,DISPSIZE/2,DISPSIZE/7,align='topleft')
    if turn == 'play':
        draw_text('turn', 20,RED,280,100,align='topleft')
        text = str(turnp) 
        draw_text(text, 20,RED,280,120,align='topleft')
    if turn == 'end':
        text = str(winner) + ' is the winner'
        draw_text(text, 50,RED,DISPSIZE/2,DISPSIZE/7,align='topleft')
    
    pg.display.flip()