import pygame
pygame.init()

TILE_SIZE = 50

save = 0
WIDTH = 650
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))

rem = pygame.sprite.Group.empty

NUM_TILES_WIDTH = WIDTH / TILE_SIZE
NUM_TILES_HEIGHT = HEIGHT / TILE_SIZE

hero = pygame.sprite.Sprite()

hero_group = pygame.sprite.GroupSingle(hero)

walls = pygame.sprite.OrderedUpdates()

doors = pygame.sprite.OrderedUpdates()

keys = pygame.sprite.OrderedUpdates()

hero.image = pygame.image.load('grams/hero.png')
hero.rect = hero.image.get_rect()

def ne_wall(v_pos,pos):
    if v_pos > 0:
        pos = pos - 13 * v_pos 
    ne_wall = pygame.sprite.Sprite()
    ne_wall.image = pygame.image.load('grams/l0_wall_2.png')
    ne_wall.rect = ne_wall.image.get_rect()
    ne_wall.rect.left = int(pos) *     TILE_SIZE
    ne_wall.rect.top = int(v_pos) * TILE_SIZE
    walls.add(ne_wall)
    
    
def se_wall(v_pos,pos):
    if v_pos > 0:
        pos = pos - 13 * v_pos 
    se_wall = pygame.sprite.Sprite()
    se_wall.image = pygame.image.load('grams/l0_wall_3.png')
    se_wall.rect = se_wall.image.get_rect()
    se_wall.rect.left = int(pos) *     TILE_SIZE
    se_wall.rect.top = int(v_pos) * TILE_SIZE
    walls.add(se_wall)
    

def sw_wall(v_pos,pos): 
    if v_pos > 0:
        pos = pos - 13 * v_pos   
    sw_wall = pygame.sprite.Sprite()
    sw_wall.image = pygame.image.load('grams/l0_wall_4.png')
    sw_wall.rect = sw_wall.image.get_rect()
    sw_wall.rect.left = int(pos) *     TILE_SIZE
    sw_wall.rect.top = int(v_pos) * TILE_SIZE
    walls.add(sw_wall)
    

def nw_wall(v_pos,pos):
    if v_pos > 0:
        pos = pos - 13 * v_pos
    nw_wall = pygame.sprite.Sprite()
    nw_wall.image = pygame.image.load('grams/l0_wall_1.png')
    nw_wall.rect = nw_wall.image.get_rect()
    nw_wall.rect.left = int(pos) *     TILE_SIZE
    nw_wall.rect.top = int(v_pos) * TILE_SIZE
    walls.add(nw_wall)
    
    
def v_wall(v_pos,pos):    
    if v_pos > 0:
        pos = pos = pos - 13 * v_pos
    v_wall = pygame.sprite.Sprite()
    v_wall.image = pygame.image.load('grams/l0_wall_5.png')
    v_wall.rect = v_wall.image.get_rect()
    v_wall.rect.left = int(pos) *     TILE_SIZE
    v_wall.rect.top = int(v_pos) * TILE_SIZE
    walls.add(v_wall)
    #print(pos)
    
    
def h_wall(v_pos,pos):
    if v_pos > 0:
        pos = pos - 13 * v_pos
    h_wall = pygame.sprite.Sprite()
    h_wall.image = pygame.image.load('grams/l0_wall_6.png')
    h_wall.rect = h_wall.image.get_rect()
    h_wall.rect.left = int(pos) *     TILE_SIZE
    h_wall.rect.top = int(v_pos) * TILE_SIZE
    walls.add(h_wall)
    print(pos)
    
def door(v_pos,pos):
    if v_pos > 0:
        pos = pos - 13 * v_pos
    door = pygame.sprite.Sprite()
    door.image = pygame.image.load('grams/door-1.png.png')
    door.rect = door.image.get_rect()
    door.rect.left = int(pos) *     TILE_SIZE
    door.rect.top = int(v_pos) * TILE_SIZE
    doors.add(door)


def key(v_pos,pos):
    if v_pos > 0:
        pos = pos - 13 * v_pos
    key = pygame.sprite.Sprite()
    key.image = pygame.image.load('grams/key-1.png.png')
    key.rect = key.image.get_rect()
    key.rect.left = int(pos) *     TILE_SIZE
    key.rect.top = int(v_pos) * TILE_SIZE
    keys.add(key)

pos = 0
v_pos = 0
level1_vwall = [1,4,6,19,21,28,32,34,44,45,52,58,62,71,80,82,84,86,92,93,99,101,108,112,114,123,125,127]
level1_hwall = [23,24,25,42,48,66,74,96]
level1_newall = [14,41,47,57,65,105]
level1_sewall = [73,95]
level1_swwall = [15,39,49,67]
level1_nwwall = [75,97,106]
level1_door = [126]
level1_keys = [2,79,12]

