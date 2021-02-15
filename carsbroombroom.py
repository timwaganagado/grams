import pygame as pg
from os import path
from collections import deque
import random
import shelve
vec = pg.math.Vector2

TILESIZE = 96
GRIDWIDTH = 18
GRIDHEIGHT = 6
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
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.only_right = []
        self.right_check = [vec(1,0),vec(0,-1),vec(0,1)]
        self.only_left = []
        self.left_check = [vec(-1,0),vec(0,-1),vec(0,1)]
        self.connections = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]
        # comment/uncomment this for diagonals:
        #self.connections += [vec(1, 1), vec(-1, 1), vec(1, -1), vec(-1, -1)]

    def in_bounds(self, node):
        return 0 <= node.x < self.width and 0 <= node.y < self.height

    def passable(self, node):
        return node not in self.walls 
    
    def road(self,node,neighbors):
        rchecks = [node + pp for pp in self.right_check]
        for demon in rchecks:
            if demon in self.only_right:
                neighbors.remove(vec2int(demon))
        lchecks = [node + pp for pp in self.left_check]
        for demon in lchecks:
            if demon in self.only_left:
                neighbors.remove(vec2int(demon))
        return neighbors
            


    def find_neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        # don't use this for diagonals:
        if (node.x + node.y) % 2:
            neighbors.reverse()
        neighbors = self.road(node,neighbors)
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors

    def draw(self):
        for wall in self.walls:
            rect = pg.Rect(wall * TILESIZE, (TILESIZE, TILESIZE))
            pg.draw.rect(screen, LIGHTGRAY, rect)



            
def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))

def draw_icons():
    
    start_center = (goal.x * TILESIZE + TILESIZE / 2, goal.y * TILESIZE + TILESIZE / 2)
    screen.blit(home_img, home_img.get_rect(center=start_center))
    


def vec2int(v):
    return (int(v.x), int(v.y))

def breadth_first_search(graph, goal, end):
    frontier = deque()
    frontier.append(goal)
    area = []
    path = {}
    path[vec2int(goal)] = None
    while len(frontier) > 0:
        current = frontier.popleft()
        if current == end:
            
            break
        for next in graph.find_neighbors(current):
            if vec2int(next) not in path:
                frontier.append(next)
                path[vec2int(next)] = current - next
                
        
                
    return path



