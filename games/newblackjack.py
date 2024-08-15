import random

class Deck:
    def __init__(self):
        self.deck_items = {}
        self.deck = []
        self.discard = []
        self.build_deckitems()
    
    def build_deck(self):
        for x in self.deck_items:
            self.deck.append(x)
    
    def pick_randomcard(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.discard.append(card)
        return card
    
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

deck = Deck()
deck.build_deck()
card = deck.pick_randomcard()
print(card)
print(deck.card_info(card))
print(deck.deck)