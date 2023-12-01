from guess_number import guess_number
from rps import rps
import sys

# This function greets the player and asks which game they would like to play.

# Currently the funciton doesn't start the game

def greeting(name = "PlayerOne"):
    welcome_back = False

    msg = f"Hello {name}!"
    print(msg)
    print(f"\nWhich game would you like to play?")

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        game_choice = input("\nG for 'Number Guess' or \nR for 'Rock, Paper, Scissors' or\nQ for quit")

        if game_choice.lower() not in ["g", "r", "q"]:
            print(f"{name}, please enter 'G', 'R', or 'Q'.")
            return greeting(name)

        welcome_back = True

# Determines what game the player chose and calls that game function

        if game_choice.lower() == "g":
            number_guess_game = guess_number(name)
            number_guess_game()
        elif game_choice.lower() == "r":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        else:
            print("\nThank you for playing!\n")
            sys.exit(f"Bye! {name}!")
    
    
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person to greet."
    )

    args = parser.parse_args()

    greeting(args.name)