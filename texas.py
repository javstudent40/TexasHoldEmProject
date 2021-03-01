import random
import itertools
from helpers import *

pot = 0
player_chips = 1000
computer_chips = 1000
player_hand = []
computer_hand = []
game_over = False

#create deck of cards
deck = []
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

cards = list(itertools.product(vals, suits))

for val, suit in cards:
    card = f"{val} of {suit}"
    deck.append(card)



#deal two cards to player 1
print("Player 1 cards:")
deal_two_cards()
print("")
print("")

#deal two cards to computer - will hide later
print("Computer cards:")
deal_two_cards()
print("")
print("")

#first betting round
bet()


#deal flop
print("The flop is:")
deal_3_cards()
print("")
print("")

#deal turn
print("The turn is:")
deal_one_card()
print("")
print("")

#deal river
print("The river is:")
deal_one_card()


