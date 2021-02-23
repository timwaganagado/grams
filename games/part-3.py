# Pathfinding - Part 3
# Breadth First Search (BFS) - finding shortest path
# KidsCanCode 2017
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

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

font_name = pg.font.match_font('hack')
def draw_text(text, size, color, x, y, align="topleft"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(**{align: (x, y)})
    screen.blit(text_surface, text_rect)

class SquareGrid:
    def __init__(self, width, height,plate_value,plate_connection):
        self.width = width
        self.height = height
        self.walls = []
        self.winarea = []
        self.plate_location = []
        self.plate_value = plate_value
        self.plate_connection = plate_connection
        self.plate_awall = []
        self.active = True
        
    def con(self,dif):
        self.connections = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]
        # comment/uncomment this for diagonals:
        if dif == 'HARD':
            self.connections += [vec(1, 1), vec(-1, 1), vec(1, -1), vec(-1, -1)]
    def in_bounds(self, node):
        return 0 <= node.x < self.width and 0 <= node.y < self.height

    def passable(self, node):
        return node not in self.walls and node not in self.plate_awall

    def find_neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        # don't use this for diagonals:
        #if (node.x + node.y) % 2:
         #   neighbors.reverse()
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors

    def draw(self):
        for wall in self.walls:
            rect = pg.Rect(wall * TILESIZE, (TILESIZE, TILESIZE))
            pg.draw.rect(screen, LIGHTGRAY, rect)
        for area in self.winarea:
            rect = pg.Rect(area * TILESIZE, (TILESIZE, TILESIZE))
            pg.draw.rect(screen, GREEN, rect)
        for plate in self.plate_location:
            rect = pg.Rect(plate * TILESIZE, (48, 48))
            pg.draw.rect(screen, (230,230,250), rect)
        for pwall in self.plate_awall:
            rect = pg.Rect(pwall * TILESIZE, (TILESIZE, TILESIZE))
            pg.draw.rect(screen, BROWN, rect)
    def plateactive(self,player):
        for check in self.plate_location:
            if player == check:
                platetoact = check
            else:
                break
        platetoact = vec2int(platetoact)
        some = plate_value[platetoact]
        if self.active == True:
            for dumb in plate_wall:
                
                
                if some == self.plate_connection[dumb]:
                    if dumb in self.plate_awall:
                        self.plate_awall.remove(dumb)
            self.active = False
            
        elif self.active == False:
            for dumb in plate_wall:
        
                if some == plate_connection[dumb]:
                    if dumb not in self.plate_awall:
                        self.plate_awall.append(vec(dumb))
            self.active = True


def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))

def draw_icons(dif):
    for goals in goal:
        start_center = (goals.x * TILESIZE + TILESIZE / 2, goals.y * TILESIZE + TILESIZE / 2)
        screen.blit(home_img, home_img.get_rect(center=start_center))
    goal_center = (start.x * TILESIZE + TILESIZE / 2, start.y * TILESIZE + TILESIZE / 2)
    screen.blit(cross_img, cross_img.get_rect(center=goal_center))
    if dif == 'HARD':
        circle_center = (circle.x * TILESIZE + TILESIZE / 2, circle.y * TILESIZE + TILESIZE / 2)
        screen.blit(circle_img, circle_img.get_rect(center=circle_center))

def vec2int(v):
    return (int(v.x), int(v.y))

def breadth_first_search(graph, goal, start):
    frontier = deque()
    frontier.append(goal)
    area = []
    path = {}
    path[vec2int(goal)] = None
    while len(frontier) > 0:
        current = frontier.popleft()
        if current in start:
            currentgoal = vec(current)
            break
        for next in graph.find_neighbors(current):
            if vec2int(next) not in path:
                frontier.append(next)
                path[vec2int(next)] = current - next
                area.append(next)
        currentgoal = vec((random.choice(area)),(random.choice(area)))
                
    return path,currentgoal

