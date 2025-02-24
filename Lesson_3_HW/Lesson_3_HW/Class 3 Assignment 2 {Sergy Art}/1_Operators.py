"""
# 1. Operators
# Exercise: Create a simple calculator game that performs
addition, subtraction, multiplication, and division.
"""


def get_valid_number(prompt, min_value=None):
    #helper function to get a valid integer from the user.
    while True:
        try:
            user_num = int(input(prompt))
            if min_value is not None and user_num < min_value:
                print(f"Please enter a number greater than or equal to {min_value}.")
            else:
                return user_num
        except ValueError:
            print("Invalid input, Please enter a valid number")


def calculator_game():
    print("Welcome to the Calculator game")
    print("Please choose what would you like to do:")
    print("""1 - addition
2 - subtraction
3 - multiplication
4 - division
exit - to quit""")
    while True:
        player_choice = input("Your choice: \n").lower()
        if player_choice == "exit":
            break
        try:
            player_choice = int(player_choice)
            if player_choice not in range(1,5):
                print("Please choose a number between 1 and 4.")
                continue
        except ValueError:
            print("Invalid  input. Please enter a number between 1 and 4 or 'exit'.")
            continue

        # addition block

        if player_choice == 1:
            print("You chose Addition")
            addition_prompt = "How many numbers do you want to add? \n"
            amount_of_numbers = get_valid_number(addition_prompt,0)

            if amount_of_numbers == 0:
                print("0 = 0")
                return

            numbers = [get_valid_number(f"Enter number {i + 1}: ") for i in range(amount_of_numbers)]
            addition_result = sum(numbers)
            addition_string = " + ".join(map(str, numbers)) + f" = {addition_result}"

            print(addition_string)

        #subtraction block

        elif player_choice == 2:
            print("You chose Subtraction")
            subt_prompt = "Enter the base number you want to subtract from: \n"
            base_number = get_valid_number(subt_prompt, 0)
            number_to_subt = get_valid_number("Enter the number you want to subtract: \n", 0 )

            subt_result = base_number - number_to_subt
            print(f"{base_number} - {number_to_subt} = {subt_result}")

        #multiplication block

        elif player_choice == 3:
            print("You chose Multiplication")
            print("Please enter 2 numbers to multiply:")
            first_mult_number = get_valid_number("Enter the first number: \n")
            second_mult_number = get_valid_number("Enter the second number: \n")
            mult_calculation = first_mult_number * second_mult_number

            print(f"{first_mult_number} * {second_mult_number} = {mult_calculation}")

        #division block

        elif player_choice == 4:
            print("You chose Division")
            numerator = get_valid_number("Enter the numerator: \n")
            while True:
                denominator  = get_valid_number("Enter the denominator: \n")
                if denominator != 0:
                    break
                print("Denominator cannot be zero, Please enter a valid number")

            division_result = numerator / denominator
            print(f"{numerator} / {denominator} = {division_result:.2f}")
        print("Goodbye")
        break

calculator_game()