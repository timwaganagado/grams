
import pygame
vec = pygame.math.Vector2
aura = []
movement = 3
poopee = vec(0,0)
checker = [vec(0,1),vec(0,-1),vec(1,0),vec(-1,0)]
for x in range(0,movement+movement): # checks the where the enemy can move 
    #print(x)
    if x == 1: # first check around the enemy
        for x in checker:
            new = poopee+ x # restricts movements to the grid
            aura.append((new.x,new.y))
    else: # second and more checks and if the movement is more
        oldchecked = list(aura)
        for y in oldchecked: #grabs the already checked positions and checks around them
            for x in checker:
                new = y+ x 
                if new not in aura: #prevents already checked vecs to be added to the list
                    if movement*-1< new.x < movement and movement*-1< new.y < movement:
                        aura.append((new.x,new.y))
print(aura)