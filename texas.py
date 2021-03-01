import random
from helpers import *

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


