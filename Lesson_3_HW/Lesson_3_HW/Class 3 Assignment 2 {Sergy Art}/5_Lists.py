"""
# Exercise: Create a memory game where the user has to
remember a sequence of numbers. The sequence starts with one
number and adds one more each round. The user has to input the
correct sequence to proceed to the next round.
"""
from random import choice
from time import sleep

def memory_game():
    print("""Welcome to the memory game, the computer will choose 5 numbers
The chosen numbers will be shown on screen only for 5 seconds
after that you would have to try and guess each number in a row
You can make only 3 mistakes""")
    numbers = range(1,10)
    chosen_numbers = [choice(numbers) for _ in range(5)]
    print("the chosen list of numbers is:", chosen_numbers, end="", flush=True)
    sleep(5)
    print("\r" + " " *  len(str(chosen_numbers)) + "\r", end="", flush=True)
    current_guesses = []
    guesses = 3

    for number in chosen_numbers:
        if guesses == 0:
            print("you got no more guesses left")
            break
        while True:
            try:
                player_guess = int(input("Input the next number: \n"))
                if player_guess < 1 or player_guess > 10:
                    print("The numbers can only be between 1 and 10")
                    continue
            except ValueError:
                print("Please enter a valid number")
                continue

            if player_guess == number:
                current_guesses.append(player_guess)
                print("you guessed right!")
                print("current list:", current_guesses, end="\n")
                break
            else:
                print("wrong!")
                guesses -= 1
                if guesses == 0:
                    print("You got no more guesses left")
                    break
                else:
                    print(f"You've got {guesses} left")
        if guesses == 0:
            break
    if current_guesses == chosen_numbers:
        print("Congratulations you found all the numbers")
        print("secret list:", current_guesses)
    else:
        print("you havent found all the secret numbers")
        print(f"your numbers are: \n{current_guesses}\nand the secret numbers are: \n{chosen_numbers}")

memory_game()