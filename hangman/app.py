import random
import names
import artwork
# Welcome Logo 
print(artwork.logo)
print("\n\n")
# initialization
stages = artwork.stages
word_list = names.names_list
chosen_word = random.choice(word_list)
lives = 6

display = []

for letter in chosen_word:
    display += "_"
end_of_game = False

# start the game
print(display)
print("\n")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
            print(f"You have alreay selected {guess}. Please choose other letter.")
            continue
    guessFound = False
    for num in range(len(chosen_word)):
        if chosen_word[num] == guess:
            display[num] = guess
            guessFound = True
            
    if guessFound:
        print("Bingo! you have selected a correct letter. carry on !!")
    else:
        print("The letter you have chosen is not correct, you have lost one life.")
        lives -= 1
        print(stages[lives])
    
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You Won!!")
    
    if lives <=0:
        end_of_game = True
        print("You Lose!!")
        print(f"The word is : {chosen_word}")
