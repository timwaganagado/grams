#print(51 // 25)

#ages = [5, 12, 17, 18, 24, 32]

#def myFunc(x):
#  if x < 18:
#    return False
#  else:
#    return True
#
#adults = filter(myFunc, ages)
#
#
#
#for x in adults:
#  print(x)
#from collections import deque
#
#m = deque()
#
#for i in range(10):
#    m.append(i)
#
#for i in range(2):
#    print(m)
#    
#    d = m.popleft()
#    
#    print(d)
#    
#for i in range(10,20):
#    m.append(i)
#
#print(m)
#
#m = deque()
#print(m)
import pygame as pg
import random
#vec = pg.math.Vector2
#
#start = vec(2, 2)
#hidden = []
#print(start)
#
#def vec2int(v):
#    return (int(v.x), int(v.y))
#
#check = [vec(0,1),vec(1,0),vec(0,-1),vec(-1,0)]


#for thing in check:
 #   checked = start + thing
  #  print(checked)
   # hidden.append(vec2int(checked))
    
#print(hidden)

#hidden = [start + thing for thing in check]
#
#hidden2 = [(int(loc.x),int(loc.y)) for loc in hidden]
#
#hidden3  = [hidden3 + check for check in check for hidden3 in hidden2]
#
#while start in hidden3:
#      hidden3.remove(start)
#for x in hidden3:
#      hidden3.remove(x)
#      while x in hidden3:
#        hidden3.remove(x)
#      hidden3.append(x)
#hidden3 += hidden
#hidden4 = [(int(loc.x),int(loc.y)) for loc in hidden3]
#
#print(hidden4)
#
#for x in hidden4:
#      hidden4.remove(x)
#      while x in hidden4:
#        hidden4.remove(x)
#      hidden4.append(x)
#            
#print(hidden2)
#print(hidden4)
#
#print(len(hidden4))
#print(vec(3,3) in hidden4)
#print(vec(20,1) in hidden)
#
#some = [vec(i,1) for i in range(5)]
#some2 = [(int(loc.x),int(loc.y)) for loc in some]
#some3 = some2
#v = [vec(3,1),vec(4,1)]

#print(some)

#print(some2)
#print((1,2) == (1,2))
#for c in some:
  #  if c in v:
 #       some2.remove(c)
        
#print(some2)

#def myFunc(x):
 # if x in v:
  #  return False
  #else:
   # return True

#some3d = filter(myFunc,some3)
#print(list(some3d))

#adults = filter(myFunc, ages)



#for x in adults:
 # print(x)
 
#ng = ((random.randint(0,27),random.randint(0,14)))
#print(ng)

#li = ['pog','log']
#il = list(li) 
#print(il)
#li.append('nog')
#
#
#print(li)
#print(il)
#pg.init()
#WIDTH = 60
#HEIGHT = 60
#screen = pg.display.set_mode((WIDTH, HEIGHT))
pp = ['l','e','w']
p = {'l':'t','e':'t','w':'92'}
print(p)
for w in pp:
    print(p[w])
    print(w)
#pg.time.set_timer(pg.USEREVENT, 50)
#running = True
#while running:
#    
#    for event in pg.event.get():
#        
#        if event.type == pg.QUIT:
#            running = False
#        if event.type == pg.USEREVENT:
#            if event.type == pg.KEYDOWN:
#                  if event.key == pg.K_w:
#                      print('a')
