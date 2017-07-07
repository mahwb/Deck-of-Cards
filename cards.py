import random

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
values = [2,3,4,5,6,7,8,9,10, "Jack", "Queen", "King", "Ace"]

class Cards(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def info(self):
        print self.suit
        print self.value
        return self

class Deck(Cards):
    def __init__(self):
        self.cards = []
        for i in range(0, len(suits)):
            for j in range(0, len(values)):
                self.cards.append(Cards(suits[i], values[j]))

    def shuffle(self):
        for i in range(0, len(self.cards)):
            temp = self.cards[i]
            swap = random.randint(0,len(self.cards)-1)
            self.cards[i] = self.cards[swap]
            self.cards[swap] = temp
        return self

    def show(self):
        for i in range(0,len(self.cards)):
            print self.cards[i].value, "of", self.cards[i].suit
        print "\nNumber of cards in deck:", str(len(self.cards))
        return self

class Player(object):
    def __init__(self, name, deck = None):
        self.name = name
        self.cards = []
        self.deck = deck

    def draw(self):
        if len(self.deck.cards) >= 1:
            drawn = self.deck.cards.pop()
            self.cards.append(drawn)
            # print "Drew a", drawn.value, "of", drawn.suit
        return self

    def discard(self, card = None):
        if len(self.cards) >= 1:
            if card == None:
                discarded = self.cards.pop()
                self.deck.cards.append(discarded)
            else: 
                for i in range(0, len(self.cards)):
                    if card == self.cards[i]:
                        discarded = self.cards.pop(self.cards[i])
                        self.deck.cards.append(discarded)
                        break
        return self

    def hand(self):
        print self.name +"'s hand:"
        for i in range(0,len(self.cards)):
            print self.cards[i].value, "of", self.cards[i].suit
        return self