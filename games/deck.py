import random
import time
def draw(c,d,drawn,hand):
    
    cards = ['c2','d2','h2','s2','c3','d3','h3','s3','c4','d4','h4','s4','c5','d5','h5','s5','c6','d6','h6','s6','c7','d7','h7','s7','c8','d8','h8','s8','c9','d9','h9','s9','ct10','dt10','ht10','st10','cj10','dj10','hj10','sj10','cq10','dq10','hq10','sq10','ck10','dk10','hk10','sk10','ca','da','ha','sa']
    bj_cards = []
    for x in range(4):
      bj_cards += cards
    c = random.choice(bj_cards)
    lop = 1
    while lop > 0:
      if len(drawn) == len(bj_cards):
        time.sleep(1)
        print('Reshuffling')
        time.sleep(1)
        print()
        drawn = []
        lop = 1
      if c in drawn:
        c = random.choice(bj_cards) #satys c to present actual card in game
        lop = 1
      else:
        if 'a' in c:
          drawn.append(c)
          v = 'a'   
        elif '10' in c:
          drawn.append(c)
          v = 10               
        elif '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in c:
          drawn.append(c)
          v = int(c[-1:])       
        lop = 0
    if v == 'a':
      if d > 11:
        v = 1
      else:
        v = 11
        ace = 'a'
        hand.append(ace)
    theo = v + d
    if theo > 21:
      if 'a' in hand:
        v = v - 10
        del hand[0]
    return v, c, hand, drawn