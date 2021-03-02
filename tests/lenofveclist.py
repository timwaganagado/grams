import pygame as pg
from os import path
from collections import deque
import random
import shelve

vec = pg.math.Vector2
n = 1
checkmove = [vec(0,1),vec(1,0),vec(0,-1),vec(-1,0)]
#checkmove += [vec(1, 1), vec(1, 1), vec(1, -1), vec(-1, -1),vec(0,2),vec(2,0),vec(0,-2),vec(-2,0)]
#checkmove += [vec(2, 1), vec(-2, 1), vec(2, -1), vec(-2, -1),vec(1,2),vec(3,0),vec(1,-2),vec(-3,0),
#vec(1, 2), vec(-1, 2), vec(1, -2), vec(-1, -2),vec(0,3),vec(2,1),vec(0,-3),vec(-2,1)]
#print(len(checkmove))
#print(checkmove[0].x)
for movement in range(1,n+1):
    checkmovea = list(checkmove)
    checkmovea += list(checkmovea)
    print(checkmovea)
    ha = int(len(checkmovea)/2)
    for ind in range(0,ha):
        print(ind)
        target = checkmovea.pop()
        print(target)
        if target.x <= 0:
            checkmovea.append(target.x - 1)
        
        #if checkmovea[ind].x <= 0:
            
            
        #else:
            
    print('after firsthalf',checkmovea)
    otherha = len(checkmovea)
    for indother in range(ha,otherha):
        print(indother)
        print(checkmovea[indother])
        print(checkmovea[indother].y)
        if checkmovea[indother].y <= 0:
            print(checkmovea[indother].y)
            checkmovea[indother].y = checkmovea[indother].y - 1
            print(checkmovea[indother].y)
        else:
            checkmovea[indother].y = checkmovea[indother].y + 1
            print('+',checkmovea[indother].y)
    print("after lasthalf",checkmovea)
    checkmove += list(checkmovea)
for movement in range(0,n):
    checkmovea = list(checkmove)
    checkmovea += checkmovea
    print(checkmovea)
    ha = int(len(checkmovea)/2)
    for ind in range(0,ha):
        print(ind)
        if checkmovea[ind].x <= 0:
            checkmovea[ind].x = checkmovea[ind].x - 1
        else:
            checkmovea[ind].x = checkmovea[ind].x + 1
    print(checkmovea)
    otherha = len(checkmovea)
    for indother in range(ha,otherha):
        print(indother)
        if checkmovea[indother].y <= 0:
            checkmovea[indother].y = checkmovea[indother].y - 1
        else:
            checkmovea[indother].y = checkmovea[indother].y + 1
    print(checkmovea)
    checkmove += checkmovea