import pygame
import random
import pygame.freetype
import shelve
import time
from deck import draw
pygame.init()


WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill((255,255,255))
white = (255,255,255)

TILE_SIZE = 50
NUM_TILES_WIDTH = WIDTH / TILE_SIZE
NUM_TILES_HEIGHT = HEIGHT / TILE_SIZE

d2 = {'c2':'grams/l0_card41.png','d2':'grams/l0_card15.png','h2':'grams/l0_card02.png','s2':'grams/l0_card28.png',
      'c3':'grams/l0_card42.png','d3':'grams/l0_card16.png','h3':'grams/l0_card03.png','s3':'grams/l0_card29.png',
      'c4':'grams/l0_card43.png','d4':'grams/l0_card17.png','h4':'grams/l0_card04.png','s4':'grams/l0_card30.png',
      'c5':'grams/l0_card44.png','d5':'grams/l0_card18.png','h5':'grams/l0_card05.png','s5':'grams/l0_card31.png',
      'c6':'grams/l0_card45.png','d6':'grams/l0_card19.png','h6':'grams/l0_card06.png','s6':'grams/l0_card32.png',
      'c7':'grams/l0_card46.png','d7':'grams/l0_card20.png','h7':'grams/l0_card07.png','s7':'grams/l0_card33.png',
      'c8':'grams/l0_card47.png','d8':'grams/l0_card21.png','h8':'grams/l0_card08.png','s8':'grams/l0_card34.png',
      'c9':'grams/l0_card48.png','d9':'grams/l0_card22.png','h9':'grams/l0_card09.png','s9':'grams/l0_card35.png',
      'ct10':'grams/l0_card49.png','dt10':'grams/l0_card23.png','ht10':'grams/l0_card10.png','st10':'grams/l0_card36.png',
      'cj10':'grams/l0_card50.png','dj10':'grams/l0_card24.png','hj10':'grams/l0_card11.png','sj10':'grams/l0_card37.png',
      'cq10':'grams/l0_card51.png','dq10':'grams/l0_card25.png','hq10':'grams/l0_card12.png','sq10':'grams/l0_card38.png',
      'ck10':'grams/l0_card52.png','dk10':'grams/l0_card26.png','hk10':'grams/l0_card13.png','sk10':'grams/l0_card39.png',
      'ca':'grams/l0_card40.png','da':'grams/l0_card14.png','ha':'grams/l0_card01.png','sa':'grams/l0_card27.png'}

pont=pygame.freetype.SysFont(None, 34)
pont.origin=True

load = pygame.sprite.OrderedUpdates()
loaded = pygame.sprite.Sprite()

def add_load(loaded,loc,toc,nok,yep,dh):
    c=dh
    d = c
    c=d2.get(c, 'the door remains shut')
    
    
    loaded.image = pygame.image.load(c)
    loaded.rect = loaded.image.get_rect()
    loaded.rect.left = (1+int(loc) - 1) * TILE_SIZE
    if loc >= 11:
        loaded.rect.top = (1+toc+(nok) * TILE_SIZE)
        loc = 1
        toc = toc + 1
        nok = nok + 1
    
    else:
        loaded.rect.top = (1+toc+(nok) * TILE_SIZE)
        loc = loc+1
    load.add(loaded)
    pygame.draw.rect(screen,(white),(190,10,100,40))
    print(d)
    return loc, toc, nok, yep


cont = 1
d = shelve.open('score.txt')
highscorel = d['highscorel']
d.close()

loc = 1
toc = 0
nok = 1
yep = 0

input_box = pygame.Rect(100, 100, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
betable = ''

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
    
    
        skip = 0
        loop = 1
        drawn = []
        bet = 50
        
        if cont == 1:
            d = (f'Highscore {highscorel}')

            pont.render_to(screen, (100, 40), str(d), pygame.Color('dodgerblue'))
            pont.render_to(screen, (100, 80), 'Amount to bet 50', pygame.Color('dodgerblue'))
            cv = 0   #card value
            w = ''
            won = ''
            if skip == 0:
                betting = True
                pain = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(betable)
                            pain = True
                        elif event.key == pygame.K_BACKSPACE:
                            betable = betable[:-1]
                        else:
                            betable += event.unicode
                if pain == True:
                    
                    if betable == '':
                        bett = int(bet/2)
                    elif betable.isdigit:
                        bett = int(betable)
                    else:
                        bett = int(bet/2)
                    betable = ''
                    pain = False
                    screen.fill((255,255,255))
                    pont.render_to(screen, (100, 120), (f'betting {betable}'), pygame.Color('dodgerblue'))
                    
                    pygame.time.wait(1)
                    betting = False
                    cont = 2
            else:
                skip = 0
        elif cont == 2:
            screen.fill((255,255,255))
            dd = 0 #how many cards the dealer has drawn
            ht = 0  #the total value of the drawn hand
            dh = ''  #the actual card e.g a,hq10,s6
            hhand = []
            
            sv = 0
            if dd < 1: #does the loop twice to draw two cards
                cv,dh,hhand,drawn = draw(dh,ht,drawn,hhand) #function to draw cards
                
                
                dd = dd + 1   #adds to cards drawn
                loc,toc,nok,yep = add_load(loaded,loc,toc,nok,yep,dh)
                load.draw(screen)
            pont.render_to(screen, (100, 120), (f'Dealers total {cv}'), pygame.Color('dodgerblue'))
            hh = ''
            pygame.time.wait(1)
            if dd == 1:
                cv,hh,hhand,drawn = draw(hh,ht,drawn,hhand)
                ht = ht + cv + sv
                
                dd = dd + 1
                cont = 3
                if ht == 22:
                    ht = ht - 10
        pygame.display.update()
 

    if betting == True:
        
        font = pygame.font.Font(None, 32)
         # Render the current text.
        txt_surface = font.render(str(betable), True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box,2)
        pygame.display.flip()
        if pain == True:
            betting = False

    
pygame.quit()