import pygame
vec = pygame.math.Vector2
pygame.init()
tilesize = 48
GRIDWIDTH = 28
GRIDHEIGHT = 15
width = tilesize * GRIDWIDTH
height = tilesize * GRIDHEIGHT
screen = pygame.display.set_mode((width,height))

class map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    def draw_walls(self):
        for wall in self.walls:
            rect = pygame.Rect(wall * tilesize, (tilesize, tilesize))
            pygame.draw.rect(screen, (140,140,140), rect)
    def enemy():
            
def player(pp):
    for axis in pp:
        rect = pygame.Rect(axis * tilesize, (tilesize, tilesize))
        pygame.draw.rect(screen, (255,0,0), rect)

walls = [(0,1),(2,3)]

m= map(GRIDWIDTH, GRIDHEIGHT)

pp = vec(0,0)

player(pp)

for wall in walls:
    m.walls.append(vec(wall))


        

run = False
while not run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mpos = vec(pygame.mouse.get_pos()) // tilesize
            if event.button == 1:
                if mpos in m.walls:
                    m.walls.remove(mpos)
                else:
                    m.walls.append(mpos)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            print([(int(loc.x), int(loc.y))  for loc in m.walls])
                
    screen.fill((40,40,40))    
    player()
    m.draw_walls()
    pygame.display.update()
pygame.QUIT




    