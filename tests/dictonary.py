import random
#l = {'connected':True,'conncode':0,'lsit':[1,'gay',True]}
#
#l.update({'lost':True})
#
#for w in l:
#    print(l[w])

d = {'p1':[5,3,(1,2)],'p2':[2,5,(1,0)],'p3':[4,1,(2,2)]}
sortedd = {k:v for k, v in sorted(d.items(), key = lambda t:t[1][1])}

print(sortedd)
for he in sortedd:
    print(he)
    print(d[he][0])

d = random.choice(sortedd)