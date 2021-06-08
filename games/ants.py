import pygame as pg
from os import path
from collections import deque
import random
import shelve
import heapq
vec = pg.math.Vector2

TILESIZE = 30
GRIDWIDTH = 9
GRIDHEIGHT = 9
WIDTH = 800
HEIGHT = 800
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
def draw_grid():
    for x in range(0, WIDTH, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, TILESIZE):
        pg.draw.line(screen, LIGHTGRAY, (0, y), (WIDTH, y))
def vec2int(v):
    return (int(v.x), int(v.y))
class PriorityQueue:
    def __init__(self):
        self.nodes = []

    def put(self, node, cost):
        heapq.heappush(self.nodes, (cost, node))

    def get(self):
        return heapq.heappop(self.nodes)[1]

    def empty(self):
        return len(self.nodes) == 0
def heuristic(a, b):
    # return abs(a.x - b.x) ** 2 + abs(a.y - b.y) ** 2
    return (abs(a.x - b.x) + abs(a.y - b.y)) * 10
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

def breadth_first_search(graph, goal, start):
    M.current = goal
    frontier = deque()
    frontier.append(goal)
    area = []
    M.path = {}
    M.path[vec2int(goal)] = None
    while len(frontier) > 0:
        current = frontier.popleft()
        if current in start:
            currentgoal = vec(current)
            break
        for next in graph.find_neighbors(current):
            if vec2int(next) not in M.path:
                frontier.append(next)
                M.path[vec2int(next)] = current - next
                area.append(next)
        currentgoal = vec((random.choice(area)),(random.choice(area)))
                
    return M.path,currentgoal

def a_star_search(graph, start, end):
    frontier = PriorityQueue()
    frontier.put(vec2int(start), 0)
    area = []
    M.path = {}
    cost = {}
    M.path[vec2int(start)] = None
    cost[vec2int(start)] = 0
    while not frontier.empty():
        current = frontier.get()
        if current == end:
            currentgoal = vec(current)
            break
        for next in graph.extrafind_neighbors(vec(current)):
            next = vec2int(next)
            next_cost = cost[current] + graph.cost(current, next)
            if next not in cost or next_cost < cost[next]:
                cost[next] = next_cost
                priority = next_cost + heuristic(end, vec(next))
                frontier.put(next, priority)
                M.path[next] = vec(current) - vec(next)
                area.append(next)
        currentgoal = vec((random.choice(area)),(random.choice(area)))   
    return M.path, currentgoal

class Main():
    def __init__(self):
        pass
    def movecam(self,direction):
        for x in self.squares:
            x += direction
        self.ant += direction
        self.cg += direction
        for x in self.food:
            x += direction
    def draw_squares(self):
        for x in self.squares:
            rect = pg.Rect(x.x*TILESIZE,x.y*TILESIZE,TILESIZE,TILESIZE)
            pg.draw.rect(screen, LIGHTGRAY, rect)
        for x in self.food:
            rect = pg.Rect(x.x*TILESIZE,x.y*TILESIZE,TILESIZE,TILESIZE)
            pg.draw.rect(screen, GREEN, rect)
        for x in self.ant:
            rect = pg.Rect(int(self.ant[x][0].x*TILESIZE),int(self.ant[x][0].y*TILESIZE),TILESIZE,TILESIZE)
            pg.draw.rect(screen, RED, rect)


    def in_bounds(self, node):
        return M.current.x-10 <= node.x < M.current.x+10 and M.current.y-10 <= node.y < M.current.y+10

    def passable(self, node):
        return node not in self.squares

    def find_neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        # don't use this for diagonals:
        if (node.x + node.y) % 2:
            neighbors.reverse()
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors

    def extrain_bounds(self, node):
        return -1000 <= node.x < +1000 and -1000 <= node.y < +1000

    def extrapassable(self, node):
        return node not in self.squares

    def extrafind_neighbors(self, node):
        neighbors = [node + connection for connection in self.connections]
        # don't use this for diagonals:
        #if (node.x + node.y) % 2:
         #   neighbors.reverse()
        neighbors = filter(self.extrain_bounds, neighbors)
        neighbors = filter(self.extrapassable, neighbors)
        return neighbors

    def cost(self, from_node, to_node):
        if (vec(to_node) - vec(from_node)).length_squared() == 1:
            return self.weights.get(to_node, 0) + 10
        else:
            return self.weights.get(to_node, 0) + 14

