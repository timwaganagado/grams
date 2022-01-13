import random

spark = 160 #max
fehpass = 15.50 #in aud

credit = float(input('Amount of credit: '))

currentorbs = float(input('Current Orbs (leave blank for purchase efficiency): '))
buypass = input('Buying the Feh pass(y/n): ')
amountoftickets = int(input('How many tickets are there: '))

for x in range(0,amountoftickets):
    spark -= 5
print(spark)

if buypass == 'y':
    buypass = True
else:
    buypass = False

methodofpurchase = {'143':[143,119.99],'77':[77,62.99],'50':[50,41.99],'36':[36,30.99],'23':[23,19.99],'10':[10,9.99],'3':[3,2.99]}
listofpurchase = ['143','77','50','36','23','10','3']
leastamountofmoneyspent = {}

for x in methodofpurchase:
    times = 1
    cur = methodofpurchase[x]
    newamount = float(cur[0])
    newmoney = float(cur[1])
    while newamount + currentorbs < spark:
        times += 1
        newamount += cur[0]
        newmoney += cur[1]
    if buypass:
        totalwithoutcredit = newmoney + fehpass
    else:
        totalwithoutcredit = newmoney
    totalwithcredit = totalwithoutcredit - credit

    print(f'The amount of money needed to purchase orbs and feh pass with {x} orbs: {totalwithcredit}')
    print(f"You'll need to buy this pack {times} times")
    print(f'The orb efficiency: {cur[0]/cur[1]}')
    
    leftover = newamount + currentorbs - spark

    print(f'Remaining orbs: {int(leftover)}')
    leastamountofmoneyspent.update({x:totalwithcredit})
    print()

moneyeffecient = x
best = leastamountofmoneyspent[x]
for x in leastamountofmoneyspent:
    cur = leastamountofmoneyspent[x]
    if cur < best:
        moneyeffecient = x
        best = cur
print(f'The most money effecient option is {moneyeffecient}')



amountofattempts = int(input("how many times would you like to find a more effective combination of purchases: "))
attempts = 0
currentmoney = 0
spark -= currentorbs
currentorbs = 0 
bestmoney = best
monies = []
bestmonies = []
while attempts < amountofattempts:
    new = random.choice(listofpurchase)
    chosenorb = methodofpurchase[new][0]
    chosenmoney = methodofpurchase[new][1]
    currentorbs += chosenorb
    currentmoney += chosenmoney
    monies.append(chosenorb)
    attempts += 1
    if currentorbs > spark:
        if currentmoney < bestmoney:
            bestmoney = currentmoney
            bestmonies = monies
            attempts = 0
            monies = []
            currentmoney = 0
            currentorbs = 0
    if attempts%50 == 0:
        monies = []
        currentmoney = 0
        currentorbs = 0
        #print('checking a new combination')
    if attempts%(amountofattempts/100) == 0:
        print(f'{int(round(attempts/amountofattempts*100,0))}%')
    if attempts == amountofattempts/2:
        print("this is taking it's time finding a new one")
    if attempts == amountofattempts*3/4:
        print("looks like we cant find a better combination")
print(bestmoney)
if len(bestmonies) != 0:
    print(bestmonies)
else:
    print(f"there's no better combination so {moneyeffecient} is the best")