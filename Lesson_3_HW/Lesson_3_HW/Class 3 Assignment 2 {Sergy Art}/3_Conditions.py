"""
# 3. Conditions
# Exercise: Create a rock-paper-scissors game. The user should
be able to play against the computer, which randomly chooses
rock, paper, or scissors.
"""

from random import choice

def win_lose(player, computer):
    #player rock choice
    if player.capitalize() == 'Rock':
        if computer == 'Rock':
            return None
        elif computer == 'Scissors':
            return True
        return False
    #player paper choice
    if player.capitalize() == "Paper":
        if computer == "Paper":
            return None
        elif computer == 'Rock':
            return True
        return False
    #player scissors choice
    if player.capitalize() == "Scissors":
        if computer == "Scissors":
            return None
        elif computer == 'Paper':
            return True
        return False


def rock_paper_scissors():
    options = [
        "Rock",
        "Paper",
        "Scissors"
    ]

    print("""Welcome to the "Rock, Paper & Scissors" game - 
you will need to enter your choice VS the computer
'exit' - to quit
'points' - to see the current scoreboard""")
    player_score = 0
    computer_score = 0

    while True:
        player_choice = str(input("Enter your choice: \n"))

        if player_choice.lower() == 'exit':
            break

        elif player_choice.lower() == 'points':
            print(f"Player score: {player_score}\nComputer score: {computer_score}")
            continue

        if player_choice.capitalize() not in options :
            print("Invalid choice")
            continue

        computer_choice = choice(options)

        if win_lose(player_choice, computer_choice) is None:
            print(f"Both you and the computer chose {player_choice}, neither of you get a point")
        elif win_lose(player_choice, computer_choice) is True:
            print(f"You chose {player_choice} and the computer chose {computer_choice}, you win")
            player_score += 1
        elif win_lose(player_choice, computer_choice) is False:
            print(f"You chose {player_choice} and the computer chose {computer_choice}, you lose")
            computer_score += 1

    print("The final score is:")
    print(f"Player score: {player_score}\nComputer score: {computer_score}")
    print("Goodbye")

rock_paper_scissors()