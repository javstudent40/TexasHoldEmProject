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
    player_ask = input("Do you wish to fold, call or bet? ")
    if player_ask == "fold":
        game_over = True
        print("Computer wins the hand")
    elif player_ask == "bet":
        player_bet = input("How much do you wish to bet?")
        player_chips -= player_bet
        pot += player_bet
    # else:
    #     player_chips -= computer_bet
    #     pot += computer_bet