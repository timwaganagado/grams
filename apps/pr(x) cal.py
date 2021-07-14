n = input('n = ')

r = input('r = ')

p = input('p = ')

q = input('q = ')

side = input('< or > or = ')
topf = 1
for ll in range(1,int(n)+1):
    topf *= ll
print('topf',topf)
bottomf = 1
for ll in range(1,int(r)+1):
    bottomf *= ll
print('bottomf',bottomf)
fact2 = int(n)-int(r)
print('fact2',fact2)
bottomf2 = 1
for ll in range(1,fact2+1):
    print('ll',ll)
    bottomf2 *= ll
print(bottomf2)
comb = topf/(bottomf*bottomf2)
print(comb)

if p == '' and q == '':
    pass 
elif p == '':
    p = 1 - float(q)
elif q == '':
    q = 1 - float(p)

final = comb * float(p)**int(r) * float(q)**(int(n)-int(r)) 
print(final)