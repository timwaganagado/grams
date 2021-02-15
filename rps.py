import random
import numpy
from scipy import stats
rps = ["rock","scissors","paper"]
rpsnum = [1,2,3]
winprediction = []
playerprediction = []
playing = True
def rpsconvert(hand):
    if hand == "rock":
        hand = 1
    elif hand == "scissors":
        hand = 2
    elif hand == "paper":
        hand = 3
    elif hand == 1:
        hand = "rock"
        print('pfpppt')
    elif hand == 2:
        hand = "scissors"
        print('pfpppt')
    elif hand == 3:
        hand = "paper"
        print('pfpppt')
    return hand
    
while playing == True:
    x = len(playerprediction)
    if x == 0:
        hand = random.choice(rpsnum)
    else:  
        if len(winprediction) != 0:  #checks if player has lost and will attempt to counter
            print(playerprediction)
            print(winprediction)
            print(stats.mode(winprediction))
            print(stats.mode(winprediction)[0])
            print(stats.mode(winprediction)[1])
            print(stats.mode(winprediction)[0][0])
            if stats.mode(winprediction)[0] == 0:
                if stats.mode(winprediction)[0][0] == 1:
                    hand = stats.mode(playerprediction)
                    hand = hand[0]
                    hand = hand[0] - 1
                hand = playerprediction[-1] + 1
            else:
                if stats.mode(winprediction)[1][0] >= 2:
                    hand = playerprediction[-1]
                    winprediction = []
        else:
            hand = stats.mode(playerprediction)
            hand = hand[0]
            hand = hand[0] - 1
        if hand == 0:
            hand = 3
        elif hand == 4:
            hand = 1
    print("Rock! Paper! Scissors!")
    playerhand = int(input("1/rock 2/scissors 3/paper: "))
    print(hand)
    nhand = rpsconvert(hand)
    playerprediction.append(playerhand)
    if hand == playerhand:
        print("tie, They chose")
        print(nhand)
        winprediction.append(0)
    elif hand == 1 and playerhand == 2:
        print("You lose, They chose")
        print(nhand)
        winprediction.append(1)
    elif hand == 2 and playerhand == 3:
        print("You lose, They chose")
        print(nhand)
        winprediction.append(1)
    elif hand == 3 and playerhand == 1:
        print("You lose, They chose")
        print(nhand)
        winprediction.append(1)
    elif hand == 1 and playerhand == 3:
        print("You win, They chose")
        print(nhand)
        winprediction.append(2)
    elif hand == 2 and playerhand == 1:
        print("You win, They chose")
        print(nhand)
        winprediction.append(2)
    elif hand == 3 and playerhand == 2:
        print("You win, They chose")
        print(nhand)
        winprediction.append(2)
    print()
    another = int(input("Another? 1/No 2/Yes: "))
    if another == 1:
        playing = False
        print(playerprediction)
    else:
        playing = True