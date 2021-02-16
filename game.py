import pygame
import random
import pygame.freetype
pygame.init()
clock = pygame.time.Clock()

save = 0
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))

hero = pygame.sprite.Sprite()

hero.image = pygame.image.load('grams/hero.png')
hero.rect = hero.image.get_rect()

TILE_SIZE = hero.rect.width
NUM_TILES_WIDTH = WIDTH / TILE_SIZE
NUM_TILES_HEIGHT = HEIGHT / TILE_SIZE


hero_group = pygame.sprite.GroupSingle(hero)

candies = pygame.sprite.OrderedUpdates()

rare = pygame.sprite.OrderedUpdates()

class Mysprite(pygame.sprite.Sprite):
    def __int__(self):
        super(Mysprite, self).__int__()
        self.images = []
        self.images.append(pygame.image.load('grams/circle-1.png.png'))
        self.images.append(pygame.image.load('grams/cross-1.png.png'))
        
        self.index = 0
        
        self.image = self.images[self.index]
        
        self.rect = pygame.rect(5,5,50,50)
    
    def update(self):
        self.index += 1
        
        if self.index >=len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]

def add_candy(candies):
    candy = pygame.sprite.Sprite()
    candy.image = pygame.image.load('grams/candy.png')
    candy.rect = candy.image.get_rect()
    candy.rect.left = random.randint(0, int(NUM_TILES_WIDTH) - 1) *     TILE_SIZE
    candy.rect.top = random.randint(0, int(NUM_TILES_HEIGHT) - 1) * TILE_SIZE
    candies.add(candy)


clock=pygame.time.Clock()
font=pygame.freetype.SysFont(None, 34)
font.origin=True

rarecandy = pygame.sprite.Sprite()
rarecandy.image = pygame.image.load('grams/New Piskel-1.png.png')
rarecandy.rect = rarecandy.image.get_rect()
rarecandy.rect.left = 1 *     TILE_SIZE
rarecandy.rect.top = 1 * TILE_SIZE

rare.add(rarecandy)

for i in range(10):
    add_candy(candies)

pygame.time.set_timer(pygame.USEREVENT, 3000)

finish = False
win = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
        if event.type == pygame.KEYDOWN:
            screen.fill((0, 0, 0))
        # Move the hero around the screen
            if event.key == pygame.K_UP:
                hero.rect.top -= TILE_SIZE
            elif event.key == pygame.K_DOWN:
                hero.rect.top += TILE_SIZE
            elif event.key == pygame.K_RIGHT:
                hero.rect.right += TILE_SIZE
            elif event.key == pygame.K_LEFT:
                hero.rect.right -= TILE_SIZE
        if event.type == pygame.USEREVENT:
            if win == False:
                add_candy(candies)
        
        
        pygame.sprite.groupcollide(hero_group, candies, False, True)
        pygame.sprite.groupcollide(hero_group, rare, False, True)
        if len(candies) == 0 and len(rare) == 0:
            win = True
        screen.fill((0,0,0))
        candies.draw(screen)
        hero_group.draw(screen)
        rare.draw(screen)
        hero.update()
        if win:
            font = pygame.font.Font(None, 36)
            text_image = font.render("You Win!", True, (255, 255, 255))
            text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100)
            screen.blit(text_image, text_rect)
        
        pygame.display.update()
    pygame.draw.rect(screen,(0,0,0),(470,0,200,50))
    if win != True:
        

        font=pygame.freetype.SysFont(None, 34)
        font.origin=True    
   
        ticks=pygame.time.get_ticks()
        millis=ticks%1000
        seconds=int(ticks/1000 % 60)
        minutes=int(ticks/60000 % 24)
        out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
        font.render_to(screen, (470, 40), out, pygame.Color('dodgerblue'))
        pygame.display.flip()
        clock.tick(30)
    elif win == True:
        if save != 1:
            fin = pygame.time.get_ticks()
            millis=fin%1000
            seconds=int(fin/1000 % 60)
            minutes=int(fin/60000 % 24)
            pri='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
            save = 1

        font=pygame.freetype.SysFont(None, 34)
        font.origin=True    
        font.render_to(screen, (470, 40), pri, pygame.Color('dodgerblue'))
pygame.quit()


