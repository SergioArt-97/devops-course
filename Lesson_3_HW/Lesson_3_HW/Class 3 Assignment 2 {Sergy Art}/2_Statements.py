"""
# 2. Statements
# Exercise: Write a number guessing game. The program should
randomly select a number between 1 and 100, and the player has
to guess it.
"""

from random import choice


#border choosing
def guessing_game():
    print("""Welcome to the guessing game.
You will provide the computer with the range of numbers for the computer to choose a number from.
And then you would have to guess the number the computer chose""")
    while True:
        try:
            min_val = int(input("Please enter the minimum number: \n"))
            break
        except ValueError:
            print("Please enter a valid number")
    while True:
        try:
            max_val = int(input("Please enter the maximum number: \n"))
            if max_val <= min_val:
                print("maximum number cannot be lower or equal to the minimum number")
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    #game logic

    chosen_number = choice(range(min_val, max_val))
    print("You get 5 tries to guess the number")
    guesses = 5
    player_guess = None
    for i in range(guesses):
        while True:
            try:
                player_guess = int(input("Input your guess: \n"))
                if player_guess < min_val or player_guess > max_val:
                    print(f"your choice cannot be lower than {min_val} or higher than {max_val}, try again")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")
        if player_guess < chosen_number:
            print("Your guess is too low, try a bit higher\n")
            if i == 4:
                print("You got no more guesses left")
            else:
                print(f"you got {4 - i} more guesses")
            continue
        elif player_guess > chosen_number:
            print("Your guess is too high, try a bit lower\n")
            if i == 4:
                print("You got no more guesses left")
            else:
                print(f"you got {4 - i} more guesses")
            continue
        elif player_guess == chosen_number:
            break
    if player_guess == chosen_number:
        print("Congratulations!!!, you found the correct number")
    else:
        print("Too bad, you haven't found the number, try again")
guessing_game()