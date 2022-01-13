import random
from fractions import Fraction
def re():
  p = print('Another hand')
times = int(input('how many times would you like to run this? '))
see = ''
if times <= 20:
  see = input('would you like to see the card values as well? ')
n = 0
t = 0
w = 0
a = 0
aw = 0
lop = 1
hand = []
bj_cards = ['c2','d2','h2','s2','c3','d3','h3','s3','c4','d4','h4','s4','c5','d5','h5','s5','c6','d6','h6','s6','c7','d7','h7','s7','c8','d8','h8','s8','c9','d9','h9','s9','ct10','dt10','ht10','st10','cj10','dj10','hj10','sj10','cq10','dq10','hq10','sq10','ck10','dk10','hk10','sk10','ca','da','ha','sa']
drawn = []
while t < times:
  while n < 21:
    c = random.choice(bj_cards)
    lop = 1
    while lop > 0:
      if len(drawn) == len(bj_cards):
        drawn = []
        lop = 1
      if c in drawn:
        c = random.choice(bj_cards)
        lop = 1
      else:
        if 'a' in c:
          drawn.append(c)
          c = 'a'   
        elif '10' in c:
          drawn.append(c)
          c = 10               
        elif '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in c:
          drawn.append(c)
          c = int(c[-1:])       
        lop = 0
    if c == 'a':
      a = 1
      if n > 11:
        c = 1
      else:
        c = 11
        ace = 'a'
        hand.append(ace)
    if 'y' in see:
      print(f'{n}+{c}')
    n = n + c
    if 'y' in see:  
      print(n)
  if n == 21:
    w = w + 1
    n = 0
    t = t + 1
    hand = []
    if 'y' in see:
      re()
    if a == 1:
      aw = aw + 1
      a = 0
  
    else:
      n = 0
      a = 0
      t = t + 1
      if 'y' in see:
        re()
print(f'Out of {times} attempts you got black jack {w} time/s')
if aw > 0:
  print(f'and you won {aw} game/s with an ace')
f = Fraction(w,times)
print(f'''In a fraction thats {f}
those arent very good odds''')