"""Rock Paper Scissors"""

import random
import time

def main():
    items = ["Rock", "Paper", "Scissors"]
    user_choice = player(items)
    com_choice = computer(items)
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {com_choice}")
    determine_winner(user_choice, com_choice)


def player(items):
    while True:
        user_input = input(f"Rock, Paper, or Scissors. ").title()
        
        if user_input in items:
            return user_input
        
        elif user_input not in items:
            print("input error")
            continue


def computer(items):
    return random.choice(items)


def determine_winner(player_choice, com_choice):
    if player_choice == com_choice:
        print("It's a tie!")
    elif (
        (player_choice == "Rock" and com_choice == "Scissors") or
        (player_choice == "Scissors" and com_choice == "Paper") or
        (player_choice == "Paper" and com_choice == "Rock")
    ):
        print("You win!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    main()