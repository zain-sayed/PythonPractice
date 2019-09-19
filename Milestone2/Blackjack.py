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
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                value = values.get(rank)
                tempCard = Card(suit, rank, value)
                self.deck.append(tempCard)

    def __str__(self):
        for card in self.deck:
            print(f"{card.rank} of {card.suit}\n")
        return "Printed all cards"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        toRet = self.deck.pop()
        return toRet


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):

        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    game_on = 1
    while game_on:
        try:
            bet = int(input("Please place your bets!"))

        except:
            print("Please enter valid format of bet, try again")
        else:
            if bet > chips.total:
                print("Insufficient Funds, place smaller bet")
                continue
            else:

                chips.bet=bet
                print("Bet Placed")
                break


def hit(deck, hand):
    tempCard = deck.deal()
    hand.add_card(tempCard)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        choice = input("Would you like to hit or stand? Press 'h' for hit or 's' for stand")

        if choice.lower() == 'h':
            hit(deck, hand)

        elif choice.lower() == 's':
            print("Dealer is now playing")
            playing = False

        else:
            print("Not valid choice, try again")
            continue
        break


def show_some(player, dealer):
    print("Only face up dealer card is ", dealer.cards[1], sep='\n')

    print("\nThe player's hand: ", *player.cards, sep='\n')


def show_all(player, dealer):
    print("\nThe dealer's hand: ", *dealer.cards, sep='\n')
    print("Value of dealer's hand:", dealer.value)
    print("\nThe player's hand: ", *player.cards, sep='\n')
    print("Value of player's hand", player.value)


def player_busts(player, dealer, player_chips):
    print("Player loses,over 21")
    player_chips.lose_bet()


def player_wins(player, dealer, player_chips):
    print("Player wins, better than dealer")
    player_chips.win_bet()


def dealer_busts(player, dealer, player_chips):
    print("Player wins, dealer over 21")
    player_chips.win_bet()


def dealer_wins(player, dealer, player_chips):
    print("Player loses, dealer has better than player")
    player_chips.lose_bet()


def push(player, dealer):
    print("It's a tie")

print("Welcome to blackjack! Let's play!")
on = True
while on:
        # Print an opening statement


        # Create & shuffle the deck, deal two cards to each player
        card_deck = Deck()
        card_deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        player_hand.add_card(card_deck.deal())
        player_hand.add_card(card_deck.deal())

        dealer_hand.add_card(card_deck.deal())
        dealer_hand.add_card(card_deck.deal())

        # Set up the Player's chips

        player_chips = Chips(200)

        # Prompt the Player for their bet

        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)

        show_some(player_hand, dealer_hand)
#---------------------------------------------------------------------------------------------------------------------#
        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(card_deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                print("You've been busted!")
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 18:
                hit(card_deck, dealer_hand)

            # Show all cards

            show_all(player_hand, dealer_hand)

            # Run different winning scenarios

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

                # Inform Player of their chips total

            print(f"\nYour total chips are {player_chips.total}")

        # Ask to play again

            next_game = input("Would you like to play again? Enter y or n")

            if next_game == 'y':
                playing = True
                continue
            else:
                playing = False
                print("Thanks for playing")
                break


