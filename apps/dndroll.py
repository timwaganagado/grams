import random

def roll_d6(times):
    total = 0
    for x in range(times):
        total += random.randint(1,6)
    return total

def amountofrolls():
    roll = 0
    amountofrolls = 0
    while roll != 22:
        amountofrolls += 1
        roll = roll_d6(4)
    return amountofrolls

def averageofrolls():
    totalrolls = 0
    amoofset = 100000
    for x in range(amoofset):
        totalrolls += amountofrolls()
    print(totalrolls/amoofset)

def rolld6lowest():
    lowest = float('inf')
    for x in range(100):
        roll = roll_d6(4)
        if roll < lowest:
            lowest = roll
    print(lowest)

rolld6lowest()