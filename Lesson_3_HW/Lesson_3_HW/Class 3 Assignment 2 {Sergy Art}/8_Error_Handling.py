"""
# Exercise: Create a game where the user inputs a number to roll
a die. Handle invalid inputs gracefully, and inform the user of
the error.
"""
from random import randint
def roll_die_game():
    print("""Welcome to the die roll game
here you roll a six sided die a bunch of times""")
    player_choice = None
    while True:
        try:
            player_choice = str(input("Please choose what would you like to do:\n'roll' - roll the die\n'exit' - to quit\n"))
        except ValueError as e:
            print("Invalid choice\nError message:", e)
        if player_choice.lower() == 'roll':
            print(f"You rolled {randint(1,6)}")
        elif player_choice.lower() == 'exit':
            print("You chose to quit\nGoodbye")
            break
        else:
            print("Invalid Choice")
            continue


roll_die_game()