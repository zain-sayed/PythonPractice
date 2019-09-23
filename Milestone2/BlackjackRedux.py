import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True
class Card:

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                value = values.get(rank)
                tempCard = Card(suit,rank,value)
                self.deck.append(tempCard)

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        toRet = self.deck.pop()
        return toRet

class Hand:

    def __init__(self):
        self.cards = []
        self.aces = 0
        self.value = 0

    def addCard(self,card):
        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.aces+=1

    def aceAdjustment(self):
        if self.value > 21 and self.aces > 0:
            while(self.value > 21):
                self.value -= 10
                self.aces -= 1

class Chips:

    def __init__(self,total = 100):
        self.total = total
        self.bet = 0

    def winBet(self):
        self.total += self.bet

    def loseBet(self):
        self.total -= self.bet

def takeBet(chips):

    taking = True
    while(taking):
        try:
            bet = int(input("Place your bets!"))

        except:
            print("Incorrect format, try again")
            continue

        else:
            if (chips.total < bet):
                print("Not enough chips, try again")
                continue
            else:
                print("Bet accepted")
                chips.bet = bet
                break
def hit(deck,hand):

    tempCard=deck.deal()
    hand.addCard(tempCard)
    hand.aceAdjustment()

def chipCheck(player_chips):
    if player_chips.total == 0:
        return -1

def hitOrStand(deck,hand):

    global playing

    while True:
        choice = input("Input 'h' for hit or 's' for stand")

        if(choice[0].lower() == 'h'):

            hit(deck,hand)

        elif(choice[0].lower() == 's'):

            print("Player stands, dealer is now playing")
            playing = False

        else:
            print("Incorrect input, try again")
            continue
        break

def showSome(player,dealer):
    print("Dealers hand:")
    print(f"<Hidden Card>")
    print(f"{dealer.cards[0]}\n")
    print("Players hand:")
    print("", *player.cards, sep='\n')

def showAll(player,dealer):
    print("\nThe dealer's hand: ", *dealer.cards, sep='\n')
    print("Value of dealer's hand:", dealer.value)
    print("\nThe player's hand: ", *player.cards, sep='\n')
    print("Value of player's hand", player.value)

def playerBust(player,dealer,player_chips):
    print("Player loses\n")
    player_chips.loseBet()

def playerWin(player,dealer,player_chips):
    print("Player wins\n")
    player_chips.winBet()

def dealerBust(player,dealer,player_chips):
    print("Dealer Loses\n")
    player_chips.winBet()

def dealerWin(player,dealer,player_chips):
    print("Dealer wins\n")
    player_chips.loseBet()

def tieGame(player,dealer):
    print("No one wins, its a tie!\n")
player_chips = Chips()
print("Player starts with 100\n")
print("BlackJack has started, get ready to play\n")

while True:
    if chipCheck(player_chips)==-1:
        print("No more coins, restart")
        break

    deck = Deck()
    deck.shuffle()
    playerHand = Hand()
    dealerHand = Hand()

    playerHand.addCard(deck.deal())
    playerHand.addCard(deck.deal())
    dealerHand.addCard(deck.deal())
    dealerHand.addCard(deck.deal())


    takeBet(player_chips)
    showSome(playerHand,dealerHand)
    i = 0
#----------------------------------------------------------------------------------------------------------------------#
    while playing:
        print(f"{i}")
        i+=1
        hitOrStand(deck,playerHand)
        showSome(playerHand,dealerHand)

        if playerHand.value > 21:
            playerBust(playerHand,dealerHand,player_chips)
            break

    if playerHand.value <= 21:
        while dealerHand.value < 18:
           hit(deck,dealerHand)

        showAll(playerHand,dealerHand)
        if dealerHand.value > 21:
            dealerBust(playerHand,dealerHand,player_chips)
        elif dealerHand.value >playerHand.value:
            dealerWin(playerHand,dealerHand,player_chips)
        elif playerHand.value > dealerHand.value:
            playerWin(playerHand,dealerHand,player_chips)
        else:
            tieGame(playerHand,dealerHand)

    print(f"\nPlayer now has {player_chips.total} in total\n")

    repeat = input("Would you like to play again? Enter 'y' to do so\n")
    if repeat[0].lower() == 'y':
        playing = True
        continue
    else:
        playing = False
        print("Thanks for playing\n")
        break





























