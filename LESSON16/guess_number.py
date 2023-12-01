import sys
import random
# from enum import Enum


def guess_number(name = 'PlayerOne'):
    
    player_wins = 0
    game_count = 0

    def play_guess_number():
        nonlocal player_wins
        nonlocal game_count
        

        playerchoice = input(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess_number()
        
        player=int(playerchoice)
        computer_choice=random.choice("123")
        computer=int(computer_choice)

        print(f"\n{name}, you chose {player}")
        print(f"I was thinking about the number {computer}")
        
        def decide_correct(player, computer):
            nonlocal player_wins
            nonlocal name

            if player == computer:
                player_wins += 1
                return f"{name}, you win!"
            else:
                return f"Sorry {name}, you lost!"

        game_result=decide_correct(player, computer)
        print(game_result)

        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins / game_count:.2%}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("\nThank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye! {name}! 👏")
            else:
                return

    return play_guess_number

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    number_guess = guess_number(args.name)
    number_guess()