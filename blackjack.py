import shelve
cont = 1
#d = shelve.open('score.txt')
#highscorel = d['highscorel']
#d.close()
#pp cool will see what happens
while cont == 1:
   skip = 0
   loop = 1
   drawn = []
   bet = 50
   #print('Highscore',highscorel)
   print('Amount to bet 50')
   while loop > 0:
      import time
      from deck import draw
      cv = 0   #card value
      w = ''
      won = ''

      if skip == 0:
         betable = input('how much do you want to bet? ')
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
          print()
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