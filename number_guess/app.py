from artwork import logo
import random
import os

def generate_number(start,end):
    return random.randint(start,end)
    
def play_game():
    print(logo)
    print("Welcome to the number guessing game.")
    print("I am thinking of a number between 1 and 100")
    level = input("Choose a difficulty. Type 'easy' or 'hard'\n")
    
    LIVES = 10
    if level == "hard":
        LIVES = 5
        
    random_number = generate_number(1,100)
    is_game_over = False
    
    while not is_game_over and LIVES > 0:
        print(f"You have {LIVES} attempts left.")
        guess = int(input("Make a guess "))
        
        if guess > random_number:
            print("Too high!\nGuess again")
            LIVES -= 1
        elif guess < random_number:
            print("Too low!\nGuess again")
            LIVES -=1
        else:
            print("Wohoo! you got it right")
            is_game_over = True
            
    if LIVES <= 0:
        print("You have reached to max attempts. You lost the game. Please try again.")

while(input("Do you want to play number guessing game? Type 'y' or 'n' ") == "y"):
    os.system('clear')
    play_game()
    

    
