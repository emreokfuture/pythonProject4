import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing=True
#############
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank+"of"+self.suit
######

class Deck():
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp +='\n'+card.__str__()
            return "the deck has"+deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
test_deck=Deck()
print(test_deck)
################
class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]

        if card.rank=='Ace':
            self.aces +=1
    def adjustaces(self):
        while self.value>21 and self.aces:
            self.value=self.value-10
            self.ace=self.aces-1
test_deck=Deck()


test_player=Hand()
pulled_card=test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

#####
class Chips():
    def __init__(selfself,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total=self.total+self.win_bet()
    def lose_bet(self):
        self.total=self.total-self.bet
  ###########

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("how many chips would you like to bet?"))
        except:
            print("please provide an integer")
        else:
            if chips.bet > chips.total:
                print("sorry you do not have enoughh chips ").format(chips.total)
            else:
                break
def hit(deck,hand):
    single_card=deck.deal()

    hand.add_card(single_card)
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input("hit or stand? h or s")
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower() =='s':
            print("player stands, Dealer's turn")
            playing=False
        else:
            print("sorry , please h or s is appliacable ")
######################
def show_some(player,dealer):
    print("\n Dealer's Hand:")
    print("First card hidden")
    print(dealer.cards[1])
    for card in player.cards:
        print(card)

    #
def show_all(player,dealer):
     for card in player.cards:
        print(card)
     print("Value of Dealer'S hand is: {dealer.value}")


     for card in player.cards:
         print(card)
     print("value hand is: {dealer.value}")
##########
def player_busts(player,dealer,chips):
    print("Bust Player!")
    chip.lose_bet()
def player_wins(player,dealer,chips):
    print("player wins")
    chip.win_bet()

def dealer_wins(player,dealer,chips):
    print("dealer qins")
    chip.lose_bet()
def push(player,dealer):
    print("Tıe")
#####################
while True:
    deck=Deck()
    deck.shuffle()

    player_hand=Hand()
    player_hand.add_card(card.deal())
    player_hand.add_card(card.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(card.deal())
    dealer_hand.add_card(card.deal())

    player_chips=Chips()
    take_bet(player)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)

        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value<=21:
        while dealer_hand.value<player_hand.value:
            hit(deck,dealer_hand)


        show_all(player_hand,dealer_hand)

        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    print("platetr" .format(player_chips.total))
    new_game=input("would you like to playe another hand y/N")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("thank you for playin")
        break


