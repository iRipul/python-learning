from data import data as d
import random 
from artwork import logo,vs
import os

def pick_2_random_profiles():
    profile1 = random.choice(d)
    profile2 = random.choice(d)
    if profile1["name"] != profile2["name"]:
        return [profile1,profile2]
    else:
        pick_2_random_profiles()
        
def compare(profile1, profile2):
    if profile1["follower_count"] > profile2["follower_count"]:
        return 'A'
    else:
        return 'B' 
        
def start_game():
    print(logo)
    game_over = False
    score = 0
        
    while not game_over:
        profiles = pick_2_random_profiles()
        
        if score > 0:
            print(f"Your score is {score}.\n")
            
        print(f'Compare A: { profiles[0]["name"] }, a { profiles[0]["description"] }, from { profiles[0]["country"] }.')
        print(vs)
        print(f'Against B: { profiles[1]["name"] }, a { profiles[1]["description"] }, from { profiles[1]["country"] }.')
        
        ans = input("Who has more followers? Type 'A' or 'B' ")
        result = compare(profiles[0], profiles[1])

        if result != ans:
            game_over = True
            print(f"No, your answer is wrong. The correct ans is {result}")
        else:
            score += 1
            os.system('clear')
        
start_game()
