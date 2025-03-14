import random

numtoselect = {1:"rock",2:"paper",3:"sissorcs"}

beats = {1:3,3:2,2:1}

def playerchoice():
    print("rock paper sissorcs")
    player = int(input("0 | stop , 1 | rock ,  2 | paper , 3 | sissorcs"))
    while 3 < player or player <= -1: 
        player = int(input("0 | stop , 1 | rock ,  2 | paper , 3 | sissorcs"))
    if player == 0:
        player = False
    return player
    
player = playerchoice()

while player:
    ai = random.choice([1,2,3])
    
    print(f'I pick {numtoselect[ai]}, you picked {numtoselect[player]}')
    
    if player == ai:
        print("draw")
    if beats[player] == ai:
        print("wins")
    if beats[ai] == player:
        print("loss")
    
    player = playerchoice()