def level_1(v_pos,pos):
    while pos <= 128:
        if pos == 13 or pos == 26 or pos == 39 or pos == 52 or pos == 65 or pos == 78 or pos == 91 or pos == 104 or pos == 117 :
             v_pos = v_pos + 1
        if pos in level1_vwall: # up wall
            v_wall(v_pos,pos)
        elif pos in level1_hwall: # flat wall
            h_wall(v_pos,pos)
        elif pos in level1_newall : # ne wall
            ne_wall(v_pos,pos)
        elif pos in level1_sewall: # se wall
            se_wall(v_pos,pos)
        elif pos in level1_swwall: # sw wall
            sw_wall(v_pos,pos)
        elif pos in level1_nwwall : # nw wall
            nw_wall(v_pos,pos)
        elif pos in level1_door:
            door(v_pos,pos)
        elif pos in level1_keys:
            key(v_pos,pos)
        pos += 1
        #print(pos)
        
level2_vwall =[1,5,10,12,14,16,18,23,25,27,29 ,31,33,40,44,46,48,50,53,55,57,59,68,70,72 ,75,88,92,94,105]
level2_hwall = [21,78,82,100,103,108,110,111,112,113,114]
level2_newall = [61,85,99,107]
level2_sewall =[20,81,102]
level2_swwall = [62,86,79]
level2_nwwall = [63,76,83,101,115]
level2_door = [116]
level2_keys = [69,87,89]
        
def level_2(v_pos,pos):
    while pos <= 128:
        # checks vertical position so walls arent placed off screen
        if pos == 13 or pos == 26 or pos == 38 or pos == 51 or pos == 64 or pos == 77 or pos == 90 or pos == 104 or pos == 117 :
             v_pos = v_pos + 1
             
        if pos in level2_vwall: # up wall
            v_wall(v_pos,pos)
        elif pos in level2_hwall: # flat wall
            h_wall(v_pos,pos)
        elif pos in level2_newall: # ne wall
            ne_wall(v_pos,pos)
        elif pos in level2_sewall: # se wall
            se_wall(v_pos,pos)
        elif pos in level2_swwall: # sw wall
            sw_wall(v_pos,pos)
        elif pos in level2_nwwall: # nw wall
            nw_wall(v_pos,pos)
        elif pos in level2_door:
            door(v_pos,pos)
        elif pos in level2_keys:
            key(v_pos,pos)
        pos += 1

def v_cords():
    if cur_v == 0:
         v_can = [0,1,2,3,4,5,6,7,8,9,10,11,12]

#def enemy():
    

finish = False
win = False
level = 1
level_com = 1
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
        if level == 1 and level_com == 1:
            level_1(v_pos,pos)
            level_com = 2
        elif level == 2 and level_com == 2:
            pos = 0
            v_pos = 0
            level_2(v_pos,pos)    
            level_com = 3
        
        hero_pos_t = hero.rect.top
        hero_pos_r = hero.rect.right
        
        if event.type == pygame.KEYDOWN:
            screen.fill((0, 0, 0))
        # Move the hero around the screen
            if event.key == pygame.K_UP:
                hero.rect.top -= TILE_SIZE
                if pygame.sprite.spritecollideany(hero,walls):
                    hero.rect.top = hero_pos_t
            elif event.key == pygame.K_DOWN:
                hero.rect.top += TILE_SIZE
                if pygame.sprite.spritecollideany(hero,walls):
                    hero.rect.top = hero_pos_t
            elif event.key == pygame.K_RIGHT:
                hero.rect.right += TILE_SIZE
                if pygame.sprite.spritecollideany(hero,walls):
                    hero.rect.right = hero_pos_r
            elif event.key == pygame.K_LEFT:
                hero.rect.right -= TILE_SIZE
                if pygame.sprite.spritecollideany(hero,walls):
                    hero.rect.right = hero_pos_r
        
        pygame.sprite.groupcollide(hero_group, keys, False, True)
        
        if pygame.sprite.spritecollideany(hero,doors):   
            if len(keys) == 0:
                win = True
            else:
                hero.rect.top = hero_pos_t
                hero.rect.right = hero_pos_r
         
        
        
        if win == True:
            font = pygame.font.Font(None, 36)
            text_image = font.render("Level Complete", True, (255, 255, 255))
            text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100)
            screen.blit(text_image, text_rect)      
            
            rem(walls)
            rem(doors)
            
            hero.rect.top = 0
            hero.rect.right = 50
            level += 1
            win = False
        hero_group.draw(screen)
    walls.draw(screen)
    doors.draw(screen)
    keys.draw(screen)
    pygame.display.update()
pygame.quit()