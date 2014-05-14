'''
Created on May 10, 2014

@author: tdongsi
'''

import simpleguitk as simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
MAX_VALUE = 21
DEALER_MIN_VALUE = 17


# define card class
class Card:
    '''Class that represents individual cards in a deck'''
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        '''Draw the graphic representation of the card's face'''
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
              [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    def draw_back(self, canvas, pos):
        '''Draw the graphic representation of the card's back'''
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
              [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return " ".join([str(card) for card in self.cards])

    def add_card(self, card):
        self.cards.append(card)


    def get_value(self):
        # compute the value of the hand, see Blackjack video
        # count aces as 1, if the hand has an ace, 
        # then add 10 to hand value if it doesn't bust
        value = 0
        foundAce = False
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                foundAce = True
        
        if foundAce:
            if value + 10 > MAX_VALUE:
                return value
            else:
                return value + 10
        else:
            return value
    
    def clear(self):
        self.cards[:] = []
   
    def draw(self, canvas, pos, hidden = False):
        if hidden:
            self.cards[0].draw_back(canvas, pos)
        else:
            self.cards[0].draw(canvas, pos)
            
        for i in range(1, len(self.cards)):
            self.cards[i].draw(canvas, [pos[0] + i * 100, pos[1]])
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)
                
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        # remove the card from the back of the deck
        return self.cards.pop()
    
    def __str__(self):
        # return a string representing the deck
        # Shows the last 10 cards only (those will be dealt to players soon)
        return " ".join([str(card) for card in self.cards[-10:]])


deck = Deck()
player = Hand()
dealer = Hand()

# define event handlers for buttons
def deal():
    global outcome, in_play
    global deck, player, dealer

    # your code goes here
    in_play = True
    
    deck.shuffle()
    print "First 10 in deck: ", deck
    player.clear()
    dealer.clear()
    
    # Dealing cards    
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    # TODO: mark this card as hole card
    dealer.add_card(deck.deal_card())
    
    print "Player's hand:", player
    print "Dealer's hand:", dealer
    

def hit():
    global in_play, player, score, outcome
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())
        
        # DEBUG:
        print "Player's hand:", player
   
        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > MAX_VALUE:
            print "Player busted: %d" % player.get_value()
            outcome = 'Player went busted'
            in_play = False
            score -= 1
       
def stand():
    global in_play, player, dealer, score, outcome
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < DEALER_MIN_VALUE:
            dealer.add_card(deck.deal_card())
            
        # assign a message to outcome, update in_play and score
        in_play = False
        if dealer.get_value() > MAX_VALUE :
            # Dealer busted
            print "Dealer busted %d" % dealer.get_value()
            outcome = 'Dealer went busted'
            score += 1
        elif dealer.get_value() >= player.get_value():
            print "Dealer won"
            outcome = 'Dealer won'
            score -= 1
        else:
            print "Player won"
            outcome = 'Player won'
            score += 1

# draw handler    
def draw(canvas):
    global in_play, outcome
    
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Black Jack", (50, 50), 25, 'Red')
    canvas.draw_text("Score %d" % score, (300, 50), 25, 'Black')
    
    canvas.draw_text("Dealer", (50, 150), 25, 'Black')
    dealer.draw(canvas, [50, 150], in_play)
    
    canvas.draw_text("Player", (50, 350), 25, 'Black')
    player.draw(canvas, [50, 350])
    
    if in_play:
        canvas.draw_text("Hit or Stand?", (50, 550), 25, 'Yellow')
    else:
        canvas.draw_text(outcome, (50, 500), 25, 'Yellow')
        canvas.draw_text("Press Deal to start a new game", (50, 550), 25, 'Yellow')
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
