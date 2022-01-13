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
bj_cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,'a','a','a','a']
while t < times:
  while n < 21:
    c = random.choice(bj_cards)
    if c == 'a':
      a = 1
      if n > 11:
        c = 1
      else:
        c = 11
    if 'y' in see:
      print(f'{n}+{c}')
    n = n + c
    if 'y' in see:  
      print(n)
  if n == 21:
    w = w + 1
    n = 0
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