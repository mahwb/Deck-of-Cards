from cards import Player, Cards, Deck

# starts game
def start_game():
    deck, player, opponent = reset()
    print "Options to choose from: Black Jack - War - Test"
    line = raw_input('What game do you want to play? ').lower()
    if line == "black jack" or line == "bj":
        start_black_jack(player, opponent)
    elif line == "war":
        start_war(player, opponent)
    elif line == "test":
        test(player)
    elif line == "end" or line == "exit":
        print "Ending."
        return
    start_game()

# reset game
def reset():
    deck = Deck().shuffle()
    player = Player("Ray", deck)
    opponent = Player("Dealer", deck)
    return deck, player, opponent

# testing for class methods
def test(player):
    line = raw_input('What to do? ').lower()
    if line == "draw":
        player.draw()
    elif line == "discard":
        player.discard()
    elif line == "hand":
        player.hand()
    elif line == "show":
        player.deck.show()
    elif line == "shuffle":
        player.deck.shuffle()
        print "Shuffled deck."
    elif line == "commands":
        print "Draw    - draws a card"
        print "Discard - discards a card"
        print "Hand    - shows hand"
        print "Show    - shows deck"
        print "Shuffle - shuffles deck"
        print "Exit"
    elif line == "end" or line == "exit":
        print "Ending test.\n"
        return
    else:
        pass
    test(player)

# initializes Black Jack game
def start_black_jack(player, opponent):
    opponent.draw().draw()
    print opponent.name, "showing:"
    print opponent.cards[0].value, "of", opponent.cards[0].suit, "\n"
    player.draw().draw().hand()
    print ""
    questions_black_jack(player, opponent)

# questions for Black Jack game
def questions_black_jack(player, opponent): 
    line = raw_input('What to do? ').lower()
    if line == "hit":
        player.draw().hand()
        print ""
    elif line == "stay":
        opponent_sum = count_opponent_helper(opponent, opponent_sum = 0)
        while opponent_sum < 17:
            opponent.draw()
            opponent_sum = count_opponent_helper(opponent, opponent_sum = 0)
        player_sum = 0
        for i in range(0,len(player.cards)):
            if player.cards[i].value == "Ace":
                player_sum += 11
            elif player.cards[i].value == "Jack" or player.cards[i].value == "Queen" or player.cards[i].value == "King":
                player_sum += 10
            else:
                player_sum += player.cards[i].value
        opponent.hand()
        print "\n", opponent_sum, "|", player_sum
        if opponent_sum > player_sum and opponent_sum <= 21 or player_sum > 21:
            print opponent.name, "Wins!\n"
            deck, player, opponent = reset()
            start_black_jack(player, opponent)
            return
        elif opponent_sum == player_sum:
            print "Tie game!\n"
            deck, player, opponent = reset()
            start_black_jack(player, opponent)
            return
        else: 
            print player.name, "Wins!\n"
            deck, player, opponent = reset()
            start_black_jack(player, opponent)
            return
    elif line == "end" or line == "exit":
        print "Ending Black Jack game.\n"
        return
    elif line == "commands":
        print "Hit - Stay - Exit"
    else:
        pass
    questions_black_jack(player, opponent)

# helper function to count value of cards in opponents hand
def count_opponent_helper(opponent, opponent_sum):
    for i in range(0,len(opponent.cards)):
        if opponent.cards[i].value == "Ace":
            opponent_sum += 11
        elif opponent.cards[i].value == "Jack" or opponent.cards[i].value == "Queen" or opponent.cards[i].value == "King":
            opponent_sum += 10
        else:
            opponent_sum += opponent.cards[i].value
    return opponent_sum

# initializes War game
def start_war(player, opponent):
    opponent.draw().hand()
    print ""
    player.draw().hand()
    print ""
    opponent_value = 0;
    player_value = 0;
    if player.cards[0].value == "Ace":
        player_value = 14
    elif player.cards[0].value == "Jack":
        player_value = 11
    elif player.cards[0].value == "Queen":
        player_value = 12
    elif player.cards[0].value == "King":
        player_value = 13
    else:
        player_value = player.cards[0].value
    if opponent.cards[0].value == "Ace":
        opponent_value = 14
    elif opponent.cards[0].value == "Jack":
        opponent_value = 11
    elif opponent.cards[0].value == "Queen":
        opponent_value = 12
    elif opponent.cards[0].value == "King":
        opponent_value = 13
    else:
        opponent_value = opponent.cards[0].value
    if opponent_value == player_value:
        if opponent.cards[0].suit == "Clubs":
            opponent_value += 1
        if opponent.cards[0].suit == "Diamonds":
            opponent_value += 2
        if opponent.cards[0].suit == "Hearts":
            opponent_value += 3
        if opponent.cards[0].suit == "Spades":
            opponent_value += 4
        if player.cards[0].suit == "Clubs":
            player_value += 1
        if player.cards[0].suit == "Diamonds":
            player_value += 2
        if player.cards[0].suit == "Hearts":
            player_value += 3
        if player.cards[0].suit == "Spades":
            player_value += 4
    if opponent_value > player_value:
        print opponent.name, "wins!\n"
    else:
        print player.name, "wins!\n"
    questions_war()

# questions for War game
def questions_war():
    line = raw_input("Go again? ").lower()
    if line == "yes" or line == "y":
        deck, player, opponent = reset()
        start_war(player, opponent)
    elif line == "no" or line == "n" or line == "end" or line == "exit":
        return
    else:
        questions_war()

start_game()