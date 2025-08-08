#Rock-Paper_Scissors game

import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
    player = None #after every game player and computer both resets
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("it's a tie")

    elif player == "paper" and computer == "rock":
        print("You win!")

    elif player == "scissors" and computer == "paper":
        print("You win!")

    elif player == "rock" and computer == "scissors":
        print("You win!")

    else:
        print("You lose!")

    if not input("Play again?(Yes/No): ").lower() == "yes":
        playing = False

print("Thanks for playing")