from newblackjack import Deck

d = Deck(4)

def cardvalue(card):
    suite = card[0]
    value = card[1]
    


def drawcards(times,cards,outvalue):
    for x in range(times):
        card = d.pick_randomcard()
        cards.append(card)
        value,kind = d.card_info(card)
        if kind == "Ace":
            value = kind
        outvalue.append(value)
    return cards,outvalue

    

def cardtotal(value):
    total = 0
    for x in value:
        if x == "Ace":
            x = 11
        total += x
    if total > 21:
        for x in value:
            if x == "Ace":
                total -= 10
    return total

def new():
    cards = []

    value = []


    cards,value = drawcards(2,cards,value)


    total = 0
    total = cardtotal(value)
    return cards,value,total

def testhand():
    playercards,playervalue,playertotal = new()

    while playertotal < 21:
            playercards,playervalue = drawcards(1,playercards,playervalue)
            playertotal = cardtotal(playervalue)
    return playertotal
        

spools = 100000000

running = True
while running:
    numberofbj = 0
    for x in range(spools):
        #print(x%(spools/10))
        if x % (spools/100) == 0 and x != 0:
            print(x/spools)
        x = testhand()
        if x == 21:
            numberofbj += 1
    print(numberofbj,"out of",spools)
    print(f"{(numberofbj/spools)*100}%")
    input("")
