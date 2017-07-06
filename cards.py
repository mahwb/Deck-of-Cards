import random

class Cards(object):
    def __init__(self):
        suits = ["spade", "heart", "diamond", "clubs"]
        suit_num = random.randint(0,3)
        self.suit = suits[suit_num]
        value_num = random.randint(1,13)
        if value_num == 1:
            value = "Ace"
        elif value_num == 11:
            value = "Jack"
        elif value_num == 12:
            value = "Queen"
        elif value_num == 13:
            value = "King"
        else:
            value = value_num
        self.value = value

    def info(self):
        print self.suit
        print self.value
        return self

class Deck(Cards):
    def __init__(self, num = 52):
        self.num = num
        self.cards = []
        for i in range(0,num):
            self.cards.append(Cards())

    def add(self):
        self.cards.append(Cards())
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
        for i in range(0,len(self.cards)):
            print self.cards[i].value, "of", self.cards[i].suit
        return self      

deck1 = Deck()
player1 = Player("Ray", deck1).draw().draw().hand().discard().hand()