class menu:
    def add(self,button,button2,button3,titl,button_name,button2_name,button3_name,text,text2,text3):
        self.button = button
        self.button2 = button2
        self.button3 = button3
        self.title = title
        self.button_name = button_name
        self.button2_name = button2_name
        self.button3_name = button3_name
        self.text = text
        self.text2 = text2
        self.text3 = text3
    def draw(self,dif):
        draw_text('GAME',100, GREY,title.x*TILESIZE,title.y*TILESIZE, align="topleft")
        rect = pg.Rect(self.button * TILESIZE, (500, TILESIZE))
        pg.draw.rect(screen, LIGHTGRAY, rect)
        draw_text('PLAY',50, BLACK,button_name.x*TILESIZE,button_name.y*TILESIZE + 5, align="topleft")
        rect = pg.Rect(self.button2 * TILESIZE, (500, TILESIZE))
        pg.draw.rect(screen, LIGHTGRAY, rect)
        draw_text('TOGGLE DIFFICULTY',30, GREY,11*TILESIZE,8*TILESIZE, align="topleft")
        draw_text(dif,50, BLACK,button2_name.x*TILESIZE,button2_name.y*TILESIZE, align="topleft")
        draw_text('HOW TO PLAY',30, GREY,text.x*TILESIZE,text.y*TILESIZE, align="topleft")
        draw_text('WASD TO MOVE RIGHT CLICK TO PLACE COLLECTED FOOD BOTTOM RIGHT TO SEE HOW MUCH FOOD RUN FORM THE CROSS',30, GREY,text2.x*TILESIZE,text2.y*TILESIZE, align="topleft")
        draw_text('BROWN WALLS ARE DEACTIVATED/ACTIVATED BY THE WHITE PRESSURE PLATES TRY TO CATCH CROSS IN THE GREEN AREA',30, GREY,text3.x*TILESIZE,text3.y*TILESIZE, align="topleft")
    def dogwhat(self):
        draw_text('PAUSE',100, GREY,title.x*TILESIZE,title.y*TILESIZE, align="topleft")
        rect = pg.Rect(self.button * TILESIZE, (500, TILESIZE))
        pg.draw.rect(screen, LIGHTGRAY, rect)
        draw_text('MAIN MENU',50, BLACK,button_name.x*TILESIZE,button_name.y*TILESIZE + 5, align="topleft")
        rect = pg.Rect(self.button3 * TILESIZE, (500, TILESIZE))
        pg.draw.rect(screen, LIGHTGRAY, rect)
        draw_text('QUIT',50, BLACK,button3_name.x*TILESIZE,button3_name.y*TILESIZE + 5, align="topleft")
        rect = pg.Rect(self.button2 * TILESIZE, (500, TILESIZE))
        pg.draw.rect(screen, LIGHTGRAY, rect)
        draw_text('RESTART',50, BLACK,button2_name.x*TILESIZE,button2_name.y*TILESIZE, align="topleft")
    def press(self,mpos,state,dif):
        box_1 = pg.Rect(self.button * TILESIZE,(500,TILESIZE))
        box_2 = pg.Rect(self.button2 * TILESIZE,(500,TILESIZE))
        box_3 = pg.Rect(self.button3 * TILESIZE,(500,TILESIZE))
        if state == 'menu':
            if box_1.collidepoint(mpos):
                playing = True
                running = True
                pause = False
            elif box_2.collidepoint(mpos):
                playing = False
                running = True 
                pause = False
                restart = False
                if dif == 'HARD':
                    dif = 'EASY'
                else:
                    dif = 'HARD'
            else:
                playing = False
                running = True
                pause = False
                
            restart = False
            dif = dif
        elif state == 'pause':
            if box_1.collidepoint(mpos):
                playing = False
                running = True
                pause = False
                restart = False
            elif box_3.collidepoint(mpos):
                running = False
            elif box_2.collidepoint(mpos):
                restart = True
                playing = True
                pause = False
                running = True
            else:
                running = True
                playing = True
                pause = True
                restart = False
            dif = dif
        return playing, running, pause , dif , restart

home_img = pg.image.load('grams/house-1.png.png').convert_alpha()
home_img = pg.transform.scale(home_img, (50, 50))
home_ui = pg.transform.scale(home_img, (40, 40))
home_ui.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
home_img.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)