arrows = {}
arrow_img = pg.image.load('images/arrow.png').convert_alpha()
arrow_img = pg.transform.scale(arrow_img, (50, 50))
for dir in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
    arrows[dir] = pg.transform.rotate(arrow_img, vec(dir).angle_to(vec(-1, 0)))

M = Main()

M.squares = []
l = [(0.0, 0.0), (0.0, 1.0), (0.0, 2.0), (0.0, 3.0), (0.0, 4.0), (0.0, 5.0), (0.0, 6.0), (0.0, 7.0), (0.0, 8.0), (0.0, 9.0), (0.0, 10.0), (0.0, 11.0), (0.0, 12.0), (0.0, 13.0), (0.0, 14.0), (0.0, 15.0), (0.0, 16.0), (0.0, 17.0), (0.0, 18.0), (0.0, 19.0), (0.0, 20.0), (0.0, 22.0), (0.0, 23.0), (0.0, 24.0), (0.0, 25.0), (0.0, 26.0), (0.0, 27.0), (0.0, 28.0), (0.0, 29.0), (0.0, 30.0), (0.0, 21.0), (0.0, 31.0), (0.0, 32.0), (0.0, 33.0), (0.0, 34.0), 
(0.0, 35.0), (0.0, 36.0), (0.0, 37.0), (0.0, 38.0), (0.0, 39.0), (0.0, 40.0), (0.0, 41.0), (0.0, 42.0), (0.0, 43.0), (0.0, 44.0), (0.0, 45.0), (0.0, 46.0), (0.0, 47.0), (0.0, 48.0), (0.0, 49.0), (0.0, 50.0), (0.0, 51.0), (0.0, 52.0), (1.0, 52.0), (2.0, 52.0), (3.0, 52.0), (4.0, 52.0), (5.0, 52.0), (6.0, 52.0), (7.0, 52.0), (8.0, 52.0), (9.0, 52.0), (10.0, 52.0), (12.0, 52.0), (13.0, 53.0), (13.0, 52.0), (14.0, 53.0), (15.0, 52.0), (15.0, 51.0), (14.0, 51.0), (13.0, 51.0), (11.0, 52.0), (14.0, 52.0), (16.0, 52.0), (17.0, 52.0), (18.0, 52.0), (19.0, 52.0), (20.0, 52.0), (22.0, 52.0), (23.0, 52.0), (25.0, 52.0), (27.0, 53.0), (28.0, 53.0), (29.0, 53.0), (26.0, 53.0), (24.0, 52.0), (28.0, 52.0), (31.0, 52.0), (32.0, 52.0), (30.0, 52.0), (21.0, 52.0), (27.0, 52.0), (29.0, 52.0), (33.0, 52.0), (34.0, 52.0), (26.0, 52.0), (36.0, 52.0), (37.0, 52.0), (38.0, 52.0), (39.0, 51.0), (40.0, 51.0), (41.0, 51.0), (42.0, 51.0), (43.0, 51.0), (43.0, 52.0), (42.0, 52.0), (40.0, 52.0), (39.0, 52.0), (35.0, 52.0), (44.0, 52.0), (45.0, 52.0), (41.0, 52.0), (48.0, 52.0), (50.0, 52.0), (51.0, 52.0), (49.0, 52.0), (47.0, 52.0), (46.0, 52.0), (52.0, 52.0), (52.0, 51.0), (52.0, 50.0), (52.0, 49.0), (52.0, 48.0), (52.0, 47.0), (52.0, 46.0), (52.0, 45.0), (52.0, 44.0), (52.0, 43.0), (51.0, 43.0), (51.0, 42.0), (51.0, 41.0), (52.0, 40.0), (52.0, 
39.0), (52.0, 38.0), (52.0, 37.0), (52.0, 36.0), (52.0, 35.0), (52.0, 34.0), (52.0, 33.0), (52.0, 32.0), (52.0, 31.0), (52.0, 30.0), (52.0, 29.0), (52.0, 28.0), (52.0, 27.0), (52.0, 26.0), (52.0, 25.0), (52.0, 24.0), (52.0, 23.0), (52.0, 22.0), (52.0, 21.0), (52.0, 20.0), (52.0, 19.0), (52.0, 18.0), (52.0, 17.0), (52.0, 16.0), (52.0, 15.0), (52.0, 14.0), (52.0, 13.0), (52.0, 12.0), (52.0, 11.0), (52.0, 10.0), (52.0, 9.0), (52.0, 8.0), (52.0, 
7.0), (52.0, 6.0), (52.0, 5.0), (52.0, 4.0), (52.0, 3.0), (52.0, 2.0), (52.0, 1.0), (52.0, 0.0), (51.0, 0.0), (50.0, 0.0), (49.0, 0.0), (48.0, 0.0), (47.0, 0.0), (46.0, 0.0), (45.0, 0.0), (44.0, 0.0), (43.0, 0.0), (42.0, 0.0), (41.0, 0.0), (40.0, 0.0), (39.0, 0.0), (38.0, 0.0), (37.0, 0.0), (36.0, 0.0), (35.0, 0.0), (34.0, 0.0), (33.0, 0.0), (32.0, 0.0), (31.0, 0.0), (30.0, 0.0), (29.0, 0.0), (28.0, 0.0), (27.0, 0.0), (26.0, 0.0), (25.0, 0.0), (24.0, 0.0), (23.0, 0.0), (22.0, 0.0), (21.0, 0.0), (20.0, 0.0), (19.0, 0.0), (18.0, 0.0), (17.0, 0.0), (16.0, 0.0), (15.0, 0.0), (14.0, 0.0), (13.0, 0.0), (12.0, 0.0), (11.0, 0.0), (10.0, 0.0), (9.0, 0.0), (8.0, 0.0), (7.0, 0.0), (6.0, 0.0), (5.0, 0.0), (4.0, 0.0), (3.0, 0.0), (2.0, 0.0), (1.0, 0.0), (1.0, 49.0), (2.0, 49.0), (3.0, 49.0), (4.0, 49.0), (4.0, 48.0), (4.0, 47.0), (4.0, 46.0), (1.0, 43.0), (2.0, 43.0), (3.0, 43.0), (4.0, 43.0), (4.0, 42.0), (4.0, 41.0), (4.0, 40.0), (4.0, 39.0), (5.0, 39.0), (6.0, 39.0), (7.0, 39.0), (8.0, 39.0), (9.0, 39.0), (10.0, 39.0), (10.0, 43.0), (10.0, 42.0), (10.0, 41.0), (10.0, 40.0), (7.0, 46.0), (8.0, 46.0), (9.0, 46.0), (10.0, 46.0), (11.0, 43.0), (12.0, 43.0), (13.0, 43.0), (14.0, 43.0), (14.0, 42.0), (14.0, 41.0), (14.0, 40.0), (14.0, 39.0), (14.0, 38.0), (14.0, 37.0), (14.0, 36.0), (11.0, 36.0), (10.0, 36.0), (9.0, 36.0), (8.0, 36.0), (7.0, 36.0), (6.0, 36.0), (5.0, 36.0), (4.0, 36.0), (4.0, 35.0), (4.0, 34.0), (4.0, 33.0), (4.0, 32.0), (4.0, 29.0), (4.0, 28.0), (4.0, 27.0), (4.0, 26.0), (4.0, 25.0), (4.0, 24.0), (5.0, 29.0), (6.0, 29.0), (7.0, 29.0), (8.0, 29.0), (9.0, 29.0), (10.0, 29.0), (11.0, 29.0), (12.0, 29.0), (7.0, 32.0), (8.0, 32.0), (9.0, 32.0), (10.0, 32.0), (11.0, 32.0), (11.0, 33.0), (11.0, 34.0), (11.0, 35.0), (12.0, 28.0), (12.0, 27.0), (12.0, 26.0), (12.0, 25.0), (12.0, 24.0), (11.0, 24.0), (10.0, 24.0), (9.0, 24.0), (8.0, 24.0), (7.0, 24.0), (4.0, 20.0), (5.0, 20.0), (6.0, 20.0), (7.0, 20.0), (8.0, 20.0), (9.0, 20.0), (10.0, 20.0), (11.0, 20.0), (13.0, 20.0), (12.0, 20.0), (14.0, 20.0), (15.0, 20.0), (16.0, 20.0), (16.0, 19.0), (16.0, 18.0), (16.0, 17.0), (16.0, 16.0), (16.0, 15.0), (4.0, 19.0), (4.0, 18.0), (4.0, 17.0), (4.0, 16.0), (4.0, 15.0), (4.0, 14.0), (4.0, 13.0), (4.0, 12.0), (4.0, 11.0), (4.0, 10.0), (3.0, 20.0), (2.0, 20.0), (1.0, 20.0), (15.0, 40.0), (16.0, 40.0), (17.0, 40.0), (18.0, 40.0), (19.0, 40.0), (19.0, 39.0), (20.0, 39.0), (20.0, 40.0), (21.0, 40.0), (22.0, 40.0), (23.0, 40.0), (24.0, 
40.0), (19.0, 38.0), (19.0, 37.0), (19.0, 36.0), (19.0, 35.0), (19.0, 34.0), (19.0, 33.0), (19.0, 32.0), (19.0, 31.0), (19.0, 30.0), (19.0, 29.0), (18.0, 29.0), (17.0, 29.0), (16.0, 29.0), (15.0, 29.0), (14.0, 29.0), (13.0, 29.0), (25.0, 40.0), (26.0, 40.0), (27.0, 40.0), (28.0, 40.0), (29.0, 40.0), (30.0, 40.0), (31.0, 40.0), (25.0, 39.0), (25.0, 38.0), (25.0, 37.0), (25.0, 36.0), (25.0, 35.0), (29.0, 30.0), (30.0, 29.0), (30.0, 31.0), (30.0, 32.0), (30.0, 33.0), (30.0, 34.0), (30.0, 35.0), (30.0, 36.0), (30.0, 37.0), (30.0, 38.0), (30.0, 39.0), (28.0, 30.0), (27.0, 30.0), (26.0, 30.0), (25.0, 30.0), (24.0, 30.0), (23.0, 30.0), (23.0, 31.0), (23.0, 32.0), (22.0, 41.0), (22.0, 42.0), (22.0, 43.0), (22.0, 44.0), (22.0, 45.0), (22.0, 46.0), (21.0, 46.0), (20.0, 46.0), (19.0, 46.0), (18.0, 46.0), (17.0, 46.0), (16.0, 46.0), (15.0, 46.0), (22.0, 51.0), (22.0, 50.0), (22.0, 49.0), (22.0, 48.0), (21.0, 48.0), (21.0, 49.0), (20.0, 49.0), (19.0, 49.0), (18.0, 49.0), (17.0, 49.0), (16.0, 49.0), (15.0, 49.0), (33.0, 51.0), (33.0, 50.0), (33.0, 49.0), (33.0, 48.0), (32.0, 47.0), (32.0, 46.0), (32.0, 45.0), (32.0, 44.0), (32.0, 43.0), (32.0, 42.0), (32.0, 48.0), (12.0, 15.0), (11.0, 15.0), (10.0, 15.0), (9.0, 15.0), (8.0, 15.0), (8.0, 14.0), (8.0, 13.0), (8.0, 12.0), (8.0, 11.0), (8.0, 10.0), (8.0, 9.0), (8.0, 8.0), (13.0, 15.0), (13.0, 14.0), (13.0, 13.0), (13.0, 12.0), (13.0, 11.0), (13.0, 10.0), (13.0, 9.0), (13.0, 8.0), (13.0, 7.0), (13.0, 6.0), (8.0, 7.0), (8.0, 6.0), (8.0, 5.0), (8.0, 4.0), (8.0, 3.0), (8.0, 2.0), (8.0, 1.0), (17.0, 15.0), (18.0, 15.0), (19.0, 15.0), (20.0, 15.0), (21.0, 15.0), (21.0, 14.0), (21.0, 13.0), (21.0, 12.0), (21.0, 11.0), (24.0, 15.0), (24.0, 14.0), (24.0, 13.0), (24.0, 12.0), (24.0, 11.0), (24.0, 10.0), (24.0, 9.0), (24.0, 8.0), (24.0, 7.0), (24.0, 6.0), (24.0, 5.0), (24.0, 4.0), (24.0, 3.0), (24.0, 2.0), (25.0, 15.0), (26.0, 15.0), (27.0, 15.0), (28.0, 15.0), (29.0, 15.0), (30.0, 15.0), (31.0, 15.0), (32.0, 15.0), (33.0, 15.0), (29.0, 14.0), (29.0, 
13.0), (29.0, 12.0), (29.0, 11.0), (29.0, 10.0), (29.0, 9.0), (29.0, 8.0), (29.0, 7.0), (29.0, 6.0), (29.0, 5.0), (29.0, 4.0), (29.0, 3.0), (30.0, 8.0), (31.0, 8.0), (32.0, 8.0), (33.0, 8.0), (34.0, 8.0), (35.0, 8.0), (33.0, 14.0), (33.0, 13.0), (33.0, 12.0), (33.0, 11.0), (32.0, 40.0), (33.0, 40.0), (34.0, 40.0), (35.0, 40.0), (36.0, 40.0), (36.0, 45.0), (36.0, 44.0), (36.0, 43.0), (36.0, 42.0), (36.0, 41.0), (39.0, 50.0), (39.0, 49.0), (39.0, 48.0), (39.0, 47.0), (39.0, 46.0), (39.0, 45.0), (39.0, 44.0), (39.0, 43.0), (39.0, 42.0), (39.0, 41.0), (39.0, 40.0), (42.0, 43.0), (43.0, 43.0), (44.0, 43.0), (45.0, 43.0), (46.0, 43.0), (46.0, 42.0), (46.0, 41.0), (46.0, 40.0), (46.0, 39.0), (46.0, 38.0), (46.0, 37.0), (46.0, 36.0), (46.0, 35.0), (45.0, 35.0), (44.0, 35.0), (43.0, 35.0), (42.0, 35.0), (41.0, 35.0), (40.0, 35.0), (39.0, 35.0), (38.0, 35.0), (37.0, 35.0), (36.0, 35.0), (35.0, 35.0), (35.0, 34.0), (35.0, 33.0), (35.0, 32.0), (35.0, 31.0), (35.0, 30.0), (35.0, 29.0), (46.0, 51.0), (46.0, 50.0), (46.0, 49.0), (46.0, 48.0), (46.0, 47.0), (46.0, 46.0), (51.0, 30.0), (50.0, 30.0), (49.0, 30.0), (48.0, 30.0), (47.0, 30.0), (46.0, 30.0), (45.0, 30.0), (44.0, 30.0), (43.0, 30.0), (42.0, 30.0), (41.0, 30.0), (40.0, 30.0), (39.0, 30.0), (47.0, 35.0), (48.0, 35.0), (45.0, 33.0), (44.0, 33.0), (43.0, 33.0), (42.0, 33.0), 
(41.0, 33.0), (41.0, 32.0), (41.0, 31.0), (45.0, 32.0), (34.0, 15.0), (35.0, 15.0), (36.0, 15.0), (37.0, 15.0), (37.0, 16.0), (37.0, 17.0), (37.0, 18.0), (37.0, 19.0), (37.0, 20.0), (37.0, 21.0), (37.0, 22.0), (37.0, 23.0), (37.0, 24.0), (36.0, 24.0), (35.0, 24.0), (38.0, 23.0), (39.0, 23.0), (40.0, 23.0), (41.0, 23.0), (41.0, 24.0), (41.0, 25.0), (41.0, 26.0), (41.0, 27.0), (51.0, 23.0), (50.0, 23.0), (49.0, 23.0), (48.0, 23.0), (47.0, 23.0), (46.0, 23.0), (45.0, 23.0), (45.0, 24.0), (45.0, 25.0), (45.0, 26.0), (45.0, 27.0), (46.0, 26.0), (47.0, 26.0), (48.0, 26.0), (49.0, 26.0), (38.0, 15.0), (39.0, 15.0), (40.0, 15.0), (41.0, 15.0), (42.0, 15.0), (42.0, 16.0), (42.0, 17.0), (42.0, 18.0), (42.0, 19.0), (47.0, 1.0), (47.0, 2.0), (47.0, 3.0), (47.0, 4.0), (47.0, 5.0), (47.0, 6.0), (47.0, 7.0), (47.0, 8.0), (46.0, 8.0), (45.0, 8.0), (44.0, 8.0), (43.0, 8.0), (42.0, 8.0), (41.0, 8.0), (40.0, 8.0), (39.0, 8.0), (38.0, 8.0), (41.0, 14.0), (41.0, 13.0), (41.0, 12.0), (41.0, 11.0), (38.0, 9.0), (38.0, 10.0), (38.0, 11.0), (38.0, 12.0), (51.0, 15.0), (50.0, 15.0), (49.0, 15.0), (48.0, 15.0), (47.0, 15.0), (46.0, 15.0), (47.0, 9.0), (47.0, 10.0), (47.0, 11.0), (51.0, 8.0), (50.0, 8.0), (48.0, 11.0), (49.0, 11.0), (17.0, 20.0), (18.0, 20.0), (19.0, 20.0), (23.0, 29.0), (23.0, 28.0), (23.0, 27.0), (23.0, 26.0), (23.0, 25.0), (23.0, 24.0), (24.0, 24.0), (25.0, 24.0), (26.0, 24.0), (27.0, 24.0), (28.0, 24.0), (29.0, 24.0), (19.0, 21.0), (19.0, 22.0), (19.0, 23.0), (19.0, 24.0), (19.0, 25.0), (19.0, 26.0)]
for x in l:
    M.squares.append(vec(x))

