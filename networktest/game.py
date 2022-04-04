from turtle import Screen
import pygame
from network import Network
import random
vec = pygame.math.Vector2

BLUE = (0,0,255)
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
DARKBLUE = (0,0,139)
MOMENTUMCOLOR = (166, 138, 178)
PURPLE = (149, 53, 83)
VIOLET = (127,0,255)
ORANGE = (255, 165, 0)




class Game:

    def __init__(self, w, h):
        self.net = Network()
        self.width = w
        self.height = h
        self.phase = 'roll'
        self.turnplayer = 1
        self.players = {0:["player",vec(50,50)],1:['ai',vec(100,100)],2:['ai',vec(150,150)],3:['ai',vec(200,200)]}

        self.canvas = Canvas(self.width, self.height, "Testing...")

    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.K_ESCAPE:
                    run = False
            #if self.phase == 'roll':
            #    self.masterorder[self.turnplayer] = random.randint(1,6)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                if self.players[int(self.net.id)][1].x <= self.width - 50:
                    self.players[int(self.net.id)][1].x += 2

            if keys[pygame.K_LEFT]:
                if self.players[int(self.net.id)][1].x >= 0:
                    self.players[int(self.net.id)][1].x -= 2

            if keys[pygame.K_UP]:
                if self.players[int(self.net.id)][1].y >= 0:
                    self.players[int(self.net.id)][1].y -= 2

            if keys[pygame.K_DOWN]:
                if self.players[int(self.net.id)][1].y <= self.height - 50:
                    self.players[int(self.net.id)][1].y += 2

            # Send Network Stuff
            self.parse_data(self.send_data())

            # Update Canvas
            self.canvas.draw_background()
            self.canvas.drawplayers()
            self.canvas.draw_grid()
            self.canvas.update()

        pygame.quit()

    def send_data(self):
        """
        Send position to server
        :return: None
        """
        print(self.players)
        data = str(self.net.id) + ":[" + str(self.players[int(self.net.id)][0]) + ',' +str(self.players[int(self.net.id)][1].x) + ',' + str(self.players[int(self.net.id)][1].y) + ']'
        data = data.replace(' ','')
        reply = self.net.send(data)
        return reply

    def parse_data(self,data):
        #try:

            data = data.replace('"','')
            data = data[1:-1]
            data = data.split(', ')
            
            

            
            for x in data:
                print('x',x)
                x = x[1:-1]
                x = x.split(':')
                print(x[1])
                
                ww = x[1]
                ww = ww[1:-1]
                ww = ww.split(',')
                print(ww)
                
                self.players.update({int(x[0]):[ww[0],vec(float(ww[1]),float(ww[2]))]})


        #except:
        #    pass


class Canvas:

    def __init__(self, w, h, name="None"):
        self.width = w
        self.height = h
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption(name)
    def draw_grid(self):
        for x in range(0, self.width, int(self.width/4)):
            pygame.draw.line(self.screen, LIGHTGRAY, (x, 0), (x, self.height))
        for y in range(0, self.height, int(self.height/4)):
            pygame.draw.line(self.screen, LIGHTGRAY, (0, y), (self.width, y))
        pass
    @staticmethod
    def update():
        pygame.display.update()

    def draw_text(self, text, size, x, y):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", size)
        render = font.render(text, 1, (0,0,0))

        self.screen.draw(render, (x,y))

    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill((255,255,255))
    
    def drawplayers(self):
        for x in g.players:
            x = g.players[x]
            pos = x[1]
            pygame.draw.rect(self.screen, RED ,(pos.x, pos.y, 50, 50),0 )

g = Game(500,500)
g.run()


