import random
import itertools

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


