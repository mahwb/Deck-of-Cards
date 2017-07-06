import random

suits = ["spades", "hearts", "diamonds", "clubs"]
values = [2,3,4,5,6,7,8,9,10,"jack", "Queen", "King", "Ace"]

class Cards(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def info(self):
        print self.suit
        print self.value
        return self

class Deck(Cards):
    def __init__(self,):
        self.cards = []
        for i in range(0, len(suits)):
            for j in range(0, len(values)):
                self.cards.append(Cards(suits[i], values[j]))

    def add(self):
        self.cards.append(Cards(suits[random.randint(0,len(suits))],values[random.randint(0,len(values))]))
        return self

    def shuffle(self):
        for i in range(0, len(self.cards)):
            temp = self.cards[i]
            swap = random.randint(0,len(self.cards))
            self.cards[i] = self.cards[swap]
            self.cards[swap] = temp
        return self

    def show(self):
        for i in range(0,len(self.cards)):
            print self.cards[i].value, "of", self.cards[i].suit
        return self

class Player(object):
    def __init__(self, name, deck):
        self.name = name
        self.cards = []
        self.deck = deck

    def draw(self):
        drawn = self.deck.cards.pop()
        self.cards.append(drawn)
        print "Drew a", drawn.value, "of", drawn.suit
        return self

    def discard(self, card = None):
        if card == None:
            self.cards.pop()
        else: 
            for i in range(0, len(self.cards)):
                if card == self.cards[i]:
                    self.cards.pop(self.cards[i])
        return self

    def hand(self):
        print "Hand:"
        for i in range(0,len(self.cards)):
            print self.cards[i].value, "of", self.cards[i].suit
        return self      

deck1 = Deck().shuffle().show()
player1 = Player("Ray", deck1).draw().draw().hand().discard().hand()