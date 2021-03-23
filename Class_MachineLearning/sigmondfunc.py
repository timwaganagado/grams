import math
def lol(x):
    return 1/(1+math.exp(-x))

x = [33,2,1,5,5,7,89,9,6,5,4,32,1,2,3,5,6]
t=[]
for s in x:
    w = lol(s)
    t.append(w)

print(t)