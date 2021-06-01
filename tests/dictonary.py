import random

from pygame import Vector2
vec = Vector2
#l = {'connected':True,'conncode':0,'lsit':[1,'gay',True]}
#
#l.update({'lost':True})
#
#for w in l:
#    print(l[w])

#d = {'p1':[5,3,(1,2)],'p2':[2,5,(1,0)],'p3':[4,1,(2,2)]}
#sortedd = {k:v for k, v in sorted(d.items(), key = lambda t:t[1][1])}
#
#print(sortedd)
#for he in sortedd:
#    print(he)
#    print(d[he][0])
#
#d = random.choice(sortedd)
#x = 0
#y=0
#z=0
#xyz = {x:5,y:0,z:0}
#print(xyz[x])



dad = 'dad'
mom = 'mom'
sis = 'sis'
bro = 'bro'
friend = 'friend'
l = {dad:vec(22,33),mom:['2',2],sis:['3',1],bro:['4',0],friend:['5',-1]}
move = 99
while move:
    move = input()
    if move in l:
        new = input()
        newl = {}
        save = {}
        for x in l:
            save.update({x:l[x]})
        for x in l:
            newl.update({x:x})
        newl[move] = new
        newl[new] = move
        print(save)
        l = {value:key for key, value in newl.items()}
        for x in save:
            l[x] = save[x]
        print(l)