import random
level = 1
statspread = 0
stats = [19, 27, 13, 10, 9]
statsold = list(stats)
dif = list(stats)
def addtostat(add):
    while add != 0:
        add -= 1
        stat = random.randint(1,5)
        if stat == 1:
            stats[0] += 1
        elif stat == 2:
            stats[1] += 1
        elif stat == 3:
            stats[2] += 1
        elif stat == 4:
            stats[3] += 1
        elif stat == 5:
            stats[4] += 1
def difference():
    for i in range(0,5):
        dif[i] = stats[i] - statsold[i]

while statspread < 180:
    level += 1

    if level % 3 == 0:
        addtostat(3)
    else:
        addtostat(1)
    #l = input('level up')
    #print(stats)
    #print(statsold)
    
    difference()
    statsold = list(stats)
    statspread = 0
    for x in stats:
        statspread += x
print(statspread)
print(f'''Level {level}
HP  {stats[0] , f'+{dif[0]}'}
Atk {stats[1] , f'+{dif[1]}'}
Spd {stats[2] , f'+{dif[2]}'}
Def {stats[3] , f'+{dif[3]}'}
Res {stats[4] , f'+{dif[4]}'}''')
    



#print([int(random.randint(16,22)),int(random.randint(16,27)),int(random.randint(3,13)),int(random.randint(3,13)),int(random.randint(3,10))])
