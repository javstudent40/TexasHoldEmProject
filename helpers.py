import random
import itertools

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

def deal_one_card():
    rand_card = random.choice(deck)
    print(rand_card)
    deck.remove(rand_card) # removes card from deck       
    

def deal_two_cards():
    for _ in range(2):
        deal_one_card()

def deal_3_cards():
    for _ in range(3):
        deal_one_card()

def bet():
    global player_chips, pot
    player_ask = input("Do you wish to fold, call or bet? ")
    if player_ask == "fold":
        game_over = True
        print("Computer wins the hand")
    elif player_ask == "bet":
        player_bet = input("How much do you wish to bet?")
        player_chips -= int(player_bet)
        pot += int(player_bet)
    # else:
    #     player_chips -= computer_bet
    #     pot += computer_bet