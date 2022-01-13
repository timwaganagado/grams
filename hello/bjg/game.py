import pygame
import random
import pygame.freetype
import time
from deck import draw
import shelve
pygame.init()


WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill((255,255,255))

font=pygame.freetype.SysFont(None, 34)
font.origin=True

cont = 1
d = shelve.open('score.txt')
highscorel = d['highscorel']
d.close()

finish = False
win = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
        
        
        
        skip = 0
        loop = 1
        drawn = []
        bet = 50
        d = ('Highscore' , highscorel)
        font.render_to(screen, (200, 40), str(d), pygame.Color('dodgerblue'))
        font.render_to(screen, (200, 40), 'amount to bet 50', pygame.Color('dodgerblue'))
        while loop > 0:
            
            cv = 0   #card value
            w = ''
            won = ''
        if skip == 0:
            betting = True
            font = pygame.font.Font(None, 32)
            input_box = pygame.Rect(100, 100, 140, 32)
            color_inactive = pygame.Color('lightskyblue3')
            color_active = pygame.Color('dodgerblue2')
            color = color_inactive
            active = False
            text = ''
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
                        print(text)
                        text = ''
                        betting = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            if betable == '':
                betable = int(bet/2)
            elif betable.isdigit:
                betable = int(betable)
            else:
                betable = int(bet/2)
        else:
            skip = 0
        
        while betable > bet:
            betable = input('how much do you want to bet? ')
            if betable == '':
                betable = int(bet/2)
            elif betable.isdigit:
                betable = int(betable)
            else:
                betable = int(bet/2)
        if betable == 0:
            betable = 1
    
        print()
        print(f'betting {betable}')
        print()
        time.sleep(1)
        dd = 0 #how many cards the dealer has drawn
        ht = 0  #the total value of the drawn hand
        dh = ''  #the actual card e.g a,hq10,s6
        hhand = []
        comd = []
        sv = 0
        while dd < 1: #does the loop twice to draw two cards
            cv,dh,hhand,drawn = draw(dh,ht,drawn,hhand) #function to draw cards
            comd.append(dh)
            sv = cv
            dd = dd + 1   #adds to cards drawn
        print(f'Dealers card {comd}')
        print(f'Dealers total {cv}')
        print()
        hh = ''
        comh = comd
        while dd == 1:
            cv,hh,hhand,drawn = draw(hh,ht,drawn,hhand)
            ht = ht + cv + sv
            comh.append(hh)
            dd = dd + 1
            if ht >= 22:
                ht = ht - 10
        time.sleep(1)
        pd = 0
        pt = 0
        ph = ''
        comp = []
        phand = []
        while pd < 2:
            cv,ph,phand,drawn = draw(ph,pt,drawn,phand)
            pt = pt + cv
            comp.append(ph)
            pd = pd + 1
        print(f'Player cards {comp}')
        print(f'Player total {pt}')
        time.sleep(1)
        if ht != 21:
            if pt != 21:
                if loop == 1:
                    hit = input('Hit or Stand (enter key to hit/s key + enter to stand) ')
                    print()
                elif loop == 2:
                    hit = input('Hit or Stand ')
                    print()
                while hit != 's':
                    cv,ph,phand,drawn = draw(ph,pt,drawn,phand)
                    pt = pt + cv
                    comp.append(ph)
                    print(f'Player cards {comp}')
                    print(f'Player total {pt}')
                    time.sleep(1)
                    if pt == 21:
                        hit = 's'
                        print()
                    elif pt < 22:   
                        hit = input('Hit or Stand ')
                        print()
                    else:
                        hit = 's'
                        print('Player Bust')
                        won = 'The Dealer wins'
                    print()
                    time.sleep(1)
            else:
                print('A natural')
                print()
        else:
            print()

        print(f'Dealers hand {comh}')
        print(f'Dealers total {ht}')
        print()
        time.sleep(1)
        if pt == 21 and len(comp) == 2:
            w = '' 
        else:
            if pt < 22:
                while ht < 17:
                    cv,hh,hhand,drawn = draw(hh,ht,drawn,hhand)
                    ht = ht + cv
                    comh.append(hh)
                    print(comh)
                    print(f'Dealers total {ht}')
                    print()
                    time.sleep(1)
                if ht > 21:
                    w = 'dealer'
                    print('Dealer Busted')
                    won = 'The Player won'
                    print()
            else:
                w = 'dealer'
                won = 'The Dealer wins'

        if w != 'dealer':
            if pt == 21 and len(comp) == 2:
                if ht == 21 and len(comh) == 2:
                    won = 'Tie'
                else:
                    won = 'The Player wins'
            elif ht == 21 and len(comh) == 2:
                won = 'The Dealer wins'
            else:
                if pt == ht:
                    won = 'Tie'
                elif 21 >= pt > ht:
                    won = 'The Player won'
                elif 21 >= ht > pt:
                    won = 'The Dealer won' 
                elif ht == 21:
                    won = 'The Dealer wins'
        print(f'{won}, Dealer got {ht} Player got {pt}')
        print()
        if 'Player' in won and pt == 21 and len(comp) == 2:
            bet = bet + betable*2
        elif 'Dealer' in won and ht == 21 and len(comh) == 2:
            bet = bet - betable*2
        elif 'Player' in won:
            bet = bet + betable
        elif 'Dealer' in won:
            bet = bet - betable
        else:
            bet = bet
        print(bet)
        print()
    
        time.sleep(1)
        highscore = bet
        highscorel = highscore
        d = shelve.open('score.txt')
        highscorel = d['highscorel']
        d.close()
        if highscore > highscorel:   
            highscorel = highscore
            d = shelve.open('score.txt')
            d['highscorel'] = highscorel
            d.close()
            print('new highscore',highscorel)
            print()
        replay = 'n'
        if loop == 1 and bet > 0:
            replay = input('Do you want to play again?(enter to replay/n to stop) ')
        elif loop == 2 and bet > 0:
            replay = input('Do you want to play again? ')
        print()
    
        if replay.isdigit():
            betable = int(replay)
            skip = 1
        loop = 2
        if bet <= 0:
            replay = 'n'
        elif bet >= 1000:
            replay = 'n'
        if 'n' in replay:
            loop = 0
    print('Come again soon')
    print('highscore',highscorel)
    if bet <= 0:
        print('You no longer have anything to bet')
    elif bet >= 1000:
        print('You have earned to much')


    c = input('would you like to play again? ')
    if 'n' in c:
        cont = 2
    elif 'd' in c:
        debuging = 1
        while debuging == 1:  
            debug = input('debug')
            if 'h' in debug:
                highscorel = 0
                d = shelve.open('score.txt')
                d['highscorel'] = highscorel
                d.close()
                print('hs reset',highscorel)
            if 'r' in debug:
                drawn = [] 
                print('Cards reshuffled',drawn)
            if 'n' in debug:
                debuging = 0
            debug = input('debug')
    elif '' in c:
        cont = 1
    if betting == True:
         # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
pygame.quit()