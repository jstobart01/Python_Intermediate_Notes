from guess_number import number_guess
# import rps
# import sys

# This function greets the player and asks which game they would like to play.

# Currently the funciton doesn't start the game


number_guess()
# def greeting(name):
#     msg = f"Hello {name}!"
#     print(msg)
#     print(f"\nWhich game would you like to play {name}?")

#     while True:
#         game_choice = input("\nG for 'Number Guess' or \nR for 'Rock, Paper, Scissors' or\nQ for quit")
#         if game_choice.lower() not in ["g", "r", "q"]:
#             continue
#         else:
#             break

#     if game_choice.lower() == "g":
#         guess_number.number_guess
#     elif game_choice.lower() == "r":
#         rps.rps()
#     else:
#         print("Thank you for playing!\n")
#         sys.exit(f"Bye! {name}!")



# if __name__ == '__main__':
#     import argparse

#     parser = argparse.ArgumentParser(
#         description="Provides a personal greeting."
#     )

#     parser.add_argument(
#         "-n", "--name", metavar="name", required=True, help="The name of the person to greet."
#     )

#     args = parser.parse_args()

#     greeting(args.name)