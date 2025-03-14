import random

class Deck:
    def __init__(self,amountsofdecks,autoshuffle=True):
        self.deck_items = {}
        self.drawn = []
        self.deck = []
        self.build_deckitems()
        self.amodecks = amountsofdecks
        self.build_deck()
        self.autoshuffle = autoshuffle
    
    def build_deck(self):
        self.deck = []
        self.drawn = []
        self.discard_pile = []
        for emt in range(self.amodecks):
            for x in self.deck_items:
                self.deck.append(x)
    def checkifempty(self):
        if len(self.deck) <= 0:
            self.build_deck()
    def pick_randomcard(self):
        if len(self.deck) <= 0:
            if self.autoshuffle:
                self.checkifempty()
            else:
                print("deck is empty")
                return
            #self.build_deck()
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.drawn.append(card)
        return card
    
    def discard(self):
        for x in self.drawn:
            self.discard_pile.append(x)
        self.drawn = []

    def card_info(self,card):
        return self.deck_items[card]
        
        
    def build_deckitems(self):
        suites = ["Clubs", "Spades", "Hearts", "Diamonds"]
        cardnumber = 13

        for x in suites:
            for y in range(cardnumber):
                y += 1
                value = y
                if y > 10:
                    value = 10
                if y == 1:
                    y = "Ace"
                match y:
                    case 11:
                        y = "Jack"
                    case 12:
                        y = "Queen"
                    case 13:
                        y = "King"

                self.deck_items.update({x+" "+str(y):[value,y]})

    def show_deck(self):
        print(self.deck_items)


if __name__ == "__main__":
    deck = Deck(4,False)
    running = True
    while running:
        print("1 : quit | 2 : Draw | 3 : Draw all | 4 : toggle shuffle | 5 : show deck")
        cont = int(input(""))

        if cont == 1:
            running = False
            
        if cont == 2:
            print(deck.pick_randomcard())
        
        if cont == 3:
            cards = []
            while len(deck.deck) > 0:
                cards.append(deck.pick_randomcard())
            print(cards)
        if cont == 4:
            if deck.autoshuffle:
                deck.autoshuffle = False
            else:
                deck.autoshuffle = True
            print(deck.autoshuffle)
        if cont == 5:
            print(deck.deck)
            
