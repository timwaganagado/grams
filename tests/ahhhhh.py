import pygame as pg
vec = pg.math.Vector2

def b():
    path = {'lololo':1}
    ccg = [2,2]
    return path,ccg

def start():
    goal = [vec(14, 8),vec(0,5)]
    start = vec(20, 0)
    circle = vec(10,0)
    path,cg = b()
    cgoal = list(goal)
    cpath,ccg = b()
    player = vec(0,0)
    return goal,start,circle,path,cg,cgoal,cpath,ccg,player

goal,start,circle,path,cg,cgoal,cpath,ccg,player = start()
print(goal,start,circle,path,cg,cgoal,cpath,ccg,player)