#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:

    def __init__(self):
        print('Creating new deck')
        self.cards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print('Shuffle')
        shuffle(self.cards)

    def handcards(self):
        print("Splitting cards for u and opponent")
        return(self.cards[:26],self.cards[26:])

class Hand:

    def __init__(self, cards):
        self.cards = cards




    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    pass

class Player:

    def __init__(self, name, hand):

        self.name = name
        self.hand = hand

    def remove(self):

        self.hand.cards.pop(0)

    def add(self, table):

        self.hand.cards.extend(table)




    def quant(self):
        return len(self.hand.cards)
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """





######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

d = Deck()
d.shuffle()
p1deck, p2deck = d.handcards()

p1 = Player(input('Give me your name '), Hand(p1deck))
p2 = Player(input('Give me your component name '), Hand(p2deck))
table = []
skip = 0


print("Let's start!!!")
while p1.quant() > 0 and p2.quant() > 0:
    print(p1.name,"'s card is'", p1.hand.cards[0], 'vs', p2.hand.cards[0],p2.name,"'s card'")
    table.append(p1.hand.cards[0])
    table.append(p2.hand.cards[0])

    if RANKS.index(p1.hand.cards[0][1]) > RANKS.index(p2.hand.cards[0][1]):

        p1.remove()
        p2.remove()
        p1.add(table)
        print("This round won ", p1.name)
        table.clear()

    elif RANKS.index(p1.hand.cards[0][1]) < RANKS.index(p2.hand.cards[0][1]):

        p1.remove()
        p2.remove()

        p2.add(table)
        print("This round won ", p2.name)
        table.clear()

    elif RANKS.index(p1.hand.cards[0][1]) == RANKS.index(p2.hand.cards[0][1]):



        print("DRAW!!!")
        p1.remove()
        p2.remove()

        if p1.quant() == 0:
            print(p1.name,'has no cards!!!!')
            break
        if p2.quant() == 0:
            print(p2.name,'has no cards!!!!')
            break

        for _ in range(3):
            table.append(p1.hand.cards[0])
            table.append(p2.hand.cards[0])
            p1.remove()
            p2.remove()
            if p1.quant() == 1 or p2.quant() == 1:
                break
        #if RANKS.index(p1.hand.cards[0][1]) > RANKS.index(p2.hand.cards[0][1]):


    #print(p1.name,"'s cards: '", p1.hand.cards,'\n')
    #print(p2.name,"'s cards: '", p2.hand.cards, '\n')
    print("Table: ", table,'\n','\n','\n')


    if skip == 0:
        r = '2'
        while r == '2' :
            r = input("If u want skip all game enter '1'\nIf u want check your deck enter '2' \nIf You want continue press enter\n")
            if r == '1':
                skip = 1
            if r == '2':
                print(p1.name,"'s card '", p1.hand.cards,'\n')

if p1.quant() == 0:
    print(p2.name,"'s cards: '", p2.hand.cards, '\n')
    print(p2.name, 'WON!!! CONGRATULATIONS!')
if p2.quant() == 0:
    print(p1.name,"'s cards: '", p1.hand.cards,'\n')
    print(p1.name, 'WON!!! CONGRATULATIONS!')





# Use the 3 classes along with some logic to play a game of war!