add = False
dvec = 0
dpath = 1
dmove = 2
dcg = 3
dfoodcount = 4
M.ant = {1:[vec(2,2),[],deque(),0,0]}
M.food = [vec(15,15)]
M.home = vec(30,30)
M.connections = [vec(1, 0), vec(-1, 0), vec(0, 1), vec(0, -1)]
M.weights = {}
for x in M.ant:
    M.ant[x][dpath],M.ant[x][dcg] = breadth_first_search(M, M.ant[x][0], M.food)


M.move = deque()
move_timer = 500
produce_timer = 0

foodcount = 0
colonyfood = 0
numberant = 2

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        mpos = mpos = vec(pg.mouse.get_pos()) // TILESIZE
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                add = True
            if event.button == 3:
                M.food.append(mpos)
                for x in M.ant:
                    M.ant[x][dpath],M.ant[x][dcg] = breadth_first_search(M, M.ant[x][dvec], M.food)
                    M.ant[x][dmove] = deque()
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                add = False
                if mpos not in M.squares:
                    M.squares.append(mpos)
                elif mpos in M.squares:
                    M.squares.remove(mpos)
                for x in M.ant:
                    M.ant[x][dpath],M.ant[x][dcg] = breadth_first_search(M, M.ant[x][dvec], M.food)
                    M.ant[x][dmove] = deque()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                print([(l.x,l.y)for l in M.squares])
            if event.key == pg.K_w:
                M.movecam(vec(0,1))
            if event.key == pg.K_s:
                M.movecam(vec(0,-1))
            if event.key == pg.K_a:
                M.movecam(vec(1,0))
            if event.key == pg.K_d:
                M.movecam(vec(-1,0))
            if event.key == pg.K_q:
                TILESIZE = int(TILESIZE/2)
            if event.key == pg.K_e:
                TILESIZE = int(TILESIZE*2)
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit
            for x in M.ant:
                M.ant[x][dpath],M.ant[x][dcg] = breadth_first_search(M, M.ant[x][dvec], M.food)
                M.ant[x][dmove] = deque()
                if foodcount > 0:
                    M.ant[x][dpath],M.ant[x][dcg] = a_star_search(M,M.ant[x][dvec],M.home)
                    M.ant[x][dmove] = deque() 
                    
                
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    if add:
        pass
    screen.fill(WHITE) # fills screnn with color
    current_time = pg.time.get_ticks()
    #for node in M.path:
    #    x, y = node
    #    rect = pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE)
    #    pg.draw.rect(screen, MEDGRAY, rect)
    for ll in M.ant:
        current = M.ant[ll][dcg] + M.ant[ll][dpath][vec2int(M.ant[ll][dcg])]
        while current != M.ant[ll][0]:
            x = current.x * TILESIZE + TILESIZE / 2
            y = current.y * TILESIZE + TILESIZE / 2
            if M.ant[ll][dpath][(current.x,current.y)] == None:
                break
            img = arrows[vec2int(M.ant[ll][dpath][(current.x, current.y)])]

            if current not in M.ant[ll][dmove]:
                M.ant[ll][dmove].appendleft(vec2int(current))
            r = img.get_rect(center=(x, y))
            screen.blit(img, r)
            # find next in M.path
            current = current + M.ant[ll][dpath][vec2int(current)]
    
        if len(M.ant[ll][dmove]) > 0:
            if current_time - move_timer > 200:
                for ll in M.ant:
                    if len(M.ant[ll][dmove]) > 0:
                        M.ant[ll][dvec] = vec(M.ant[ll][dmove].popleft())
                move_timer = pg.time.get_ticks()
        else:
            if M.ant[ll][dfoodcount] > 0:
                if M.ant[ll][dcg] == M.home:
                    M.ant[ll][dfoodcount] -= 1
                    colonyfood += 1
                M.ant[ll][dpath],M.ant[ll][dcg] = a_star_search(M,M.ant[ll][0],M.home)
                M.ant[ll][dmove] = deque() 
            elif M.ant[ll][dcg] in M.food:
                M.food.remove(M.ant[ll][dcg])
                M.ant[ll][dfoodcount] += 1
            else:
                M.ant[ll][dpath],M.ant[ll][dcg] = breadth_first_search(M, M.ant[ll][0], M.food)
                M.ant[ll][dmove] = deque()
    if current_time - produce_timer > 10000:
        produce_timer = pg.time.get_ticks()
        if colonyfood > 0:
            colonyfood -= 1
            M.ant.update({numberant:[vec(M.home.x+2,M.home.y),[],deque(),0,0]})
            M.ant[numberant][dpath],M.ant[numberant][dcg] = breadth_first_search(M, M.ant[numberant][dvec], M.food)
            M.ant[numberant][dmove] = deque()
            numberant += 1

    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application

    # anything down here will be displayed ontop of anything above
    draw_grid()
    M.draw_squares()
    pg.display.flip() # dose the changes goto doccumentation for other ways