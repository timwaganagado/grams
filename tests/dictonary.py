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



#dad = 'dad'
#mom = 'mom'
#sis = 'sis'
#bro = 'bro'
#friend = 'friend'
#l = {dad:vec(22,33),mom:['2',2],sis:['3',1],bro:['4',0],friend:['5',-1]}
#move = 99
#while move:
#    move = input()
#    if move in l:
#        new = input()
#        newl = {}
#        save = {}
#        for x in l:
#            save.update({x:l[x]})
#        for x in l:
#            newl.update({x:x})
#        newl[move] = new
#        newl[new] = move
#        print(save)
#        l = {value:key for key, value in newl.items()}
#        for x in save:
#            l[x] = save[x]
#        print(l)
pierce = 'pierce'
bleed = 'ble'
erosion = 'e'
weapons = {'shard gun':{'direct fire':[2,[{pierce:1}],False,5,5],'spray fire':[1,[{}],False,5,1]},'shrapnel cannon':{'cannon fire':[5,[{erosion:1}],False,2,2],'cannon malfunction':[5,[0],False,1,2]},'silicer cannon':{'sclicer fire':[5,[0],False,1,2],'sclicer malfunction':[5,[0],False,1,2]}}
attacks = {'leg slash':[5,[{bleed:1}],False,1,5],'change weapon':[0,[{}],True,1,2],'malfunction':[0,[{}],False,1,3]}
cweapons = []
for x in weapons:
    cweapons.append(x)
selectedweapon = random.choice(cweapons)
attacks.update(weapons[selectedweapon])
print(attacks)
for x in weapons[selectedweapon]:
    print(x)
    del attacks[x]
print(attacks)