home_img = pg.image.load('grams/house-1.png.png').convert_alpha()
home_img = pg.transform.scale(home_img, (24, 24))
home_ui = pg.transform.scale(home_img, (40, 40))
home_ui.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
home_img.fill((0, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)

cross_img = pg.image.load('grams/New Piskel-1.png (2).png').convert_alpha()
cross_img = pg.transform.scale(cross_img, (24, 24))
cross_img.fill((255, 0, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
arrows = {}
arrow_img = pg.image.load('grams/arrow.png').convert_alpha()
arrow_img = pg.transform.scale(arrow_img, (24, 24))
circle_img = pg.image.load('grams/circle-1.png.png').convert_alpha()
circle_img = pg.transform.scale(circle_img, (24, 24))
circle_img.fill((255, 255, 0, 255), special_flags=pg.BLEND_RGBA_MULT)
for dir in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
    arrows[dir] = pg.transform.rotate(arrow_img, vec(dir).angle_to(vec(1, 0)))
    crosses = {}
for dir in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
    crosses[dir] = pg.transform.rotate(cross_img, vec(dir).angle_to(vec(1, 0)))


g = SquareGrid(GRIDWIDTH, GRIDHEIGHT)

only_right = [(1, 2), (2, 2), (3, 2), (4, 2), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (12, 2), (12,4), (13, 2), (14, 2), (15, 2), (16, 2)]
for pp in only_right:
    g.only_right.append(pp)
only_left = [(12, 5), (10, 5), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5),(3, 3), (2, 3), (1, 3), (16, 3), (15, 3), (14, 3)]
for pp in only_left:
    g.only_left.append(pp)

walls = [(0, 0), (1, 0), (0, 1), (1, 1), (0, 4), (1, 4), (1, 5), (0, 5), (2, 0), (2, 1), (3, 1), (3, 0), (2, 4), (2, 5), (3, 5), (3, 4), (6, 0), (6, 1), (6, 2), (6, 3), (8, 3), (9, 3), (10, 3), (11, 3), (11, 0), (11, 1), (11, 2), (10, 2), (10, 1), (10, 0), (9, 0), (9, 1), (9, 2), (8, 2), (8, 1), (8, 0), (7, 0), (7, 1), (7, 3), (7, 2), (14, 0), (14, 1), (15, 1), (16, 1), (17, 1), (17, 0), (16, 0), (15, 0), (14, 4), (14, 5), (15, 5), (15, 4), (16, 4), (16, 5), (17, 5), (17, 4)]
for wall in walls:
    g.walls.append(vec(wall))
goal = vec(17,3)
goalpos = vec(14,8)
start = vec(2,3)



enemy_move = deque()

move = deque()


moveevent = pg.USEREVENT + 0
circleevent = pg.USEREVENT + 2
addgoal = pg.USEREVENT + 1
wincheck = pg.USEREVENT + 3
levelfin = pg.USEREVENT + 4
platecheck = pg.USEREVENT + 5

pg.time.set_timer(moveevent, 10)
pg.time.set_timer(addgoal, 3053)
pg.time.set_timer(circleevent, 450)
pg.time.set_timer(wincheck, 1000)
pg.time.set_timer(levelfin, 500)
pg.time.set_timer(platecheck, 500)


path = breadth_first_search(g, goal, start)


big = []


pause = False

nextmove = True

i = True

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE and pause == False:
                pause = True
            elif event.key == pg.K_ESCAPE and pause == True:
                pause = False
        if pause == False:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m:
                    # dump the wall list for saving
                    print([(int(loc.x), int(loc.y)) for loc in g.walls])
                    
                    print([(int(loc.x), int(loc.y)) for loc in big])
                if event.key == pg.K_p:
                    mpos = vec(pg.mouse.get_pos()) // TILESIZE
                    if mpos in g.winarea:
                        g.winarea.remove(mpos)
                    else:
                        g.winarea.append(mpos)
                if event.key == pg.K_l:
                    mpos = vec(pg.mouse.get_pos()) // TILESIZE
                    big.append(mpos)
            if event.type == pg.MOUSEBUTTONDOWN:
                mpos = vec(pg.mouse.get_pos()) // TILESIZE
                if event.button == 1:
                    if mpos in g.walls:
                        g.walls.remove(mpos)
                    else:
                        g.walls.append(mpos)
                if event.button == 2:
                    start = mpos
                if event.button == 3 :
                    goal = mpos
                path = breadth_first_search(g, goal, start)
                enemy_move = deque()
            if event.type == moveevent and len(move)>0:
                print(move)    
                if xdif == 0:
                    start = m
                    nextmove = True
                if nextmove == True:
                    m = move.popleft()
                    x = start.x * TILESIZE + TILESIZE / 2
                    y = start.y * TILESIZE + TILESIZE / 2
                    
                    m = vec(m)
                
                    mx = m.x * TILESIZE + TILESIZE / 2
                    my = m.y * TILESIZE + TILESIZE / 2
                    
                nextmove = False
                #print((x, y))
                #print((mx,my))
                #print(start)
                
                
                
                xdif = mx - x
                #print(xdif)
                
                if xdif != 0:
                    if xdif > 0:
                        x += 1
                    elif xdif < 0:
                        x -= 1
                
                print(x)
                
                
                
                img = crosses[vec2int(path[(start.x, start.y)])]
                
                r = img.get_rect(center=(x, y))
                
                screen.blit(img, r)        
        
        
        pg.display.set_caption("{:.2f}".format(clock.get_fps()))
        screen.fill(DARKGRAY)
       #for node in path:
       #    nx,ny = node
       #    rect = pg.Rect(nx * TILESIZE,ny*TILESIZE,TILESIZE,TILESIZE)
       #    pg.draw.rect(screen, MEDGRAY, rect)
        draw_grid()
        g.draw()
        
        current = start + path[vec2int(start)]
        while current != goal:
        
            cx = current.x * TILESIZE + TILESIZE / 2
            cy = current.y * TILESIZE + TILESIZE / 2
            if path[(current.x,current.y)] == None:
            
                break
            
            
            img = arrows[vec2int(path[(current.x, current.y)])]
            if current not in enemy_move:
                enemy_move.append(vec2int(current))
                move.append(vec2int(current))
            #if current not in enemy_move:
             #   circle_move.appendleft(vec2int(current))
            r = img.get_rect(center=(cx, cy))
            screen.blit(img, r)
            # find next in path
            #if path[(current.x, current.y)] != None:
            #    
            #    img = crosses[vec2int(path[(current.x, current.y)])]
            #    
            #    r = img.get_rect(center=(x,y))
            #    
            #    screen.blit(img, r)
            current = current + path[vec2int(current)]
        
        
        
        if i == True:
            xdif = 1
            x = start.x * TILESIZE + TILESIZE / 2
            y = start.y * TILESIZE + TILESIZE / 2
            i = False
        img = crosses[vec2int(path[(start.x, start.y)])]
        r = img.get_rect(center=(x, y))
        screen.blit(img, r)
        draw_icons()
        pg.display.flip()
            