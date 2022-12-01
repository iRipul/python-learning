import random
import os
from artwork import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
    
def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)
        
def compare(user_score, comp_score):
    if comp_score == user_score:
        return 0
    elif comp_score == 0:
        return -1
    elif user_score == 0:
        return 1
    elif user_score > 21:
        return -1
    elif comp_score > 21:
        return 1
    elif user_score > comp_score:
        return 1
    else:
        return -1
        
def play_game():
    print(logo)
    user_cards = []
    comp_cards = []
    # deal 2 cards to both comp and user
    for deal in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
    
    is_game_over = False
    # user will draw the cards
    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}. Your score is {user_score}")
        print(f"Computer's first card: {comp_cards[0]}.")
        
        if comp_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    #computer will draw the cards
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)
    
    
    result = compare(user_score,comp_score)
    
    print(f"Your cards: {user_cards}. Your score is {user_score}")
    print(f"Computer's cards: {comp_cards}. Computer's score is {comp_score}")
    
    if result == 0:
        print("Draw!")
    elif result == -1:
        print("You Lose!")
    else:
        print("You Won!")

#############################################################################    

while input("Do you want to play blackjack 21 ? Type: 'y' or 'n'\n").lower() == "y":
    os.system('clear')
    play_game()


