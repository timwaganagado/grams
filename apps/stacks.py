import random
import collections


def addstack(stack):
    total = 0
    for x in stacks:
        total += x
    return total

def takefrom(total,removed):
    amount = removed
    if removed > total or len(stacks)+1 == piles:
        amount = total
    return amount
start = random.randint(100,1000)
total = int(start)
stacks = []

diff = int(total/100)
mini = int(start/10)

pilesize = mini + random.randint(-diff,diff)
piles = random.randint(2,15)
stacks.append(pilesize)
total -= pilesize

while total > 0:
    pilesize = mini + random.randint(-diff,diff)
    actualsize = takefrom(total,pilesize)
    stacks.append(actualsize)
    total -= actualsize

amountofstacks = len(stacks)
    
averageamountinstacks = addstack(stacks)/amountofstacks

equaltest = False
for x in stacks:
    if x == averageamountinstacks:
        equaltest = False

def ttas():
    smallest = float('inf')
    largest = 0
    for idx,x in enumerate(stacks):
        if x < smallest:
            smallest = x 
            smallestidx = idx
    for idx,x in enumerate(stacks):
        if x > largest:
            largest = x 
            largestidx = idx
    averagedistance =1 #int((largest+smallest)/2)
    stacks[largestidx] -= averagedistance
    stacks[smallestidx] += averagedistance
    return stacks

def ttass():
    listofstacks = []
    times = 0
    same = 0
    while same < 2:
        times += 1
        same = 0
        stacks = ttas()
        listofstacks.append(list(stacks))
        ll = collections.Counter(stacks)
        for x in listofstacks:
            ww = collections.Counter(x)
            if ww == ll:
                same+=1
    return stacks,times
#for x in range(50):
#    stacks = ttas()
stacks,times = ttass()
print(averageamountinstacks)
print(stacks,times)
print(addstack(stacks))