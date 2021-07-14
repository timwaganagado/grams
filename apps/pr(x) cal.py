n = input('n = ')

r = input('r = ')

p = input('p = ')

q = input('q = ')

side = input('< or > or = ')




if p == '' and q == '':
    pass 
elif p == '':
    p = 1 - float(q)
elif q == '':
    q = 1 - float(p)

if side == '<' or side == '>':
    if side == '>':
        total = 0
        for ww in range(int(r)+1,int(n)+1):
            print(ww)            
            topf = 1
            for ll in range(1,int(n)+1):
                topf *= ll

            bottomf = 1
            for ll in range(1,int(ww)+1):
                bottomf *= ll

            fact2 = int(n)-int(ww)

            bottomf2 = 1
            for ll in range(1,fact2+1):
            
                bottomf2 *= ll

            comb = topf/(bottomf*bottomf2)
            total += comb * float(p)**int(ww) * float(q)**(int(n)-int(ww))
    if side == '<':
        total = 0
        for ww in range(0,int(r)):
            

            topf = 1
            for ll in range(1,int(n)+1):
                topf *= ll

            bottomf = 1
            for ll in range(1,int(ww)+1):
                bottomf *= ll

            fact2 = int(n)-int(ww)

            bottomf2 = 1
            for ll in range(1,fact2+1):
            
                bottomf2 *= ll

            comb = topf/(bottomf*bottomf2)
            total += comb * float(p)**int(ww) * float(q)**(int(n)-int(ww))
elif side == '<=' or side == '>=':
    if side == '>=':
        total = 0
        for ww in range(int(r),int(n)+1):    
            print(ww)  
            topf = 1
            for ll in range(1,int(n)+1):
                topf *= ll

            bottomf = 1
            for ll in range(1,int(ww)+1):
                bottomf *= ll

            fact2 = int(n)-int(ww)

            bottomf2 = 1
            for ll in range(1,fact2+1):
            
                bottomf2 *= ll

            comb = topf/(bottomf*bottomf2)
            total += comb * float(p)**int(ww) * float(q)**(int(n)-int(ww))
    if side == '<=':
        total = 0
        for ww in range(0,int(r)+1):
            print(ww)
            topf = 1
            for ll in range(1,int(n)+1):
                topf *= ll

            bottomf = 1
            for ll in range(1,int(ww)+1):
                bottomf *= ll

            fact2 = int(n)-int(ww)

            bottomf2 = 1
            for ll in range(1,fact2+1):
            
                bottomf2 *= ll

            comb = topf/(bottomf*bottomf2)
            total += comb * float(p)**int(ww) * float(q)**(int(n)-int(ww))
else:
    topf = 1
    for ll in range(1,int(n)+1):
        topf *= ll

    bottomf = 1
    for ll in range(1,int(r)+1):
        bottomf *= ll

    fact2 = int(n)-int(r)

    bottomf2 = 1
    for ll in range(1,fact2+1):

        bottomf2 *= ll

    comb = topf/(bottomf*bottomf2)
    total = comb * float(p)**int(r) * float(q)**(int(n)-int(r)) 
print(total)