cross_img = pg.image.load('grams/cross-1.png.png').convert_alpha()
cross_img = pg.transform.scale(cross_img, (50, 50))
cross_img.fill((255, 0, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
arrows = {}
arrow_img = pg.image.load('grams/arrow.png').convert_alpha()
arrow_img = pg.transform.scale(arrow_img, (50, 50))
circle_img = pg.image.load('grams/circle-1.png.png').convert_alpha()
circle_img = pg.transform.scale(circle_img, (50, 50))
circle_img.fill((255, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
for dir in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
    arrows[dir] = pg.transform.rotate(arrow_img, vec(dir).angle_to(vec(-1, 0)))


plate_value = {(23, 11):1}

plate_connection = {(20, 13):1, (17, 11):1}
he = 'hehe'
dif = 'HARD'
g = SquareGrid(GRIDWIDTH, GRIDHEIGHT,plate_value,plate_connection)


button = vec(9, 6)
button2 = vec(9,9)
title = vec(12,3)
button_name = vec(12,6)
button2_name = vec(12,9)
button3 = vec (9,12)
button3_name = vec(12,12)
text = vec(12, 11)
text2 = vec(1,12)
text3 = vec(1,13)
menu = menu()
menu.add(button,button2,button3,title,button_name,button2_name,button3_name,text,text2,text3)

plate_location = [(23,11)]
for loc in plate_location:
    g.plate_location.append(vec(loc))
plate_wall = [(20, 13),(17, 11)]
for loc in plate_wall:

    g.plate_awall.append(vec(loc))

walls = [(10, 7), (11, 7), (12, 7), (14, 7), (15, 7), (16, 7), (7, 7), (6, 7), (5, 7), (5, 5), (5, 6), (1, 6), (2, 6), (3, 6), (5, 10), (5, 11), (5, 12), (5, 9), (12, 8), (12, 9), (12, 10), (12, 11), (15, 13), (15, 12), (15, 11), (15, 10), (17, 7), (18, 7), (21, 7), (21, 6), (21, 5), (21, 4), (21, 3), (22, 5), (23, 5), (24, 5), (25, 5), (18, 10), (20, 10), (19, 10), (21, 10), (22, 10), (14, 4), (14, 5), (14, 6), (14, 0), (14, 1), (9, 2), (9, 1), (7, 3), (8, 3), (10, 3), (9, 3), (11, 3), (2, 5), (2, 4), (2, 3), (2, 2), (2, 1), (0, 11), (1, 11), (2, 11), (21, 2), (20, 11), (20, 12), (23, 13), (23, 14), (25, 10), (6, 12), (7, 12), (10, 12), (11, 12), (12, 12), (5, 3), (6, 3), (5, 4), (9, 4), (9, 5), (9, 
7), (9, 9), (9, 10), (9, 11), (9, 14), (7, 14), (7, 11), (7, 10), (7, 6), (7, 4), (7, 2), (7, 1), (16, 5), (16, 4), (16, 3), (16, 2), (16, 1), (18, 3), (19, 3), (18, 1), (19, 1), (21, 1), (20, 1), (23, 3), (26, 3), (24, 3), (1, 9), (1, 8), (3, 8), (3, 9), (21, 9), (27, 10), (8, 6), (20, 8), (19, 13), (18, 13), (17, 13), (17, 12), (17, 10)]
#walls = [(10, 7), (11, 7), (12, 7), (14, 7), (15, 7), (16, 7), (7, 7), (6, 7), (5, 7), (5, 5), (5, 6), (1, 6), (2, 6), (3, 6), (5, 10), (5, 11), (5, 12), (5, 9), (12, 8), (12, 9), (12, 10), (12, 11), (15, 13), (15, 12), (15, 11), (15, 10), (17, 7), (18, 7), (21, 7), (21, 6), (21, 5), (21, 4), (21, 3), (22, 5), (23, 5), (24, 5), (25, 5), (18, 10), (20, 10), (19, 10), (21, 10), (22, 10), (14, 4), (14, 5), (14, 6), (14, 0), (14, 1), (9, 2), (9, 1), (7, 3), (8, 3), (10, 3), (9, 3), (11, 3), (2, 5), (2, 4), (2, 3), (2, 2), (2, 1), (0, 11), (1, 11), (2, 11), (21, 2), (20, 11), (20, 12), (23, 13), (23, 14), (25, 10), (6, 12), (7, 12), (10, 12), (11, 12), (12, 12), (5, 3), (6, 3), (5, 4), (9, 4), (9, 5), (9, 
#7), (9, 9), (9, 10), (9, 11), (9, 14), (7, 14), (7, 11), (7, 10), (7, 6), (7, 4), (7, 2), (7, 1), (16, 5), (16, 4), (16, 3), (16, 2), (16, 1), (18, 3), (19, 3), (18, 1), (19, 1), (21, 1), (20, 1), (23, 3), (26, 3), (24, 3), (1, 9), (1, 8), (3, 8), (3, 9), (21, 9), (27, 10), (8, 6), (20, 8), (9, 0), (11, 0), (11, 1), (11, 2), (22, 0), (17, 0)]
for wall in walls:
    g.walls.append(vec(wall))




player = vec(0,0)

winarea = [(19, 11), (18, 11), (18, 12), (19, 12)]
#winarea = [(19, 11), (18, 11), (18, 12), (19, 12), (18, 0), (19, 0), (20, 0), (21, 0)]
for area in winarea:
    g.winarea.append(vec(area))



#player = vec(24, 11)

x, y = player
rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)


points = 0
cpoints = 0

red_image = pg.Surface((50,50))
red_image.set_alpha(50)
pg.draw.rect(red_image, WHITE, red_image.get_rect(), 10)

goal_ui = vec(2,13)

#d = shelve.open('aipoint.txt')
#points = d['a_p']

#cpoints = d['ca_p']
#d.close()


moveevent = pg.USEREVENT + 0
circleevent = pg.USEREVENT + 2
addgoal = pg.USEREVENT + 1
wincheck = pg.USEREVENT + 3
levelfin = pg.USEREVENT + 4
platecheck = pg.USEREVENT + 5

pg.time.set_timer(moveevent, 500)
pg.time.set_timer(addgoal, 3053)
pg.time.set_timer(circleevent, 450)
pg.time.set_timer(wincheck, 1000)
pg.time.set_timer(levelfin, 500)
pg.time.set_timer(platecheck, 500)


enemy_move = deque()
circle_move = deque()

check = [vec(0,1),vec(1,0),vec(0,-1),vec(-1,0)]
check += [vec(1, 1), vec(-1, 1), vec(1, -1), vec(-1, -1)]

died = False
win = False


food_count=0

big = []

winchecks = 0

playing = False

pause = False

state = 'menu'



running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        if playing == False:
            if event.type == pg.MOUSEBUTTONDOWN:
                
                mpos = pg.mouse.get_pos()
                if event.button == 1:
                    state = 'menu'
                    playing,running,pause,dif,restart = menu.press(mpos,state,dif)
                    g.con(dif)
                    if playing == True:     
                        died = False
                        player = vec(0,0)
                        goal = [vec(14, 8),vec(0,5)]
                        start = vec(20, 0)
                        cgoal = list(goal)
                        if dif == 'HARD':
                            
                            circle = vec(10,0)
                            cpath,ccg = breadth_first_search(g, circle, cgoal)
                            ccgc = [ccg + thing for thing in check]
                        path,cg = breadth_first_search(g, start, goal)
                        cgc = [cg + thing for thing in check]
                        
                        pcgc = [player + thing for thing in check]
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_l:
                        mpos = vec(pg.mouse.get_pos()) // TILESIZE
                        big.append(mpos)
                        text2 = mpos
                if event.key == pg.K_m:
                    print([(int(loc.x), int(loc.y)) for loc in big])    
        if playing == True:
            if restart == True:
                died = False
                player = vec(0,0)
                goal = [vec(14, 8),vec(0,5)]
                start = vec(20, 0)
                cgoal = list(goal)
                if dif == 'HARD':
                    
                    circle = vec(10,0)
                    cpath,ccg = breadth_first_search(g, circle, cgoal)
                    ccgc = [ccg + thing for thing in check]
                path,cg = breadth_first_search(g, start, goal)
                cgc = [cg + thing for thing in check]
                
                pcgc = [player + thing for thing in check]
            restart = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    
                    if pause == False:
                        
                        pause = True
                    elif pause == True:
                        pause = False
            if pause == False:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_m:
                        # dump the wall list for saving
                        print([(int(loc.x), int(loc.y)) for loc in g.walls])
                        print([(int(loc.x), int(loc.y)) for loc in g.winarea])
                        print((int(loc.x), int(loc.y)) for loc in big)
                    if event.key == pg.K_p:
                        mpos = vec(pg.mouse.get_pos()) // TILESIZE
                        if mpos in g.winarea:
                            g.winarea.remove(mpos)
                        else:
                            g.winarea.append(mpos)
                    if event.key == pg.K_l:
                        mpos = vec(pg.mouse.get_pos()) // TILESIZE
                        big.append(mpos)


                    if event.key == pg.K_w:
                        player += vec(0,-1)
                        if player in g.walls:
                            player += vec(0,1)
                    if event.key == pg.K_s:
                        player += vec(0,1)
                        if player in g.walls:
                            player += vec(0,-1)
                    if event.key == pg.K_a:
                        player += vec(-1,0)
                        if player in g.walls:
                            player += vec(1,0)         
                    if event.key == pg.K_d:
                        player += vec(1,0)
                        if player in g.walls:
                            player += vec(-1,0)
                    if player in goal:
                        
                        while player in goal:
                            goal.remove(player)

                    if player in cgoal:
                        food_count +=1
                        if dif == 'HARD':
                            cgoal.remove(player)
                    goal.append(player)
                    path,cg = breadth_first_search(g, start, goal)
                    enemy_move = deque()

                if event.type == pg.MOUSEBUTTONDOWN:
                    mpos = vec(pg.mouse.get_pos()) // TILESIZE
                    # if event.button == 1:
                    #    if mpos in g.walls:
                    #        g.walls.remove(mpos)
                    #    else:
                    #        g.walls.append(mpos)
                    if event.button == 2:
                        start = mpos
                    if event.button == 3 and food_count > 0:
                        goal.append(vec(mpos))
                        cgoal.append(vec(mpos))
                        food_count -= 1
                    path,cg = breadth_first_search(g, start, goal)
                    if dif == 'HARD':
                        cpath,ccg = breadth_first_search(g, circle, cgoal)
                    enemy_move = deque()
                    circle_move = deque()



                if event.type == wincheck:
                    if start in g.winarea:
                        winchecks = winchecks + 1

                        if winchecks == 3:
                            win = True
                            pg.time.set_timer(levelfin, 5000)
                    else:
                        winchecks = 0   
                        pg.time.set_timer(levelfin, 500)
                if player in plate_location and event.type == platecheck:
                    g.plateactive(player)
                    pg.time.set_timer(platecheck, 5000)
                    path,cg = breadth_first_search(g, start, goal)
                    if dif == 'HARD':
                        cpath,ccg = breadth_first_search(g, circle, cgoal)
                    enemy_move = deque()
                    circle_move = deque()
                elif player not in plate_location:
                    pg.time.set_timer(platecheck, 500)

                #how the ai moves
                hidden = [start + thing for thing in check]
                hidden = [(int(loc.x),int(loc.y)) for loc in hidden]
                if start not in hidden and event.type == moveevent and len(enemy_move) != 0:
                    m = enemy_move.popleft()

                    start = vec(m)

                    pcgc = [player + thing for thing in check]

                if len(goal) == 0:
                    empty = True
                else:
                    empty = False
                cgc = [cg + thing for thing in check]
                #checks if the ai can pick up a triangle
                if start in cgc and empty != True and cg in goal:
                    if cg == player:    
                        goal.remove(cg)
                    else:
                        goal.remove(cg)    
                        if dif == 'HARD':
                            cgoal.remove(cg)
                    #points += 1
                    if len(goal) == 0:
                        empty = True
                    else:
                        empty = False
                        circle_move = deque()
                        path,cg = breadth_first_search(g, start, goal)
                        if dif == 'HARD':
                            cpath,ccg = breadth_first_search(g, circle, cgoal)
                if dif == 'HARD':
                    chidden = [circle + thing for thing in check]

                    chidden = [(int(loc.x),int(loc.y)) for loc in chidden]
                    if circle not in chidden and event.type == circleevent and len(circle_move) != 0:
                        cm = circle_move.popleft()

                        circle = vec(cm)

                    if len(goal) == 0:
                        empty = True
                    else:
                        empty = False
                    ccgc = [ccg + thing for thing in check]
                    if circle in ccgc and empty != True and ccg in cgoal:

                        cgoal.remove(ccg)
                        goal.remove(ccg)
                        #cpoints += 1
                        if len(goal) == 0:
                            empty = True
                        else:
                            empty = False
                            enemy_move = deque()
                            cpath,ccg = breadth_first_search(g, circle, cgoal)
                            path,cg = breadth_first_search(g, start, goal)


                if start in pcgc:
                    player = vec(-10,-10)
                    died = True

                #adds goal at random in a random location
                if event.type == addgoal:
                    ng = ((random.randint(0,27),random.randint(0,14)))
                    while ng in g.walls:
                        ng = ((random.randint(0,27),random.randint(0,14)))
                    if dif == 'HARD':
                        if ng == m or ng == cm:
                            break
                    else:
                        if ng == m:
                            break
                    ng = vec(ng)

                    goal.append(ng)
                    cgoal.append(ng)
                    enemy_move = deque()
                    path,cg = breadth_first_search(g, start, goal)
                    if dif == 'HARD':
                        
                        circle_move = deque()
                        cpath,ccg = breadth_first_search(g, circle, cgoal)
                    pg.time.set_timer(addgoal, random.randint(553,3553))
                    
            if pause == True:
                if event.type == pg.MOUSEBUTTONDOWN:
                    state = 'pause'
                    mpos = pg.mouse.get_pos()
                    if event.button == 1:
                        playing,running,pause,dif,restart = menu.press(mpos,state,dif)  
    pg.display.set_caption("{:.2f}".format(clock.get_fps()))
    screen.fill(DARKGRAY)
    # fill explored area
    #for node in path:
     #   x, y = node
      #  rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
       # pg.draw.rect(screen, MEDGRAY, rect)
    if playing == True:
        if pause == False:    
            draw_grid()
            g.draw()
            # draw path from start to goal
            start = vec(start)
            current = cg + path[vec2int(cg)]

            while current != start:
                x = current.x * TILESIZE + TILESIZE / 2
                y = current.y * TILESIZE + TILESIZE / 2
                if path[(current.x,current.y)] == None:
                    break
                #img = arrows[vec2int(path[(current.x, current.y)])]

                if current not in enemy_move:
                    enemy_move.appendleft(vec2int(current))


                #r = img.get_rect(center=(x, y))
                #screen.blit(img, r)
                # find next in path
                current = current + path[vec2int(current)]
            if dif == 'HARD':
                circle = vec(circle)

                ccurrent = ccg + cpath[vec2int(ccg)]
                while ccurrent != circle:
                    x = ccurrent.x * TILESIZE + TILESIZE / 2
                    y = ccurrent.y * TILESIZE + TILESIZE / 2
                    if cpath[(ccurrent.x,ccurrent.y)] == None:
                        break
                    #img = arrows[vec2int(cpath[(ccurrent.x, ccurrent.y)])]

                    #if current not in enemy_move:
                     #   enemy_move.appendleft(vec2int(current))

                    if ccurrent not in circle_move:
                        circle_move.appendleft(vec2int(ccurrent))

                    #r = img.get_rect(center=(x, y))
                    #screen.blit(img, r)
                    # find next in path
                    ccurrent = ccurrent + cpath[vec2int(ccurrent)]

            xprint = 'cross points ' + str(points)
            cprint = 'circle points ' + str(cpoints)
            disfc = str(food_count)

            draw_icons(dif)
            draw_text(xprint,30, GREEN, WIDTH - 10, HEIGHT - 10, align="bottomright")
            draw_text(cprint,30,GREEN,WIDTH - 10, HEIGHT - 45,align="bottomright")

            if died:
                draw_text('You Died',50, GREEN, WIDTH - 750, HEIGHT - 600, align="topleft")
            if win:
                draw_text('You get to eat',50, GREEN, WIDTH - 750, HEIGHT - 600, align="topleft")


                if event.type == levelfin and start not in g.winarea:
                    win = False
            x, y = player
            rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
            pg.draw.rect(screen, CYAN, rect)


            for l in range(3):
                screen.blit(red_image,(72,600))
            lol_center = (goal_ui.x * TILESIZE + 5 / 2, goal_ui.y * TILESIZE + 1 / 2)
            screen.blit(home_ui, home_ui.get_rect(center=lol_center))
            draw_text(disfc,45,(0,0,255),WIDTH-1240,HEIGHT-90,align='topleft')
        else:
            screen.blit(red_image,(1344,600))
    else:
        menu.draw(dif)
    if pause == True:
        menu.dogwhat()
    pg.display.flip()
d = shelve.open('aipoint.txt')
d['a_p'] = points
d['ca_p'] = cpoints
d.close()


