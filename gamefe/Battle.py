import random
#print([int(random.randint(16,22)),int(random.randint(16,27)),int(random.randint(3,13)),int(random.randint(3,13)),int(random.randint(3,10))])
#print([int(random.randint(16,22)),int(random.randint(16,27)),int(random.randint(3,13)),int(random.randint(3,13)),int(random.randint(3,10))])
statsp =[20, 30, 11, 7, 5]
statse = [19, 18, 6, 6, 8]
running = True


class Player():
    def __init__(self,stat):
        self.stat = stat
        self.Spd = self.stat[2]
        self.statold = list(stat)
        self.dif = list(stat)

class Enemy():
    def __init__(self,stat):
        self.stat = stat
        self.Spd = self.stat[2]
        self.statold = list(stat)
        self.dif = list(stat)

P = Player(statsp)
E = Enemy(statse)



def differenceh(x):
    i = 0    
    x.dif[i] =  x.statold[i] - x.stat[i]


def attacking(defending,attacker):
    defending.stat[0] = defending.stat[0] - (attacker.stat[1] - defending.stat[3])

while running:
    attack = input('attack ')
    
    if attack == 'y':
        attacking(E,P)
        #print(statse)
        differenceh(E)
        if E.stat[0] >= 0:
            attacking(P,E)
            differenceh(P)
        if P.Spd >= E.Spd + 5:
            attacking(E,P)
            differenceh(E)
        print(f'''Enemy                 Player
HP  {E.stat[0] } { f'-{E.dif[0]}'}             HP  {P.stat[0]} { f'-{P.dif[0]}'}''')

    if E.stat[0] <= 0:
        newstat = [int(random.randint(16,22)),int(random.randint(16,27)),int(random.randint(3,13)),int(random.randint(3,13)),int(random.randint(3,10))]
        E = Enemy(newstat)
    if P.stat[0] <= 0:
        print(P.stat[0])
        print('dead')
        running = False