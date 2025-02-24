"""
# Exercise: Write a game where the user has to find the hidden
treasure on a 5x5 grid. The treasure is randomly placed on the
grid, and the user has to guess the coordinates.
"""
from random import randint

def map_print(already_guessed_spots):
    grid_size = 5

    for row in range(1, grid_size + 1):
        row_display = []

        for col in range(1, grid_size + 1):
            if (row, col) in already_guessed_spots:
                row_display.append('X')
            else:
                row_display.append('.')
        print(" ".join(row_display))

def treasure_hunt():
    print("""Welcome to the 'Treasure Hunt' game
in this game you will have to guess where the treasure is hidden in a 5X5 grid
you will have 10 tries""")
    chosen_row = randint(1, 5)
    chosen_col = randint(1, 5)
    guessed_spots = []

    tries = 5
    row_guess = None
    col_guess = None
    while tries > 0:
        print(f"\nTries left: {tries}")

        #row selection
        while True:
            try:
                row_guess = int(input("Please enter the row number (1-5): \n"))
                if 1 <= row_guess <= 5:
                    break
                print("Invalid row number  - rows are (1-5)")
            except ValueError:
                print("Invalid input, please enter a number")
        #column selection
        while True:
            try:
                col_guess = int(input("Please enter the column number (1-5): \n"))
                if 1 <= col_guess <= 5:
                    break
                print("Invalid col number - columns are (1-5)")
            except ValueError:
                print("Invalid input, please enter a number")

        guessed_spots.append((row_guess, col_guess))

        #found treasure
        if chosen_row == row_guess and chosen_col == col_guess:
            print("\n🎉 Congratulations you found the treasure it was at:")
            print(f"({row_guess} , {col_guess})")
            break

        #right row - wrong column
        if row_guess == chosen_row and col_guess != chosen_col:
            print("\nCorrect row, but incorrect column")
            print("Try a " + ("higher" if col_guess < chosen_col else "lower") + " column")

        #right column - wrong row
        elif col_guess == chosen_col and row_guess != chosen_row:
            print("\nCorrect column, but incorrect row")
            print("Try a " + ("higher" if row_guess < chosen_row else "lower") + " row")

        #both row and column are incorrect
        else:
            print("Both row and column are incorrect, Try again")

        map_print(guessed_spots)
        tries -= 1
    if tries == 0:
        print("\nYou are out of tries! GAME OVER!")
        print(f"The treasure was at ({chosen_row} , {chosen_col}).")


treasure_hunt()