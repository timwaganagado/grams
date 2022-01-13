import random
import pygame
import pygame.freetype
pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill((255,255,255))



TILE_SIZE = 50
NUM_TILES_WIDTH = WIDTH / TILE_SIZE
NUM_TILES_HEIGHT = HEIGHT / TILE_SIZE

d1 = ['c2','d2','h2','s2','c3','d3','h3','s3','c4','d4','h4','s4','c5','d5','h5','s5','c6','d6','h6','s6','c7','d7','h7','s7','c8','d8','h8','s8','c9','d9','h9','s9','ct10','dt10','ht10','st10','cj10','dj10','hj10','sj10','cq10','dq10','hq10','sq10','ck10','dk10','hk10','sk10','ca','da','ha','sa']
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
c=random.choice(d1)
d = c
c=d2.get(c, 'the door remains shut')

white = (255,255,255)

loc = 1
toc = 0
nok = 1
yep = 0

dog = 0

ch = 2
# w = input('theres a door')
#c=d2.get(w, 'the door remains shut')
while ch == 1:
    if w == 'open' or w == 'close':
        ch = 0
    else:
        # w = input("there's still a door")
        c=d2.get(w, 'the door remains shut')

load = pygame.sprite.OrderedUpdates()
loaded = pygame.sprite.Sprite()

def add_load(loaded,loc,toc,nok,yep):
    c=random.choice(d1)
    d = c
    c=d2.get(c, 'break')
    
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
    font.render_to(screen, (200, 40), d, pygame.Color('dodgerblue'))
    return loc, toc, nok, yep

def add_dealer(loaded,loc,toc,nok,yep):
    c=random.choice(d1)
    d = c
    c=d2.get(c, 'break')
    
    loaded.image = pygame.image.load(c)
    loaded.rect = loaded.image.get_rect()
    loaded.rect.left = (1+int(loc) - 1) * TILE_SIZE
    if loc >= 11:
        loaded.rect.top = (200+toc+(nok) * TILE_SIZE)
        loc = 1
        toc = toc + 1
        nok = nok + 1
      
    else:
        loaded.rect.top = (200+toc+(nok) * TILE_SIZE)
        loc = loc+1
    load.add(loaded)
    pygame.draw.rect(screen,(white),(190,10,100,40))
    font.render_to(screen, (200, 40), d, pygame.Color('dodgerblue'))
    return loc,toc,nok,yep

font=pygame.freetype.SysFont(None, 34)
font.origin=True


c=random.choice(d1)
c=d2.get(c, 'the door remains shut')
    
loaded.image = pygame.image.load(c)
loaded.rect = loaded.image.get_rect()
loaded.rect.left =  (1+loc - 1) * TILE_SIZE
loaded.rect.top = 1 * TILE_SIZE + 1
load.add(loaded)
loc = loc + 1

#pygame.time.set_timer(pygame.USEREVENT, 1000)

w = 0

finish = False
win = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
        if dog == 0:
            
            load.draw(screen) 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                loc,toc,nok,yep = add_load(loaded,loc,toc,nok,yep)
                dog = 0
            if event.key == pygame.K_s:
                #screen.fill((255,255,255))
                if w == 0:
                    w = 1
                    loc = 1
                toc = 0
                dog = 0
                nok = 1
                loc,toc,nok,yep = add_dealer(loaded,loc,toc,nok,yep)
                



        #if event.type == pygame.USEREVENT:
           # if win == False:
                #loc,toc = add_load(loaded,loc,toc)
        
        pygame.display.update()
    
pygame.quit()