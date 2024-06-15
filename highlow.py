from game_data import data
from art import logo,vs
from random import randint
from os import system
continue_= True
continue_play = "y"
while continue_play == "y":
    system('cls')
    print(logo)
    choice_A = randint(0,49)
    score_count = 0
    while continue_ == True and score_count!=50:
        print(f"Your score is:  {score_count}")
        choice_B = randint(0,49)
        print(f"Compare A: {data[choice_A]['name']}, a {data[choice_A]['description']}, from {data[choice_A]['country']}.")

        print(vs)

        print(f"Compare B: {data[choice_B]['name']}, a {data[choice_B]['description']}, from {data[choice_B]['country']}.")

        if (data[choice_A]['follower_count'])>(data[choice_B]['follower_count']):
            answer = "A"
        else:
            answer = "B"

        decision = input("Who has more followers? Type 'A' or 'B': ").upper()

        if decision == answer:
            continue_ = True
            score_count = score_count+1
            choice_A = choice_B
            system('cls')
        else:
            continue_ = False

    if score_count == 50:
        print(f"Congratulation you've won the game with the score of {score_count}")
        continue_play = input("Press 'y' if you want to play again: ").lower()
        if continue_play == "y":
            continue_ = True

    else:
        print(f"You lost, final score was: {score_count}")
        continue_play = input("Press 'y' if you want to try again: ").lower()
        if continue_play == "y":
            continue_ = True






