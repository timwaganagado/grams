from re import A
import pygame as pg
from os import path
from collections import deque
import random
import shelve
import os , sys
import math
vec = pg.math.Vector2

TILESIZE = 30
GRIDWIDTH = 9
GRIDHEIGHT = 9
WIDTH = 1000
HEIGHT = 1000
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
def draw_text(text, size, color, x, y, x_bound, align="topleft"):
    current_text = ''
    space_text = ''
    font = pg.font.Font(font_name, size)
    ty = y
    box_size = 1 
    for qq in text:
        space_text += qq
        text_surface = font.render(current_text + space_text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
        if text_rect[0]+text_rect[2] > x_bound + x:
            
            text_surface = font.render(current_text , True, color)
            text_rect = text_surface.get_rect(**{align: (x, y)})
            ty += text_rect[3]
            current_text = ''
            current_text += space_text
            space_text = ''
            box_size += 1
        elif qq == ' ':
            current_text += space_text
            space_text = ''
    box_size +=1
    #if text == '':
    #    text_rect = [0,0,0,50]
    rect = pg.Rect(x,y, x_bound, text_rect[3]*box_size)
    global textboxrect
    textboxrect = pg.Rect(x,y, x_bound, text_rect[3]*box_size)
    pg.draw.rect(screen,GREEN,rect)
    
    current_text = ''
    space_text = ''
    for qq in text:
        space_text += qq
        text_surface = font.render(current_text + space_text, True, color)
        
        text_rect = text_surface.get_rect(**{align: (x, y)})
        if text_rect[0]+text_rect[2] > x_bound + x:
            text_surface = font.render(current_text , True, color)
            text_rect = text_surface.get_rect(**{align: (x+10, y)})
            screen.blit(text_surface, text_rect)
            y += text_rect[3]
            current_text = ''
            current_text += space_text
            space_text = ''

        elif qq == ' ':
            current_text += space_text
            space_text = ''
        
    current_text += space_text
    text_surface = font.render(current_text, True, color)
    text_rect = text_surface.get_rect(**{align: (x+10, y)})
    screen.blit(text_surface, text_rect)
     

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

tick_time = pg.time.get_ticks()

first = (36, 117) 
second = 410

textboxrect = 0
active = False
text = 'Enter text while switching between different keyboard layouts and Input Method Editors (IMEs). Verify the ability of the application to accept input from various input methods, regardless of other locale settings. Either check that multilingual input is enabled with all supported input methods or that it is blocked for all languages except supported ones.'

pause = False

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get(): # to find what this does print: event
        # write important things here 
        # duh
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit
            if event.key == pg.K_SPACE:
                if pause:
                    pause = False
                else:
                    pause = True
            if active:
                if event.key == pg.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        if event.type == pg.MOUSEBUTTONDOWN:
            mpos = pg.mouse.get_pos()
            if textboxrect.collidepoint(mpos):
                active = True
            if event.button == 1:
                first = mpos
            if event.button == 3:
                second = mpos[0]
            print(first,second)
        elif event.type == pg.MOUSEWHEEL:
            print(event)
            print(event.x, event.y)
            print(event.flipped)
            print(event.which)
            first = (first[0],first[1] + 10*event.y)

            # can access properties with
            # proper notation(ex: event.y)    
        if event.type == pg.QUIT: # allows for quit when clicking on the X 
            running = False
            pg.quit() 
    
    current_time = pg.time.get_ticks()
    if pause:
        tick_time = current_time
    if current_time - tick_time > 200:
        tick_time = pg.time.get_ticks()
        second += 5
    pg.display.set_caption("{:.2f}".format(clock.get_fps())) # changes the name of the application
    screen.fill(WHITE) # fills screnn with color
    # anything down here will be displayed ontop of anything above
    if second != 0 and first != 0:
        draw_text(str(text),50,(0,0,0),WIDTH/2,HEIGHT/2,second,'center')
    
    pg.display.flip() # dose the changes goto doccumentation for other ways