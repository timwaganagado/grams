import random

def d20():
    return random.randint(1,20)

average = {}
times = 100000000
checkint = times/10
for x in range(times):
    if x%checkint == 0:
        print(x/times)
    first = d20()
    second = d20()
    high = max(first,second)
    low = min(first,second)
    change = high - low
    average.update({x:(high,low,change)})

total = 0
for x in average:
    total += average[x][2]

total /= len(average)

print(total)