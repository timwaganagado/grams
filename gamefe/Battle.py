import random
import time
from FE_TestLevel import levelincrease
#print([int(random.randint(16,22)),int(random.randint(16,27)),int(random.randint(3,13)),int(random.randint(3,13)),int(random.randint(3,10))])
#print([int(random.randint(16,22)),int(random.randint(16,27)),int(random.randint(3,13)),int(random.randint(3,13)),int(random.randint(3,10))])
statsp =[20, 30, 11, 99, 5, 1]

statse = [19, 18, 6, 6, 8, 1]
xpe = 50
running = True


class Player():
    def __init__(self,stat):
        self.stat = stat
        self.stata = list(stat)
        self.Spd = self.stat[2]
        self.statold = list(stat)
        self.dif = list(stat)
        self.levelup = stat[5] * 60
        self.xp = 0

class Enemy():
    def __init__(self,stat,xpe):
        self.stat = stat
        self.stata = list(stat)
        self.Spd = self.stat[2]
        self.statold = list(stat)
        self.dif = list(stat)
        self.rewardxp = xpe

P = Player(statsp)
E = Enemy(statse,xpe)



def differenceh(x):
    i = 0    
    x.dif[i] =  x.statold[i] - x.stata[i]


def attacking(defending,attacker):
    defending.stata[0] = defending.stata[0] - (attacker.stat[1] - defending.stat[3])

while running:
    print(f'''Enemies stats 
    level {E.stat[5]}
        HP  {E.stat[0]}
        Atk {E.stat[1]}
        Spd {E.stat[2]}
        Def {E.stat[3]}
        Res {E.stat[4]}''')
    attack = input('attack ')
    time.sleep(1)
    
    if attack == 'y':
        attacking(E,P)
        #print(statse)
        differenceh(E)
        if E.stata[0] >= 0:
            attacking(P,E)
            differenceh(P)
        else:
            P.dif[0] = 0
        if P.Spd >= E.Spd + 5:
            attacking(E,P)
            differenceh(E)
        print(f'''Enemy                 Player
HP  {E.stata[0] } { f'-{E.dif[0]}'}             HP  {P.stata[0]} { f'-{P.dif[0]}'}''')
    time.sleep(1)
    if E.stata[0] <= 0 and P.stata[0] >= 0:
        newstat = [int(random.randint(16,22)),int(random.randint(16,27)),int(random.randint(3,13)),int(random.randint(3,13)),int(random.randint(3,10)),int(E.stat[5])]
        print(newstat)
        newstat[5],newstat = levelincrease(newstat[5],newstat,newstat[5],0)
        E = Enemy(newstat,E.rewardxp)
        exp = E.stat[5] * E.rewardxp
        if P.stat[5] % 2 == 0:
            E.rewardxp -= 5
        print(E.rewardxp)
        P.xp += exp
        if P.xp > P.levelup:
            print('level up')
            time.sleep(1)
            P.stat[5],P.stat = levelincrease(P.stat[5],P.stat,1,1)
            P.xp = 0
        P.stata = list(P.stat)
    if P.stata[0] <= 0:
        
        print('dead')
        time.sleep(1)
        running = False
    