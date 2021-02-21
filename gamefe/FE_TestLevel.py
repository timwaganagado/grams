import random
import time
def levelincrease(level,stats,levelup,dis):


    
    statsold = list(stats)
    dif = list(stats)
    statadd = range(1,6) 
    def addtostat(add):
        while add != 0:
            add -= 1
            stat = int(random.choices(statadd, weights=[1,1,2,1,1])[0])

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
    level += 1
    while levelup != 0:
        

        if level % 3 == 0:
            addtostat(random.randint(1,5))
        else:
            addtostat(random.randint(1,2))
        #l = input('level up')
        #print(stats)
        #print(statsold)

        difference()
        statsold = list(stats)
        statspread = 0
        for x in stats:
            statspread += x
        #print(statspread)
        levelup -= 1
        
        if dis == 1:
            print(f'''Level {level}
            HP  {stats[0] , f'+{dif[0]}'}
            Atk {stats[1] , f'+{dif[1]}'}
            Spd {stats[2] , f'+{dif[2]}'}
            Def {stats[3] , f'+{dif[3]}'}
            Res {stats[4] , f'+{dif[4]}'}''')
            time.sleep(1)
            input('continue')
        
        
        
    return level,stats


#print([int(random.randint(16,22)),int(random.randint(16,27)),int(random.randint(3,13)),int(random.randint(3,13)),int(random.randint(3,10))])
